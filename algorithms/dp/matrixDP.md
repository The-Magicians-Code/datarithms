# Matrix DP (Grid-Based Dynamic Programming)
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Dynamic Programming`

### Topics
**Topics:** `grid traversal`, `path counting`, `minimum path`, `matrix chain multiplication`

### Definition
Dynamic programming problems solved on 2D grids, including path counting, minimum/maximum path sums, and optimal matrix operations.

### Use cases
- Robot navigation (unique paths)
- Minimum cost path problems
- Image processing
- Game board problems
- Matrix chain multiplication

### Prerequisites
- 2D array manipulation
- Understanding of DP state transitions
- Recognizing subproblems in grids

### Step-by-step
**Unique Paths:**
1. dp[i][j] = number of ways to reach cell (i, j)
2. dp[i][j] = dp[i-1][j] + dp[i][j-1]
3. Base case: first row and column are all 1s

**Minimum Path Sum:**
1. dp[i][j] = minimum sum to reach cell (i, j)
2. dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
3. Base case: accumulate first row and column

### In code
```python
def unique_paths(m, n):
    """
    Count unique paths from top-left to bottom-right.
    Can only move right or down.
    """
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]

def unique_paths_with_obstacles(grid):
    """Unique paths with obstacles (1 = obstacle)"""
    m, n = len(grid), len(grid[0])

    if grid[0][0] == 1 or grid[m-1][n-1] == 1:
        return 0

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    # First column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] if grid[i][0] == 0 else 0

    # First row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] if grid[0][j] == 0 else 0

    # Fill rest
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]

def min_path_sum(grid):
    """
    Find minimum sum path from top-left to bottom-right.
    Can only move right or down.
    """
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = grid[0][0]

    # First row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # First column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Fill rest
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[m - 1][n - 1]

def min_path_sum_all_directions(grid):
    """Min path allowing up/down/left/right (Dijkstra-style)"""
    import heapq

    m, n = len(grid), len(grid[0])
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = grid[0][0]

    pq = [(grid[0][0], 0, 0)]  # (cost, row, col)

    while pq:
        cost, r, c = heapq.heappop(pq)

        if cost > dist[r][c]:
            continue

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                new_cost = cost + grid[nr][nc]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))

    return dist[m - 1][n - 1]

def max_path_sum(grid):
    """Maximum sum path (top-left to bottom-right)"""
    m, n = len(grid), len(grid[0])
    dp = [[float('-inf')] * n for _ in range(m)]

    dp[0][0] = grid[0][0]

    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + max(dp[i - 1][j], dp[i][j - 1])

    return dp[m - 1][n - 1]

def triangle_min_path(triangle):
    """
    Minimum path sum from top to bottom of triangle.
    triangle[i] has i+1 elements.
    """
    n = len(triangle)
    # Start from bottom
    dp = triangle[-1].copy()

    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

    return dp[0]

def maximal_square(matrix):
    """
    Find largest square of 1s in binary matrix.
    Returns area of largest square.
    """
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1' or matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])

    return max_side * max_side

def matrix_chain_multiplication(dims):
    """
    Minimum multiplications to compute matrix chain product.
    dims: dimensions where matrix i is dims[i-1] x dims[i]
    """
    n = len(dims) - 1  # Number of matrices

    # dp[i][j] = min cost to multiply matrices i to j
    dp = [[0] * n for _ in range(n)]

    # Length of chain
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            # Try all split points
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]

def dungeon_game(dungeon):
    """
    Minimum initial health to reach bottom-right with health > 0.
    Cells can have positive (health) or negative (damage) values.
    """
    m, n = len(dungeon), len(dungeon[0])

    # dp[i][j] = min health needed at (i,j) to reach end
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    dp[m][n - 1] = dp[m - 1][n] = 1

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            min_health = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
            dp[i][j] = max(1, min_health)

    return dp[0][0]

# Usage
# Unique paths
print(f"Unique paths (3x7): {unique_paths(3, 7)}")  # 28

# Min path sum
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(f"Min path sum: {min_path_sum(grid)}")  # 7

# Maximal square
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print(f"Maximal square area: {maximal_square(matrix)}")  # 4

# Matrix chain multiplication
dims = [10, 30, 5, 60]  # 3 matrices: 10x30, 30x5, 5x60
print(f"Min multiplications: {matrix_chain_multiplication(dims)}")  # 4500
```

### Time complexity

| Problem | Complexity |
|---------|------------|
| Unique Paths | O(m × n) |
| Min/Max Path Sum | O(m × n) |
| Maximal Square | O(m × n) |
| Matrix Chain | O(n³) |

### Space complexity
O(m × n) for most problems. Can often be optimized to O(n) with row-by-row processing.

### Edge cases
- Single cell grid
- Single row or column
- All obstacles (no valid path)
- Grid with negative values

### Variants
- **Cherry Pickup**: Two robots collecting cherries
- **Falling Path Sum**: Choose any start column
- **Paint House**: No two adjacent same color
- **Burst Balloons**: Interval DP on array

### When to use vs avoid
- **Use when**: Grid traversal problems, path optimization, counting paths, submatrix problems
- **Avoid when**: Need actual path (add backtracking), graph is not grid-like, need shortest path with variable costs (use Dijkstra)

### Related
- [A*](../graphs/aStar.md)
- [Dijkstra](../graphs/dijkstra.md)
