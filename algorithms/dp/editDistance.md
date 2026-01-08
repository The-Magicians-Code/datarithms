# Edit Distance (Levenshtein Distance)
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Dynamic Programming`

### Topics
**Topics:** `string similarity`, `spell checking`, `fuzzy matching`, `sequence alignment`

### Definition
The minimum number of single-character operations (insertions, deletions, or substitutions) required to transform one string into another.

### Use cases
- Spell checkers and auto-correct
- DNA sequence alignment
- Fuzzy string matching
- Plagiarism detection
- Natural language processing

### Prerequisites
- 2D dynamic programming
- Understanding of string operations
- Recursion with memoization

### Step-by-step
1. Create DP table: dp[i][j] = edit distance between first i chars of s1 and first j chars of s2
2. Base cases: dp[i][0] = i (delete all), dp[0][j] = j (insert all)
3. If chars match: dp[i][j] = dp[i-1][j-1]
4. Else: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
5. Answer is dp[m][n]

### In code
```python
def edit_distance(s1, s2):
    """
    Compute minimum edit distance (Levenshtein distance).
    Operations: insert, delete, substitute (each costs 1).
    """
    m, n = len(s1), len(s2)

    # dp[i][j] = edit distance for s1[:i] and s2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all chars from s1
    for j in range(n + 1):
        dp[0][j] = j  # Insert all chars from s2

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete from s1
                    dp[i][j - 1],      # Insert into s1
                    dp[i - 1][j - 1]   # Substitute
                )

    return dp[m][n]

def edit_distance_space_optimized(s1, s2):
    """Space-optimized using two rows"""
    m, n = len(s1), len(s2)

    prev = list(range(n + 1))
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        curr[0] = i
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev, curr = curr, [0] * (n + 1)

    return prev[n]

def edit_distance_with_operations(s1, s2):
    """Return edit distance and the sequence of operations"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    # Backtrack to find operations
    operations = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i-1] == s2[j-1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + 1:
            operations.append(f"Substitute '{s1[i-1]}' with '{s2[j-1]}' at position {i-1}")
            i -= 1
            j -= 1
        elif j > 0 and dp[i][j] == dp[i][j-1] + 1:
            operations.append(f"Insert '{s2[j-1]}' at position {i}")
            j -= 1
        else:
            operations.append(f"Delete '{s1[i-1]}' at position {i-1}")
            i -= 1

    return dp[m][n], list(reversed(operations))

def weighted_edit_distance(s1, s2, insert_cost=1, delete_cost=1, sub_cost=1):
    """Edit distance with custom operation costs"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i * delete_cost
    for j in range(n + 1):
        dp[0][j] = j * insert_cost

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + delete_cost,
                    dp[i][j - 1] + insert_cost,
                    dp[i - 1][j - 1] + sub_cost
                )

    return dp[m][n]

def damerau_levenshtein(s1, s2):
    """
    Damerau-Levenshtein distance.
    Includes transposition of adjacent characters as a single operation.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,      # Deletion
                dp[i][j - 1] + 1,      # Insertion
                dp[i - 1][j - 1] + cost  # Substitution
            )

            # Transposition
            if i > 1 and j > 1 and s1[i-1] == s2[j-2] and s1[i-2] == s2[j-1]:
                dp[i][j] = min(dp[i][j], dp[i-2][j-2] + cost)

    return dp[m][n]

def is_one_edit_away(s1, s2):
    """Check if two strings are at most one edit apart"""
    m, n = len(s1), len(s2)

    if abs(m - n) > 1:
        return False

    if m > n:
        s1, s2 = s2, s1
        m, n = n, m

    i = j = 0
    found_difference = False

    while i < m and j < n:
        if s1[i] != s2[j]:
            if found_difference:
                return False
            found_difference = True
            if m == n:
                i += 1
        else:
            i += 1
        j += 1

    return True

# Usage
s1 = "kitten"
s2 = "sitting"

distance = edit_distance(s1, s2)
print(f"Edit distance: {distance}")  # 3

dist, ops = edit_distance_with_operations(s1, s2)
print(f"Operations ({dist}):")
for op in ops:
    print(f"  {op}")
# Substitute 'k' with 's' at position 0
# Substitute 'e' with 'i' at position 4
# Insert 'g' at position 6
```

### Time complexity

| Case | Complexity |
|------|------------|
| All  | O(m × n)   |

Where m, n are lengths of the two strings.

### Space complexity
O(m × n) for full table. O(min(m, n)) for space-optimized version.

### Edge cases
- Empty string(s)
- Identical strings
- One string is substring of other
- Very different length strings

### Variants
- **Damerau-Levenshtein**: Includes transposition as single operation
- **Hamming Distance**: Only substitutions (strings must be same length)
- **Longest Common Subsequence**: Related but different metric
- **Weighted Edit Distance**: Different costs for different operations

### When to use vs avoid
- **Use when**: Spell checking, fuzzy matching, DNA alignment, measuring string similarity
- **Avoid when**: Exact matching needed, strings are very long (consider approximate methods), only need boolean similarity

### Related
- [LCS](./lcs.md)
- [KMP](../strings/kmp.md)
