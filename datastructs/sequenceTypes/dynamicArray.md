# Dynamic Array
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Sequence types`

### Topics
**Topics:** `amortized analysis`, `resizing`, `contiguous storage`, `memory management`

### Definition
A resizable array that automatically grows or shrinks as elements are added or removed, providing O(1) amortized append operations.

### Use cases
- Collections where the final size is unknown at creation time
- Implementing stacks with array backing
- Buffers that need to grow dynamically
- Any scenario requiring flexible-size sequential storage

### Attributes
- Contiguous memory allocation like static arrays
- Automatic resizing when capacity is exceeded
- Growth factor determines memory/time trade-off (typically 1.5x-2x)
- May have unused capacity (allocated but not filled)

### Common operations

| Operation | Time Complexity | Description |
|-----------|-----------------|-------------|
| Access    | O(1)            | Get element at index |
| Search    | O(n)            | Linear scan for value |
| Append    | O(1) amortized  | Add to end, may trigger resize |
| Insert    | O(n)            | Shift elements right |
| Delete    | O(n)            | Shift elements left |
| Resize    | O(n)            | Copy all elements to new array |

### In code
```python
# Python list IS a dynamic array
nums = []

# Append - O(1) amortized
for i in range(10):
    nums.append(i)

# Insert at position - O(n)
nums.insert(0, -1)

# Pop from end - O(1)
nums.pop()

# Pop from position - O(n)
nums.pop(0)

# Simple dynamic array implementation
class DynamicArray:
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._arr = [None] * self._capacity

    def append(self, item):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._arr[self._size] = item
        self._size += 1

    def _resize(self, new_cap):
        new_arr = [None] * new_cap
        for i in range(self._size):
            new_arr[i] = self._arr[i]
        self._arr = new_arr
        self._capacity = new_cap
```

### Time complexity
- **Access**: O(1) - direct index calculation
- **Append**: O(1) amortized, O(n) worst case during resize
- **Insert/Delete**: O(n) - requires shifting elements
- **Resize**: O(n) - copying all elements

**Amortized analysis**: With 2x growth factor, the amortized cost per append is O(1) because expensive resizes happen exponentially less frequently.

### Space complexity
O(n) for elements, but may use up to 2n space due to pre-allocated capacity. No auxiliary space during normal operations; O(n) temporary during resize.

### Trade-offs
**Pros:**
- Flexible size without manual memory management
- O(1) random access like static arrays
- Cache-friendly due to contiguous memory
- O(1) amortized append

**Cons:**
- Wasted space from over-allocation
- Occasional expensive O(n) resize operations
- Insert/delete in middle still O(n)

### Variants
- **Growth factor 1.5x**: Java ArrayList - less memory waste, more frequent resizes
- **Growth factor 2x**: Simpler analysis, more memory overhead
- **Python list**: Growth factor ~1.125x for large lists

### When to use vs avoid
- **Use when**: Need flexible-size collection with fast index access and mostly append operations
- **Avoid when**: Frequent insertions/deletions in middle (use linked list), or memory is very constrained

### Related
- [Array](./array.md)
- [Singly Linked List](./singlyLinkedList.md)
- [Doubly Linked List](./doublyLinkedList.md)
