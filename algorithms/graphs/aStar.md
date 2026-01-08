# A* Search Algorithm
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Pathfinding`

### Topics
**Topics:** `heuristic search`, `game AI`, `robotics`, `navigation`

### Definition
An informed search algorithm that finds the shortest path using a heuristic function to estimate the cost to the goal, combining the best of Dijkstra's (optimal) and greedy best-first search (fast).

### Use cases
- Video game pathfinding
- Robot navigation
- GPS routing
- Puzzle solving (8-puzzle, 15-puzzle)
- Any shortest path with good heuristic available

### Prerequisites
- Priority queue
- Admissible heuristic function
- Graph or grid representation

### Step-by-step
1. Initialize open set (priority queue) with start node
2. f(n) = g(n) + h(n) where g = cost from start, h = heuristic to goal
3. Pop node with lowest f from open set
4. If goal reached, reconstruct path
5. For each neighbor, calculate tentative g score
6. If better path found, update and add to open set
7. Repeat until goal found or open set empty

### In code
```python
import heapq

def a_star(graph, start, goal, heuristic):
    """
    A* search algorithm.
    graph: dict of {vertex: [(neighbor, cost), ...]}
    heuristic: function(node) -> estimated cost to goal
    """
    open_set = [(0 + heuristic(start), 0, start, [start])]
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return g, path

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic(neighbor)
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return float('inf'), []  # No path found

def a_star_grid(grid, start, goal):
    """
    A* on 2D grid.
    grid: 2D array (0 = walkable, 1 = obstacle)
    start, goal: (row, col) tuples
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Manhattan distance heuristic
    def heuristic(pos):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    # (f, g, position, path)
    open_set = [(heuristic(start), 0, start, [start])]
    g_scores = {start: 0}

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return g, path

        if g > g_scores.get(current, float('inf')):
            continue

        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            neighbor = (nr, nc)

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1:
                new_g = g + 1

                if new_g < g_scores.get(neighbor, float('inf')):
                    g_scores[neighbor] = new_g
                    new_f = new_g + heuristic(neighbor)
                    heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return float('inf'), []

# With diagonal movement
def a_star_8_directions(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    # 8 directions including diagonals
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]

    # Euclidean or Chebyshev heuristic for diagonals
    def heuristic(pos):
        dx = abs(pos[0] - goal[0])
        dy = abs(pos[1] - goal[1])
        # Chebyshev distance (diagonal cost = 1)
        return max(dx, dy)
        # Or Euclidean: return (dx*dx + dy*dy) ** 0.5

    open_set = [(heuristic(start), 0, start, [start])]
    g_scores = {start: 0}

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return g, path

        if g > g_scores.get(current, float('inf')):
            continue

        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            neighbor = (nr, nc)

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1:
                # Diagonal movement costs sqrt(2) ≈ 1.414
                move_cost = 1.414 if dr != 0 and dc != 0 else 1
                new_g = g + move_cost

                if new_g < g_scores.get(neighbor, float('inf')):
                    g_scores[neighbor] = new_g
                    new_f = new_g + heuristic(neighbor)
                    heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return float('inf'), []

# Common heuristics
def manhattan_distance(pos, goal):
    """For 4-directional movement"""
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def euclidean_distance(pos, goal):
    """For any-direction movement"""
    return ((pos[0] - goal[0])**2 + (pos[1] - goal[1])**2) ** 0.5

def chebyshev_distance(pos, goal):
    """For 8-directional movement with equal diagonal cost"""
    return max(abs(pos[0] - goal[0]), abs(pos[1] - goal[1]))

# Usage
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

cost, path = a_star_grid(grid, (0, 0), (4, 4))
print(f"Cost: {cost}")  # 8
print(f"Path: {path}")  # [(0,0), (0,1), (0,2), (0,3), (0,4), (1,4), (2,4), (3,4), (4,4)]
```

### Time complexity

| Case | Complexity |
|------|------------|
| Best | O(1) - goal is start |
| Average | O(b^d) - depends on heuristic quality |
| Worst | O(b^d) |

Where b = branching factor (average neighbors per node), d = depth of solution.

With perfect heuristic: O(d). With h=0: becomes Dijkstra O(E log V).

### Space complexity
O(b^d) for open and closed sets. Can be significant for large search spaces.

### Edge cases
- No path exists
- Start equals goal
- Heuristic overestimates (non-admissible) - may not find optimal
- Large open spaces (high branching factor)

### Variants
- **IDA* (Iterative Deepening A*)**: Memory-efficient, uses depth limit
- **SMA* (Simplified Memory-bounded A*)**: Bounds memory usage
- **Weighted A***: f = g + w*h, trades optimality for speed
- **Bidirectional A***: Search from both ends

### When to use vs avoid
- **Use when**: Good heuristic available, need optimal path, grid/game pathfinding
- **Avoid when**: No good heuristic (use Dijkstra), very large graphs with poor heuristic, real-time constraints (use hierarchical approaches)

### Related
- [Dijkstra](./dijkstra.md)
- [BFS](./bfs.md)
