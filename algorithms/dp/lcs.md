# Longest Common Subsequence (LCS)
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Dynamic Programming`

### Topics
**Topics:** `string comparison`, `sequence alignment`, `diff algorithms`, `bioinformatics`

### Definition
Find the longest subsequence present in both sequences, where a subsequence is a sequence derived by deleting some or no elements without changing the order of remaining elements.

### Use cases
- File diff tools (git diff)
- DNA/protein sequence alignment
- Spell checking
- Plagiarism detection
- Version control systems

### Prerequisites
- Understanding of subsequence vs substring
- 2D dynamic programming
- String manipulation

### Step-by-step
1. Create DP table: dp[i][j] = LCS length of first i chars of X and first j chars of Y
2. If X[i-1] == Y[j-1]: dp[i][j] = dp[i-1][j-1] + 1
3. Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
4. Answer is dp[m][n]
5. Backtrack to reconstruct the actual LCS

### In code
```python
def lcs_length(X, Y):
    """
    Find length of Longest Common Subsequence.
    """
    m, n = len(X), len(Y)

    # dp[i][j] = LCS length for X[:i] and Y[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def lcs_with_string(X, Y):
    """Find LCS length and the actual subsequence"""
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the actual LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], ''.join(reversed(lcs))

def lcs_space_optimized(X, Y):
    """Space-optimized LCS using two rows"""
    m, n = len(X), len(Y)

    # Only need current and previous row
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, [0] * (n + 1)

    return prev[n]

def lcs_three_strings(X, Y, Z):
    """LCS of three strings"""
    l, m, n = len(X), len(Y), len(Z)
    dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(l + 1)]

    for i in range(1, l + 1):
        for j in range(1, m + 1):
            for k in range(1, n + 1):
                if X[i-1] == Y[j-1] == Z[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

    return dp[l][m][n]

def longest_common_substring(X, Y):
    """
    Longest Common Substring (contiguous).
    Different from subsequence - must be continuous.
    """
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0
    end_pos = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_pos = i

    return max_len, X[end_pos - max_len:end_pos]

def print_diff(X, Y):
    """Print diff-like output showing changes from X to Y"""
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack and build diff
    diff = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and X[i - 1] == Y[j - 1]:
            diff.append(('=', X[i - 1]))
            i -= 1
            j -= 1
        elif j > 0 and (i == 0 or dp[i][j - 1] >= dp[i - 1][j]):
            diff.append(('+', Y[j - 1]))
            j -= 1
        else:
            diff.append(('-', X[i - 1]))
            i -= 1

    return list(reversed(diff))

# Usage
X = "ABCDGH"
Y = "AEDFHR"

length, lcs = lcs_with_string(X, Y)
print(f"LCS: '{lcs}' (length {length})")  # "ADH" (length 3)

# Substring example
s1 = "GeeksforGeeks"
s2 = "GeeksQuiz"
length, substr = longest_common_substring(s1, s2)
print(f"Longest Common Substring: '{substr}'")  # "Geeks"
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
- No common characters
- One string is subsequence of other

### Variants
- **Longest Common Substring**: Must be contiguous
- **Shortest Common Supersequence**: Shortest string containing both as subsequences
- **LCS of multiple strings**: Extension to 3+ strings
- **Longest Palindromic Subsequence**: LCS(s, reverse(s))

### When to use vs avoid
- **Use when**: Comparing sequences, diff tools, similarity metrics, bioinformatics alignment
- **Avoid when**: Need exact match (use string matching), order doesn't matter (use set intersection)

### Related
- [Edit Distance](./editDistance.md)
- [LIS](./lis.md)
