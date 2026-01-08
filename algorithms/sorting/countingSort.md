# Counting Sort
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Sorting`

### Topics
**Topics:** `integer sorting`, `linear time`, `non-comparison sort`, `frequency counting`

### Definition
A non-comparison sorting algorithm that counts the occurrences of each unique element, then uses those counts to determine element positions in the sorted output, achieving O(n + k) time complexity.

### Use cases
- Sorting integers within a known, limited range
- As a subroutine in radix sort
- Sorting characters (ASCII values)
- When the range k is not significantly larger than n

### Prerequisites
- Elements must be integers (or mappable to integers)
- Range of values must be known
- Sufficient memory for count array

### Step-by-step
1. Find the minimum and maximum values to determine range
2. Create count array of size (max - min + 1) initialized to zeros
3. Count occurrences of each element
4. Compute cumulative counts (prefix sums) for positions
5. Place each element in its correct position in output array
6. Copy output back to original array (if needed)

### In code
```python
def counting_sort(arr):
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    # Count occurrences
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1

    # Build sorted array
    result = []
    for i, c in enumerate(count):
        result.extend([i + min_val] * c)

    return result

# Stable counting sort (preserves relative order)
def counting_sort_stable(arr):
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    # Count occurrences
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1

    # Cumulative count (positions)
    for i in range(1, range_size):
        count[i] += count[i - 1]

    # Build output (traverse input backwards for stability)
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output

# Counting sort for a specific digit (used in radix sort)
def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Digits 0-9

    # Count occurrences of digit at position exp
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # Cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output (backwards for stability)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]

    return output

# Usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)  # [1, 2, 2, 3, 3, 4, 8]

# With negative numbers
arr = [4, -2, 2, -8, 3, -3, 1]
sorted_arr = counting_sort(arr)  # [-8, -3, -2, 1, 2, 3, 4]
```

### Time complexity

| Case    | Complexity |
|---------|------------|
| Best    | O(n + k)   |
| Average | O(n + k)   |
| Worst   | O(n + k)   |

Where n = number of elements, k = range of values (max - min + 1).
- When k = O(n): Linear time O(n)
- When k >> n: May be worse than comparison sorts

### Space complexity
O(n + k) - count array of size k plus output array of size n.

### Edge cases
- Empty array
- Single element
- All elements identical
- Large range with sparse elements (inefficient)
- Negative numbers (adjust with offset)

### Variants
- **Stable counting sort**: Preserves relative order of equal elements
- **In-place counting sort**: Possible but complex for limited ranges
- **Generalized counting sort**: For objects with integer keys

### When to use vs avoid
- **Use when**: Small range k relative to n, integers or mappable keys, need linear time, stability required
- **Avoid when**: Large or unknown range, floating-point numbers, memory constrained

### Related
- [Radix Sort](./radixSort.md)
- [Quick Sort](./quickSort.md)
