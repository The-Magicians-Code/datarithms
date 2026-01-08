# Binary Search
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Searching`

### Topics
**Topics:** `sorted data`, `divide and conquer`, `monotonic predicates`, `search on answer`

### Definition
A search algorithm that finds the position of a target value within a sorted array by repeatedly dividing the search interval in half, achieving O(log n) time complexity.

### Use cases
- Searching in sorted arrays
- Finding insertion points
- Lower/upper bound queries
- Search on answer (optimization problems)
- Square root, cube root calculations

### Prerequisites
- Array must be sorted
- Random access to elements
- Comparable elements

### Step-by-step
1. Initialize left and right pointers to array bounds
2. Calculate mid point: mid = (left + right) // 2
3. If target equals arr[mid], return mid (found)
4. If target < arr[mid], search left half (right = mid - 1)
5. If target > arr[mid], search right half (left = mid + 1)
6. Repeat until left > right (not found)

### In code
```python
# Basic binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Not found

# Recursive version
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Lower bound (first element >= target)
def lower_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

# Upper bound (first element > target)
def upper_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left

# Using Python's bisect module
import bisect

arr = [1, 2, 4, 4, 4, 6, 8]
bisect.bisect_left(arr, 4)   # 2 (first 4)
bisect.bisect_right(arr, 4)  # 5 (after last 4)
bisect.bisect(arr, 4)        # Same as bisect_right

# Search on answer pattern
def min_capacity_to_ship(weights, days):
    """Find minimum ship capacity to ship all packages in D days"""
    def can_ship(capacity):
        current_weight = 0
        days_needed = 1
        for w in weights:
            if current_weight + w > capacity:
                days_needed += 1
                current_weight = 0
            current_weight += w
        return days_needed <= days

    left = max(weights)
    right = sum(weights)

    while left < right:
        mid = left + (right - left) // 2
        if can_ship(mid):
            right = mid
        else:
            left = mid + 1

    return left

# Find first True in boolean array
def first_true(arr):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid]:
            right = mid
        else:
            left = mid + 1
    return left if left < len(arr) else -1

# Square root using binary search
def sqrt_int(n):
    if n < 2:
        return n
    left, right = 1, n // 2

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            left = mid + 1
        else:
            right = mid - 1

    return right

# Usage
arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 7))    # 3
print(lower_bound(arr, 6))      # 3 (first >= 6 is 7)
print(upper_bound(arr, 7))      # 4 (first > 7 is 9)
```

### Time complexity

| Case    | Complexity |
|---------|------------|
| Best    | O(1)       |
| Average | O(log n)   |
| Worst   | O(log n)   |

Each comparison eliminates half the remaining elements.

### Space complexity
O(1) for iterative. O(log n) for recursive (call stack).

### Edge cases
- Empty array
- Single element array
- Target not in array
- Target at boundaries
- Duplicate elements (use lower/upper bound)
- Integer overflow in mid calculation

### Variants
- **Lower bound (bisect_left)**: First element >= target
- **Upper bound (bisect_right)**: First element > target
- **Search on answer**: Binary search on result space
- **Exponential search**: Find range first, then binary search
- **Ternary search**: For unimodal functions

### When to use vs avoid
- **Use when**: Sorted data, O(log n) needed, finding boundaries, optimization problems with monotonic predicates
- **Avoid when**: Unsorted data, linked lists (no random access), small arrays (linear may be faster)

### Related
- [Two Pointers](./twoPointers.md)
- [Quick Sort](../sorting/quickSort.md)
