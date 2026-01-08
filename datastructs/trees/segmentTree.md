# Segment Tree
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Trees`

### Topics
**Topics:** `range queries`, `interval updates`, `competitive programming`, `range minimum/maximum`

### Definition
A binary tree data structure that stores information about array intervals (segments), enabling efficient range queries and point updates in O(log n) time.

### Use cases
- Range sum/min/max queries
- Finding GCD/LCM over a range
- Counting elements in a range
- Range updates with lazy propagation
- Competitive programming problems

### Attributes
- Each node represents an interval of the array
- Root covers entire array [0, n-1]
- Leaf nodes represent individual elements
- Internal nodes store aggregate of children (sum, min, max, etc.)

### Common operations

| Operation      | Time     | Description |
|----------------|----------|-------------|
| Build          | O(n)     | Construct tree from array |
| Query          | O(log n) | Get aggregate over range |
| Point update   | O(log n) | Update single element |
| Range update   | O(log n) | Update range (with lazy prop) |

### In code
```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self._build(arr)

    def _build(self, arr):
        # Store leaves at indices [n, 2n-1]
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        # Build internal nodes bottom-up
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, idx, val):
        """Point update - O(log n)"""
        idx += self.n
        self.tree[idx] = val
        # Update ancestors
        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def query(self, left, right):
        """Range sum query [left, right) - O(log n)"""
        result = 0
        left += self.n
        right += self.n
        while left < right:
            if left % 2 == 1:  # left is right child
                result += self.tree[left]
                left += 1
            if right % 2 == 1:  # right is right child
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

# Usage
arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)

st.query(1, 4)   # Sum of arr[1:4] = 3+5+7 = 15
st.update(2, 6)  # arr[2] = 6
st.query(1, 4)   # Sum = 3+6+7 = 16

# Recursive implementation (more intuitive)
class SegmentTreeRecursive:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self._build(arr, 1, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self._build(arr, 2 * node, start, mid)
            self._build(arr, 2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0  # Out of range
        if left <= start and end <= right:
            return self.tree[node]  # Fully in range
        mid = (start + end) // 2
        return (self.query(2 * node, start, mid, left, right) +
                self.query(2 * node + 1, mid + 1, end, left, right))
```

### Time complexity
- **Build**: O(n) - visit each element once, fill 2n nodes
- **Query**: O(log n) - traverse at most 2 nodes per level
- **Point update**: O(log n) - update path from leaf to root
- **Range update (lazy)**: O(log n) with lazy propagation

### Space complexity
O(n) for iterative implementation (2n nodes). O(4n) for recursive implementation to safely handle all cases. Recursive calls use O(log n) stack space.

### Trade-offs
**Pros:**
- O(log n) query and update
- Flexible - works with any associative operation
- Supports range updates with lazy propagation

**Cons:**
- More complex than simple arrays or prefix sums
- 2-4x memory overhead
- Overkill for static arrays (use prefix sum)

### Variants
- **Lazy propagation**: Defer range updates for efficiency
- **Persistent segment tree**: Keep history of all versions
- **2D segment tree**: For matrix range queries
- **Dynamic segment tree**: Sparse arrays, create nodes on demand

### When to use vs avoid
- **Use when**: Need both range queries AND updates, dynamic array modifications
- **Avoid when**: Array is static (prefix sum is simpler), only need point queries (use array)

### Related
- [Fenwick Tree](./fenwickTree.md)
- [Binary Tree](./binaryTree.md)
