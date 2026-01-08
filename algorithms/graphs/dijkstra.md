# Dijkstra's Algorithm
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Shortest Path`

### Topics
**Topics:** `weighted graphs`, `routing`, `priority queue`, `greedy algorithm`

### Definition
A greedy algorithm that finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights, using a priority queue to always expand the closest unvisited vertex.

### Use cases
- GPS navigation systems
- Network routing protocols (OSPF)
- Finding shortest routes in maps
- Robot path planning
- Any shortest path in weighted graph

### Prerequisites
- Graph with non-negative edge weights
- Priority queue (min-heap)
- Adjacency list representation

### Step-by-step
1. Initialize distances: source = 0, all others = infinity
2. Add source to priority queue with distance 0
3. Extract vertex with minimum distance from queue
4. For each neighbor, calculate distance through current vertex
5. If shorter, update distance and add to queue
6. Repeat until queue is empty

### In code
```python
import heapq
from collections import defaultdict

def dijkstra(graph, start):
    """
    Find shortest distances from start to all vertices.
    graph: dict of {vertex: [(neighbor, weight), ...]}
    """
    distances = {start: 0}
    pq = [(0, start)]  # (distance, vertex)

    while pq:
        curr_dist, curr_vertex = heapq.heappop(pq)

        # Skip if we've found a better path
        if curr_dist > distances.get(curr_vertex, float('inf')):
            continue

        for neighbor, weight in graph[curr_vertex]:
            distance = curr_dist + weight

            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def dijkstra_with_path(graph, start, end):
    """Find shortest path and distance to specific destination"""
    distances = {start: 0}
    previous = {start: None}
    pq = [(0, start)]

    while pq:
        curr_dist, curr_vertex = heapq.heappop(pq)

        if curr_vertex == end:
            break

        if curr_dist > distances.get(curr_vertex, float('inf')):
            continue

        for neighbor, weight in graph[curr_vertex]:
            distance = curr_dist + weight

            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                previous[neighbor] = curr_vertex
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous.get(current)

    path.reverse()

    if path[0] != start:
        return float('inf'), []  # No path exists

    return distances.get(end, float('inf')), path

# Dijkstra on grid
def shortest_path_grid(grid):
    """Find shortest path from top-left to bottom-right"""
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]

    while pq:
        dist, r, c = heapq.heappop(pq)

        if r == rows - 1 and c == cols - 1:
            return dist

        if dist > distances[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                new_dist = dist + grid[nr][nc]

                if new_dist < distances[nr][nc]:
                    distances[nr][nc] = new_dist
                    heapq.heappush(pq, (new_dist, nr, nc))

    return distances[rows - 1][cols - 1]

# Building graph from edges
def build_graph(edges, directed=False):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        if not directed:
            graph[v].append((u, w))
    return graph

# Usage
edges = [
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'C', 1), ('B', 'D', 5),
    ('C', 'D', 8), ('C', 'E', 10),
    ('D', 'E', 2), ('D', 'F', 6),
    ('E', 'F', 3)
]
graph = build_graph(edges)

distances = dijkstra(graph, 'A')
print(distances)  # {'A': 0, 'B': 3, 'C': 2, 'D': 8, 'E': 10, 'F': 13}

dist, path = dijkstra_with_path(graph, 'A', 'F')
print(f"Distance: {dist}, Path: {path}")  # Distance: 13, Path: ['A', 'C', 'B', 'D', 'E', 'F']
```

### Time complexity

| Implementation | Complexity |
|----------------|------------|
| Binary heap    | O((V + E) log V) |
| Fibonacci heap | O(E + V log V) |
| Array (naive)  | O(V²) |

Where V = number of vertices, E = number of edges.

Binary heap is most practical for sparse graphs.

### Space complexity
O(V) for distances, previous, and priority queue.

### Edge cases
- Disconnected vertices (return infinity)
- Negative edge weights (algorithm fails - use Bellman-Ford)
- Self-loops
- Multiple edges between same vertices
- Source equals destination

### Variants
- **Bidirectional Dijkstra**: Search from both ends, faster in practice
- **A* Search**: Use heuristic to guide search
- **Dial's algorithm**: For integer weights in small range
- **Johnson's algorithm**: All-pairs shortest path

### When to use vs avoid
- **Use when**: Weighted graph with non-negative edges, single source shortest path
- **Avoid when**: Negative edge weights (use Bellman-Ford), unweighted graph (BFS simpler), all-pairs needed (Floyd-Warshall)

### Related
- [Bellman-Ford](./bellmanFord.md)
- [A* Search](./aStar.md)
- [BFS](./bfs.md)
- [Heap](../../datastructs/trees/heap.md)
