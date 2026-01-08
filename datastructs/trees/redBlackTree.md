# Red-Black Tree
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Trees`

### Topics
**Topics:** `balanced BST`, `ordered maps/sets`, `language libraries`, `consistent performance`

### Definition
A self-balancing binary search tree where each node has a color (red or black) and specific properties that ensure the tree remains approximately balanced, guaranteeing O(log n) operations.

### Use cases
- Standard library implementations (C++ map/set, Java TreeMap/TreeSet)
- Linux kernel scheduling (CFS scheduler)
- Database indexing with frequent updates
- Applications with mixed read/write workloads

### Attributes
- Every node is red or black
- Root is always black
- Red nodes cannot have red children (no red-red)
- Every path from root to null has same number of black nodes
- Less strictly balanced than AVL but fewer rotations

### Common operations

| Operation | Time     | Description |
|-----------|----------|-------------|
| Search    | O(log n) | Standard BST search |
| Insert    | O(log n) | Insert + recolor/rotate |
| Delete    | O(log n) | Delete + recolor/rotate |
| Min/Max   | O(log n) | Traverse to leaf |

### In code
```python
RED = True
BLACK = False

class RBNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.color = RED  # New nodes are red

class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None)
        self.NIL.color = BLACK
        self.root = self.NIL

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, val):
        node = RBNode(val)
        node.left = self.NIL
        node.right = self.NIL

        # Standard BST insert
        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if node.val < current.val:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.val < parent.val:
            parent.left = node
        else:
            parent.right = node

        # Fix Red-Black properties
        self._fix_insert(node)

    def _fix_insert(self, node):
        while node.parent and node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RED:
                    # Case 1: Uncle is red - recolor
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 2: Node is right child - left rotate
                        node = node.parent
                        self.rotate_left(node)
                    # Case 3: Node is left child - right rotate
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.rotate_right(node.parent.parent)
            else:
                # Mirror cases for right subtree
                uncle = node.parent.parent.left
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.rotate_left(node.parent.parent)
        self.root.color = BLACK
```

### Time complexity
- **All operations**: O(log n) guaranteed
- **Rotations per insert**: At most 2
- **Rotations per delete**: At most 3
- **Height**: At most 2 * log(n+1)

### Space complexity
O(n) for n nodes. Each node stores one bit for color (often uses full byte in practice). Uses sentinel NIL nodes to simplify boundary cases.

### Trade-offs
**Pros:**
- Guaranteed O(log n) operations
- Fewer rotations than AVL (faster insert/delete)
- Used in major language standard libraries
- Constant-time rotations per operation

**Cons:**
- Slightly less balanced than AVL (slower lookups)
- Complex implementation
- More cases to handle than AVL

### Variants
- **Left-leaning Red-Black Tree (LLRB)**: Simplified variant with left-leaning reds only
- **AA Tree**: Simpler variant with only right-leaning reds
- **2-3-4 Tree**: Equivalent representation using multiway nodes

### When to use vs avoid
- **Use when**: Frequent insertions/deletions, need guaranteed O(log n), implementing ordered map/set
- **Avoid when**: Lookups dominate (AVL may be slightly faster), simple unbalanced BST suffices, custom balancing not needed

### Related
- [Binary Search Tree](./bst.md)
- [AVL Tree](./avlTree.md)
- [Binary Tree](./binaryTree.md)
