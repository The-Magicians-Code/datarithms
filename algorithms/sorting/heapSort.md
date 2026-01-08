# Heap Sort
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Sorting`

### Topics
**Topics:** `heap data structure`, `in-place sorting`, `worst-case bounds`, `selection`

### Definition
A comparison-based sorting algorithm that uses a binary heap data structure, building a max-heap from the input and repeatedly extracting the maximum element to build the sorted array from right to left.

### Use cases
- When guaranteed O(n log n) worst-case is required
- Memory-constrained environments (in-place)
- Priority queue implementations
- Finding k largest/smallest elements

### Prerequisites
- Binary heap structure
- Heapify operation
- Array representation of complete binary tree

### Step-by-step
1. Build a max-heap from the input array (heapify)
2. Swap the root (maximum) with the last element
3. Reduce heap size by 1 (exclude sorted element)
4. Restore heap property by heapifying the root
5. Repeat steps 2-4 until heap size is 1

### In code
```python
def heap_sort(arr):
    n = len(arr)

    # Build max heap - O(n)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one - O(n log n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move max to end
        heapify(arr, i, 0)  # Restore heap property

    return arr

def heapify(arr, n, i):
    """
    Heapify subtree rooted at index i.
    n is the size of heap.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Using Python's heapq (min-heap)
import heapq

def heap_sort_heapq(arr):
    heapq.heapify(arr)  # O(n)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# In-place with heapq (ascending order)
def heap_sort_inplace(arr):
    # heapq is min-heap, so negate for descending behavior
    n = len(arr)
    for i in range(n):
        arr[i] = -arr[i]

    heapq.heapify(arr)

    result = []
    while arr:
        result.append(-heapq.heappop(arr))

    return result

# Iterative heapify (avoids recursion)
def heapify_iterative(arr, n, i):
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest == i:
            break

        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest

# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
heap_sort(arr)  # [11, 12, 22, 25, 34, 64, 90]
```

### Time complexity

| Case    | Complexity |
|---------|------------|
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   | O(n log n) |

- **Build heap**: O(n) - tighter analysis than O(n log n)
- **Extract all**: O(n log n) - n extractions, each O(log n)

### Space complexity
O(1) auxiliary space - in-place sorting. O(log n) for recursive heapify call stack (can be made iterative for O(1)).

### Edge cases
- Empty array or single element
- Already sorted array (still O(n log n))
- All elements identical

### Variants
- **Min-heap sort**: Build min-heap for ascending order directly
- **Bottom-up heapsort**: Alternative heap construction
- **Smoothsort**: Adaptive variant with better best-case
- **Weak heapsort**: Uses weak heap, fewer comparisons

### When to use vs avoid
- **Use when**: Need guaranteed O(n log n), in-place required, worst-case matters
- **Avoid when**: Need stable sort, cache performance critical (poor locality), quicksort's average case is acceptable

### Related
- [Quick Sort](./quickSort.md)
- [Merge Sort](./mergeSort.md)
- [Heap](../../datastructs/trees/heap.md)
