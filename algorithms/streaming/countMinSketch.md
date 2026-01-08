# Count-Min Sketch
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Streaming Algorithms`

### Topics
**Topics:** `frequency estimation`, `probabilistic data structure`, `heavy hitters`, `streaming`

### Definition
A probabilistic data structure that serves as a frequency table of events in a stream of data, using sub-linear space at the cost of overcounting some events due to hash collisions.

### Use cases
- Network traffic analysis
- NLP word frequency counting
- Database query optimization
- Finding heavy hitters
- Click stream analysis

### Prerequisites
- Hash functions
- Probability (Chebyshev/Markov inequalities)
- Understanding of approximation algorithms

### Step-by-step
1. Create d × w array of counters (all zeros)
2. Use d independent hash functions, each mapping to [0, w)
3. To add item:
   - Hash item with each function
   - Increment counter at each position
4. To query frequency:
   - Hash item with each function
   - Return minimum of all counters

### In code
```python
import hashlib
import math

class CountMinSketch:
    """
    Count-Min Sketch for frequency estimation.
    Error ≤ ε*n with probability ≥ 1-δ
    where w = ceil(e/ε) and d = ceil(ln(1/δ))
    """

    def __init__(self, epsilon=0.01, delta=0.01):
        """
        epsilon: error factor (smaller = more accurate)
        delta: failure probability (smaller = more reliable)
        """
        self.w = math.ceil(math.e / epsilon)
        self.d = math.ceil(math.log(1 / delta))
        self.table = [[0] * self.w for _ in range(self.d)]
        self.total = 0

    def _hash(self, item, i):
        """Hash item to bucket index for row i"""
        # Use different seeds for different hash functions
        h = hashlib.md5(f"{i}:{item}".encode()).hexdigest()
        return int(h, 16) % self.w

    def add(self, item, count=1):
        """Add item to sketch"""
        self.total += count
        for i in range(self.d):
            j = self._hash(item, i)
            self.table[i][j] += count

    def query(self, item):
        """
        Estimate frequency of item.
        Returns minimum count across all hash functions.
        """
        return min(self.table[i][self._hash(item, i)] for i in range(self.d))

    def merge(self, other):
        """Merge another CMS into this one"""
        if self.w != other.w or self.d != other.d:
            raise ValueError("Dimensions must match")

        for i in range(self.d):
            for j in range(self.w):
                self.table[i][j] += other.table[i][j]

        self.total += other.total

    def inner_product(self, other):
        """
        Estimate inner product of two frequency vectors.
        Useful for similarity estimation.
        """
        if self.w != other.w or self.d != other.d:
            raise ValueError("Dimensions must match")

        return min(
            sum(self.table[i][j] * other.table[i][j] for j in range(self.w))
            for i in range(self.d)
        )

class ConservativeCountMinSketch(CountMinSketch):
    """
    Conservative Update variant - reduces overcounting.
    Only updates counters that would equal the minimum.
    """

    def add(self, item, count=1):
        """Add with conservative update"""
        self.total += count

        # Get current minimum
        min_count = self.query(item)

        for i in range(self.d):
            j = self._hash(item, i)
            # Only update if this counter is at minimum
            self.table[i][j] = max(self.table[i][j], min_count + count)

class CountMinSketchWithHeavyHitters:
    """
    CMS with heavy hitter tracking.
    Maintains items that appear more than threshold fraction.
    """

    def __init__(self, epsilon=0.01, delta=0.01, threshold=0.1):
        self.cms = CountMinSketch(epsilon, delta)
        self.threshold = threshold
        self.candidates = {}  # item -> count
        self.total = 0

    def add(self, item, count=1):
        self.cms.add(item, count)
        self.total += count

        estimated = self.cms.query(item)

        # Update candidates
        if estimated >= self.threshold * self.total:
            self.candidates[item] = estimated
        elif item in self.candidates:
            del self.candidates[item]

    def get_heavy_hitters(self):
        """Return items above threshold"""
        return {item: self.cms.query(item)
                for item in self.candidates
                if self.cms.query(item) >= self.threshold * self.total}

def count_min_sketch_simple(width, depth):
    """
    Minimal implementation for understanding.
    """
    table = [[0] * width for _ in range(depth)]

    def add(item):
        for i in range(depth):
            j = hash(f"{i}:{item}") % width
            table[i][j] += 1

    def query(item):
        return min(table[i][hash(f"{i}:{item}") % width] for i in range(depth))

    return add, query

