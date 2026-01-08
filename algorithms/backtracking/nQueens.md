# N-Queens Problem
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Backtracking`

### Topics
**Topics:** `constraint satisfaction`, `chess`, `combinatorial search`, `pruning`

### Definition
Place N queens on an N×N chessboard so that no two queens threaten each other (no two queens share the same row, column, or diagonal).

### Use cases
- Constraint satisfaction examples
- Teaching backtracking
- Puzzle generation
- Parallel algorithm benchmarks
- VLSI testing

### Prerequisites
- Backtracking pattern
- Understanding of chess queen movement
- 2D array manipulation

### Step-by-step
1. Place queens row by row
2. For each row, try each column
3. Check if placement is valid:
   - No queen in same column
   - No queen in same diagonal
4. If valid, move to next row
5. If row complete (placed queen in all rows), found solution
6. If no valid column, backtrack to previous row

### In code
```python
def solve_n_queens(n):
    """
    Find all solutions to N-Queens problem.
    Returns list of board configurations.
    """
    solutions = []
    board = [['.'] * n for _ in range(n)]

    # Track which columns and diagonals are under attack
    cols = set()
    diag1 = set()  # row - col (top-left to bottom-right)
    diag2 = set()  # row + col (top-right to bottom-left)

    def backtrack(row):
        if row == n:
            # Found valid configuration
            solutions.append([''.join(r) for r in board])
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # Place queen
            board[row][col] = 'Q'
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            # Remove queen (backtrack)
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return solutions

def count_n_queens(n):
    """
    Just count solutions without storing them.
    More memory efficient.
    """
    count = [0]
    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        if row == n:
            count[0] += 1
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return count[0]

def n_queens_bitmask(n):
    """
    Optimized solution using bitmasks.
    Faster due to bit operations.
    """
    count = [0]

    def backtrack(row, cols, diag1, diag2):
        if row == n:
            count[0] += 1
            return

        # Available positions = ~(cols | diag1 | diag2)
        available = ((1 << n) - 1) & ~(cols | diag1 | diag2)

        while available:
            # Get rightmost available position
            pos = available & (-available)
            available &= available - 1

            backtrack(
                row + 1,
                cols | pos,
                (diag1 | pos) << 1,
                (diag2 | pos) >> 1
            )

    backtrack(0, 0, 0, 0)
    return count[0]

def solve_n_queens_one(n):
    """Find just one solution (faster)"""
    board = [-1] * n  # board[row] = column of queen

    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        if row == n:
            return True

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            board[row] = col
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            if backtrack(row + 1):
                return True

            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

        return False

    if backtrack(0):
        return board
    return None

def is_valid_board(board):
    """Validate a queen placement"""
    n = len(board)
    cols = set()
    diag1 = set()
    diag2 = set()

    for row in range(n):
        col = board[row]
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            return False
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

    return True

def print_board(board_str):
    """Pretty print a board configuration"""
    for row in board_str:
        print(' '.join(row))
    print()

def n_queens_all_symmetries(n):
    """
    Find all unique solutions considering symmetries.
    (rotations and reflections)
    """
    solutions = solve_n_queens(n)

    def rotate_90(board):
        n = len(board)
        return [''.join(board[n-1-j][i] for j in range(n)) for i in range(n)]

    def reflect_horizontal(board):
        return [row[::-1] for row in board]

    def get_all_transforms(board):
        transforms = set()
        current = board
        for _ in range(4):
            transforms.add(tuple(current))
            transforms.add(tuple(reflect_horizontal(current)))
            current = rotate_90(current)
        return transforms

    unique = []
    seen = set()

    for sol in solutions:
        key = tuple(sol)
        if key not in seen:
            unique.append(sol)
            for transform in get_all_transforms(sol):
                seen.add(transform)

    return unique

def n_rooks(n):
    """
    Simpler problem: N rooks (only row/column constraints).
    Number of solutions = n!
    """
    solutions = []
    board = [-1] * n
    cols = set()

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if col not in cols:
                board[row] = col
                cols.add(col)
                backtrack(row + 1)
                cols.remove(col)

    backtrack(0)
    return solutions

# Usage
n = 4

# Find all solutions
solutions = solve_n_queens(n)
print(f"N-Queens ({n}x{n}): {len(solutions)} solutions")
print("\nFirst solution:")
print_board(solutions[0])

# Count solutions for different n
for size in range(1, 9):
    count = count_n_queens(size)
    print(f"n={size}: {count} solutions")

# Single solution for larger board
n = 8
one_solution = solve_n_queens_one(n)
print(f"\nOne solution for n={n}: {one_solution}")

# Unique solutions (excluding symmetries)
unique = n_queens_all_symmetries(4)
print(f"\nUnique solutions for n=4 (excluding symmetries): {len(unique)}")
```

### Time complexity

| Method | Complexity |
|--------|------------|
| Basic backtracking | O(n!) |
| With pruning | O(n!) but faster in practice |
| Bitmask | O(n!) with lower constant |

Exponential but heavily pruned.

### Space complexity
O(n) for recursion depth and tracking sets. O(solutions × n²) to store all solutions.

### Edge cases
- n = 1 (trivial, 1 solution)
- n = 2 or 3 (no solution)
- n = 4+ (solutions exist)
- Large n (use counting only)

### Variants
- **N-Rooks**: Only row/column constraints (easier, n! solutions)
- **Super Queens**: Queens + knights moves
- **N-Queens on toroidal board**: Wraparound diagonals
- **Minimum attacking pairs**: Optimization version

### When to use vs avoid
- **Use when**: Teaching backtracking, constraint satisfaction, small n (n < 15 for all solutions)
- **Avoid when**: Need exact count for large n (use mathematical formulas or lookup tables)

### Related
- [Subsets](./subsets.md)
- [Permutations](./permutations.md)

### Known values

| n | Solutions | Unique |
|---|-----------|--------|
| 1 | 1 | 1 |
| 4 | 2 | 1 |
| 5 | 10 | 2 |
| 6 | 4 | 1 |
| 7 | 40 | 6 |
| 8 | 92 | 12 |
