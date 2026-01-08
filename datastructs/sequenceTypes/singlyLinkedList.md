# Singly Linked List
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Sequence types`

### Topics
**Topics:** `pointer manipulation`, `LRU caches`, `memory-constrained systems`, `dynamic memory allocation`

### Definition
A linear data structure where each element (node) contains data and a pointer to the next node, enabling efficient insertion and deletion without contiguous memory.

### Use cases
- Implementing stacks with O(1) push/pop operations
- Building queues when combined with a tail pointer
- Memory-efficient storage when elements frequently added/removed
- Undo functionality in applications (chain of states)

### Attributes
- Nodes connected via next pointers (one direction only)
- Dynamic size - grows and shrinks as needed
- No random access - must traverse from head
- Memory overhead per element (stores pointer alongside data)

### Common operations

| Operation      | Time Complexity | Description |
|----------------|-----------------|-------------|
| Access         | O(n)            | Traverse from head to index |
| Search         | O(n)            | Linear scan through nodes |
| Insert (head)  | O(1)            | Update head pointer |
| Insert (tail)  | O(n) or O(1)*   | Traverse to end (*O(1) with tail pointer) |
| Insert (middle)| O(n)            | Traverse to position, update pointers |
| Delete (head)  | O(1)            | Update head pointer |
| Delete (other) | O(n)            | Traverse to find predecessor |

### In code
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        """Insert at head - O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        """Insert at tail - O(n)"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, data):
        """Delete first occurrence - O(n)"""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next

    def search(self, data):
        """Search for value - O(n)"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
```

### Time complexity
- **Access**: O(n) - must traverse from head
- **Search**: O(n) - linear scan required
- **Insert at head**: O(1) - pointer update only
- **Insert at tail**: O(n) without tail pointer, O(1) with tail pointer
- **Delete at head**: O(1) - pointer update only
- **Delete at position**: O(n) - must find predecessor

### Space complexity
O(n) for n elements. Each node requires extra space for the next pointer (typically 8 bytes on 64-bit systems). No auxiliary space for operations.

### Trade-offs
**Pros:**
- O(1) insertion/deletion at head
- Dynamic size without reallocation overhead
- Memory allocated only as needed
- Simple implementation

**Cons:**
- O(n) access time (no random access)
- Extra memory per node for pointer storage
- Poor cache locality (nodes scattered in memory)
- Cannot traverse backwards

### Variants
- **With tail pointer**: Maintains reference to last node for O(1) append
- **Circular singly linked list**: Last node points back to head
- **Sentinel node**: Dummy head node simplifies edge cases

### When to use vs avoid
- **Use when**: Frequent insertions/deletions at front, unknown or variable size, implementing stacks/queues
- **Avoid when**: Need random access, cache performance matters, memory overhead per element is a concern

### Related
- [Doubly Linked List](./doublyLinkedList.md)
- [Array](./array.md)
- [Dynamic Array](./dynamicArray.md)
