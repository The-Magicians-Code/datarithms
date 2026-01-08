# Binary Tree
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Trees`

### Topics
**Topics:** `tree traversal`, `recursion`, `hierarchical data`, `expression parsing`

### Definition
A hierarchical data structure where each node has at most two children, referred to as the left child and right child, with no ordering constraint on node values.

### Use cases
- Representing hierarchical relationships
- Expression trees for parsing mathematical expressions
- Decision trees in machine learning
- Huffman coding trees for compression
- DOM tree representation

### Attributes
- Each node has at most two children
- No ordering constraint on values (unlike BST)
- Can be complete, full, perfect, or balanced
- Height ranges from log(n) (balanced) to n (skewed)

### Common operations

| Operation    | Average | Worst | Description |
|--------------|---------|-------|-------------|
| Search       | O(n)    | O(n)  | Must traverse entire tree |
| Insert       | O(n)    | O(n)  | Find position, then insert |
| Delete       | O(n)    | O(n)  | Find node, then remove |
| Traversal    | O(n)    | O(n)  | Visit all nodes |
| Height       | O(n)    | O(n)  | Calculate tree height |

### In code
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Tree traversals
def preorder(node):
    """Root -> Left -> Right"""
    if node:
        print(node.val)
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    """Left -> Root -> Right"""
    if node:
        inorder(node.left)
        print(node.val)
        inorder(node.right)

def postorder(node):
    """Left -> Right -> Root"""
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val)

def level_order(root):
    """BFS - level by level"""
    if not root:
        return
    from collections import deque
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Common operations
def height(node):
    if not node:
        return -1
    return 1 + max(height(node.left), height(node.right))

def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)
```

### Time complexity
- **All operations**: O(n) worst case - tree may be completely unbalanced
- **Traversal**: O(n) - must visit all nodes
- **Space for recursion**: O(h) where h is height (O(n) worst, O(log n) balanced)

### Space complexity
O(n) for n nodes. Recursive operations use O(h) stack space where h is tree height. Level-order traversal uses O(w) queue space where w is maximum width.

### Trade-offs
**Pros:**
- Simple structure for hierarchical data
- Flexible - no ordering constraints
- Foundation for more specialized trees

**Cons:**
- O(n) search without ordering property
- Can become unbalanced (degenerating to linked list)
- No efficient lookup without additional structure

### Variants
- **Full binary tree**: Every node has 0 or 2 children
- **Complete binary tree**: All levels filled except possibly last (filled left to right)
- **Perfect binary tree**: All internal nodes have 2 children, all leaves at same level
- **Balanced binary tree**: Height difference between subtrees is bounded

### When to use vs avoid
- **Use when**: Need hierarchical structure, expression parsing, decision trees, no ordering needed
- **Avoid when**: Need fast search/lookup (use BST), need guaranteed balance (use AVL/Red-Black)

### Related
- [Binary Search Tree](./bst.md)
- [Heap](./heap.md)
- [AVL Tree](./avlTree.md)