class SpaceSaving:
    """
    Space-Saving algorithm for top-k frequent items.
    Deterministic alternative to CMS for heavy hitters.
    """

    def __init__(self, k):
        self.k = k
        self.counters = {}  # item -> count
        self.min_count = 0

    def add(self, item):
        if item in self.counters:
            self.counters[item] += 1
        elif len(self.counters) < self.k:
            self.counters[item] = 1
        else:
            # Replace item with minimum count
            min_item = min(self.counters, key=self.counters.get)
            self.min_count = self.counters[min_item]
            del self.counters[min_item]
            self.counters[item] = self.min_count + 1

    def query(self, item):
        return self.counters.get(item, 0)

    def top_k(self):
        return sorted(self.counters.items(), key=lambda x: -x[1])

class CountSketch:
    """
    Count Sketch - can have negative counts, unbiased estimator.
    Better for point queries, but requires median of means.
    """

    def __init__(self, width, depth):
        self.w = width
        self.d = depth
        self.table = [[0] * width for _ in range(depth)]

    def _hash(self, item, i):
        h = hash(f"{i}:{item}")
        return h % self.w

    def _sign(self, item, i):
        h = hash(f"sign:{i}:{item}")
        return 1 if h % 2 == 0 else -1

    def add(self, item, count=1):
        for i in range(self.d):
            j = self._hash(item, i)
            s = self._sign(item, i)
            self.table[i][j] += s * count

    def query(self, item):
        estimates = []
        for i in range(self.d):
            j = self._hash(item, i)
            s = self._sign(item, i)
            estimates.append(s * self.table[i][j])

        # Return median
        estimates.sort()
        mid = len(estimates) // 2
        if len(estimates) % 2 == 0:
            return (estimates[mid - 1] + estimates[mid]) // 2
        return estimates[mid]

# Usage
# Basic Count-Min Sketch
cms = CountMinSketch(epsilon=0.001, delta=0.01)

# Add items
words = ["apple", "banana", "apple", "cherry", "apple", "banana", "date"]
for word in words:
    cms.add(word)

print(f"Estimated count of 'apple': {cms.query('apple')}")  # ~3
print(f"Estimated count of 'banana': {cms.query('banana')}")  # ~2
print(f"Estimated count of 'grape': {cms.query('grape')}")  # ~0 (with possible overcount)

# Heavy hitters
hh_cms = CountMinSketchWithHeavyHitters(threshold=0.2)
for word in ["a"]*100 + ["b"]*50 + ["c"]*10 + ["d"]*5:
    hh_cms.add(word)
print(f"Heavy hitters: {hh_cms.get_heavy_hitters()}")

# Space-saving
ss = SpaceSaving(k=3)
for word in ["a"]*100 + ["b"]*50 + ["c"]*10 + ["d"]*5:
    ss.add(word)
print(f"Top 3: {ss.top_k()}")  # [('a', 100), ('b', 50), ('c', 10)]

print(f"\nCMS dimensions: {cms.d} rows × {cms.w} columns")
print(f"Memory usage: ~{cms.d * cms.w * 8} bytes")
```

### Time complexity

| Operation | Complexity |
|-----------|------------|
| Add | O(d) = O(log(1/δ)) |
| Query | O(d) = O(log(1/δ)) |
| Merge | O(d × w) |

### Space complexity
O(d × w) = O((1/ε) × log(1/δ)) - sub-linear in stream size.

### Edge cases
- Query for unseen item (may return > 0 due to collisions)
- Negative counts (not supported in basic CMS)
- Merging sketches with different dimensions

### Variants
- **Conservative Update**: Reduces overcounting
- **Count Sketch**: Unbiased, can handle negative updates
- **CM-CU**: Conservative update variant
- **Augmented Sketch**: Combines with hash table for frequent items

### When to use vs avoid
- **Use when**: Streaming data, memory constrained, approximate counts acceptable
- **Avoid when**: Need exact counts, mostly unique items, small data fits in memory

### Related
- [HyperLogLog](./hyperLogLog.md)
- [Reservoir Sampling](./reservoirSampling.md)
