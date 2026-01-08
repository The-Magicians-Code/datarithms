# Quickselect
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Selection`

### Topics
**Topics:** `order statistics`, `k-th element`, `median finding`, `top-k problems`

### Definition
A selection algorithm to find the k-th smallest (or largest) element in an unordered list, using quicksort's partitioning but only recursing into one partition, achieving O(n) average time.

### Use cases
- Finding median of unsorted array
- Finding k-th smallest/largest element
- Top-k problems (combined with heap)
- Order statistics

### Prerequisites
- Array partitioning (from quicksort)
- Understanding of pivot selection
- Recursion

### Step-by-step
1. Choose a pivot element (random for better average case)
2. Partition array: elements < pivot go left, > pivot go right
3. If pivot is at position k, return it (found!)
4. If k < pivot position, recurse on left partition only
5. If k > pivot position, recurse on right partition only

### In code
```python
import random

def quickselect(arr, k):
    """Find k-th smallest element (0-indexed)"""
    if not arr or k < 0 or k >= len(arr):
        return None
    return quickselect_helper(arr, 0, len(arr) - 1, k)

def quickselect_helper(arr, low, high, k):
    if low == high:
        return arr[low]

    # Random pivot for better average case
    pivot_idx = random.randint(low, high)
    pivot_idx = partition(arr, low, high, pivot_idx)

    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return quickselect_helper(arr, low, pivot_idx - 1, k)
    else:
        return quickselect_helper(arr, pivot_idx + 1, high, k)

def partition(arr, low, high, pivot_idx):
    pivot = arr[pivot_idx]
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]

    store_idx = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[store_idx] = arr[store_idx], arr[i]
            store_idx += 1

    arr[store_idx], arr[high] = arr[high], arr[store_idx]
    return store_idx

# Iterative version
def quickselect_iterative(arr, k):
    if not arr or k < 0 or k >= len(arr):
        return None

    low, high = 0, len(arr) - 1

    while low < high:
        pivot_idx = random.randint(low, high)
        pivot_idx = partition(arr, low, high, pivot_idx)

        if k == pivot_idx:
            return arr[k]
        elif k < pivot_idx:
            high = pivot_idx - 1
        else:
            low = pivot_idx + 1

    return arr[low]

# Find k-th largest (convert to k-th smallest)
def kth_largest(arr, k):
    n = len(arr)
    return quickselect(arr, n - k)

# Find median
def median(arr):
    n = len(arr)
    if n % 2 == 1:
        return quickselect(arr.copy(), n // 2)
    else:
        left = quickselect(arr.copy(), n // 2 - 1)
        right = quickselect(arr.copy(), n // 2)
        return (left + right) / 2

# Top-k smallest elements
def top_k_smallest(arr, k):
    if k >= len(arr):
        return sorted(arr)
    # Find k-th smallest, then all elements <= it
    kth = quickselect(arr.copy(), k - 1)
    return sorted([x for x in arr if x <= kth][:k])

# Median of medians (guaranteed O(n) worst case)
def median_of_medians(arr, k):
    """Guaranteed O(n) selection algorithm"""
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Divide into groups of 5 and find medians
    chunks = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks]

    # Recursively find median of medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partition around pivot
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return median_of_medians(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return median_of_medians(highs, k - len(lows) - len(pivots))

# Usage
arr = [3, 2, 1, 5, 6, 4]
print(quickselect(arr.copy(), 2))  # 3 (3rd smallest, 0-indexed)
print(kth_largest(arr.copy(), 2))   # 5 (2nd largest)
print(median(arr))                  # 3.5
```

### Time complexity

| Case    | Complexity |
|---------|------------|
| Best    | O(n)       |
| Average | O(n)       |
| Worst   | O(n²)      |

- **Average**: O(n) - each partition eliminates half the elements
- **Worst**: O(n²) - bad pivot selection (like quicksort)
- **Median of medians**: Guaranteed O(n) but with larger constants

### Space complexity
O(1) extra space for iterative version. O(log n) for recursive call stack on average.

### Edge cases
- Empty array
- k out of bounds
- All elements identical
- Array already sorted (bad for deterministic pivot)
- k = 0 (minimum) or k = n-1 (maximum)

### Variants
- **Randomized quickselect**: Random pivot, expected O(n)
- **Median of medians**: Guaranteed O(n) worst case
- **Introselect**: Switches to median-of-medians if too many iterations
- **Floyd-Rivest**: Practical improvement with better constants

### When to use vs avoid
- **Use when**: Need k-th element without full sort, finding median, partial sorting
- **Avoid when**: Need multiple order statistics (sort instead), worst-case guarantee needed (use median of medians)

### Related
- [Quick Sort](./quickSort.md)
- [Heap Sort](./heapSort.md)
- [Heap](../../datastructs/trees/heap.md)
