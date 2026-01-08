# LRU Cache
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Specialized`

### Topics
**Topics:** `caching`, `memory efficiency`, `eviction policies`, `web browsers`

### Definition
A fixed-capacity cache that evicts the Least Recently Used item when full, providing O(1) access while maintaining access order.

### Use cases
- Browser cache (recently visited pages)
- Database query caching
- Memory page replacement
- API response caching
- Memoization with bounded memory

### Attributes
- Fixed capacity - evicts oldest on overflow
- Tracks access order (not insertion order)
- Both get and put update recency
- O(1) operations using hash map + doubly linked list

### Common operations

| Operation | Time | Description |
|-----------|------|-------------|
| Get       | O(1) | Retrieve value and mark as recently used |
| Put       | O(1) | Insert/update value, evict LRU if full |
| Delete    | O(1) | Remove specific key |
| Peek      | O(1) | Get without updating recency |

### In code
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """Get value and mark as recently used - O(1)"""
        if key not in self.cache:
            return -1
        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """Insert/update and evict LRU if needed - O(1)"""
        if key in self.cache:
            # Update existing and move to end
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Remove oldest (first item)
            self.cache.popitem(last=False)

# Using functools.lru_cache (for memoization)
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Check cache stats
fibonacci(100)
print(fibonacci.cache_info())
# CacheInfo(hits=98, misses=101, maxsize=128, currsize=101)

# Manual implementation (hash map + doubly linked list)
class DLLNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCacheManual:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Dummy head and tail
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_end(self, node):
        """Add node before tail (most recent)"""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node):
        """Remove node from list"""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_end(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = DLLNode(key, value)
        self.cache[key] = node
        self._add_to_end(node)

        if len(self.cache) > self.capacity:
            # Remove LRU (after head)
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

# Usage
cache = LRUCache(2)
cache.put(1, 1)      # cache: {1=1}
cache.put(2, 2)      # cache: {1=1, 2=2}
cache.get(1)         # returns 1, cache: {2=2, 1=1}
cache.put(3, 3)      # evicts 2, cache: {1=1, 3=3}
cache.get(2)         # returns -1 (not found)
```

### Time complexity
- **Get**: O(1) - hash lookup + move to end
- **Put**: O(1) - hash update + potential eviction
- **Delete**: O(1) - hash delete + list removal

### Space complexity
O(n) where n is the capacity. Each entry stores key, value, and two pointers (for doubly linked list) plus hash table overhead.

### Trade-offs
**Pros:**
- O(1) all operations
- Automatic memory management
- Good cache hit rates for temporal locality
- Simple to understand and implement

**Cons:**
- Fixed capacity requires tuning
- Not optimal for all access patterns
- Extra memory for linked list pointers
- Single eviction policy

### Variants
- **LRU-K**: Consider last K accesses instead of just most recent
- **2Q (Two Queue)**: Separate queues for new and frequently accessed
- **ARC (Adaptive Replacement Cache)**: Dynamically balances recency and frequency
- **SLRU (Segmented LRU)**: Protected and probationary segments

### When to use vs avoid
- **Use when**: Access patterns show temporal locality, fixed memory budget, need fast eviction
- **Avoid when**: Access is uniform random (no benefit), frequency matters more than recency (use LFU)

### Related
- [LFU Cache](./lfuCache.md)
- [Hash Map](../hashBased/hashmap.md)
- [Doubly Linked List](../sequenceTypes/doublyLinkedList.md)
