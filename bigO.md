---
render_with_liquid: false
---

# Big O Notation
[Home](./index.md)

## What is Big O?
Big O is a notation used to describe the "computational complexity" of an algorithm. The computational complexity of an algorithm is split into two parts: time complexity and space complexity. 
- The time complexity: the amount of **time** the algorithm needs to run relative to the input size. 
- The space complexity: the amount of **memory** used by the algorithm relative to the input size.

Typically, people care about the time complexity more than the space complexity, but both are important to know.
Time complexity: as the input size grows, how much longer does the algorithm take to complete?
Space complexity: as the input size grows, how much more memory does the algorithm use?

Big O notation describes **how an algorithm's performance scales** as input size grows. It answers: "If I double my data, how much longer will this take?"

Think of it as a **speed rating** for algorithms - not the exact time, but how time grows with more data.

### Rules
1. **Ignore constants**, the point of complexity is to analyze the algorithm as the input changes. $O(9999999n)=O(8n)=O(n/500)=O(n)$. Assume algorithm ``A`` uses ``n`` operations, ``B`` uses ``5n`` operations. We estimate the patterns we see when **input changes**. In this case the number of operations increase for both algorithms in a **linear** pattern, therefore $O(n)$.
2. Consider the **complexity as the variables approach infinity**. When we have addition/subtraction between terms of the **same** variable, we ignore all terms except the most powerful one. Sample: $O(2^n+n^2-100n)=O(2^n)$. Reasoning: as ``n`` approaches infinity, the first part becomes massive, making the others irrelevant.

### The Three case scenario
In most algorithms all of them are equal, some algorithms have them different.
- Best case
- Average case
- Worst case (most correct when describing the time or space complexity)

### Analysing time complexity
Let's look at some example algorithms in pseudo-code:
```text
// Given an integer array "arr" with length n,

for (int num: arr) {
    print(num)
}
```
This algorithm has a time complexity of O(n). In each for loop iteration, we are performing a print, which costs $O(1)$. The for loop iterates $n$ times, which gives a time complexity of $O(1⋅n)=O(n)$.
```text
// Given an integer array "arr" with length n,

for (int num: arr) {
    for (int i = 0; i < 500,000; i++) {
        print(num)
    }
}
```
This algorithm has a time complexity of $O(n)$. In each inner for loop iteration, we are performing a print, which costs $O(1)$. This for loop iterates 500,000 times, which means each outer for loop iteration costs $O(500000)=O(1)$. The outer for loop iterates n times, which gives a time complexity of O(n).

Even though the first two algorithms technically have the same time complexity, in reality the second algorithm is much slower than the first one. It's correct to say that the time complexity is $O(n)$, but it's important to be able to discuss the differences between practicality and theory.

### Analyzing space complexity
When you initialize variables like arrays or strings, your algorithm is allocating memory. We never count the space used by the input (it is bad practice to modify the input), and usually don't count the space used by the output (the answer) unless an interviewer asks us to.

>In the below examples, the code is only allocating memory so that we can analyze the space complexity, so we will consider everything we allocate as part of the space complexity (there is no "answer").

```text
// Given an integer array "arr" with length n

for (int num: arr) {
    print(num)
}
```
This algorithm has a space complexity of $O(1)$. The only space allocated is an integer variable `num`, which is constant relative to $n$.
```text
// Given an integer array "arr" with length n

Array doubledNums = int[]

for (int num: arr) {
    doubledNums.add(num * 2)
}
```
This algorithm has a space complexity of $O(n)$. The array `doubledNums` stores $n$ integers at the end of the algorithm.
```text
// Given an integer array "arr" with length n

Array nums = int[]
int oneHundredth = n / 100

for (int i = 0; i < oneHundredth; i++) {
    nums.add(arr[i])
}
```
This algorithm has a space complexity of $O(n)$. The array `nums` stores the first 1% of numbers in `arr`. This gives a space complexity of $O(\dfrac{n}{100})=O(n)$.
```text
// Given integer arrays "arr" with length n and "arr2" with length m,

Array grid = int[n][m]

for (int i = 0; i < arr.length; i++) {
    for (int j = 0; j < arr2.length; j++) {
        grid[i][j] = arr[i] * arr2[j]
    }
}
```
This algorithm has a space complexity of $O(n \cdot m)$. We are creating a `grid` that has dimensions $n \cdot m$.

## The Key Insight

We don't measure actual seconds (that depends on your computer). Instead, we count **operations** and see how that count grows.

```python
# Example: Finding maximum in a list
def find_max(items):
    """How many comparisons do we make?"""
    if not items:
        return None

    max_val = items[0]      # 1 operation
    for item in items[1:]:  # n-1 iterations
        if item > max_val:  # 1 comparison each
            max_val = item
    return max_val

# 10 items = ~10 comparisons
# 100 items = ~100 comparisons
# 1000 items = ~1000 comparisons
# Pattern: operations grow linearly with input -> O(n)

result = find_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Max: {result}")  # 9
```

## Common Complexities (Slowest to Fastest)

