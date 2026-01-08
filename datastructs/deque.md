# Deque (Double-Ended Queue)
[Back](./summary.md)
[Home](../index.md)

### Category
**Category:** `Stacks & Queues`

### Topics
**Topics:** `sliding window`, `BFS`, `task scheduling`, `palindrome checking`

### Definition
A linear data structure that allows insertion and removal of elements from both ends in O(1) time, combining the capabilities of stacks and queues.

### Use cases
- Sliding window problems
- Implementing both stacks and queues
- Browser history (back and forward)
- Undo/redo with bidirectional navigation
- Work-stealing algorithms

### Attributes
- O(1) operations at both ends
- Can act as both stack and queue
- Implemented as doubly-linked list of blocks
- Thread-safe for single-end operations

### Common operations

| Operation    | Time | Description |
|--------------|------|-------------|
| append       | O(1) | Add to right end |
| appendleft   | O(1) | Add to left end |
| pop          | O(1) | Remove from right end |
| popleft      | O(1) | Remove from left end |
| Access [i]   | O(n) | Index access (slow in middle) |
| rotate       | O(k) | Rotate k steps |

### In code
```python
from collections import deque

# Basic operations
d = deque()

# Add elements
d.append(1)         # Right: [1]
d.append(2)         # Right: [1, 2]
d.appendleft(0)     # Left:  [0, 1, 2]

# Remove elements
right = d.pop()     # Returns 2, deque: [0, 1]
left = d.popleft()  # Returns 0, deque: [1]

# Peek (without removing)
d.append(2)
d.append(3)         # [1, 2, 3]
front = d[0]        # 1
back = d[-1]        # 3

# Extend from both ends
d.extend([4, 5])        # [1, 2, 3, 4, 5]
d.extendleft([0, -1])   # [-1, 0, 1, 2, 3, 4, 5] (reversed!)

# Rotate
d.rotate(2)         # Rotate right: [4, 5, -1, 0, 1, 2, 3]
d.rotate(-2)        # Rotate left:  [-1, 0, 1, 2, 3, 4, 5]

# Fixed-size deque (auto-discards old elements)
recent = deque(maxlen=3)
recent.append(1)    # [1]
recent.append(2)    # [1, 2]
recent.append(3)    # [1, 2, 3]
recent.append(4)    # [2, 3, 4] - 1 is discarded

# Sliding window maximum using deque
def max_sliding_window(nums, k):
    result = []
    dq = deque()  # Stores indices of potential maximums

    for i, num in enumerate(nums):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements (they can't be max)
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # Window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Use as stack
stack = deque()
stack.append(1)     # Push
stack.pop()         # Pop

# Use as queue
queue = deque()
queue.append(1)     # Enqueue
queue.popleft()     # Dequeue

# Palindrome check
def is_palindrome(s):
    d = deque(s.lower())
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True
```

### Time complexity
- **append/appendleft**: O(1)
- **pop/popleft**: O(1)
- **Access ends [0], [-1]**: O(1)
- **Access middle [i]**: O(n) - must traverse
- **rotate(k)**: O(k)
- **extend**: O(k) where k is number of elements

### Space complexity
O(n) for n elements. Implemented as doubly-linked list of fixed-size blocks (typically 64 elements per block), providing good cache locality while maintaining O(1) operations at both ends.

### Trade-offs
**Pros:**
- O(1) operations at both ends
- More versatile than stack or queue alone
- Fixed-size option for recent history
- Thread-safe for append/pop operations

**Cons:**
- O(n) random access (unlike list)
- More memory than simple list
- Not as cache-friendly as array for traversal

### Variants
- **Bounded deque**: maxlen parameter limits size
- **Steque**: Stack-ended queue (push at both, pop from one)
- **Output-restricted deque**: Pop only from one end
- **Input-restricted deque**: Push only at one end

### When to use vs avoid
- **Use when**: Need O(1) operations at both ends, sliding window problems, need both stack and queue behavior
- **Avoid when**: Need fast random access (use list), simple LIFO or FIFO suffices (use stack/queue)

### Related
- [Stack](./stack.md)
- [Queue](./queue.md)
- [Circular Buffer](./specialized/circularBuffer.md)
