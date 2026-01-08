# Permutations
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Backtracking`

### Topics
**Topics:** `combinatorics`, `recursion`, `arrangement`, `enumeration`

### Definition
Generate all possible arrangements of elements where order matters. For n distinct elements, there are n! (n factorial) permutations.

### Use cases
- Password cracking (brute force)
- Game move sequences
- Task scheduling orderings
- Cryptographic analysis
- Test case generation

### Prerequisites
- Recursion
- Backtracking pattern
- Understanding of factorial growth

### Step-by-step
**Backtracking Approach:**
1. If current permutation is complete, add to result
2. For each unused element:
   - Add element to current permutation
   - Mark as used
   - Recurse
   - Remove element (backtrack)
   - Mark as unused

**Swap-based Approach:**
1. Fix first position with each element
2. Recursively permute remaining positions
3. Swap back to restore original state

### In code
```python
def permutations_backtrack(nums):
    """
    Generate all permutations using backtracking with visited set.
    Time: O(n × n!), Space: O(n)
    """
    result = []
    used = [False] * len(nums)

    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                used[i] = False

    backtrack([])
    return result

def permutations_swap(nums):
    """
    Generate permutations using swap method.
    More memory efficient - modifies array in place.
    """
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result

def permutations_with_duplicates(nums):
    """
    Generate unique permutations when input has duplicates.
    """
    nums.sort()  # Important for duplicate handling
    result = []
    used = [False] * len(nums)

    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return

        for i in range(len(nums)):
            # Skip used elements
            if used[i]:
                continue

            # Skip duplicates: if previous same element wasn't used
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            current.append(nums[i])
            backtrack(current)
            current.pop()
            used[i] = False

    backtrack([])
    return result

def next_permutation(nums):
    """
    Find next lexicographically greater permutation (in-place).
    Returns False if already at last permutation.
    """
    n = len(nums)

    # Find first decreasing element from right
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i < 0:
        # Already at last permutation, reverse to first
        nums.reverse()
        return False

    # Find smallest element greater than nums[i] to the right
    j = n - 1
    while nums[j] <= nums[i]:
        j -= 1

    # Swap
    nums[i], nums[j] = nums[j], nums[i]

    # Reverse suffix
    nums[i + 1:] = reversed(nums[i + 1:])
    return True

def prev_permutation(nums):
    """Find previous lexicographically smaller permutation."""
    n = len(nums)

    i = n - 2
    while i >= 0 and nums[i] <= nums[i + 1]:
        i -= 1

    if i < 0:
        nums.reverse()
        return False

    j = n - 1
    while nums[j] >= nums[i]:
        j -= 1

    nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])
    return True

def kth_permutation(n, k):
    """
    Find k-th permutation sequence (1-indexed).
    Without generating all permutations.
    """
    numbers = list(range(1, n + 1))
    factorials = [1] * (n + 1)

    for i in range(1, n + 1):
        factorials[i] = factorials[i - 1] * i

    k -= 1  # Convert to 0-indexed
    result = []

    for i in range(n, 0, -1):
        # Determine which number to use
        idx = k // factorials[i - 1]
        result.append(numbers[idx])
        numbers.pop(idx)
        k %= factorials[i - 1]

    return result

def permutation_rank(perm):
    """
    Find the rank (1-indexed) of a permutation.
    Inverse of kth_permutation.
    """
    n = len(perm)
    factorials = [1] * n
    for i in range(1, n):
        factorials[i] = factorials[i - 1] * i

    rank = 0
    for i in range(n):
        # Count elements smaller than perm[i] that come after
        smaller = sum(1 for j in range(i + 1, n) if perm[j] < perm[i])
        rank += smaller * factorials[n - 1 - i]

    return rank + 1  # 1-indexed

def permutations_of_string(s):
    """Generate all permutations of a string"""
    chars = list(s)
    result = []

    def backtrack(start):
        if start == len(chars):
            result.append(''.join(chars))
            return

        seen = set()
        for i in range(start, len(chars)):
            if chars[i] not in seen:
                seen.add(chars[i])
                chars[start], chars[i] = chars[i], chars[start]
                backtrack(start + 1)
                chars[start], chars[i] = chars[i], chars[start]

    backtrack(0)
    return result

def count_permutations(n, has_duplicates=None):
    """
    Count permutations without generating.
    has_duplicates: dict of {element: count}
    """
    import math

    if has_duplicates is None:
        return math.factorial(n)

    # n! / (c1! × c2! × ...)
    result = math.factorial(n)
    for count in has_duplicates.values():
        result //= math.factorial(count)

    return result

def partial_permutations(nums, r):
    """
    Generate all r-length permutations (arrangements).
    P(n, r) = n! / (n-r)!
    """
    result = []
    used = [False] * len(nums)

    def backtrack(current):
        if len(current) == r:
            result.append(current[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                used[i] = False

    backtrack([])
    return result

# Usage
nums = [1, 2, 3]

print("All permutations:")
print(permutations_backtrack(nums))
# [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

# With duplicates
nums_dup = [1, 1, 2]
print("\nUnique permutations with duplicates:")
print(permutations_with_duplicates(nums_dup))
# [[1,1,2], [1,2,1], [2,1,1]]

# Next permutation
arr = [1, 2, 3]
next_permutation(arr)
print(f"\nNext permutation: {arr}")  # [1, 3, 2]

# K-th permutation
print(f"\n3rd permutation of [1,2,3]: {kth_permutation(3, 3)}")  # [2, 1, 3]

# Partial permutations
print(f"\n2-permutations of [1,2,3]: {partial_permutations([1,2,3], 2)}")
# [[1,2], [1,3], [2,1], [2,3], [3,1], [3,2]]
```

### Time complexity

| Operation | Complexity |
|-----------|------------|
| All permutations | O(n × n!) |
| Next permutation | O(n) |
| K-th permutation | O(n²) or O(n) with better data structure |

Must generate n! permutations.

### Space complexity
O(n) for recursion depth. O(n × n!) for storing all results.

### Edge cases
- Empty array
- Single element
- All elements the same
- Large n (factorial growth!)

### Variants
- **Permutations with duplicates**: Skip repeated elements
- **Next/Previous permutation**: Lexicographic ordering
- **K-th permutation**: Direct computation
- **Partial permutations**: Choose r from n

### When to use vs avoid
- **Use when**: Need all arrangements, small n (n < 10-12), order matters
- **Avoid when**: Large n (factorial explosion), only need count, can use next_permutation iteratively

### Related
- [Subsets](./subsets.md)
- [N-Queens](./nQueens.md)
