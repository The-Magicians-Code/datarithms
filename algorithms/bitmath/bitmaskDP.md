# Bitmask DP
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Dynamic Programming`

### Topics
**Topics:** `bit manipulation`, `subset enumeration`, `state compression`, `TSP`

### Definition
Dynamic programming where the state is represented as a bitmask, allowing efficient representation and manipulation of subsets. Each bit indicates whether an element is included in the current subset.

### Use cases
- Traveling Salesman Problem (TSP)
- Assignment problems
- Graph coloring
- Hamiltonian path
- Subset selection with constraints

### Prerequisites
- Bit manipulation basics
- Dynamic programming
- Understanding of 2^n subsets

### Step-by-step
**Common pattern:**
1. State: dp[mask] where mask represents current subset
2. Transition: iterate over bits to find next states
3. Use bit operations to check/set elements
4. Base case: dp[0] or dp[full_mask]

**Key operations:**
- Check if i-th bit set: `mask & (1 << i)`
- Set i-th bit: `mask | (1 << i)`
- Clear i-th bit: `mask & ~(1 << i)`
- Iterate subsets of mask

### In code
```python
def tsp(dist):
    """
    Traveling Salesman Problem using bitmask DP.
    Find minimum cost to visit all cities starting and ending at city 0.
    dist: distance matrix where dist[i][j] is cost from i to j
    """
    n = len(dist)
    INF = float('inf')

    # dp[mask][i] = min cost to reach city i having visited cities in mask
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Start at city 0, visited = {0}

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            if not (mask & (1 << u)):
                continue

            # Try visiting city v
            for v in range(n):
                if mask & (1 << v):  # Already visited
                    continue

                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])

    # Return to starting city
    full_mask = (1 << n) - 1
    result = INF
    for u in range(n):
        result = min(result, dp[full_mask][u] + dist[u][0])

    return result

def hamiltonian_path_count(adj):
    """
    Count number of Hamiltonian paths in a graph.
    adj: adjacency matrix (1 if edge exists)
    """
    n = len(adj)

    # dp[mask][i] = number of paths ending at i visiting vertices in mask
    dp = [[0] * n for _ in range(1 << n)]

    # Base case: single vertex paths
    for i in range(n):
        dp[1 << i][i] = 1

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            if dp[mask][u] == 0:
                continue

            for v in range(n):
                if mask & (1 << v):  # Already in path
                    continue
                if not adj[u][v]:    # No edge
                    continue

                new_mask = mask | (1 << v)
                dp[new_mask][v] += dp[mask][u]

    # Sum all paths ending at any vertex with all visited
    full_mask = (1 << n) - 1
    return sum(dp[full_mask])

def min_vertex_cover(n, edges):
    """
    Find minimum vertex cover using bitmask.
    Works for small n (< 20).
    """
    result = n

    for mask in range(1 << n):
        # Check if mask is a valid vertex cover
        is_cover = True
        for u, v in edges:
            if not ((mask & (1 << u)) or (mask & (1 << v))):
                is_cover = False
                break

        if is_cover:
            result = min(result, bin(mask).count('1'))

    return result

def assignment_problem(cost):
    """
    Assign n workers to n tasks with minimum total cost.
    cost[i][j] = cost of assigning worker i to task j
    """
    n = len(cost)
    INF = float('inf')

    # dp[mask] = min cost when tasks in mask are assigned
    dp = [INF] * (1 << n)
    dp[0] = 0

    for mask in range(1 << n):
        if dp[mask] == INF:
            continue

        worker = bin(mask).count('1')  # Current worker to assign
        if worker >= n:
            continue

        for task in range(n):
            if mask & (1 << task):  # Task already assigned
                continue

            new_mask = mask | (1 << task)
            dp[new_mask] = min(dp[new_mask], dp[mask] + cost[worker][task])

    return dp[(1 << n) - 1]

def count_subsets_sum(nums, target):
    """
    Count subsets with given sum using bitmask (brute force for small n).
    More efficient DP version exists for larger n.
    """
    n = len(nums)
    count = 0

    for mask in range(1 << n):
        total = 0
        for i in range(n):
            if mask & (1 << i):
                total += nums[i]
        if total == target:
            count += 1

    return count

def iterate_submasks(mask):
    """
    Iterate over all submasks of a given mask.
    Total iterations for all masks: O(3^n)
    """
    submasks = []
    submask = mask
    while submask:
        submasks.append(submask)
        submask = (submask - 1) & mask
    submasks.append(0)
    return submasks

def partition_into_two_equal_sets(nums):
    """
    Check if array can be partitioned into two subsets with equal sum.
    """
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    n = len(nums)

    for mask in range(1 << n):
        subset_sum = sum(nums[i] for i in range(n) if mask & (1 << i))
        if subset_sum == target:
            return True

    return False

def steiner_tree(n, terminals, edges):
    """
    Find minimum Steiner tree connecting terminal vertices.
    """
    INF = float('inf')
    k = len(terminals)

    # Build adjacency list with weights
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    # dp[mask][v] = min cost to connect terminals in mask using v as hub
    dp = [[INF] * n for _ in range(1 << k)]

    # Base case
    for i, t in enumerate(terminals):
        dp[1 << i][t] = 0

    for mask in range(1, 1 << k):
        # Combine submasks
        submask = mask
        while submask:
            complement = mask ^ submask
            if complement < submask:  # Avoid counting twice
                for v in range(n):
                    dp[mask][v] = min(dp[mask][v],
                                     dp[submask][v] + dp[complement][v])
            submask = (submask - 1) & mask

        # Dijkstra-like relaxation
        import heapq
        pq = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(pq)

        while pq:
            d, u = heapq.heappop(pq)
            if d > dp[mask][u]:
                continue
            for v, w in adj[u]:
                if dp[mask][u] + w < dp[mask][v]:
                    dp[mask][v] = dp[mask][u] + w
                    heapq.heappush(pq, (dp[mask][v], v))

    full_mask = (1 << k) - 1
    return min(dp[full_mask])

# Usage
# TSP example
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(f"TSP min cost: {tsp(dist)}")  # 80

# Assignment problem
cost = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]
print(f"Min assignment cost: {assignment_problem(cost)}")  # 7 (0->1, 1->2, 2->0)

# Submask iteration
mask = 0b1011  # 11
submasks = iterate_submasks(mask)
print(f"Submasks of {bin(mask)}: {[bin(s) for s in submasks]}")
```

### Time complexity

| Problem | Complexity |
|---------|------------|
| TSP | O(n² × 2^n) |
| Assignment | O(n × 2^n) |
| Submask iteration | O(3^n) total |

Exponential in n (number of elements).

### Space complexity
O(2^n) or O(n × 2^n) depending on state representation.

### Edge cases
- n = 0 (empty set)
- n = 1 (single element)
- n > 20 (typically too slow)
- Unreachable states

### Variants
- **Profile DP**: Bitmask for boundary of explored region
- **SOS DP (Sum over Subsets)**: Efficiently compute function over all subsets
- **Meet in the Middle**: Split bitmask into two halves

### When to use vs avoid
- **Use when**: Small n (< 20), need subset states, TSP-like problems
- **Avoid when**: Large n, simpler DP exists, can use greedy or other approaches

### Related
- [Subsets](../backtracking/subsets.md)
- [Knapsack](../dp/knapsack.md)
