# Stack
[Back](./summary.md)
[Home](../index.md)

### Category
**Category:** `Stacks & Queues`

### Topics
**Topics:** `parsing`, `recursion`, `expression evaluation`, `backtracking`

### Definition
A linear data structure following Last-In-First-Out (LIFO) principle, where elements are added and removed from the same end (top).

### Use cases
- Function call stack (recursion)
- Expression evaluation and parsing
- Undo/redo operations
- Backtracking algorithms (DFS, maze solving)
- Balanced parentheses checking

### Attributes
- LIFO (Last-In-First-Out) ordering
- Operations only at top of stack
- Can be implemented with array or linked list
- Constant time push and pop operations

### Common operations

| Operation | Time | Description |
|-----------|------|-------------|
| Push      | O(1) | Add element to top |
| Pop       | O(1) | Remove and return top element |
| Peek/Top  | O(1) | View top element without removing |
| IsEmpty   | O(1) | Check if stack is empty |
| Size      | O(1) | Get number of elements |

### In code
```python
# Python list as stack (simplest)
stack = []
stack.append(1)     # Push
stack.append(2)
top = stack.pop()   # Pop - returns 2
peek = stack[-1]    # Peek - returns 1

# Using collections.deque (more efficient)
from collections import deque
stack = deque()
stack.append(1)     # Push
stack.pop()         # Pop

# Stack class implementation
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Classic problem: Valid parentheses
def is_valid_parens(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0

# Monotonic stack (find next greater element)
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []  # Stack of indices
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            result[stack.pop()] = num
        stack.append(i)
    return result
```

### Time complexity
- **Push/Pop/Peek**: O(1) - operations at one end only
- **Search**: O(n) - must traverse stack (not a typical operation)
- **Access by index**: O(n) - must pop elements (not recommended)

### Space complexity
O(n) for n elements. Array-based implementation may have unused capacity. Linked-list-based uses extra space for pointers.

### Trade-offs
**Pros:**
- Simple and intuitive
- O(1) push/pop operations
- Natural for LIFO problems
- Useful for tracking state in recursion

**Cons:**
- Only access to top element
- No random access
- Search requires popping elements

### Variants
- **Min stack**: Track minimum element in O(1)
- **Max stack**: Track maximum element in O(1)
- **Two-stack queue**: Implement queue using two stacks
- **Monotonic stack**: Maintain sorted order for range queries

### When to use vs avoid
- **Use when**: Need LIFO ordering, parsing expressions, backtracking, tracking nested structures
- **Avoid when**: Need FIFO (use queue), need random access (use array)

### Related
- [Queue](./queue.md)
- [Deque](./deque.md)
- [Dynamic Array](./sequenceTypes/dynamicArray.md)
