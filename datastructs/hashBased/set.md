# Set
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Hash-based`

### Topics
**Topics:** `membership testing`, `deduplication`, `graph visited sets`, `set theory operations`

### Definition
An unordered collection of unique hashable elements, implemented as a hash table with only keys (no values), providing O(1) average membership testing.

### Use cases
- Removing duplicates from a collection
- Fast membership testing (visited nodes in graph traversal)
- Set operations (union, intersection, difference)
- Finding common elements between collections

### Attributes
- No duplicate elements allowed
- Elements must be hashable (immutable)
- Unordered (no indexing)
- Supports mathematical set operations

### Common operations

| Operation         | Average | Worst | Description |
|-------------------|---------|-------|-------------|
| add(x)            | O(1)    | O(n)  | Add element |
| remove(x)         | O(1)    | O(n)  | Remove element, raises KeyError if missing |
| discard(x)        | O(1)    | O(n)  | Remove element if present |
| x in s            | O(1)    | O(n)  | Check membership |
| len(s)            | O(1)    | O(1)  | Number of elements |
| s \| t (union)    | O(n+m)  | O(n+m)| Elements in either set |
| s & t (intersect) | O(min)  | O(n*m)| Elements in both sets |
| s - t (diff)      | O(n)    | O(n)  | Elements in s but not t |
| s ^ t (sym diff)  | O(n+m)  | O(n+m)| Elements in exactly one set |

### In code
```python
# Creation
s = {1, 2, 3}
s = set([1, 2, 2, 3])  # {1, 2, 3} - duplicates removed

# Empty set (not {} which creates dict)
empty = set()

# Add/Remove
s.add(4)
s.remove(1)      # KeyError if missing
s.discard(10)    # No error if missing
s.pop()          # Remove and return arbitrary element

# Membership - O(1) average
if 2 in s:
    print("Found!")

# Set operations
a = {1, 2, 3}
b = {2, 3, 4}

union = a | b           # {1, 2, 3, 4}
intersection = a & b    # {2, 3}
difference = a - b      # {1}
symmetric_diff = a ^ b  # {1, 4}

# Set comparisons
a.issubset(b)      # Is a contained in b?
a.issuperset(b)    # Does a contain b?
a.isdisjoint(b)    # No common elements?

# Set comprehension
evens = {x for x in range(10) if x % 2 == 0}

# Common patterns: deduplication
duplicated_list = [1, 2, 2, 3, 3, 3]
unique = list(set(duplicated_list))  # [1, 2, 3]

# Graph visited set pattern
visited = set()
def dfs(node, graph):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph.get(node, []):
        dfs(neighbor, graph)
```

### Time complexity
- **Add/Remove/Contains**: O(1) average, O(n) worst case
- **Union/Symmetric difference**: O(n + m) where n, m are set sizes
- **Intersection**: O(min(n, m)) average - iterates smaller set
- **Difference**: O(n) - iterates first set
- **Subset check**: O(n) - must check all elements

### Space complexity
O(n) for n elements. Like dictionaries, Python sets over-allocate for fast access. Each element stores the object reference and its hash.

### Trade-offs
**Pros:**
- O(1) membership testing (vs O(n) for lists)
- Automatic deduplication
- Built-in set theory operations
- Memory-efficient for unique element storage

**Cons:**
- Elements must be hashable
- No ordering or indexing
- Cannot store duplicates (use Counter if needed)
- Slightly more memory than needed for element count

### Variants
- **frozenset**: Immutable set - can be used as dict key or set element
- **Multiset/Counter**: Allows duplicates, counts occurrences
- **SortedSet** (external): Maintains order, O(log n) operations

### When to use vs avoid
- **Use when**: Need fast membership testing, deduplication, set operations, tracking visited states
- **Avoid when**: Elements are not hashable, need to maintain order, need duplicates, need indexing

### Related
- [Hash Map](./hashmap.md)
- [Dictionary](./dictionary.md)
