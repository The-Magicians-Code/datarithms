# KMP (Knuth-Morris-Pratt) Algorithm
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `String Matching`

### Topics
**Topics:** `pattern matching`, `text search`, `prefix function`, `failure function`

### Definition
An efficient string matching algorithm that searches for occurrences of a pattern within a text by using a precomputed "failure function" to avoid redundant comparisons.

### Use cases
- Text editors (find/replace)
- DNA sequence matching
- Spam filters
- Intrusion detection systems
- Log file analysis

### Prerequisites
- Understanding of prefix and suffix
- String indexing
- The concept of proper prefix/suffix

### Step-by-step
**Build Failure Function:**
1. lps[i] = length of longest proper prefix that is also suffix of pattern[0..i]
2. lps[0] = 0 always
3. Use previously computed values to compute next values

**Search:**
1. Compare pattern and text characters
2. On mismatch, use lps to skip characters
3. Never backtrack in text (linear time guarantee)

### In code
```python
def compute_lps(pattern):
    """
    Compute Longest Proper Prefix which is also Suffix (LPS) array.
    Also called failure function or prefix function.
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # Length of previous longest prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Don't increment i, try shorter prefix
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(text, pattern):
    """
    Find all occurrences of pattern in text.
    Returns list of starting indices.
    """
    if not pattern:
        return []

    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    result = []

    i = 0  # Index in text
    j = 0  # Index in pattern

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                result.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result

def kmp_search_first(text, pattern):
    """Find first occurrence of pattern in text. Returns -1 if not found."""
    if not pattern:
        return 0

    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)

    i = j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                return i - j
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1

def count_occurrences(text, pattern):
    """Count non-overlapping occurrences"""
    return len(kmp_search(text, pattern))

def count_overlapping(text, pattern):
    """Count overlapping occurrences"""
    if not pattern:
        return 0

    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    count = 0

    i = j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                count += 1
                j = lps[j - 1]  # Allow overlap
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return count

def shortest_repeating_pattern(s):
    """
    Find the shortest pattern that repeats to form the string.
    Uses LPS property: if n % (n - lps[n-1]) == 0, pattern repeats.
    """
    if not s:
        return ""

    lps = compute_lps(s)
    n = len(s)
    pattern_len = n - lps[n - 1]

    if n % pattern_len == 0 and lps[n - 1] > 0:
        return s[:pattern_len]

    return s  # No repeating pattern

def longest_prefix_suffix(s):
    """Find longest proper prefix which is also suffix"""
    if not s:
        return ""

    lps = compute_lps(s)
    length = lps[-1]

    return s[:length]

# Usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

indices = kmp_search(text, pattern)
print(f"Pattern found at indices: {indices}")  # [10]

# Overlapping example
text2 = "AAAAAA"
pattern2 = "AA"
print(f"Non-overlapping count: {count_occurrences(text2, pattern2)}")  # 3
print(f"Overlapping count: {count_overlapping(text2, pattern2)}")  # 5

# Repeating pattern
s = "abcabcabc"
print(f"Shortest repeating pattern: '{shortest_repeating_pattern(s)}'")  # 'abc'
```

### Time complexity

| Operation | Complexity |
|-----------|------------|
| Build LPS | O(m) |
| Search | O(n) |
| Total | O(n + m) |

Where n = text length, m = pattern length.

### Space complexity
O(m) for the LPS array.

### Edge cases
- Empty pattern
- Empty text
- Pattern longer than text
- Pattern equals text
- No match exists
- Multiple overlapping matches

### Variants
- **Aho-Corasick**: Multiple pattern matching
- **Boyer-Moore**: Often faster in practice
- **Z-Algorithm**: Similar linear time, different approach

### When to use vs avoid
- **Use when**: Single pattern search, need linear guarantee, streaming text
- **Avoid when**: Multiple patterns (use Aho-Corasick), short text (naive may be faster), need approximate matching

### Related
- [Rabin-Karp](./rabinKarp.md)
- [Z-Algorithm](./zAlgorithm.md)
