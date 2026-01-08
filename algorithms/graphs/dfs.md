# Depth-First Search (DFS)
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Graph Traversal`

### Topics
**Topics:** `graph traversal`, `backtracking`, `cycle detection`, `topological sort`

### Definition
A graph traversal algorithm that explores as far as possible along each branch before backtracking, using recursion or a stack to track the path.

### Use cases
- Detecting cycles in graphs
- Topological sorting
- Finding connected components
- Solving mazes and puzzles
- Path finding (any path, not necessarily shortest)

### Prerequisites
- Graph representation (adjacency list/matrix)
- Stack or recursion
- Visited set to avoid infinite loops

### Step-by-step
1. Start at a vertex, mark it visited
2. Explore an unvisited neighbor recursively
3. When no unvisited neighbors, backtrack
4. Repeat until all reachable vertices visited
5. For disconnected graphs, start DFS from unvisited vertices

### In code
```python
# Recursive DFS
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result

# Iterative DFS using stack
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            # Add neighbors in reverse order for consistent traversal
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result

# Cycle detection in directed graph
def has_cycle_directed(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}

    def dfs(node):
        color[node] = GRAY

        for neighbor in graph[node]:
            if color[neighbor] == GRAY:  # Back edge = cycle
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True

        color[node] = BLACK
        return False

    for node in graph:
        if color[node] == WHITE:
            if dfs(node):
                return True

    return False

# Cycle detection in undirected graph
def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:  # Back edge (not parent)
                return True

        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True

    return False

# Find all paths between two nodes
def all_paths(graph, start, end, path=None):
    if path is None:
        path = []

    path = path + [start]

    if start == end:
        return [path]

    paths = []
    for neighbor in graph[start]:
        if neighbor not in path:  # Avoid cycles
            new_paths = all_paths(graph, neighbor, end, path)
            paths.extend(new_paths)

    return paths

# Connected components
def connected_components(graph):
    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)

    return components

# DFS on grid
def dfs_grid(grid, row, col, visited):
    rows, cols = len(grid), len(grid[0])

    if (row < 0 or row >= rows or col < 0 or col >= cols or
        grid[row][col] == 0 or (row, col) in visited):
        return 0

    visited.add((row, col))
    size = 1

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        size += dfs_grid(grid, row + dr, col + dc, visited)

    return size

# Usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(dfs_recursive(graph, 'A'))  # ['A', 'B', 'D', 'E', 'F', 'C']
print(all_paths(graph, 'A', 'F'))  # [['A', 'B', 'E', 'F'], ['A', 'C', 'F']]
```

### Time complexity

| Case | Complexity |
|------|------------|
| All  | O(V + E)   |

Where V = vertices, E = edges. Each vertex and edge visited once.

### Space complexity
O(V) for visited set. O(V) for recursion stack in worst case (linear graph).

### Edge cases
- Disconnected graph
- Graph with cycles
- Single vertex
- Empty graph
- Self-loops

### Variants
- **Preorder DFS**: Process node before children (standard)
- **Postorder DFS**: Process node after children (topological sort)
- **Iterative deepening**: Combine DFS depth limit with BFS completeness

### When to use vs avoid
- **Use when**: Exploring all possibilities, backtracking problems, detecting cycles, topological sort
- **Avoid when**: Need shortest path (use BFS), very deep graphs (stack overflow), need level-order processing

### Related
- [BFS](./bfs.md)
- [Topological Sort](./topologicalSort.md)
- [Stack](../../datastructs/stack.md)
