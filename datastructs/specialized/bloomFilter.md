# Bloom Filter
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Specialized`

### Topics
**Topics:** `probabilistic membership`, `caching`, `distributed systems`, `deduplication`

### Definition
A space-efficient probabilistic data structure that tests whether an element is in a set, with possible false positives but no false negatives.

### Use cases
- Cache lookup optimization (check before expensive DB query)
- Spell checkers (quickly reject non-words)
- Network routers (check if URL is malicious)
- Database query optimization
- Duplicate detection in streaming data

### Attributes
- Returns "possibly in set" or "definitely not in set"
- False positives possible, false negatives impossible
- Cannot remove elements (standard variant)
- Size is fixed, independent of number of elements

### Common operations

| Operation | Time | Description |
|-----------|------|-------------|
| Add       | O(k) | Insert element using k hash functions |
| Contains  | O(k) | Check membership (may have false positive) |
| Clear     | O(m) | Reset all bits to 0 |

*k = number of hash functions, m = number of bits*

### In code
```python
import hashlib

class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size

    def _hashes(self, item):
        """Generate k hash values for item"""
        result = []
        for i in range(self.num_hashes):
            # Use different seeds for each hash
            h = hashlib.md5(f"{item}{i}".encode()).hexdigest()
            result.append(int(h, 16) % self.size)
        return result

    def add(self, item):
        """Add item to filter - O(k)"""
        for pos in self._hashes(item):
            self.bit_array[pos] = 1

    def contains(self, item):
        """
        Check if item might be in set - O(k)
        Returns True: item MIGHT be in set (possible false positive)
        Returns False: item is DEFINITELY NOT in set
        """
        return all(self.bit_array[pos] for pos in self._hashes(item))

# Usage
bf = BloomFilter(size=1000, num_hashes=3)

# Add elements
bf.add("apple")
bf.add("banana")

# Check membership
bf.contains("apple")   # True (definitely or probably in set)
bf.contains("orange")  # False (definitely not in set)
bf.contains("grape")   # Maybe True (false positive possible)

# Practical usage: Check cache before DB
def get_user(user_id, bloom_filter, cache, database):
    # Quick negative check - O(k)
    if not bloom_filter.contains(user_id):
        return None  # User definitely doesn't exist

    # Check cache
    if user_id in cache:
        return cache[user_id]

    # Fall back to database
    user = database.get(user_id)
    if user:
        cache[user_id] = user
    return user

# Optimal parameters calculation
import math

def optimal_bloom_params(n_items, fp_rate):
    """Calculate optimal size and hash count"""
    # m = -(n * ln(p)) / (ln(2)^2)
    m = -n_items * math.log(fp_rate) / (math.log(2) ** 2)
    # k = (m/n) * ln(2)
    k = (m / n_items) * math.log(2)
    return int(m), int(k)

# For 1 million items with 1% false positive rate
size, hashes = optimal_bloom_params(1_000_000, 0.01)
# size ≈ 9.6 million bits (1.2 MB), hashes ≈ 7
```

### Time complexity
- **Add**: O(k) where k is number of hash functions
- **Contains**: O(k)
- **k is typically small** (3-10), so effectively O(1)

### Space complexity
O(m) bits where m is the filter size. For n elements with false positive rate p:
- m = -n * ln(p) / (ln(2))²
- About 10 bits per element for 1% false positive rate

Much smaller than storing actual elements!

### Trade-offs
**Pros:**
- Extremely space-efficient
- O(1) operations (constant k)
- No false negatives guaranteed
- Simple implementation

**Cons:**
- False positives occur
- Cannot delete elements
- Cannot retrieve original elements
- False positive rate increases as filter fills

### Variants
- **Counting Bloom filter**: Supports deletion using counters instead of bits
- **Scalable Bloom filter**: Grows dynamically while maintaining false positive rate
- **Cuckoo filter**: Supports deletion, lower false positive rate
- **Quotient filter**: Cache-friendly alternative

### When to use vs avoid
- **Use when**: Need space-efficient set membership, can tolerate false positives, don't need to delete or enumerate
- **Avoid when**: Cannot tolerate any false positives, need to delete elements, need to retrieve stored elements

### Related
- [Set](../hashBased/set.md)
- [Hash Map](../hashBased/hashmap.md)
