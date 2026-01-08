# Breadth-First Search (BFS)
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Graph Traversal`

### Topics
**Topics:** `shortest path`, `level-order traversal`, `connectivity`, `unweighted graphs`

### Definition
A graph traversal algorithm that explores all vertices at the current depth level before moving to vertices at the next depth level, using a queue to track vertices to visit.

### Use cases
- Shortest path in unweighted graphs
- Level-order tree traversal
- Finding connected components
- Web crawling
- Social network friend suggestions (degrees of separation)

### Prerequisites
- Graph representation (adjacency list/matrix)
- Queue data structure
- Visited set to avoid cycles

### Step-by-step
1. Initialize queue with starting vertex
2. Mark starting vertex as visited
3. Dequeue a vertex and process it
4. Enqueue all unvisited neighbors, marking them visited
5. Repeat until queue is empty

### In code
```python
from collections import deque

def bfs(graph, start):
    """Basic BFS traversal"""
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

# Shortest path in unweighted graph
def shortest_path(graph, start, end):
    if start == end:
        return [start]

    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        vertex, path = queue.popleft()

        for neighbor in graph[vertex]:
            if neighbor == end:
                return path + [neighbor]

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []  # No path found

# BFS with distance tracking
def bfs_distances(graph, start):
    distances = {start: 0}
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        for neighbor in graph[vertex]:
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)

    return distances

# Level-order tree traversal
def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result

# BFS on grid (maze)
def shortest_path_grid(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque([(start[0], start[1], 0)])
    visited = {start}

    while queue:
        r, c, dist = queue.popleft()

        if (r, c) == end:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and 0 <= nc < cols and
                grid[nr][nc] != 1 and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1  # No path

# Usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
print(shortest_path(graph, 'A', 'F'))  # ['A', 'C', 'F']
```

### Time complexity

| Case | Complexity |
|------|------------|
| All  | O(V + E)   |

Where V = vertices, E = edges. Each vertex and edge visited once.

### Space complexity
O(V) for the queue and visited set. O(V) additional for path reconstruction if needed.

### Edge cases
- Disconnected graph (some vertices unreachable)
- Start equals end
- Single vertex graph
- Empty graph
- Self-loops

### Variants
- **Bidirectional BFS**: Search from both start and end, meet in middle
- **0-1 BFS**: For graphs with edge weights 0 or 1
- **Multi-source BFS**: Start from multiple sources simultaneously
- **BFS with state**: Track additional state beyond just vertex

### When to use vs avoid
- **Use when**: Shortest path in unweighted graph, level-order processing, exploring by distance
- **Avoid when**: Graph is weighted (use Dijkstra), memory constrained with wide graphs, need any path (DFS may be simpler)

### Related
- [DFS](./dfs.md)
- [Dijkstra](./dijkstra.md)
- [Queue](../../datastructs/queue.md)
