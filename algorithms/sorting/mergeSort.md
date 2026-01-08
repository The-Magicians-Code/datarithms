# Merge Sort
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Sorting`

### Topics
**Topics:** `divide and conquer`, `stable sort`, `linked lists`, `external sorting`

### Definition
A divide-and-conquer sorting algorithm that recursively divides the array into halves, sorts each half, and merges them back together in sorted order.

### Use cases
- When stable sort is required (preserves order of equal elements)
- Sorting linked lists (no random access needed)
- External sorting (large files that don't fit in memory)
- Parallel sorting (independent subproblems)

### Prerequisites
- Recursion
- Merging two sorted arrays
- Divide and conquer strategy

### Step-by-step
1. If array has 0 or 1 elements, it's already sorted (base case)
2. Divide the array into two halves
3. Recursively sort the left half
4. Recursively sort the right half
5. Merge the two sorted halves into one sorted array

### In code
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= for stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# In-place merge sort (more complex, saves space)
def merge_sort_inplace(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left < right:
        mid = (left + right) // 2
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        merge_inplace(arr, left, mid, right)

def merge_inplace(arr, left, mid, right):
    left_copy = arr[left:mid + 1]
    right_copy = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            arr[k] = left_copy[i]
            i += 1
        else:
            arr[k] = right_copy[j]
            j += 1
        k += 1

    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1

    while j < len(right_copy):
        arr[k] = right_copy[j]
        j += 1
        k += 1

# Merge sort for linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sort_linked(head):
    if not head or not head.next:
        return head

    # Find middle using slow/fast pointers
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = merge_sort_linked(head)
    right = merge_sort_linked(mid)

    return merge_linked(left, right)

def merge_linked(l1, l2):
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next

# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)  # [11, 12, 22, 25, 34, 64, 90]
```

### Time complexity

| Case    | Complexity |
|---------|------------|
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   | O(n log n) |

Always O(n log n) regardless of input - guaranteed performance.

### Space complexity
O(n) for the auxiliary array during merging. O(log n) for recursion stack. Total: O(n).

### Edge cases
- Empty array or single element
- Already sorted array (still O(n log n))
- All elements identical

### Variants
- **Bottom-up merge sort**: Iterative version, avoids recursion overhead
- **Natural merge sort**: Exploits existing sorted runs
- **Timsort**: Hybrid with insertion sort, used in Python and Java
- **Parallel merge sort**: Independent subproblems enable parallelization

### When to use vs avoid
- **Use when**: Need stable sort, sorting linked lists, guaranteed O(n log n), external sorting
- **Avoid when**: Memory is constrained (use heapsort), need in-place sort

### Related
- [Quick Sort](./quickSort.md)
- [Heap Sort](./heapSort.md)
