# Hash Map
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Hash-based`

### Topics
**Topics:** `key-value storage`, `caching`, `indexing`, `frequency counting`

### Definition
A data structure that stores key-value pairs using a hash function to compute an index into an array of buckets, providing average O(1) lookup, insertion, and deletion.

### Use cases
- Caching and memoization
- Database indexing
- Counting frequency of elements
- Symbol tables in compilers
- Implementing sets and dictionaries

### Attributes
- Uses hash function to map keys to bucket indices
- Handles collisions via chaining or open addressing
- Resizes (rehashes) when load factor exceeds threshold
- Keys must be hashable (immutable in Python)

### Common operations

| Operation | Average | Worst | Description |
|-----------|---------|-------|-------------|
| Get       | O(1)    | O(n)  | Retrieve value by key |
| Put       | O(1)    | O(n)  | Insert or update key-value pair |
| Delete    | O(1)    | O(n)  | Remove key-value pair |
| Contains  | O(1)    | O(n)  | Check if key exists |
| Resize    | O(n)    | O(n)  | Rehash all elements |

### In code
```python
# Python dict IS a hash map
cache = {}

# Insert - O(1) average
cache["key1"] = "value1"
cache["key2"] = "value2"

# Get - O(1) average
val = cache.get("key1", "default")

# Check existence - O(1) average
if "key1" in cache:
    print("Found!")

# Delete - O(1) average
del cache["key1"]

# Simple hash map implementation (chaining)
class HashMap:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
        self.load_factor = 0.75

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        if self.size / self.capacity >= self.load_factor:
            self._resize()
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))
        self.size += 1

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        raise KeyError(key)

    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
```

### Time complexity
- **Average case**: O(1) for get, put, delete - hash function distributes keys evenly
- **Worst case**: O(n) when all keys hash to same bucket (rare with good hash function)
- **Resize**: O(n) - must rehash all elements to new bucket array

**Load factor**: Python dict resizes at ~66% capacity. Higher load factor = more collisions, lower = more memory waste.

### Space complexity
O(n) for n key-value pairs. Additional space for empty buckets depends on load factor and capacity. With separate chaining, O(m + n) where m is bucket array size.

### Trade-offs
**Pros:**
- O(1) average operations - extremely fast lookup
- Flexible key types (any hashable object)
- Natural for key-value associations

**Cons:**
- O(n) worst case with poor hash function
- Unordered (iteration order not guaranteed in older Python)
- Extra memory overhead for hash table structure
- Keys must be hashable/immutable

### Variants
- **Separate chaining**: Each bucket is a linked list - simpler deletion
- **Open addressing**: Probes for next empty slot - better cache locality
- **Linear probing**: Simple but prone to clustering
- **Quadratic probing**: Reduces clustering, used in some implementations
- **Robin Hood hashing**: Minimizes variance in probe lengths

### When to use vs avoid
- **Use when**: Need fast key-based lookup, counting/grouping operations, caching, deduplication
- **Avoid when**: Need ordered iteration, keys are not hashable, memory is very constrained

### Related
- [Dictionary](./dictionary.md)
- [Set](./set.md)
