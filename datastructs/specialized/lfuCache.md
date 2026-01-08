# LFU Cache
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Specialized`

### Topics
**Topics:** `caching`, `frequency-based eviction`, `CDNs`, `database caching`

### Definition
A fixed-capacity cache that evicts the Least Frequently Used item when full, with ties broken by recency (LRU among same frequency).

### Use cases
- CDN caching (popular content stays cached)
- Database query caching
- File system caching
- API rate limiting
- Caching with stable access patterns

### Attributes
- Tracks access frequency for each item
- Evicts least frequently accessed item
- Ties broken by least recently used
- More complex than LRU but better for some workloads

### Common operations

| Operation | Time | Description |
|-----------|------|-------------|
| Get       | O(1) | Retrieve value and increment frequency |
| Put       | O(1) | Insert/update, evict LFU if full |
| Delete    | O(1) | Remove specific key |

### In code
```python
from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0

        # key -> (value, frequency)
        self.cache = {}

        # frequency -> OrderedDict of keys (for LRU within same freq)
        self.freq_to_keys = defaultdict(OrderedDict)

    def _update_freq(self, key):
        """Increment frequency and update data structures"""
        value, freq = self.cache[key]

        # Remove from current frequency list
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Add to new frequency list
        new_freq = freq + 1
        self.freq_to_keys[new_freq][key] = None
        self.cache[key] = (value, new_freq)

    def get(self, key):
        """Get value and increment frequency - O(1)"""
        if key not in self.cache:
            return -1
        self._update_freq(key)
        return self.cache[key][0]

    def put(self, key, value):
        """Insert/update, evict LFU if full - O(1)"""
        if self.capacity <= 0:
            return

        if key in self.cache:
            self.cache[key] = (value, self.cache[key][1])
            self._update_freq(key)
            return

        # Evict if at capacity
        if len(self.cache) >= self.capacity:
            # Get LRU key among minimum frequency keys
            lfu_keys = self.freq_to_keys[self.min_freq]
            evict_key = next(iter(lfu_keys))  # First = LRU
            del lfu_keys[evict_key]
            if not lfu_keys:
                del self.freq_to_keys[self.min_freq]
            del self.cache[evict_key]

        # Insert new key with frequency 1
        self.cache[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1

# Alternative: O(1) LFU with doubly linked lists
class DLLNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add(self, node):
        """Add to end (most recent)"""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1

    def pop_lru(self):
        """Remove and return LRU (first after head)"""
        if self.size == 0:
            return None
        node = self.head.next
        self.remove(node)
        return node

# Usage
cache = LFUCache(2)
cache.put(1, 1)      # freq(1)=1
cache.put(2, 2)      # freq(2)=1
cache.get(1)         # freq(1)=2, returns 1
cache.put(3, 3)      # evicts 2 (LFU), freq(3)=1
cache.get(2)         # returns -1 (not found)
cache.get(3)         # freq(3)=2, returns 3
cache.put(4, 4)      # evicts 1 (freq=2 same as 3, but 1 is LRU)
cache.get(1)         # returns -1
cache.get(3)         # returns 3
cache.get(4)         # returns 4
```

### Time complexity
- **Get**: O(1) - hash lookup + frequency update
- **Put**: O(1) - hash update + potential eviction
- **Delete**: O(1) - hash delete + list removal

Achieving O(1) requires careful data structure design with hash map + frequency-indexed linked lists.

### Space complexity
O(n) where n is the capacity. Stores key, value, frequency, and linked list pointers. Additional O(f) for frequency buckets where f is number of distinct frequencies.

### Trade-offs
**Pros:**
- Better hit rate than LRU for stable access patterns
- Keeps frequently accessed items
- O(1) operations achievable

**Cons:**
- More complex than LRU
- Cache pollution: items with high historical frequency stay even if no longer needed
- Not adaptive to changing access patterns
- New items vulnerable to immediate eviction

### Variants
- **LFU with aging**: Decay frequencies over time to handle changing patterns
- **Window LFU**: Only count frequencies within a time window
- **Adaptive LFU (ARC)**: Dynamically balance LRU and LFU behavior
- **TinyLFU**: Approximate frequency counting for better space efficiency

### When to use vs avoid
- **Use when**: Access patterns are stable, some items are consistently popular, frequency is a good predictor of future access
- **Avoid when**: Access patterns change frequently, new items should get a chance, LRU is simpler and sufficient

### Related
- [LRU Cache](./lruCache.md)
- [Hash Map](../hashBased/hashmap.md)
- [Doubly Linked List](../sequenceTypes/doublyLinkedList.md)
