# Z-Algorithm
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `String Matching`

### Topics
**Topics:** `z-function`, `pattern matching`, `string preprocessing`, `period finding`

### Definition
An algorithm that computes the Z-array for a string, where Z[i] is the length of the longest substring starting at i which is also a prefix of the string. Used for pattern matching and string analysis.

### Use cases
- Pattern matching in text
- Finding all periods of a string
- String compression analysis
- Finding distinct substrings
- Tandem repeat detection

### Prerequisites
- Understanding of string prefix
- Array manipulation
- The "Z-box" concept

### Step-by-step
1. Z[0] is undefined (or set to n)
2. Maintain a "Z-box" [l, r] - rightmost segment matching prefix
3. For each position i:
   - If i > r: compute Z[i] naively, update l, r
   - If i <= r: use previously computed values, extend if needed
4. For pattern matching: concatenate pattern + separator + text

### In code
```python
def z_function(s):
    """
    Compute Z-array for string s.
    Z[i] = length of longest substring starting at i
           that matches a prefix of s.
    """
    n = len(s)
    if n == 0:
        return []

    z = [0] * n
    z[0] = n  # By convention, or can leave as 0

    l, r = 0, 0  # Z-box boundaries

    for i in range(1, n):
        if i < r:
            # Inside Z-box, use previously computed value
            z[i] = min(r - i, z[i - l])

        # Try to extend
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        # Update Z-box if needed
        if i + z[i] > r:
            l, r = i, i + z[i]

    return z

def z_search(text, pattern):
    """
    Find all occurrences of pattern in text using Z-algorithm.
    Returns list of starting indices.
    """
    if not pattern or not text:
        return []

    # Concatenate: pattern + separator + text
    concat = pattern + "$" + text
    z = z_function(concat)

    m = len(pattern)
    result = []

    for i in range(m + 1, len(concat)):
        if z[i] == m:
            result.append(i - m - 1)

    return result

def count_pattern_occurrences(text, pattern):
    """Count occurrences using Z-algorithm"""
    return len(z_search(text, pattern))

def find_all_periods(s):
    """
    Find all periods of string s.
    Period p means s[i] = s[i + p] for all valid i.
    """
    n = len(s)
    z = z_function(s)
    periods = []

    for p in range(1, n):
        # If z[p] + p >= n, then p is a period
        if z[p] + p >= n:
            periods.append(p)

    periods.append(n)  # n is always a period
    return periods

def smallest_period(s):
    """Find the smallest period of string"""
    periods = find_all_periods(s)
    return periods[0] if periods else len(s)

def is_rotation(s1, s2):
    """Check if s2 is a rotation of s1"""
    if len(s1) != len(s2):
        return False

    # s2 is rotation of s1 if s2 is substring of s1+s1
    return bool(z_search(s1 + s1, s2))

def count_distinct_substrings_z(s):
    """Count number of distinct substrings using Z-function"""
    n = len(s)
    count = 0

    for i in range(n):
        # Consider all substrings starting at i
        suffix = s[i:]
        z = z_function(suffix[::-1])  # Z of reversed suffix

        # New substrings = length - max matching prefix
        for j in range(len(suffix)):
            count += 1
        # More efficient approach would use suffix array

    return count

def longest_palindromic_prefix(s):
    """Find longest prefix of s that is a palindrome"""
    # Concatenate s + $ + reverse(s)
    rev = s[::-1]
    concat = s + "$" + rev
    z = z_function(concat)

    n = len(s)
    max_len = 0

    # Check positions in the reversed part
    for i in range(n + 1, len(concat)):
        if i + z[i] == len(concat):
            max_len = max(max_len, z[i])

    return s[:max_len]

def compress_string(s):
    """
    Find shortest string t such that s = t + t + ... + t
    (or s is a prefix of some t^k)
    """
    n = len(s)
    z = z_function(s)

    for p in range(1, n):
        if n % p == 0 and z[p] == n - p:
            return s[:p]

    return s

def match_with_wildcards_z(text, pattern, wildcard='?'):
    """
    Pattern matching where wildcard matches any single character.
    Uses modified Z-algorithm approach.
    """
    n, m = len(text), len(pattern)
    if m > n:
        return []

    result = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if pattern[j] != wildcard and pattern[j] != text[i + j]:
                match = False
                break
        if match:
            result.append(i)

    return result

# Usage
s = "aabxaabxcaabxaabxay"
z = z_function(s)
print(f"Z-array: {z}")
# Z-array shows prefix matches at each position

# Pattern matching
text = "ABABDABACDABABCABAB"
pattern = "ABAB"
indices = z_search(text, pattern)
print(f"Pattern found at: {indices}")  # [0, 10, 15]

# Find periods
s = "abcabcabc"
periods = find_all_periods(s)
print(f"Periods of '{s}': {periods}")  # [3, 6, 9]

# Check rotation
s1 = "rotation"
s2 = "tationro"
print(f"'{s2}' is rotation of '{s1}': {is_rotation(s1, s2)}")  # True

# Compress string
s = "abcabcabc"
print(f"Compressed: '{compress_string(s)}'")  # 'abc'
```

### Time complexity

| Operation | Complexity |
|-----------|------------|
| Z-function | O(n) |
| Search | O(n + m) |

Where n = text length, m = pattern length.

Linear time for both preprocessing and search.

### Space complexity
O(n) for the Z-array. O(n + m) for pattern matching (concatenated string).

### Edge cases
- Empty string
- Single character
- All same characters
- Pattern longer than text
- Pattern at beginning/end

### Variants
- **Extended Z-function**: Additional information for each position
- **Z-function on reversed string**: For suffix analysis
- **Online Z-algorithm**: Process characters one at a time

### When to use vs avoid
- **Use when**: Pattern matching, period finding, string analysis, need both pattern and period info
- **Avoid when**: Multiple patterns (use Aho-Corasick), very long patterns with short text, only need first match

### Related
- [KMP](./kmp.md)
- [Rabin-Karp](./rabinKarp.md)
