# Union-Find (Disjoint Set Union)
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Graphs`

### Topics
**Topics:** `connectivity`, `Kruskal's algorithm`, `clustering`, `network connectivity`

### Definition
A data structure that tracks a set of elements partitioned into disjoint subsets, supporting efficient union of sets and finding which set an element belongs to.

### Use cases
- Detecting cycles in graphs (Kruskal's MST)
- Network connectivity queries
- Image processing (connected components)
- Social network friend groups
- Equivalence class problems

### Attributes
- Each set has a representative (root) element
- Path compression flattens tree structure
- Union by rank keeps trees balanced
- Near-constant time operations with optimizations

### Common operations

| Operation | Time (optimized) | Description |
|-----------|------------------|-------------|
| MakeSet   | O(1)             | Create set with single element |
| Find      | O(α(n))          | Find set representative |
| Union     | O(α(n))          | Merge two sets |
| Connected | O(α(n))          | Check if same set |

*α(n) is the inverse Ackermann function, effectively constant (< 5 for all practical n)*

### In code
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # Number of disjoint sets

    def find(self, x):
        """Find root with path compression - O(α(n))"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union by rank - O(α(n))"""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same set

        # Attach smaller tree under larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.count -= 1
        return True

    def connected(self, x, y):
        """Check if x and y are in the same set"""
        return self.find(x) == self.find(y)

    def get_count(self):
        """Return number of disjoint sets"""
        return self.count

# Usage: Detecting cycle in undirected graph
def has_cycle(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        if uf.connected(u, v):
            return True  # Edge connects nodes in same component
        uf.union(u, v)
    return False

# Usage: Kruskal's MST
def kruskal_mst(n, edges):
    """edges: list of (weight, u, v)"""
    uf = UnionFind(n)
    mst = []
    edges.sort()  # Sort by weight

    for weight, u, v in edges:
        if not uf.connected(u, v):
            uf.union(u, v)
            mst.append((u, v, weight))
            if len(mst) == n - 1:
                break

    return mst

# Usage: Number of connected components
def count_components(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.get_count()

# Example
uf = UnionFind(5)  # Elements 0, 1, 2, 3, 4
uf.union(0, 1)
uf.union(2, 3)
uf.union(1, 2)

print(uf.connected(0, 3))  # True (0-1-2-3)
print(uf.connected(0, 4))  # False (4 is isolated)
print(uf.get_count())      # 2 sets: {0,1,2,3} and {4}
```

### Time complexity
- **Without optimizations**: O(n) per operation in worst case
- **With path compression only**: O(log n) amortized
- **With union by rank only**: O(log n) worst case
- **With both optimizations**: O(α(n)) amortized - effectively O(1)

*α(n) is the inverse Ackermann function, which is ≤ 4 for any n < 10^600*

### Space complexity
O(n) for parent and rank arrays. No additional space for operations.

### Trade-offs
**Pros:**
- Near-constant time operations with optimizations
- Simple implementation
- No pointer overhead (uses arrays)
- Excellent for dynamic connectivity

**Cons:**
- Cannot efficiently split sets (union only)
- Elements must be indexed 0 to n-1 (or use hash map)
- Not suitable for finding all members of a set efficiently

### Variants
- **Weighted union-find**: Track size of each set
- **Union by size**: Alternative to rank, attach smaller to larger
- **Persistent union-find**: Maintain history of operations
- **Union-find with rollback**: Undo unions (for backtracking)

### When to use vs avoid
- **Use when**: Need dynamic connectivity queries, cycle detection, finding connected components, Kruskal's MST
- **Avoid when**: Need to split sets, iterate over set members, find shortest paths (use BFS)

### Related
- [Graph](./graph.md)
- [Hash Map](../hashBased/hashmap.md)
