# Radix Sort
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Sorting`

### Topics
**Topics:** `integer sorting`, `linear time`, `digit-by-digit`, `non-comparison sort`

### Definition
A non-comparison sorting algorithm that sorts integers by processing individual digits, from least significant to most significant (LSD) or vice versa (MSD), using a stable sort like counting sort for each digit position.

### Use cases
- Sorting large numbers of integers
- Fixed-length strings or keys
- When range is too large for counting sort alone
- Parallel sorting applications

### Prerequisites
- Counting sort or another stable sort
- Understanding of positional notation
- Elements must have fixed-length keys

### Step-by-step
1. Find the maximum number to determine the number of digits
2. Starting from least significant digit (LSD):
3. Apply stable counting sort based on current digit
4. Move to next more significant digit
5. Repeat until all digits are processed
6. Array is now sorted

### In code
```python
def radix_sort(arr):
    if not arr:
        return arr

    # Find maximum to determine number of digits
    max_val = max(arr)

    # Process each digit position
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr

def counting_sort_by_digit(arr, exp):
    """Stable counting sort by specific digit"""
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences
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

    # Copy back
    for i in range(n):
        arr[i] = output[i]

# Radix sort with different base
def radix_sort_base(arr, base=10):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort_by_base(arr, exp, base)
        exp *= base

    return arr

def counting_sort_by_base(arr, exp, base):
    n = len(arr)
    output = [0] * n
    count = [0] * base

    for num in arr:
        digit = (num // exp) % base
        count[digit] += 1

    for i in range(1, base):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % base
        count[digit] -= 1
        output[count[digit]] = arr[i]

    for i in range(n):
        arr[i] = output[i]

# Radix sort for strings (fixed length)
def radix_sort_strings(arr, max_len=None):
    if not arr:
        return arr

    if max_len is None:
        max_len = max(len(s) for s in arr)

    # Pad strings to equal length
    arr = [s.ljust(max_len) for s in arr]

    # Sort from rightmost character
    for i in range(max_len - 1, -1, -1):
        arr = sorted(arr, key=lambda x: x[i])

    return [s.rstrip() for s in arr]

# Handling negative numbers
def radix_sort_with_negatives(arr):
    if not arr:
        return arr

    negatives = [-x for x in arr if x < 0]
    non_negatives = [x for x in arr if x >= 0]

    if negatives:
        radix_sort(negatives)
        negatives = [-x for x in reversed(negatives)]

    if non_negatives:
        radix_sort(non_negatives)

    return negatives + non_negatives

# Usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)  # [2, 24, 45, 66, 75, 90, 170, 802]
```

### Time complexity

| Case    | Complexity |
|---------|------------|
| Best    | O(d * (n + k)) |
| Average | O(d * (n + k)) |
| Worst   | O(d * (n + k)) |

Where:
- n = number of elements
- d = number of digits in maximum number
- k = base (10 for decimal)

For fixed d, this is O(n) - linear time.

### Space complexity
O(n + k) for the counting sort auxiliary arrays. k is typically 10 (decimal) or 256 (bytes).

### Edge cases
- Empty array
- Single element
- Numbers with different digit counts
- Negative numbers (need special handling)
- Very large numbers (many digits)

### Variants
- **LSD Radix Sort**: Least significant digit first (shown above, stable)
- **MSD Radix Sort**: Most significant digit first, can short-circuit
- **In-place MSD**: Uses less memory but more complex
- **Binary radix sort**: Base 2, efficient for binary data

### When to use vs avoid
- **Use when**: Sorting many integers with bounded digit count, fixed-length strings, linear time needed
- **Avoid when**: Variable-length keys, floating-point numbers, small arrays (overhead), memory constrained

### Related
- [Counting Sort](./countingSort.md)
- [Quick Sort](./quickSort.md)
- [Merge Sort](./mergeSort.md)
