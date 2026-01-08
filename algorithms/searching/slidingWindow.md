# Sliding Window
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Searching`

### Topics
**Topics:** `subarrays`, `substrings`, `streaming data`, `optimization`

### Definition
A technique that maintains a window (contiguous subsequence) over data, expanding or contracting it to find optimal subarrays/substrings, reducing O(n²) brute force to O(n).

### Use cases
- Maximum/minimum sum subarray of size k
- Longest substring with k distinct characters
- Minimum window substring
- Maximum consecutive ones
- Anagram finding

### Prerequisites
- Understanding of contiguous sequences
- Hash maps for character counting
- Identifying window constraints

### Step-by-step
1. Initialize window boundaries (usually left = right = 0)
2. Expand window by moving right pointer
3. When constraint violated, shrink by moving left pointer
4. Update result at each valid state
5. Repeat until right pointer reaches end

### In code
```python
# Fixed-size window: Maximum sum of subarray size k
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return None

    # Initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Slide window
        max_sum = max(max_sum, window_sum)

    return max_sum

# Variable-size window: Longest substring with k distinct chars
def longest_k_distinct(s, k):
    char_count = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Expand window
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        # Shrink if too many distinct chars
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Minimum window substring
def min_window(s, t):
    from collections import Counter

    if not s or not t:
        return ""

    target = Counter(t)
    required = len(target)
    formed = 0
    window = {}

    left = 0
    min_len = float('inf')
    result = ""

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in target and window[char] == target[char]:
            formed += 1

        # Try to contract window
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]

            left_char = s[left]
            window[left_char] -= 1
            if left_char in target and window[left_char] < target[left_char]:
                formed -= 1
            left += 1

    return result

# Longest substring without repeating characters
def length_of_longest_substring(s):
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# Maximum consecutive ones with k flips
def max_consecutive_ones(nums, k):
    left = 0
    zeros = 0
    max_length = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Find all anagrams
def find_anagrams(s, p):
    from collections import Counter

    result = []
    p_count = Counter(p)
    window = Counter()

    for i in range(len(s)):
        # Add to window
        window[s[i]] += 1

        # Remove from window if needed
        if i >= len(p):
            left_char = s[i - len(p)]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

        # Check for anagram
        if window == p_count:
            result.append(i - len(p) + 1)

    return result

# Subarray product less than k
def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0

    left = 0
    product = 1
    count = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product //= nums[left]
            left += 1

        count += right - left + 1

    return count

# Usage
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
print(max_sum_subarray(arr, 3))  # 13 (6 + -1 + 4 + 1 + 8... wait, that's 5)
# Actually: [4, 1, 8] = 13

s = "abcabcbb"
print(length_of_longest_substring(s))  # 3 ("abc")
```

### Time complexity

| Pattern | Complexity |
|---------|------------|
| Fixed window | O(n) |
| Variable window | O(n) |
| With hash map | O(n) |

Each element is added and removed from window at most once.

### Space complexity
O(1) for simple windows. O(k) or O(alphabet size) when tracking character counts.

### Edge cases
- Empty string/array
- Window size larger than input
- No valid window exists
- All elements same
- Single element input

### Variants
- **Fixed-size window**: Window size k is constant
- **Variable-size window**: Window expands/contracts based on condition
- **Two-pointer variant**: Explicit left and right pointers
- **Circular window**: Wraps around array

### When to use vs avoid
- **Use when**: Finding subarrays/substrings with constraints, optimizing O(n²) patterns, streaming data
- **Avoid when**: Need non-contiguous elements, constraints not on consecutive elements

### Related
- [Two Pointers](./twoPointers.md)
- [Binary Search](./binarySearch.md)
