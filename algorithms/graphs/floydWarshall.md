# Floyd-Warshall Algorithm
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Shortest Path`

### Topics
**Topics:** `all-pairs shortest path`, `dynamic programming`, `transitive closure`, `dense graphs`

### Definition
A dynamic programming algorithm that finds the shortest paths between all pairs of vertices in a weighted graph, including graphs with negative edges (but no negative cycles).

### Use cases
- All-pairs shortest path computation
- Transitive closure of a graph
- Finding graph diameter
- Network analysis
- Detecting negative cycles

### Prerequisites
- Graph represented as adjacency matrix
- Understanding of dynamic programming
- Handling of infinity values

### Step-by-step
1. Initialize distance matrix from adjacency matrix
2. For each intermediate vertex k:
3. For each pair (i, j), check if path through k is shorter
4. If dist[i][k] + dist[k][j] < dist[i][j], update
5. After all k, matrix contains shortest distances
6. Negative values on diagonal indicate negative cycle

### In code
```python
def floyd_warshall(graph):
    """
    Find shortest paths between all pairs.
    graph: 2D matrix where graph[i][j] is weight from i to j
           Use float('inf') for no direct edge
    """
    n = len(graph)

    # Initialize distance matrix
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]

    # Set diagonal to 0
    for i in range(n):
        dist[i][i] = 0

    # Dynamic programming: try each vertex as intermediate
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Check for negative cycles
    for i in range(n):
        if dist[i][i] < 0:
            raise ValueError("Graph contains negative cycle")

    return dist

def floyd_warshall_with_path(graph):
    """Find shortest paths and reconstruct paths"""
    n = len(graph)
    INF = float('inf')

    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    next_vertex = [[j if graph[i][j] != INF else None for j in range(n)] for i in range(n)]

    for i in range(n):
        dist[i][i] = 0
        next_vertex[i][i] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_vertex[i][j] = next_vertex[i][k]

    return dist, next_vertex

def reconstruct_path(next_vertex, u, v):
    """Reconstruct path from u to v"""
    if next_vertex[u][v] is None:
        return []

    path = [u]
    while u != v:
        u = next_vertex[u][v]
        path.append(u)

    return path

def transitive_closure(graph):
    """
    Find if path exists between all pairs.
    graph: adjacency matrix (1 for edge, 0 for no edge)
    """
    n = len(graph)
    reach = [[graph[i][j] for j in range(n)] for i in range(n)]

    for i in range(n):
        reach[i][i] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

    return reach

def graph_diameter(dist):
    """Find the longest shortest path (diameter)"""
    max_dist = 0
    for row in dist:
        for d in row:
            if d != float('inf'):
                max_dist = max(max_dist, d)
    return max_dist

# Build matrix from edges
def build_matrix(n, edges):
    INF = float('inf')
    matrix = [[INF] * n for _ in range(n)]

    for i in range(n):
        matrix[i][i] = 0

    for u, v, w in edges:
        matrix[u][v] = w

    return matrix

# Usage
INF = float('inf')
graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

dist = floyd_warshall(graph)
print("Distance matrix:")
for row in dist:
    print(row)
# [0, 5, 8, 9]
# [inf, 0, 3, 4]
# [inf, inf, 0, 1]
# [inf, inf, inf, 0]

dist, next_v = floyd_warshall_with_path(graph)
print("Path from 0 to 3:", reconstruct_path(next_v, 0, 3))
# [0, 1, 2, 3]
```

### Time complexity

| Case | Complexity |
|------|------------|
| All  | O(V³)      |

Three nested loops over V vertices.

### Space complexity
O(V²) for the distance matrix. Additional O(V²) for path reconstruction.

### Edge cases
- Negative cycles (detect via negative diagonal)
- Disconnected pairs (remain at infinity)
- Self-loops with negative weight
- Dense vs sparse graphs

### Variants
- **Warshall's algorithm**: Just transitive closure (boolean)
- **Johnson's algorithm**: Better for sparse graphs, O(V² log V + VE)
- **Blocked Floyd-Warshall**: Cache-efficient for large graphs

### When to use vs avoid
- **Use when**: Need all-pairs shortest paths, dense graphs, graph is small-medium, transitive closure needed
- **Avoid when**: Sparse graphs (Johnson's better), only need single-source (Dijkstra), very large graphs

### Related
- [Dijkstra](./dijkstra.md)
- [Bellman-Ford](./bellmanFord.md)