### O(1) - Constant: "Instant"

**Analogy**: Looking up a word in a dictionary by page number. Whether the dictionary has 100 or 10,000 pages, turning to page 42 takes the same time.

```python
def get_first(items):
    """Always one operation, regardless of list size."""
    return items[0] if items else None

def get_by_index(items, i):
    """Array access is O(1) - direct memory lookup."""
    return items[i]

# Test with different sizes - same speed
small = list(range(10))
large = list(range(1_000_000))

print(f"First of small list: {get_first(small)}")   # 0
print(f"First of large list: {get_first(large)}")   # 0
# Both are instant - size doesn't matter
```

### O(log n) - Logarithmic: "Halving"

**Analogy**: Finding a name in a phone book. You don't check every page - you open to the middle, see if the name comes before or after, then repeat with half the book. Each step eliminates half the remaining options.

```python
def binary_search(sorted_list, target):
    """
    Each step cuts the search space in half.
    1000 items = ~10 steps (2^10 = 1024)
    1,000,000 items = ~20 steps (2^20 ≈ 1M)
    """
    left, right = 0, len(sorted_list) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2

        if sorted_list[mid] == target:
            print(f"Found in {steps} steps!")
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print(f"Not found after {steps} steps")
    return -1

# Search in 1000 items
items = list(range(1000))
binary_search(items, 777)  # ~10 steps, not 1000!
```

### O(n) - Linear: "One by One"

**Analogy**: Finding a specific card in an unsorted deck. You might get lucky (it's on top), or unlucky (it's at the bottom). On average, you check half the deck, but we say O(n) because worst case is checking all n cards.

```python
def linear_search(items, target):
    """Check each item until found. Worst case: check all n items."""
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

def sum_all(items):
    """Must visit every item once -> O(n)."""
    total = 0
    for item in items:
        total += item
    return total

numbers = [4, 2, 7, 1, 9, 3]
print(f"Index of 9: {linear_search(numbers, 9)}")  # 4
print(f"Sum: {sum_all(numbers)}")  # 26
```

### O(n log n) - Linearithmic: "Smart Sorting"

**Analogy**: Sorting a deck of cards by repeatedly splitting it in half (log n splits), then merging the sorted halves (n operations per level). This is the best we can do for comparison-based sorting.

```python
def merge_sort(items):
    """
    Split in half (log n levels), merge at each level (n work).
    Total: O(n log n)
    """
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    # Merge two sorted halves
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

unsorted = [64, 34, 25, 12, 22, 11, 90]
sorted_list = merge_sort(unsorted)
print(f"Sorted: {sorted_list}")
```

### O(n²) - Quadratic: "Nested Loops"

**Analogy**: Comparing every person in a room with every other person. With 10 people, that's ~100 comparisons. With 100 people, that's ~10,000 comparisons. Doubling people quadruples comparisons.

```python
def bubble_sort(items):
    """
    Compare every pair -> O(n²).
    Simple but slow for large inputs.
    """
    items = items.copy()
    n = len(items)
    comparisons = 0

    for i in range(n):
        for j in range(n - 1 - i):
            comparisons += 1
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    print(f"Comparisons for {n} items: {comparisons}")
    return items

# Notice how comparisons grow
bubble_sort([5, 4, 3, 2, 1])      # 5 items  -> 10 comparisons
bubble_sort(list(range(10, 0, -1)))  # 10 items -> 45 comparisons
# 20 items would be ~190 comparisons (roughly 4x for 2x input)
```

### O(2^n) - Exponential: "Double Trouble"

**Analogy**: You're at a buffet with n dishes. For each dish, you decide: take it or leave it. That's 2 choices per dish, giving 2^n possible plate combinations. Adding just ONE more dish doubles your options!

```python
def all_subsets(items):
    """
    Generate all subsets -> O(2^n) subsets.
    n=3: 8 subsets, n=4: 16, n=5: 32, n=10: 1024!
    """
    if not items:
        return [[]]

    first = items[0]
    rest_subsets = all_subsets(items[1:])

    # Each existing subset spawns two: with and without first
    with_first = [[first] + subset for subset in rest_subsets]
    return rest_subsets + with_first

items = ['a', 'b', 'c']
subsets = all_subsets(items)
print(f"All {len(subsets)} subsets of {items}:")
for s in subsets:
    print(f"  {s}")
```

### O(n!) - Factorial: "Everything with Everything"

**Analogy**: Arranging n people in a line. Person 1 has n spots, person 2 has n-1 spots, etc. That's n × (n-1) × (n-2) × ... × 1 = n! arrangements. This grows VERY fast.

```python
def all_permutations(items):
    """
    Generate all orderings -> O(n!) permutations.
    n=3: 6, n=4: 24, n=5: 120, n=10: 3,628,800!
    """
    if len(items) <= 1:
        return [items[:]]

    result = []
    for i, item in enumerate(items):
        rest = items[:i] + items[i+1:]
        for perm in all_permutations(rest):
            result.append([item] + perm)
    return result

items = [1, 2, 3]
perms = all_permutations(items)
print(f"All {len(perms)} permutations of {items}:")
for p in perms:
    print(f"  {p}")
```

