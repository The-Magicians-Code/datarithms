# Subsets (Power Set)
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Backtracking`

### Topics
**Topics:** `combinatorics`, `recursion`, `bit manipulation`, `enumeration`

### Definition
Generate all possible subsets (the power set) of a given set. For a set of n elements, there are 2^n subsets including the empty set and the set itself.

### Use cases
- Feature selection in machine learning
- Finding all combinations in shopping carts
- Network configuration options
- Test case generation
- Combinatorial optimization

### Prerequisites
- Recursion
- Backtracking pattern
- Bit manipulation (alternative approach)

### Step-by-step
**Backtracking Approach:**
1. Start with empty subset
2. At each position, make two choices:
   - Include current element
   - Exclude current element
3. When all positions processed, record the subset
4. Backtrack and try other choices

**Iterative Approach:**
1. Start with empty set in result
2. For each element, add it to all existing subsets
3. Add these new subsets to result

### In code
```python
def subsets_backtrack(nums):
    """
    Generate all subsets using backtracking.
    Time: O(n × 2^n), Space: O(n) for recursion
    """
    result = []

    def backtrack(start, current):
        result.append(current[:])  # Add copy of current subset

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result

def subsets_iterative(nums):
    """
    Generate all subsets iteratively.
    Build up subsets by adding each element to existing subsets.
    """
    result = [[]]

    for num in nums:
        result += [subset + [num] for subset in result]

    return result

def subsets_bitmask(nums):
    """
    Generate all subsets using bit manipulation.
    Each number from 0 to 2^n-1 represents a subset.
    """
    n = len(nums)
    result = []

    for mask in range(1 << n):  # 0 to 2^n - 1
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)

    return result

def subsets_with_duplicates(nums):
    """
    Generate all unique subsets when input has duplicates.
    """
    nums.sort()  # Important: sort to handle duplicates
    result = []

    def backtrack(start, current):
        result.append(current[:])

        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue

            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result

def subsets_of_size_k(nums, k):
    """
    Generate all subsets of exactly size k (combinations).
    """
    result = []

    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return

        # Optimization: not enough elements left
        if len(current) + (len(nums) - start) < k:
            return

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result

def subsets_with_target_sum(nums, target):
    """
    Find all subsets that sum to target.
    """
    result = []

    def backtrack(start, current, current_sum):
        if current_sum == target:
            result.append(current[:])
            # Don't return - there might be more valid subsets

        if current_sum > target:  # Pruning (assumes positive numbers)
            return

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current, current_sum + nums[i])
            current.pop()

    backtrack(0, [], 0)
    return result

def count_subsets(n):
    """Count subsets without generating them"""
    return 1 << n  # 2^n

def subsets_generator(nums):
    """
    Memory-efficient generator version.
    Yields subsets one at a time.
    """
    n = len(nums)

    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        yield subset

def partition_into_k_subsets(nums, k):
    """
    Check if array can be partitioned into k equal-sum subsets.
    """
    total = sum(nums)
    if total % k != 0:
        return False

    target = total // k
    nums.sort(reverse=True)  # Optimization

    if nums[0] > target:
        return False

    buckets = [0] * k

    def backtrack(index):
        if index == len(nums):
            return all(b == target for b in buckets)

        seen = set()  # Avoid duplicate bucket configurations

        for i in range(k):
            if buckets[i] in seen:
                continue
            if buckets[i] + nums[index] <= target:
                seen.add(buckets[i])
                buckets[i] += nums[index]
                if backtrack(index + 1):
                    return True
                buckets[i] -= nums[index]

        return False

    return backtrack(0)

# Usage
nums = [1, 2, 3]

# All subsets
print("All subsets (backtracking):")
print(subsets_backtrack(nums))
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

print("\nAll subsets (bitmask):")
print(subsets_bitmask(nums))

# With duplicates
nums_dup = [1, 2, 2]
print("\nSubsets with duplicates handled:")
print(subsets_with_duplicates(nums_dup))
# [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

# Subsets of size k
print("\nSubsets of size 2:")
print(subsets_of_size_k([1, 2, 3, 4], 2))
# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

# Subsets with target sum
print("\nSubsets summing to 5:")
print(subsets_with_target_sum([1, 2, 3, 4], 5))
# [[1, 4], [2, 3]]
```

### Time complexity

| Method | Complexity |
|--------|------------|
| Backtracking | O(n × 2^n) |
| Iterative | O(n × 2^n) |
| Bitmask | O(n × 2^n) |

Must generate 2^n subsets, each taking O(n) to copy.

### Space complexity
O(n) for recursion depth. O(n × 2^n) for storing all results.

### Edge cases
- Empty input array
- Single element
- All elements the same
- Large n (exponential growth)

### Variants
- **Subsets with duplicates**: Skip duplicate elements
- **Subsets of size k**: Combinations C(n, k)
- **Subsets with sum constraint**: Subset sum problem
- **Partition problems**: Split into k equal parts

### When to use vs avoid
- **Use when**: Need all combinations, small n (n < 20-25), exploring all possibilities
- **Avoid when**: Large n (exponential), only need count (use math), can prune search space significantly

### Related
- [Permutations](./permutations.md)
- [N-Queens](./nQueens.md)
