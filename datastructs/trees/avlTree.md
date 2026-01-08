# AVL Tree
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Trees`

### Topics
**Topics:** `balanced BST`, `ordered maps/sets`, `database indexing`, `consistent performance`

### Definition
A self-balancing binary search tree where the heights of the left and right subtrees of every node differ by at most one, guaranteeing O(log n) operations.

### Use cases
- Database indexing requiring predictable performance
- In-memory ordered dictionaries
- Applications where lookup frequency exceeds insertions
- Real-time systems needing worst-case guarantees

### Attributes
- BST property maintained (left < root < right)
- Balance factor = height(left) - height(right), must be -1, 0, or 1
- Self-balances using rotations after insert/delete
- More strictly balanced than Red-Black trees

### Common operations

| Operation | Time     | Description |
|-----------|----------|-------------|
| Search    | O(log n) | Guaranteed balanced height |
| Insert    | O(log n) | Insert + rebalance |
| Delete    | O(log n) | Delete + rebalance |
| Min/Max   | O(log n) | Traverse to leaf |

### In code
```python
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def height(self, node):
        return node.height if node else 0

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, y):
        """Right rotation for Left-Left case"""
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        """Left rotation for Right-Right case"""
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, root, val):
        # Standard BST insert
        if not root:
            return AVLNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        # Update height
        self.update_height(root)

        # Get balance factor
        balance = self.balance_factor(root)

        # Left-Left case
        if balance > 1 and val < root.left.val:
            return self.rotate_right(root)

        # Right-Right case
        if balance < -1 and val > root.right.val:
            return self.rotate_left(root)

        # Left-Right case
        if balance > 1 and val > root.left.val:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right-Left case
        if balance < -1 and val < root.right.val:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def search(self, root, val):
        if not root or root.val == val:
            return root
        if val < root.val:
            return self.search(root.left, val)
        return self.search(root.right, val)
```

### Time complexity
- **All operations**: O(log n) guaranteed - tree height is always O(log n)
- **Rotations**: O(1) each, at most O(log n) rotations per delete
- **Space for recursion**: O(log n) - balanced height

### Space complexity
O(n) for n nodes. Each node stores additional height information (one integer). Recursive operations use O(log n) stack space.

### Trade-offs
**Pros:**
- Guaranteed O(log n) for all operations
- More balanced than Red-Black (faster lookups)
- Height is at most 1.44 * log(n)

**Cons:**
- More rotations during insert/delete than Red-Black
- Slightly more complex implementation
- Each node stores height (extra memory)

### Variants
- **Weight-balanced trees**: Balance by subtree sizes instead of heights
- **Relaxed AVL**: Allow balance factor up to 2 for fewer rotations
- **AVL with lazy balancing**: Defer rebalancing for batch operations

### When to use vs avoid
- **Use when**: Lookups are more frequent than insertions, need guaranteed O(log n), predictable performance required
- **Avoid when**: Insertions/deletions are frequent (Red-Black may be better), simple BST suffices, memory constrained

### Related
- [Binary Search Tree](./bst.md)
- [Red-Black Tree](./redBlackTree.md)
- [Binary Tree](./binaryTree.md)
