# Fenwick Tree (Binary Indexed Tree)
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Trees`

### Topics
**Topics:** `prefix sums`, `point updates`, `competitive programming`, `inversion counting`

### Definition
A data structure that efficiently maintains prefix sums of an array, supporting both point updates and prefix queries in O(log n) time using clever bit manipulation.

### Use cases
- Dynamic prefix sum queries
- Counting inversions in an array
- Range sum queries with updates
- Frequency tables with updates
- Competitive programming problems

### Attributes
- Uses 1-based indexing internally
- Implicitly stored as array (no pointers)
- Each index stores sum of a specific range based on lowest set bit
- More space-efficient than segment tree

### Common operations

| Operation      | Time     | Description |
|----------------|----------|-------------|
| Build          | O(n)     | Initialize from array |
| Point update   | O(log n) | Add delta to element |
| Prefix sum     | O(log n) | Sum of elements [0, i] |
| Range sum      | O(log n) | Sum of elements [l, r] |

### In code
```python
class FenwickTree:
    def __init__(self, n):
        """Initialize with size n (1-indexed internally)"""
        self.n = n
        self.tree = [0] * (n + 1)

    @classmethod
    def from_array(cls, arr):
        """Build from existing array - O(n)"""
        n = len(arr)
        ft = cls(n)
        for i, val in enumerate(arr):
            ft.update(i, val)
        return ft

    def update(self, idx, delta):
        """Add delta to element at idx (0-indexed) - O(log n)"""
        idx += 1  # Convert to 1-indexed
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)  # Add lowest set bit

    def prefix_sum(self, idx):
        """Sum of elements [0, idx] (0-indexed) - O(log n)"""
        idx += 1  # Convert to 1-indexed
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & (-idx)  # Remove lowest set bit
        return total

    def range_sum(self, left, right):
        """Sum of elements [left, right] (0-indexed) - O(log n)"""
        if left == 0:
            return self.prefix_sum(right)
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

# Usage
arr = [1, 3, 5, 7, 9, 11]
ft = FenwickTree.from_array(arr)

ft.prefix_sum(3)      # Sum of arr[0:4] = 1+3+5+7 = 16
ft.range_sum(1, 4)    # Sum of arr[1:5] = 3+5+7+9 = 24
ft.update(2, 5)       # arr[2] += 5 (now arr[2] = 10)
ft.prefix_sum(3)      # Now = 1+3+10+7 = 21

# Bit manipulation explanation:
# idx & (-idx) extracts the lowest set bit
# Example: 12 = 1100 binary
#         -12 = 0100 (two's complement)
#  12 & (-12) = 0100 = 4

# Counting inversions using Fenwick Tree
def count_inversions(arr):
    """Count pairs (i, j) where i < j and arr[i] > arr[j]"""
    # Coordinate compression
    sorted_arr = sorted(set(arr))
    rank = {v: i for i, v in enumerate(sorted_arr)}

    n = len(sorted_arr)
    ft = FenwickTree(n)
    inversions = 0

    for i in range(len(arr) - 1, -1, -1):
        r = rank[arr[i]]
        inversions += ft.prefix_sum(r - 1) if r > 0 else 0
        ft.update(r, 1)

    return inversions
```

### Time complexity
- **Build**: O(n log n) naive, O(n) optimized
- **Point update**: O(log n) - traverse at most log n ancestors
- **Prefix sum**: O(log n) - traverse at most log n nodes
- **Range sum**: O(log n) - two prefix queries

### Space complexity
O(n) - just an array of size n+1. No pointers or additional structures. More space-efficient than segment tree.

### Trade-offs
**Pros:**
- Very space-efficient (just an array)
- Simple and fast implementation
- Lower constant factor than segment tree
- Easy to extend to 2D

**Cons:**
- Only works for invertible operations (sum, XOR) - not min/max
- Point updates only (no native range updates)
- Less intuitive than segment tree
- 1-based indexing can cause off-by-one errors

### Variants
- **2D Fenwick Tree**: For 2D prefix sums
- **Range update variant**: Support range updates with point queries
- **Fenwick Tree with range updates and queries**: Using two trees

### When to use vs avoid
- **Use when**: Need prefix/range sums with updates, inversion counting, memory constrained
- **Avoid when**: Need range min/max (use segment tree), no updates needed (use prefix sum array)

### Related
- [Segment Tree](./segmentTree.md)
- [Binary Tree](./binaryTree.md)
