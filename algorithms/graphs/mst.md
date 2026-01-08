# Minimum Spanning Tree (MST)
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Graph Algorithms`

### Topics
**Topics:** `network design`, `clustering`, `cost optimization`, `greedy algorithms`

### Definition
A subset of edges that connects all vertices in an undirected weighted graph with the minimum possible total edge weight, forming a tree (no cycles).

### Use cases
- Network design (cable, pipeline layout)
- Clustering algorithms
- Image segmentation
- Approximation for traveling salesman
- Circuit design

### Prerequisites
- Undirected weighted graph
- Union-Find for Kruskal's
- Priority queue for Prim's

### Step-by-step
**Kruskal's Algorithm:**
1. Sort all edges by weight
2. For each edge in sorted order:
3. If adding edge doesn't create cycle, add to MST
4. Use Union-Find to detect cycles efficiently
5. Stop when MST has V-1 edges

**Prim's Algorithm:**
1. Start from any vertex, add to MST
2. Add all edges from MST vertices to priority queue
3. Extract minimum edge that connects to non-MST vertex
4. Add that vertex to MST
5. Repeat until all vertices in MST

### In code
```python
import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def kruskal(n, edges):
    """
    Kruskal's algorithm for MST.
    edges: list of (weight, u, v)
    """
    edges.sort()  # Sort by weight
    uf = UnionFind(n)
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        if uf.union(u, v):  # No cycle
            mst.append((u, v, weight))
            total_weight += weight

            if len(mst) == n - 1:
                break

    return mst, total_weight

def prim(n, graph):
    """
    Prim's algorithm for MST.
    graph: dict of {vertex: [(neighbor, weight), ...]}
    """
    visited = [False] * n
    mst = []
    total_weight = 0

    # Start from vertex 0
    pq = [(0, 0, -1)]  # (weight, vertex, from_vertex)

    while pq and len(mst) < n:
        weight, u, from_v = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        if from_v != -1:
            mst.append((from_v, u, weight))
            total_weight += weight

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v, u))

    return mst, total_weight

def prim_adjacency_matrix(matrix):
    """Prim's with adjacency matrix"""
    n = len(matrix)
    INF = float('inf')

    in_mst = [False] * n
    key = [INF] * n
    parent = [-1] * n

    key[0] = 0

    for _ in range(n):
        # Find minimum key vertex not in MST
        min_key = INF
        u = -1
        for v in range(n):
            if not in_mst[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        in_mst[u] = True

        # Update keys of adjacent vertices
        for v in range(n):
            if matrix[u][v] and not in_mst[v] and matrix[u][v] < key[v]:
                key[v] = matrix[u][v]
                parent[v] = u

    # Build MST edges
    mst = []
    total = 0
    for v in range(1, n):
        mst.append((parent[v], v, matrix[parent[v]][v]))
        total += matrix[parent[v]][v]

    return mst, total

# Second best MST
def second_best_mst(n, edges):
    """Find the second minimum spanning tree"""
    mst_edges, mst_weight = kruskal(n, edges)
    mst_set = set((min(u, v), max(u, v)) for u, v, w in mst_edges)

    second_best = float('inf')

    # Try removing each MST edge
    for remove_u, remove_v, remove_w in mst_edges:
        uf = UnionFind(n)
        weight = 0
        count = 0

        for w, u, v in sorted(edges):
            edge_key = (min(u, v), max(u, v))
            if edge_key == (min(remove_u, remove_v), max(remove_u, remove_v)):
                continue

            if uf.union(u, v):
                weight += w
                count += 1

        if count == n - 1:
            second_best = min(second_best, weight)

    return second_best

# Usage
n = 4
edges = [
    (1, 0, 1), (2, 0, 2), (3, 1, 2),
    (4, 2, 3), (5, 1, 3), (6, 0, 3)
]

mst, total = kruskal(n, edges)
print(f"MST edges: {mst}")  # [(0, 1, 1), (0, 2, 2), (2, 3, 4)]
print(f"Total weight: {total}")  # 7

# Prim's example
graph = {
    0: [(1, 1), (2, 2), (3, 6)],
    1: [(0, 1), (2, 3), (3, 5)],
    2: [(0, 2), (1, 3), (3, 4)],
    3: [(0, 6), (1, 5), (2, 4)]
}
mst, total = prim(4, graph)
print(f"MST edges: {mst}, Total: {total}")
```

### Time complexity

| Algorithm | Complexity |
|-----------|------------|
| Kruskal   | O(E log E) |
| Prim (heap) | O(E log V) |
| Prim (matrix) | O(V²) |

### Space complexity
O(V) for Union-Find/visited. O(E) for edge list or O(V²) for adjacency matrix.

### Edge cases
- Disconnected graph (MST doesn't exist)
- Graph with single vertex
- All edges same weight
- Negative edge weights (still works)

### Variants
- **Boruvka's algorithm**: Good for parallel implementation
- **Reverse-delete algorithm**: Remove heaviest edges maintaining connectivity
- **Steiner tree**: MST for subset of vertices

### When to use vs avoid
- **Use when**: Need minimum cost to connect all vertices, network design, clustering
- **Avoid when**: Graph is directed, need shortest paths (different problem)

### Related
- [Union-Find](../../datastructs/graphs/unionFind.md)
- [Dijkstra](./dijkstra.md)
