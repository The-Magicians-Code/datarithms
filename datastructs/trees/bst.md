# Binary Search Tree
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Trees`

### Topics
**Topics:** `ordered data`, `range queries`, `in-order traversal`, `searching`

### Definition
A binary tree where each node's left subtree contains only values less than the node, and the right subtree contains only values greater, enabling O(log n) average-case search.

### Use cases
- Implementing ordered sets and maps
- Database indexing
- Range queries (find all values between x and y)
- Autocomplete systems
- Symbol tables in compilers

### Attributes
- Left child < parent < right child (BST property)
- In-order traversal yields sorted sequence
- O(log n) operations when balanced
- Degenerates to O(n) when unbalanced

### Common operations

| Operation    | Average   | Worst | Description |
|--------------|-----------|-------|-------------|
| Search       | O(log n)  | O(n)  | Binary search down tree |
| Insert       | O(log n)  | O(n)  | Find position, add node |
| Delete       | O(log n)  | O(n)  | Remove with successor replacement |
| Min/Max      | O(log n)  | O(n)  | Leftmost/rightmost node |
| In-order     | O(n)      | O(n)  | Sorted traversal |

### In code
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = TreeNode(val)

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if not node or node.val == val:
            return node
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)

    def find_min(self, node):
        """Find minimum value (leftmost node)"""
        while node.left:
            node = node.left
        return node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Node with one or no child
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Node with two children: get inorder successor
            successor = self.find_min(node.right)
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)
        return node
```

### Time complexity
- **Average case**: O(log n) for search, insert, delete - tree is reasonably balanced
- **Worst case**: O(n) when tree degenerates to linked list (sorted insertions)
- **In-order traversal**: O(n) - visits all nodes in sorted order

### Space complexity
O(n) for n nodes. Recursive operations use O(h) stack space. Worst case h = n (skewed), best case h = log n (balanced).

### Trade-offs
**Pros:**
- O(log n) average operations
- In-order traversal gives sorted output
- Supports range queries efficiently
- Dynamic - can insert/delete

**Cons:**
- O(n) worst case when unbalanced
- No guaranteed balance (use AVL or Red-Black for that)
- More complex deletion than insertion

### Variants
- **AVL Tree**: Self-balancing with height difference <= 1
- **Red-Black Tree**: Self-balancing with color properties
- **Splay Tree**: Self-adjusting, recently accessed nodes near root
- **Treap**: BST with heap property using random priorities

### When to use vs avoid
- **Use when**: Need ordered operations, range queries, moderate insert/delete frequency
- **Avoid when**: Data is sorted (causes O(n) operations), need guaranteed O(log n) (use AVL/Red-Black)

### Related
- [Binary Tree](./binaryTree.md)
- [AVL Tree](./avlTree.md)
- [Red-Black Tree](./redBlackTree.md)
