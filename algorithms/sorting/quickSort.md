# Quick Sort
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Sorting`

### Topics
**Topics:** `divide and conquer`, `in-place sorting`, `average-case performance`, `partitioning`

### Definition
A divide-and-conquer sorting algorithm that selects a pivot element and partitions the array so elements smaller than the pivot are on the left and larger on the right, then recursively sorts the subarrays.

### Use cases
- General-purpose sorting when average-case performance matters
- Systems with limited memory (in-place)
- Sorting arrays (not ideal for linked lists)
- When cache performance is important

### Prerequisites
- Recursion
- Array partitioning
- Divide and conquer strategy

### Step-by-step
1. Choose a pivot element from the array (first, last, random, or median-of-three)
2. Partition: rearrange elements so smaller values are left of pivot, larger are right
3. The pivot is now in its final sorted position
4. Recursively apply quicksort to left and right subarrays
5. Base case: arrays of size 0 or 1 are already sorted

### In code
```python
def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition(arr, low, high)
        quicksort(arr, low, pivot_idx - 1)
        quicksort(arr, pivot_idx + 1, high)
    return arr

def partition(arr, low, high):
    """Lomuto partition scheme"""
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Hoare partition (faster in practice)
def hoare_partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i, j = low - 1, high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

# Randomized quicksort (avoids worst case)
import random

def randomized_quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Random pivot selection
        rand_idx = random.randint(low, high)
        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

        pivot_idx = partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_idx - 1)
        randomized_quicksort(arr, pivot_idx + 1, high)
    return arr

# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
quicksort(arr)  # [11, 12, 22, 25, 34, 64, 90]
```

### Time complexity

| Case    | Complexity |
|---------|------------|
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   | O(n²)      |

- **Best/Average**: When pivot divides array roughly in half
- **Worst**: When pivot is always smallest or largest (sorted/reverse sorted input with bad pivot choice)

### Space complexity
O(log n) average for recursion stack. O(n) worst case with unbalanced partitions. In-place - no auxiliary array needed.

### Edge cases
- Already sorted array (worst case with first/last pivot)
- All elements identical (depends on partition scheme)
- Array with many duplicates (three-way partition helps)

### Variants
- **Randomized quicksort**: Random pivot selection avoids worst case
- **Three-way quicksort**: Handles duplicates efficiently (Dutch national flag)
- **Introsort**: Switches to heapsort when recursion too deep (used in C++ STL)
- **Dual-pivot quicksort**: Uses two pivots (Java's Arrays.sort)

### When to use vs avoid
- **Use when**: Need fast average-case in-place sort, cache performance matters
- **Avoid when**: Need stable sort, worst-case guarantee needed, sorting linked lists

### Related
- [Merge Sort](./mergeSort.md)
- [Heap Sort](./heapSort.md)
- [Quickselect](./quickselect.md)
