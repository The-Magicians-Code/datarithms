# Bubble Sort
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Sorting`

### Topics
**Topics:** `comparison sort`, `stable`, `in-place`, `educational`

### Definition
A simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed.

### Use cases
- Educational purposes (teaching sorting concepts)
- Small datasets where simplicity matters
- Nearly sorted data (with optimization)
- When code simplicity is prioritized over performance

### Prerequisites
- Array traversal
- Swapping elements
- Understanding of comparison-based sorting

### Step-by-step
1. Start at the beginning of the array
2. Compare adjacent elements
3. If left > right, swap them
4. Move to next pair
5. After one pass, largest element is at the end ("bubbles up")
6. Repeat for remaining unsorted portion
7. Stop when no swaps occur in a pass (optimized version)

### In code
```python
def bubble_sort(arr):
    """
    Basic bubble sort.
    Time: O(n²), Space: O(1)
    """
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def bubble_sort_optimized(arr):
    """
    Optimized bubble sort with early termination.
    Stops if no swaps occur in a pass (already sorted).
    Best case: O(n) for nearly sorted arrays.
    """
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps, array is sorted
        if not swapped:
            break

    return arr

def bubble_sort_recursive(arr, n=None):
    """Recursive implementation"""
    if n is None:
        n = len(arr)

    # Base case
    if n == 1:
        return arr

    # One pass of bubble sort
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recurse for remaining elements
    return bubble_sort_recursive(arr, n - 1)

def cocktail_shaker_sort(arr):
    """
    Bidirectional bubble sort (Cocktail Shaker Sort).
    Sorts in both directions, reducing passes needed.
    """
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        # Forward pass (left to right)
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        end -= 1
        swapped = False

        # Backward pass (right to left)
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1

    return arr

def count_inversions_bubble(arr):
    """
    Count inversions while sorting.
    An inversion is a pair (i, j) where i < j but arr[i] > arr[j].
    """
    arr = arr.copy()
    n = len(arr)
    inversions = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                inversions += 1

    return inversions

# Usage
arr = [64, 34, 25, 12, 22, 11, 90]

# Basic
result = bubble_sort(arr.copy())
print(f"Sorted: {result}")  # [11, 12, 22, 25, 34, 64, 90]

# Optimized (nearly sorted input)
nearly_sorted = [1, 2, 3, 5, 4]
result = bubble_sort_optimized(nearly_sorted.copy())
print(f"Nearly sorted: {result}")  # [1, 2, 3, 4, 5] - only 2 passes needed

# Count inversions
inversions = count_inversions_bubble([3, 1, 2])
print(f"Inversions: {inversions}")  # 2: (3,1) and (3,2)
```

### Time complexity

| Case | Complexity | When |
|------|------------|------|
| Best | O(n) | Already sorted (optimized version) |
| Average | O(n²) | Random order |
| Worst | O(n²) | Reverse sorted |

### Space complexity
O(1) - in-place sorting, only uses a few extra variables.

### Edge cases
- Empty array
- Single element
- Already sorted
- Reverse sorted
- All elements equal
- Two elements

### Variants
- **Cocktail Shaker Sort**: Bidirectional bubble sort
- **Comb Sort**: Improved bubble sort with gap sequence
- **Odd-Even Sort**: Parallel-friendly variant

### When to use vs avoid
- **Use when**: Teaching/learning, very small arrays (n < 10), nearly sorted data, code simplicity matters
- **Avoid when**: Performance matters, large datasets, production code (use quicksort/mergesort instead)

### Why it's slow
- Makes O(n²) comparisons even when unnecessary
- Only moves elements one position at a time
- Poor cache locality compared to other algorithms

### Related
- [Quick Sort](./quickSort.md)
- [Merge Sort](./mergeSort.md)
- [Insertion Sort](./insertionSort.md)
