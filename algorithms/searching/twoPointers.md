# Two Pointers
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Searching`

### Topics
**Topics:** `arrays`, `strings`, `sorted data`, `linear time optimization`

### Definition
A technique using two pointers that traverse a data structure (typically from opposite ends or at different speeds) to solve problems in linear time that might otherwise require nested loops.

### Use cases
- Finding pairs with target sum in sorted array
- Removing duplicates in-place
- Reversing arrays/strings
- Detecting cycles (fast/slow pointers)
- Merging sorted arrays
- Container with most water

### Prerequisites
- Understanding of array indexing
- Often requires sorted input
- Pointer movement logic

### Step-by-step
1. Initialize two pointers (start/end or slow/fast)
2. Process elements at pointer positions
3. Move pointers based on condition
4. Repeat until pointers meet or cross
5. Return result

### In code
```python
# Two sum in sorted array
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

# Remove duplicates from sorted array (in-place)
def remove_duplicates(arr):
    if not arr:
        return 0

    write = 1
    for read in range(1, len(arr)):
        if arr[read] != arr[read - 1]:
            arr[write] = arr[read]
            write += 1

    return write  # New length

# Container with most water
def max_area(heights):
    left, right = 0, len(heights) - 1
    max_water = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        max_water = max(max_water, width * height)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Three sum (find triplets that sum to zero)
def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result

# Reverse string in-place
def reverse_string(s):
    left, right = 0, len(s) - 1
    s = list(s)

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return ''.join(s)

# Valid palindrome (ignore non-alphanumeric)
def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

# Fast and slow pointers (cycle detection)
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

# Find middle of linked list
def find_middle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Merge sorted arrays
def merge_sorted(arr1, arr2):
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

# Usage
arr = [1, 2, 3, 4, 6]
print(two_sum_sorted(arr, 6))  # [1, 3] (indices of 2 and 4)
```

### Time complexity

| Pattern | Complexity |
|---------|------------|
| Opposite ends | O(n) |
| Fast/slow | O(n) |
| With sorting | O(n log n) |

Single pass through array with two pointers.

### Space complexity
O(1) typically - only storing pointer indices. Some problems may need O(n) for results.

### Edge cases
- Empty array
- Single element
- All elements same
- No valid answer exists
- Pointers crossing without finding solution

### Variants
- **Opposite ends**: Start from both ends, move toward middle
- **Same direction**: Different speeds (fast/slow)
- **Sliding window**: Special case with variable window
- **Three pointers**: For problems like three-sum

### When to use vs avoid
- **Use when**: Sorted array pair problems, in-place modifications, cycle detection, reducing O(n²) to O(n)
- **Avoid when**: Unsorted data without sorting option, random access patterns needed

### Related
- [Sliding Window](./slidingWindow.md)
- [Binary Search](./binarySearch.md)
