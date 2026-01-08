# Graph
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Graphs`

### Topics
**Topics:** `networks`, `dependencies`, `routing`, `social graphs`

### Definition
A non-linear data structure consisting of vertices (nodes) and edges (connections between nodes), used to represent relationships and networks.

### Use cases
- Social networks (users and connections)
- Road/flight networks (locations and routes)
- Dependency graphs (build systems, package managers)
- Web crawling (pages and links)
- Recommendation systems

### Attributes
- Vertices (nodes) represent entities
- Edges represent relationships between entities
- Can be directed or undirected
- Can be weighted or unweighted
- May contain cycles or be acyclic (DAG)

### Common operations

| Operation        | Adj List | Adj Matrix | Description |
|------------------|----------|------------|-------------|
| Add vertex       | O(1)     | O(V²)      | Add new node |
| Add edge         | O(1)     | O(1)       | Connect two nodes |
| Remove vertex    | O(V+E)   | O(V²)      | Remove node and edges |
| Remove edge      | O(E)     | O(1)       | Remove connection |
| Check edge       | O(V)     | O(1)       | Check if edge exists |
| Get neighbors    | O(1)     | O(V)       | Get adjacent nodes |
| BFS/DFS          | O(V+E)   | O(V²)      | Traverse graph |

### In code
```python
from collections import defaultdict, deque

# Adjacency List (most common for sparse graphs)
class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))

    def get_neighbors(self, v):
        return self.graph[v]

    def bfs(self, start):
        """Breadth-first search - O(V+E)"""
        visited = set([start])
        queue = deque([start])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor, _ in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start):
        """Depth-first search - O(V+E)"""
        visited = set()
        result = []

        def dfs_helper(node):
            visited.add(node)
            result.append(node)
            for neighbor, _ in self.graph[node]:
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start)
        return result

    def has_path(self, src, dst):
        """Check if path exists between two nodes"""
        visited = set()
        stack = [src]
        while stack:
            node = stack.pop()
            if node == dst:
                return True
            if node not in visited:
                visited.add(node)
                for neighbor, _ in self.graph[node]:
                    stack.append(neighbor)
        return False

# Adjacency Matrix (for dense graphs)
class GraphMatrix:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight=1):
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight  # Remove for directed

    def has_edge(self, u, v):
        return self.matrix[u][v] != 0

# Usage
g = Graph(directed=False)
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')

print(g.bfs('A'))  # ['A', 'B', 'C', 'D']
print(g.dfs('A'))  # ['A', 'B', 'D', 'C']
```

### Time complexity
**Adjacency List** (V vertices, E edges):
- Space: O(V + E)
- Add edge: O(1)
- Check edge: O(degree)
- Iterate neighbors: O(degree)
- BFS/DFS: O(V + E)

**Adjacency Matrix** (V vertices):
- Space: O(V²)
- Add/remove edge: O(1)
- Check edge: O(1)
- Iterate neighbors: O(V)
- BFS/DFS: O(V²)

### Space complexity
- **Adjacency List**: O(V + E) - efficient for sparse graphs
- **Adjacency Matrix**: O(V²) - fixed size regardless of edges

### Trade-offs
**Adjacency List:**
- Pros: Space-efficient for sparse graphs, fast neighbor iteration
- Cons: O(degree) edge lookup

**Adjacency Matrix:**
- Pros: O(1) edge lookup, simple implementation
- Cons: O(V²) space, inefficient for sparse graphs

### Variants
- **Directed graph (Digraph)**: Edges have direction
- **Weighted graph**: Edges have associated weights
- **DAG**: Directed acyclic graph
- **Multigraph**: Multiple edges between same nodes allowed
- **Bipartite graph**: Nodes split into two sets with edges only between sets

### When to use vs avoid
- **Use when**: Modeling relationships/networks, pathfinding, dependency resolution
- **Avoid when**: Simple hierarchical data (use tree), sequential data (use list)

### Related
- [Union-Find](./unionFind.md)
- [Binary Tree](../trees/binaryTree.md)
