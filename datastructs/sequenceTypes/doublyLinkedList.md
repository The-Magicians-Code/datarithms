# Doubly Linked List
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Sequence types`

### Topics
**Topics:** `pointer manipulation`, `LRU caches`, `browser history`, `undo/redo systems`

### Definition
A linear data structure where each node contains data and two pointers - one to the next node and one to the previous node - enabling bidirectional traversal.

### Use cases
- Browser history navigation (back and forward)
- Music playlist navigation (previous/next track)
- Undo/redo functionality in applications
- LRU cache implementation (quick removal from middle)

### Attributes
- Each node has prev and next pointers
- Bidirectional traversal capability
- Efficient insertion/deletion when node reference is known
- Higher memory overhead than singly linked list

### Common operations

| Operation         | Time Complexity | Description |
|-------------------|-----------------|-------------|
| Access            | O(n)            | Traverse from head or tail |
| Search            | O(n)            | Linear scan in either direction |
| Insert (head)     | O(1)            | Update head and its neighbor |
| Insert (tail)     | O(1)            | Update tail and its neighbor |
| Insert (at node)  | O(1)            | Update prev/next pointers |
| Delete (head)     | O(1)            | Update head pointer |
| Delete (tail)     | O(1)            | Update tail pointer |
| Delete (at node)  | O(1)            | Update neighbor pointers |

### In code
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Insert at tail - O(1)"""
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        """Insert at head - O(1)"""
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, node):
        """Delete given node - O(1)"""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def traverse_forward(self):
        """Traverse head to tail"""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def traverse_backward(self):
        """Traverse tail to head"""
        current = self.tail
        while current:
            yield current.data
            current = current.prev
```

### Time complexity
- **Access**: O(n) - must traverse, but can start from either end
- **Search**: O(n) - linear scan, can search from both directions
- **Insert at head/tail**: O(1) - pointer updates only
- **Insert at known node**: O(1) - update four pointers
- **Delete at head/tail**: O(1) - pointer updates only
- **Delete known node**: O(1) - no need to find predecessor

### Space complexity
O(n) for n elements. Each node requires extra space for two pointers (prev and next), typically 16 bytes on 64-bit systems. No auxiliary space for operations.

### Trade-offs
**Pros:**
- O(1) insertion/deletion at both ends
- O(1) deletion when node reference is known (no predecessor search)
- Bidirectional traversal
- Easier to reverse than singly linked list

**Cons:**
- Double memory overhead for pointers vs singly linked
- More complex implementation
- Still O(n) access time (no random access)
- Poor cache locality

### Variants
- **Circular doubly linked list**: Tail's next points to head, head's prev points to tail
- **With sentinel nodes**: Dummy head and tail nodes simplify edge cases
- **XOR linked list**: Memory-efficient variant using XOR of addresses (rarely used in practice)

### When to use vs avoid
- **Use when**: Need bidirectional traversal, frequent deletions at known positions, implementing LRU cache, browser-like navigation
- **Avoid when**: Memory is constrained, only need forward traversal, simple stack/queue operations suffice

### Related
- [Singly Linked List](./singlyLinkedList.md)
- [Array](./array.md)
- [Dynamic Array](./dynamicArray.md)
