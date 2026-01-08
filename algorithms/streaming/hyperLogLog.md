# HyperLogLog
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Streaming Algorithms`

### Topics
**Topics:** `cardinality estimation`, `probabilistic counting`, `distinct elements`, `sketching`

### Definition
A probabilistic algorithm for estimating the number of distinct elements (cardinality) in a multiset, using only O(log log n) space per counter with high accuracy.

### Use cases
- Unique visitor counting (web analytics)
- Database query optimization (COUNT DISTINCT)
- Network monitoring (unique IPs)
- Redis PFCOUNT
- Big data cardinality estimation

### Prerequisites
- Hash functions
- Probability and expected value
- Understanding of geometric distribution

### Step-by-step
**Key insight:**
If we hash n distinct items uniformly, the maximum number of leading zeros in the binary hash values is approximately log₂(n).

**Algorithm:**
1. Use m = 2^b registers (buckets)
2. For each item:
   - Hash to get binary string
   - First b bits determine register index
   - Count leading zeros in remaining bits
   - Update register with max(current, zeros + 1)
3. Estimate cardinality using harmonic mean of 2^register values

### In code
```python
import hashlib
import math

class HyperLogLog:
    """
    HyperLogLog for cardinality estimation.
    Uses m = 2^b registers.
    Standard error ≈ 1.04 / √m
    """

    def __init__(self, b=14):
        """
        b: number of bits for register index (4-16 typical)
        m = 2^b registers
        """
        self.b = b
        self.m = 1 << b
        self.registers = [0] * self.m

        # Bias correction constant
        if self.m == 16:
            self.alpha = 0.673
        elif self.m == 32:
            self.alpha = 0.697
        elif self.m == 64:
            self.alpha = 0.709
        else:
            self.alpha = 0.7213 / (1 + 1.079 / self.m)

    def _hash(self, item):
        """Hash item to 64-bit integer"""
        h = hashlib.md5(str(item).encode()).hexdigest()
        return int(h[:16], 16)  # Use first 64 bits

    def _get_register_and_zeros(self, hash_value):
        """Get register index and count of leading zeros"""
        # First b bits for register index
        register = hash_value >> (64 - self.b)

        # Remaining bits for zero counting
        remaining = hash_value & ((1 << (64 - self.b)) - 1)

        # Count leading zeros (position of first 1)
        if remaining == 0:
            zeros = 64 - self.b
        else:
            zeros = (64 - self.b) - remaining.bit_length()

        return register, zeros + 1

    def add(self, item):
        """Add item to HLL"""
        h = self._hash(item)
        register, zeros = self._get_register_and_zeros(h)
        self.registers[register] = max(self.registers[register], zeros)

    def count(self):
        """Estimate cardinality"""
        # Harmonic mean of 2^register values
        indicator = sum(2.0 ** (-r) for r in self.registers)
        raw_estimate = self.alpha * self.m * self.m / indicator

        # Small range correction (linear counting)
        if raw_estimate <= 2.5 * self.m:
            zeros = self.registers.count(0)
            if zeros > 0:
                return self.m * math.log(self.m / zeros)

        # Large range correction (not typically needed for 64-bit hash)
        if raw_estimate > (1 << 32) / 30:
            return -(1 << 32) * math.log(1 - raw_estimate / (1 << 32))

        return raw_estimate

    def merge(self, other):
        """Merge another HLL into this one"""
        if self.m != other.m:
            raise ValueError("Register counts must match")

        for i in range(self.m):
            self.registers[i] = max(self.registers[i], other.registers[i])

    def relative_error(self):
        """Expected relative standard error"""
        return 1.04 / math.sqrt(self.m)

class HyperLogLogPlusPlus:
    """
    HyperLogLog++ with improved small cardinality estimation.
    Based on Google's paper.
    """

    def __init__(self, p=14, sp=25):
        """
        p: precision (number of registers = 2^p)
        sp: sparse precision for small cardinalities
        """
        self.p = p
        self.sp = sp
        self.m = 1 << p
        self.registers = None  # Lazy initialization
        self.sparse_set = set()  # For small cardinalities
        self.sparse_threshold = self.m // 4

        self.alpha = self._get_alpha(self.m)

    def _get_alpha(self, m):
        if m == 16: return 0.673
        if m == 32: return 0.697
        if m == 64: return 0.709
        return 0.7213 / (1 + 1.079 / m)

    def _hash(self, item):
        h = hashlib.sha256(str(item).encode()).hexdigest()
        return int(h[:16], 16)

    def _to_dense(self):
        """Convert from sparse to dense representation"""
        self.registers = [0] * self.m

        for h in self.sparse_set:
            register = h >> (64 - self.p)
            remaining = h & ((1 << (64 - self.p)) - 1)
            zeros = (64 - self.p) - remaining.bit_length() + 1 if remaining else 64 - self.p
            self.registers[register] = max(self.registers[register], zeros)

        self.sparse_set = None

    def add(self, item):
        h = self._hash(item)

        if self.registers is None:
            # Sparse mode
            self.sparse_set.add(h)
            if len(self.sparse_set) > self.sparse_threshold:
                self._to_dense()
        else:
            # Dense mode
            register = h >> (64 - self.p)
            remaining = h & ((1 << (64 - self.p)) - 1)
            zeros = (64 - self.p) - remaining.bit_length() + 1 if remaining else 64 - self.p
            self.registers[register] = max(self.registers[register], zeros)

    def count(self):
        if self.registers is None:
            # Sparse mode - use linear counting
            return len(self.sparse_set)

        # Dense mode - standard HLL estimation
        indicator = sum(2.0 ** (-r) for r in self.registers)
        estimate = self.alpha * self.m * self.m / indicator

        # Bias correction for small cardinalities
        if estimate <= 5 * self.m:
            zeros = self.registers.count(0)
            if zeros > 0:
                linear_count = self.m * math.log(self.m / zeros)
                return linear_count

        return estimate

