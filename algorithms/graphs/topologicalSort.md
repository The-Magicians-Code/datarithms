# Topological Sort
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Graph Algorithms`

### Topics
**Topics:** `DAG`, `dependency resolution`, `build systems`, `scheduling`

### Definition
A linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge (u, v), vertex u comes before v in the ordering.

### Use cases
- Build systems (Makefile, Maven, npm)
- Task scheduling with dependencies
- Course prerequisite ordering
- Package dependency resolution
- Spreadsheet cell evaluation order

### Prerequisites
- Directed acyclic graph (DAG)
- Understanding of in-degree/out-degree
- DFS or BFS traversal

### Step-by-step
**Kahn's Algorithm (BFS):**
1. Calculate in-degree for all vertices
2. Add all vertices with in-degree 0 to queue
3. Remove vertex from queue, add to result
4. Decrease in-degree of neighbors by 1
5. If neighbor's in-degree becomes 0, add to queue
6. If result size ≠ vertex count, cycle exists

### In code
```python
from collections import deque, defaultdict

def topological_sort_kahn(graph, vertices):
    """
    Kahn's algorithm (BFS-based).
    graph: dict of {vertex: [neighbors]}
    """
    # Calculate in-degrees
    in_degree = {v: 0 for v in vertices}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Start with vertices having no dependencies
    queue = deque([v for v in vertices if in_degree[v] == 0])
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph.get(vertex, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(vertices):
        raise ValueError("Graph has a cycle - topological sort not possible")

    return result

def topological_sort_dfs(graph, vertices):
    """DFS-based topological sort"""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in vertices}
    result = []

    def dfs(vertex):
        color[vertex] = GRAY

        for neighbor in graph.get(vertex, []):
            if color[neighbor] == GRAY:
                raise ValueError("Graph has a cycle")
            if color[neighbor] == WHITE:
                dfs(neighbor)

        color[vertex] = BLACK
        result.append(vertex)

    for vertex in vertices:
        if color[vertex] == WHITE:
            dfs(vertex)

    return result[::-1]  # Reverse for correct order

def all_topological_sorts(graph, vertices):
    """Find all valid topological orderings"""
    in_degree = {v: 0 for v in vertices}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    result = []

    def backtrack(path, visited):
        if len(path) == len(vertices):
            result.append(path.copy())
            return

        for v in vertices:
            if v not in visited and in_degree[v] == 0:
                # Choose
                visited.add(v)
                for neighbor in graph.get(v, []):
                    in_degree[neighbor] -= 1
                path.append(v)

                # Explore
                backtrack(path, visited)

                # Unchoose
                path.pop()
                visited.remove(v)
                for neighbor in graph.get(v, []):
                    in_degree[neighbor] += 1

    backtrack([], set())
    return result

def can_finish_courses(num_courses, prerequisites):
    """
    Course scheduling problem.
    prerequisites: list of [course, prerequisite] pairs
    """
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    completed = 0

    while queue:
        course = queue.popleft()
        completed += 1

        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    return completed == num_courses

def find_order(num_courses, prerequisites):
    """Return one valid course order, or empty if impossible"""
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    return order if len(order) == num_courses else []

# Usage
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
graph = {
    'A': ['D'],
    'B': ['D'],
    'C': ['E'],
    'D': ['E', 'F'],
    'E': ['F'],
    'F': []
}

print(topological_sort_kahn(graph, vertices))
# One valid order: ['A', 'B', 'C', 'D', 'E', 'F'] or ['B', 'A', 'C', 'D', 'E', 'F']

# Course scheduling
prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(find_order(4, prereqs))  # [0, 1, 2, 3] or [0, 2, 1, 3]
```

### Time complexity

| Case | Complexity |
|------|------------|
| All  | O(V + E)   |

Each vertex and edge processed once.

### Space complexity
O(V) for in-degree array, queue, and result. O(V + E) for graph representation.

### Edge cases
- Graph with cycle (not a DAG - error)
- Disconnected components
- Single vertex
- Empty graph
- Multiple valid orderings

### Variants
- **Kahn's algorithm**: BFS-based, easy cycle detection
- **DFS-based**: Uses finish times, detects back edges for cycles
- **Parallel topological sort**: For dependency-free parallelization

### When to use vs avoid
- **Use when**: Ordering tasks with dependencies, detecting cycles in directed graphs, scheduling problems
- **Avoid when**: Graph has cycles (undefined), undirected graphs

### Related
- [DFS](./dfs.md)
- [BFS](./bfs.md)
