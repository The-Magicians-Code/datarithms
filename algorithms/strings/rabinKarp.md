# Rabin-Karp Algorithm
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `String Matching`

### Topics
**Topics:** `rolling hash`, `pattern matching`, `fingerprinting`, `multiple pattern search`

### Definition
A string matching algorithm that uses hashing to find pattern occurrences, using a rolling hash to efficiently compute hash values for all substrings.

### Use cases
- Plagiarism detection
- Multiple pattern matching
- Finding repeated substrings
- DNA sequence analysis
- Document similarity

### Prerequisites
- Hash functions
- Modular arithmetic
- Understanding of hash collisions

### Step-by-step
1. Compute hash of pattern
2. Compute hash of first window in text
3. Slide window: update hash using rolling hash formula
4. When hashes match, verify with actual string comparison
5. Rolling hash: new_hash = (old_hash - first_char) * base + new_char

### In code
```python
def rabin_karp(text, pattern):
    """
    Find all occurrences of pattern in text using rolling hash.
    Returns list of starting indices.
    """
    if not pattern or len(pattern) > len(text):
        return []

    n, m = len(text), len(pattern)
    d = 256  # Number of characters in alphabet
    q = 101  # A prime number for modulo

    result = []

    # Calculate d^(m-1) % q
    h = pow(d, m - 1, q)

    # Calculate initial hash values
    p_hash = 0  # Pattern hash
    t_hash = 0  # Text window hash

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # Slide pattern over text
    for i in range(n - m + 1):
        # Check if hashes match
        if p_hash == t_hash:
            # Verify character by character (handle collision)
            if text[i:i + m] == pattern:
                result.append(i)

        # Calculate hash for next window
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q

            # Handle negative hash
            if t_hash < 0:
                t_hash += q

    return result

def rabin_karp_multiple(text, patterns):
    """
    Find occurrences of multiple patterns using Rabin-Karp.
    More efficient than running single pattern search multiple times.
    """
    if not patterns:
        return {}

    d = 256
    q = 10**9 + 7
    result = {p: [] for p in patterns}

    # Group patterns by length
    length_groups = {}
    for pattern in patterns:
        m = len(pattern)
        if m not in length_groups:
            length_groups[m] = []
        length_groups[m].append(pattern)

    n = len(text)

    # Process each length group
    for m, group in length_groups.items():
        if m > n:
            continue

        h = pow(d, m - 1, q)

        # Compute pattern hashes
        pattern_hashes = {}
        for pattern in group:
            p_hash = 0
            for c in pattern:
                p_hash = (d * p_hash + ord(c)) % q
            if p_hash not in pattern_hashes:
                pattern_hashes[p_hash] = []
            pattern_hashes[p_hash].append(pattern)

        # Compute initial text hash
        t_hash = 0
        for i in range(m):
            t_hash = (d * t_hash + ord(text[i])) % q

        # Search
        for i in range(n - m + 1):
            if t_hash in pattern_hashes:
                for pattern in pattern_hashes[t_hash]:
                    if text[i:i + m] == pattern:
                        result[pattern].append(i)

            if i < n - m:
                t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
                if t_hash < 0:
                    t_hash += q

    return result

def find_repeated_substring(s, length):
    """Find all substrings of given length that appear more than once"""
    if length > len(s):
        return []

    d = 256
    q = 10**9 + 7
    h = pow(d, length - 1, q)

    # Hash -> positions
    seen = {}
    repeated = set()

    # Initial hash
    curr_hash = 0
    for i in range(length):
        curr_hash = (d * curr_hash + ord(s[i])) % q

    seen[curr_hash] = [0]

    # Rolling hash
    for i in range(1, len(s) - length + 1):
        curr_hash = (d * (curr_hash - ord(s[i-1]) * h) + ord(s[i + length - 1])) % q
        if curr_hash < 0:
            curr_hash += q

        if curr_hash in seen:
            # Verify and check for actual duplicates
            for prev_pos in seen[curr_hash]:
                if s[prev_pos:prev_pos + length] == s[i:i + length]:
                    repeated.add(s[i:i + length])
                    break
            seen[curr_hash].append(i)
        else:
            seen[curr_hash] = [i]

    return list(repeated)

def longest_repeated_substring(s):
    """Find the longest substring that appears at least twice"""
    # Binary search on length
    left, right = 0, len(s)
    result = ""

    while left < right:
        mid = (left + right + 1) // 2
        repeated = find_repeated_substring(s, mid)

        if repeated:
            result = repeated[0]
            left = mid
        else:
            right = mid - 1

    return result

def polynomial_hash(s, base=31, mod=10**9 + 9):
    """Compute polynomial hash of string"""
    h = 0
    p = 1
    for c in s:
        h = (h + (ord(c) - ord('a') + 1) * p) % mod
        p = (p * base) % mod
    return h

def count_distinct_substrings(s):
    """Count distinct substrings using rolling hash"""
    n = len(s)
    d = 256
    q = 10**9 + 7

    seen = set()

    for length in range(1, n + 1):
        h = pow(d, length - 1, q)
        curr_hash = 0

        for i in range(length):
            curr_hash = (d * curr_hash + ord(s[i])) % q

        seen.add((length, curr_hash, s[:length]))

        for i in range(1, n - length + 1):
            curr_hash = (d * (curr_hash - ord(s[i-1]) * h) + ord(s[i + length - 1])) % q
            if curr_hash < 0:
                curr_hash += q
            seen.add((length, curr_hash, s[i:i + length]))

    # Handle hash collisions by including actual substring
    return len(seen)

# Usage
text = "ABABDABACDABABCABAB"
pattern = "ABAB"

indices = rabin_karp(text, pattern)
print(f"Pattern '{pattern}' found at: {indices}")  # [0, 10, 15]

# Multiple patterns
patterns = ["AB", "ABAB", "CD"]
result = rabin_karp_multiple(text, patterns)
print(f"Multiple pattern results: {result}")

# Longest repeated substring
s = "banana"
print(f"Longest repeated substring: '{longest_repeated_substring(s)}'")  # 'ana'
```

### Time complexity

| Case | Complexity |
|------|------------|
| Average | O(n + m) |
| Worst | O(n × m) |

Where n = text length, m = pattern length.

Worst case with many hash collisions. Average case assumes good hash function.

### Space complexity
O(1) for single pattern. O(k) for k patterns.

### Edge cases
- Hash collisions (always verify matches)
- Empty pattern or text
- Pattern longer than text
- All characters same (worst case for collisions)

### Variants
- **Double hashing**: Use two hash functions to reduce collisions
- **Suffix array + LCP**: For repeated substring problems
- **Rolling polynomial hash**: Different hash formula

### When to use vs avoid
- **Use when**: Multiple pattern search, plagiarism detection, finding repeated substrings
- **Avoid when**: Single pattern (KMP more reliable), need guaranteed linear time, security-critical (hash collisions)

### Related
- [KMP](./kmp.md)
- [Z-Algorithm](./zAlgorithm.md)
