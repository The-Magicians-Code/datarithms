# Knapsack Problem
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Dynamic Programming`

### Topics
**Topics:** `optimization`, `subset selection`, `resource allocation`, `combinatorics`

### Definition
A combinatorial optimization problem where given a set of items with weights and values, determine the most valuable subset that fits within a weight capacity.

### Use cases
- Resource allocation with budget constraints
- Portfolio optimization
- Cargo loading
- Cutting stock problems
- Feature selection in machine learning

### Prerequisites
- Understanding of dynamic programming
- Recursion with memoization
- 2D array manipulation

### Step-by-step
**0/1 Knapsack:**
1. Create DP table: dp[i][w] = max value using first i items with capacity w
2. For each item, decide to include or exclude
3. If include: dp[i][w] = dp[i-1][w-weight[i]] + value[i]
4. If exclude: dp[i][w] = dp[i-1][w]
5. Take maximum of both choices
6. Answer is dp[n][W]

### In code
```python
def knapsack_01(weights, values, capacity):
    """
    0/1 Knapsack - each item can be used at most once.
    Returns maximum value achievable.
    """
    n = len(weights)

    # dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i-1
            dp[i][w] = dp[i - 1][w]

            # Take item i-1 if it fits
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])

    return dp[n][capacity]

def knapsack_01_space_optimized(weights, values, capacity):
    """Space-optimized 0/1 knapsack using 1D array"""
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        # Traverse right to left to avoid using same item twice
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

def knapsack_unbounded(weights, values, capacity):
    """
    Unbounded Knapsack - each item can be used unlimited times.
    """
    dp = [0] * (capacity + 1)

    for w in range(1, capacity + 1):
        for i in range(len(weights)):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

def knapsack_with_items(weights, values, capacity):
    """0/1 Knapsack that also returns selected items"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])

    # Backtrack to find items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], selected[::-1]

def subset_sum(nums, target):
    """Check if subset with given sum exists (special case of knapsack)"""
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for t in range(target, num - 1, -1):
            dp[t] = dp[t] or dp[t - num]

    return dp[target]

def count_subsets_with_sum(nums, target):
    """Count number of subsets with given sum"""
    dp = [0] * (target + 1)
    dp[0] = 1

    for num in nums:
        for t in range(target, num - 1, -1):
            dp[t] += dp[t - num]

    return dp[target]

# Usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8

max_value = knapsack_01(weights, values, capacity)
print(f"Max value: {max_value}")  # 10 (items with weight 3,5 and value 4,6)

max_val, items = knapsack_with_items(weights, values, capacity)
print(f"Selected items: {items}")  # [1, 3]
```

### Time complexity

| Variant | Complexity |
|---------|------------|
| 0/1 Knapsack | O(n × W) |
| Unbounded | O(n × W) |
| With backtracking | O(n × W) |

Where n = number of items, W = capacity.

### Space complexity
O(n × W) for 2D table. O(W) for space-optimized version.

### Edge cases
- Capacity is 0
- No items
- All items too heavy
- Single item fits exactly

### Variants
- **Bounded Knapsack**: Each item has a count limit
- **Fractional Knapsack**: Items can be partially taken (greedy solution)
- **Multi-dimensional Knapsack**: Multiple constraints (weight, volume, etc.)

### When to use vs avoid
- **Use when**: Resource allocation under constraints, subset selection, optimization with discrete choices
- **Avoid when**: Items are divisible (use greedy), constraints are continuous, problem is very large (consider approximation)

### Related
- [LIS](./lis.md)
- [Subset Sum (Backtracking)](../backtracking/subsets.md)
