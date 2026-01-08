# Heap
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Trees`

### Topics
**Topics:** `scheduling`, `top-k problems`, `Dijkstra's algorithm`, `priority queues`

### Definition
A complete binary tree satisfying the heap property: in a min-heap, every parent is smaller than its children; in a max-heap, every parent is larger than its children.

### Use cases
- Priority queues (task scheduling, event simulation)
- Finding k largest/smallest elements
- Dijkstra's and Prim's algorithms
- Heap sort implementation
- Median finding with two heaps

### Attributes
- Complete binary tree (filled level by level, left to right)
- Efficiently stored as array (no pointers needed)
- Root is always min (min-heap) or max (max-heap)
- Parent-child relationship via indices: parent = (i-1)//2, children = 2i+1, 2i+2

### Common operations

| Operation      | Time     | Description |
|----------------|----------|-------------|
| Peek (min/max) | O(1)     | Access root element |
| Insert (push)  | O(log n) | Add element, bubble up |
| Extract (pop)  | O(log n) | Remove root, bubble down |
| Heapify        | O(n)     | Build heap from array |
| Heap sort      | O(n log n)| Sort using heap |

### In code
```python
import heapq

# Python heapq is a MIN-HEAP
nums = [3, 1, 4, 1, 5, 9]

# Build heap in-place - O(n)
heapq.heapify(nums)

# Push element - O(log n)
heapq.heappush(nums, 2)

# Pop minimum - O(log n)
smallest = heapq.heappop(nums)

# Peek minimum - O(1)
smallest = nums[0]

# Push and pop in one operation
heapq.heappushpop(nums, 6)

# Pop and push in one operation
heapq.heapreplace(nums, 0)

# Get k largest/smallest
largest_3 = heapq.nlargest(3, nums)
smallest_3 = heapq.nsmallest(3, nums)

# MAX-HEAP: negate values
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
largest = -heapq.heappop(max_heap)  # 5

# With tuples for priority queue
tasks = []
heapq.heappush(tasks, (1, "high priority"))
heapq.heappush(tasks, (3, "low priority"))
priority, task = heapq.heappop(tasks)

# Manual min-heap implementation
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return root

    def _bubble_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def _bubble_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            left, right = 2 * i + 1, 2 * i + 2
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
```

### Time complexity
- **Peek**: O(1) - root is always at index 0
- **Push/Pop**: O(log n) - bubble up/down through height
- **Heapify**: O(n) amortized - more efficient than n insertions
- **Heap sort**: O(n log n) - n extractions

### Space complexity
O(n) for n elements. Array-based implementation has no pointer overhead. In-place heap sort uses O(1) extra space.

### Trade-offs
**Pros:**
- O(1) access to min/max element
- O(log n) insert and extract
- Array storage is cache-friendly
- Can be built from array in O(n)

**Cons:**
- Only efficient access to root (min or max)
- Search is O(n) - not designed for searching
- Cannot efficiently get both min and max (need two heaps)

### Variants
- **Min-heap**: Root is minimum (Python heapq default)
- **Max-heap**: Root is maximum (negate values in Python)
- **Binary heap**: Standard 2 children per node
- **d-ary heap**: Each node has d children
- **Fibonacci heap**: Better amortized bounds for decrease-key

### When to use vs avoid
- **Use when**: Need quick access to min/max, priority queue, top-k problems, graph algorithms
- **Avoid when**: Need to search for arbitrary elements, need both min and max frequently

### Related
- [Binary Tree](./binaryTree.md)
- [Binary Search Tree](./bst.md)