## Visual Comparison

For input size n = 1000:

| Complexity | Operations | Time at 1B ops/sec |
|------------|------------|-------------------|
| O(1) | 1 | instant |
| O(log n) | ~10 | instant |
| O(n) | 1,000 | instant |
| O(n log n) | ~10,000 | instant |
| O(n²) | 1,000,000 | 1 ms |
| O(2^n) | 10^301 | heat death of universe |
| O(n!) | 10^2567 | way past that |

```python
import math

def compare_growth(n):
    """Show how different complexities scale."""
    print(f"\nFor n = {n}:")
    print(f"  O(1)       = 1")
    print(f"  O(log n)   = {math.log2(n):.1f}")
    print(f"  O(n)       = {n}")
    print(f"  O(n log n) = {n * math.log2(n):.0f}")
    print(f"  O(n²)      = {n**2:,}")
    if n <= 20:
        print(f"  O(2^n)     = {2**n:,}")
        print(f"  O(n!)      = {math.factorial(n):,}")
    else:
        print(f"  O(2^n)     = (astronomically large)")
        print(f"  O(n!)      = (incomprehensibly large)")

compare_growth(10)
compare_growth(20)
```

## Rules of Thumb

### 1. Drop Constants
O(2n) = O(n). We care about growth rate, not exact count.

```python
def process_twice(items):
    """Two passes through data is still O(n), not O(2n)."""
    for item in items:  # n operations
        pass
    for item in items:  # n operations
        pass
    # Total: 2n, but we say O(n)
    return len(items) * 2

print(process_twice([1, 2, 3, 4, 5]))
```

### 2. Drop Smaller Terms
O(n² + n) = O(n²). The biggest term dominates as n grows.

```python
def mixed_operations(items):
    """n² dominates n when n is large."""
    n = len(items)

    # O(n²) part
    for i in items:
        for j in items:
            pass

    # O(n) part - insignificant compared to n²
    for item in items:
        pass

    # Total: n² + n, but we say O(n²)
    return n * n + n

print(f"Operations: {mixed_operations([1,2,3,4,5])}")
```

### 3. Different Inputs = Different Variables

```python
def compare_lists(list_a, list_b):
    """
    Two different inputs: use different variables.
    This is O(a × b), not O(n²).
    """
    matches = 0
    for item_a in list_a:      # a iterations
        for item_b in list_b:  # b iterations each
            if item_a == item_b:
                matches += 1
    return matches

a = [1, 2, 3]
b = [2, 3, 4, 5]
print(f"Matches: {compare_lists(a, b)}")  # 2 (values 2 and 3)
```

## Space Complexity

Big O also measures **memory usage**:

```python
def space_examples(n):
    """Different space complexities."""

    # O(1) space - fixed variables regardless of input
    total = 0
    for i in range(n):
        total += i

    # O(n) space - storing n items
    items = list(range(n))

    # O(n²) space - n×n grid
    grid = [[0] * n for _ in range(n)]

    return total, len(items), len(grid)

result = space_examples(5)
print(f"Results: {result}")
```

## Real-World Optimization Example

Here's a practical example: counting how many pairs of equal items exist in a list.

```python
# Naive Approach - O(n²)
def count_equal_pairs_slow(items):
    """Compare every item with every other item."""
    count = 0
    n = len(items)

    for i in range(n):          # n iterations
        for j in range(n):      # n iterations each
            if items[i] == items[j]:
                count += 1

    return count

# Optimized Approach - O(n)
def count_equal_pairs_fast(items):
    """Count occurrences first, then calculate pairs."""
    counts = {}
    for x in items:               # n iterations
        counts[x] = counts.get(x, 0) + 1

    total = 0
    for c in counts.values():     # at most n iterations
        total += c * c            # each item pairs with itself c times

    return total

# Test both approaches
items = [1, 2, 1, 3, 1]
slow_result = count_equal_pairs_slow(items)
fast_result = count_equal_pairs_fast(items)

print(f"Slow method (O(n²)): {slow_result} pairs")
print(f"Fast method (O(n)):  {fast_result} pairs")

# Verify both give same answer
assert slow_result == fast_result
print("Both methods agree!")

# The difference matters at scale:
# 1000 items: slow = ~1,000,000 ops, fast = ~2,000 ops
```

The key insight: Using a hash map trades O(n) space for O(n²) → O(n) time improvement.

## Quick Reference

| When you see... | Think... | Example |
|-----------------|----------|---------|
| Direct access | O(1) | array[i], dict[key] |
| Halving each step | O(log n) | binary search |
| Single loop | O(n) | find max, sum |
| Sorting | O(n log n) | mergesort, quicksort |
| Nested loops (same input) | O(n²) | bubble sort |
| All subsets | O(2^n) | power set |
| All orderings | O(n!) | permutations |

## Related
- [Algorithms](./algorithms/summary.md)
- [Data Structures](./datastructs/summary.md)