def simple_probabilistic_counter():
    """
    Simplified probabilistic counter for understanding.
    Uses maximum of trailing zeros.
    """
    max_zeros = 0

    def add(item):
        nonlocal max_zeros
        h = hash(str(item))
        if h == 0:
            zeros = 64
        else:
            # Count trailing zeros
            zeros = (h & -h).bit_length() - 1
        max_zeros = max(max_zeros, zeros)

    def count():
        return 2 ** max_zeros

    return add, count

class MinCount:
    """
    MinCount (k-minimum values) algorithm.
    Alternative to HyperLogLog with similar guarantees.
    """

    def __init__(self, k=1024):
        self.k = k
        self.min_hashes = []

    def _hash(self, item):
        h = hashlib.md5(str(item).encode()).hexdigest()
        return int(h, 16) / (1 << 128)  # Normalize to [0, 1)

    def add(self, item):
        import heapq

        h = self._hash(item)

        if len(self.min_hashes) < self.k:
            heapq.heappush(self.min_hashes, -h)  # Max-heap (negated)
        elif -self.min_hashes[0] > h:
            heapq.heapreplace(self.min_hashes, -h)

    def count(self):
        if len(self.min_hashes) < self.k:
            return len(self.min_hashes)

        # k-th minimum hash
        kth_min = -self.min_hashes[0]

        # Estimate: E[k-th order statistic] = k / (n + 1) ≈ k / n
        return (self.k - 1) / kth_min

# Usage
# Basic HyperLogLog
hll = HyperLogLog(b=10)  # 1024 registers

# Add items
for i in range(10000):
    hll.add(f"user_{i % 5000}")  # 5000 unique items

estimate = hll.count()
actual = 5000
error = abs(estimate - actual) / actual * 100

print(f"Estimated unique: {estimate:.0f}")
print(f"Actual unique: {actual}")
print(f"Error: {error:.1f}%")
print(f"Expected error: ±{hll.relative_error() * 100:.1f}%")

# Merge example
hll1 = HyperLogLog(b=10)
hll2 = HyperLogLog(b=10)

for i in range(1000):
    hll1.add(f"a_{i}")

for i in range(1000):
    hll2.add(f"b_{i}")

hll1.merge(hll2)
print(f"\nAfter merge: {hll1.count():.0f} (expected ~2000)")

# HLL++ for better small cardinality
hllpp = HyperLogLogPlusPlus()
for i in range(100):
    hllpp.add(f"item_{i}")
print(f"\nHLL++ estimate for 100 items: {hllpp.count():.0f}")

# Memory comparison
import sys
hll_memory = sys.getsizeof(hll.registers)
set_memory = sys.getsizeof(set(f"user_{i}" for i in range(5000)))
print(f"\nHLL memory: {hll_memory} bytes")
print(f"Set memory: {set_memory} bytes")
print(f"Memory ratio: {set_memory / hll_memory:.0f}x")
```

### Time complexity

| Operation | Complexity |
|-----------|------------|
| Add | O(1) |
| Count | O(m) |
| Merge | O(m) |

### Space complexity
O(m × log log n) where m = 2^b registers. Typically 1-2 KB for 1% error.

### Edge cases
- Empty set (count = 0)
- Single element
- All elements identical
- Very small cardinalities (use linear counting)

### Variants
- **HyperLogLog++**: Google's improved version with bias correction
- **LogLog**: Original precursor algorithm
- **SuperLogLog**: Uses 70th percentile instead of harmonic mean
- **Streaming HLL**: For distributed systems

### When to use vs avoid
- **Use when**: Counting unique elements, memory constrained, approximate count acceptable, streaming data
- **Avoid when**: Need exact count, cardinality < 1000 (use exact counting), need to enumerate elements

### Related
- [Count-Min Sketch](./countMinSketch.md)
- [Reservoir Sampling](./reservoirSampling.md)
- [Bloom Filter](../../datastructs/specialized/bloomFilter.md)
