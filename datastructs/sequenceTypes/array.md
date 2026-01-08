# Array
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Sequence types`

### Topics
**Topics:** `indexing`, `cache locality`, `dynamic programming`, `sliding window`

### Definition
A contiguous block of memory storing elements of the same type, accessed by integer indices starting from 0.

### Use cases
- Storing fixed-size collections where index-based access is frequent
- Implementing matrices and multidimensional data
- Buffer storage for I/O operations
- Foundation for other data structures (heaps, hash tables)

### Attributes
- Elements stored in contiguous memory locations
- Fixed size in static arrays; resizable in dynamic arrays
- Direct index-based access via pointer arithmetic
- Homogeneous element types (in typed languages)

### Common operations

| Operation | Time Complexity | Description |
|-----------|-----------------|-------------|
| Access    | O(1)            | Get element at index |
| Search    | O(n)            | Linear scan for value |
| Insert    | O(n)            | Shift elements right |
| Delete    | O(n)            | Shift elements left |
| Append    | O(1) amortized  | Add to end (dynamic) |

### In code
```python
# Static array (fixed size via array module)
from array import array
arr = array('i', [1, 2, 3, 4, 5])

# Access by index
print(arr[2])  # 3

# Modify element
arr[0] = 10

# Python list as dynamic array
nums = [1, 2, 3]
nums.append(4)      # O(1) amortized
nums.insert(0, 0)   # O(n) - shifts all elements
```

### Time complexity
- **Access**: O(1) - direct index calculation
- **Search**: O(n) - must scan linearly (O(log n) if sorted with binary search)
- **Insert/Delete**: O(n) worst case (beginning), O(1) at end

### Space complexity
O(n) where n is the number of elements. No auxiliary space beyond the array itself.

### Trade-offs
**Pros:**
- Constant-time random access
- Cache-friendly due to contiguous memory
- Simple and efficient for index-based operations

**Cons:**
- Fixed size (static arrays) or expensive resizing (dynamic)
- Insertion/deletion at arbitrary positions is slow
- Wasted space if array is not fully utilized

### Variants
- **Static array**: Fixed size, allocated at compile time
- **Dynamic array**: Resizable (Python list, Java ArrayList, C++ vector)
- **Circular array**: Wraps around for queue implementations

### When to use vs avoid
- **Use when**: You need fast index-based access, data size is known, or cache performance matters
- **Avoid when**: Frequent insertions/deletions in the middle, unknown or highly variable size

### Related
- [Dynamic Array](./dynamicArray.md)
- [Singly Linked List](./singlyLinkedList.md)
- [String](./string.md)
