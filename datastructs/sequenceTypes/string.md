# String
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Sequence types`

### Topics
**Topics:** `pattern matching`, `encoding`, `parsing`, `text processing`

### Definition
An immutable sequence of characters stored contiguously in memory, supporting efficient read operations but requiring new allocations for modifications.

### Use cases
- Text processing and manipulation
- Pattern matching and search (KMP, Rabin-Karp)
- Parsing input data and file formats
- Dictionary keys (hashable due to immutability)

### Attributes
- Immutable in Python (and Java) - modifications create new strings
- Contiguous memory storage like arrays
- Hashable - can be used as dictionary keys
- Support for Unicode and various encodings

### Common operations

| Operation       | Time Complexity | Description |
|-----------------|-----------------|-------------|
| Access (index)  | O(1)            | Get character at position |
| Slice           | O(k)            | Extract k characters |
| Concatenate     | O(n + m)        | Join two strings |
| Search (in)     | O(n)            | Check substring presence |
| Find            | O(n * m)        | Locate substring position |
| Join            | O(n)            | Combine list of strings |
| Compare         | O(n)            | Lexicographic comparison |

### In code
```python
# Strings are immutable sequences
s = "hello"

# Access - O(1)
print(s[0])  # 'h'

# Slicing - O(k)
print(s[1:4])  # 'ell'

# Concatenation creates new string - O(n + m)
s2 = s + " world"

# Inefficient: O(n^2) - avoid in loops
result = ""
for char in "abc":
    result += char  # Creates new string each time

# Efficient: O(n) - use join for building strings
chars = ['a', 'b', 'c']
result = "".join(chars)

# Common string operations
s.lower()      # O(n) - new string
s.upper()      # O(n) - new string
s.split()      # O(n) - splits on whitespace
s.strip()      # O(n) - removes leading/trailing whitespace
s.replace('l', 'L')  # O(n) - replace all occurrences

# Pattern matching
if "ell" in s:        # O(n) - substring check
    idx = s.find("ell")  # O(n*m) worst case
```

### Time complexity
- **Access**: O(1) - direct index calculation
- **Slicing**: O(k) - copies k characters to new string
- **Concatenation**: O(n + m) - creates new string of combined length
- **Loop concatenation**: O(n^2) - avoid, use join() instead
- **Join**: O(n) - efficient string building
- **Search (in)**: O(n * m) worst case, often O(n) average

### Space complexity
O(n) where n is string length. String operations create new strings (immutability), so modifications use O(n) additional space. String interning may reduce memory for repeated literals.

### Trade-offs
**Pros:**
- Immutability enables safe sharing and hashing
- Thread-safe by design
- O(1) random access like arrays
- Can be dictionary keys

**Cons:**
- Modifications create new strings (memory overhead)
- Naive concatenation in loops is O(n^2)
- Cannot modify in place

### Variants
- **Mutable strings**: Python's `bytearray`, Java's `StringBuilder`
- **Rope**: Tree structure for efficient large string operations
- **Interned strings**: Cached common strings to save memory

### When to use vs avoid
- **Use when**: Working with text data, need hashable sequences, pattern matching, dictionary keys
- **Avoid when**: Frequent in-place modifications needed (use list then join), building strings in loops (use StringBuilder pattern)

### Related
- [Array](./array.md)
- [Dynamic Array](./dynamicArray.md)
- [Trie](../trees/trie.md)
