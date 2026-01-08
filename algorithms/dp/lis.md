# Longest Increasing Subsequence (LIS)
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Dynamic Programming`

### Topics
**Topics:** `subsequence`, `patience sorting`, `binary search optimization`, `sequence analysis`

### Definition
Find the length of the longest subsequence of a given sequence in which the elements are in strictly increasing order.

### Use cases
- Stock price analysis (longest uptrend)
- DNA sequence analysis
- Box stacking problems
- Building schedules
- Chain problems (Russian doll envelopes)

### Prerequisites
- Understanding of subsequence
- Binary search (for optimized version)
- Dynamic programming

### Step-by-step
**O(n²) DP Approach:**
1. dp[i] = length of LIS ending at index i
2. For each i, check all j < i
3. If arr[j] < arr[i]: dp[i] = max(dp[i], dp[j] + 1)
4. Answer is max(dp)

**O(n log n) Binary Search Approach:**
1. Maintain a list of smallest tail elements for each length
2. For each element, binary search for its position
3. Replace or extend the list
4. Length of list is LIS length

### In code
```python
from bisect import bisect_left, bisect_right

def lis_dp(nums):
    """
    O(n²) DP solution.
    Returns length of longest increasing subsequence.
    """
    if not nums:
        return 0

    n = len(nums)
    # dp[i] = length of LIS ending at index i
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

def lis_binary_search(nums):
    """
    O(n log n) solution using binary search.
    tails[i] = smallest tail element for LIS of length i+1
    """
    if not nums:
        return 0

    tails = []

    for num in nums:
        # Find position to insert/replace
        pos = bisect_left(tails, num)

        if pos == len(tails):
            tails.append(num)  # Extend
        else:
            tails[pos] = num   # Replace

    return len(tails)

def lis_with_sequence(nums):
    """Return both LIS length and one valid LIS"""
    if not nums:
        return 0, []

    n = len(nums)
    dp = [1] * n
    parent = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    # Find the end of LIS
    max_len = max(dp)
    end_idx = dp.index(max_len)

    # Reconstruct LIS
    lis = []
    idx = end_idx
    while idx != -1:
        lis.append(nums[idx])
        idx = parent[idx]

    return max_len, lis[::-1]

def lis_binary_search_with_sequence(nums):
    """O(n log n) solution that also returns the LIS"""
    if not nums:
        return 0, []

    n = len(nums)
    tails = []          # Smallest tail for each length
    tails_idx = []      # Index of tail element
    parent = [-1] * n   # Parent pointer for reconstruction

    for i, num in enumerate(nums):
        pos = bisect_left(tails, num)

        if pos == len(tails):
            tails.append(num)
            tails_idx.append(i)
        else:
            tails[pos] = num
            tails_idx[pos] = i

        # Set parent
        if pos > 0:
            parent[i] = tails_idx[pos - 1]

    # Reconstruct
    lis = []
    idx = tails_idx[-1]
    while idx != -1:
        lis.append(nums[idx])
        idx = parent[idx]

    return len(tails), lis[::-1]

def longest_non_decreasing_subsequence(nums):
    """LIS with non-strict inequality (allows equal elements)"""
    if not nums:
        return 0

    tails = []

    for num in nums:
        # Use bisect_right for non-strict
        pos = bisect_right(tails, num)

        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)

def longest_decreasing_subsequence(nums):
    """Longest decreasing subsequence"""
    return lis_binary_search([-x for x in nums])

def count_lis(nums):
    """Count the number of LIS"""
    if not nums:
        return 0

    n = len(nums)
    length = [1] * n  # Length of LIS ending at i
    count = [1] * n   # Count of LIS ending at i

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]

    max_len = max(length)
    total_count = sum(c for l, c in zip(length, count) if l == max_len)

    return total_count

def russian_doll_envelopes(envelopes):
    """
    Maximum number of envelopes you can Russian doll.
    envelopes: list of (width, height)
    """
    # Sort by width ascending, height descending
    # This ensures we can use LIS on heights
    envelopes.sort(key=lambda x: (x[0], -x[1]))

    heights = [h for _, h in envelopes]
    return lis_binary_search(heights)

# Usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]

length = lis_binary_search(nums)
print(f"LIS length: {length}")  # 4

length, sequence = lis_with_sequence(nums)
print(f"One LIS: {sequence}")  # [2, 3, 7, 18] or [2, 5, 7, 18]

# Russian doll example
envelopes = [(5,4), (6,4), (6,7), (2,3)]
print(f"Max envelopes: {russian_doll_envelopes(envelopes)}")  # 3
```

### Time complexity

| Method | Complexity |
|--------|------------|
| DP | O(n²) |
| Binary Search | O(n log n) |
| Count LIS | O(n²) |

### Space complexity
O(n) for both methods.

### Edge cases
- Empty array
- All elements equal
- Already sorted (ascending)
- Reverse sorted (descending)
- Single element

### Variants
- **Longest Non-Decreasing Subsequence**: Allows equal consecutive elements
- **Longest Decreasing Subsequence**: Reverse problem
- **Number of LIS**: Count all longest subsequences
- **Longest Bitonic Subsequence**: Increases then decreases

### When to use vs avoid
- **Use when**: Finding trends in sequences, chain problems, envelope nesting
- **Avoid when**: Need contiguous subarray (use different approach), sequence is very short (brute force may suffice)

### Related
- [LCS](./lcs.md)
- [Knapsack](./knapsack.md)
