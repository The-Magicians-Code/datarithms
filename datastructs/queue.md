# Queue
[Back](./summary.md)
[Home](../index.md)

### Category
**Category:** `Stacks & Queues`

### Topics
**Topics:** `BFS`, `task scheduling`, `message queues`, `buffering`

### Definition
A linear data structure following First-In-First-Out (FIFO) principle, where elements are added at the rear and removed from the front.

### Use cases
- Breadth-first search (BFS)
- Task scheduling and job queues
- Print spooling
- Message queues in distributed systems
- Buffering data streams

### Attributes
- FIFO (First-In-First-Out) ordering
- Enqueue at rear, dequeue from front
- Can be implemented with array, linked list, or circular buffer
- Constant time operations with proper implementation

### Common operations

| Operation | Time | Description |
|-----------|------|-------------|
| Enqueue   | O(1) | Add element to rear |
| Dequeue   | O(1) | Remove and return front element |
| Peek/Front| O(1) | View front element without removing |
| IsEmpty   | O(1) | Check if queue is empty |
| Size      | O(1) | Get number of elements |

### In code
```python
# Using collections.deque (recommended)
from collections import deque

queue = deque()
queue.append(1)      # Enqueue
queue.append(2)
front = queue.popleft()  # Dequeue - returns 1
peek = queue[0]      # Peek front

# Using queue.Queue (thread-safe)
from queue import Queue

q = Queue()
q.put(1)             # Enqueue
q.put(2)
front = q.get()      # Dequeue - blocks if empty

# Queue class implementation
class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# BFS using queue
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

# Level-order tree traversal
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

### Time complexity
- **Enqueue/Dequeue/Peek**: O(1) with deque or circular array
- **Enqueue**: O(1) amortized with list (O(n) for dequeue from front!)
- **Search**: O(n) - must traverse queue

**Warning**: Using Python list with `pop(0)` is O(n). Always use `collections.deque` for queues.

### Space complexity
O(n) for n elements. Deque implementation uses a doubly-linked list of fixed-size blocks.

### Trade-offs
**Pros:**
- Simple FIFO semantics
- O(1) operations with proper implementation
- Natural for scheduling and BFS
- Thread-safe options available

**Cons:**
- Only access to front element
- No random access
- List-based implementation has O(n) dequeue

### Variants
- **Priority queue**: Dequeue by priority (use heap)
- **Circular queue**: Fixed-size with wrap-around
- **Double-ended queue (deque)**: Insert/remove from both ends
- **Blocking queue**: Waits when empty/full (for concurrency)

### When to use vs avoid
- **Use when**: Need FIFO ordering, BFS, task scheduling, producer-consumer patterns
- **Avoid when**: Need LIFO (use stack), need random access, need priority ordering (use heap)

### Related
- [Stack](./stack.md)
- [Deque](./deque.md)
- [Heap](./trees/heap.md)
