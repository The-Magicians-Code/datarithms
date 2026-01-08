# Name

This section must only contain two navigation paths:
- Back - to return to the summary.md file
- Home - to return to the index.md file

Make sure that the relative paths are valid, depending on where the algorithm file is located.

**Example for files directly in algorithms/:**
```
[Back](./summary.md)
[Home](../index.md)
```

**Example for files inside a subfolder within algorithms/:**
```
[Back](../summary.md)
[Home](../../index.md)
```

### Category
Primary classification of this algorithm (pick one).

Example categories:
- Sorting (bubble, quick, merge)
- Pathfinding (Dijkstra, A*, BFS)
- Searching (binary search, linear)
- Cryptography (ROT13, AES, RSA)
- Graph traversal (DFS, BFS)
- Dynamic programming

**Category:** `category-name`

### Topics
Application domains where this algorithm is commonly used (2–4 items).

Example topics:
- Distributed systems
- Caching
- Deduplication
- Networking
- Security
- Machine learning
- Compression
- Databases

**Topics:** `topic1`, `topic2`, `topic3`

### Definition
One‑sentence description of what the algorithm does.

### Use cases
Specific problem types this algorithm solves (2–4 bullets, no vague items).
- Problem type 1
- Problem type 2

### Prerequisites
Concepts or structures needed to understand this algorithm (1–3 items).
- Concept 1
- Data structure X

### Step-by-step
How the algorithm works (3–7 steps, each step a single sentence).
1. Step 1
2. Step 2
3. Step 3

### In code
Simple, short, readable implementation in Python (keep it minimal).
````python
````

### Time complexity
Big O notation; include best/avg/worst if they differ.

| Case    | Complexity |
|---------|------------|
| Best    | O(?)       |
| Average | O(?)       |
| Worst   | O(?)       |

### Space complexity
Big O notation; state extra space only (not input).

### Edge cases
2–3 concrete inputs or scenarios that can break naive implementations.
- Edge case 1
- Edge case 2

### Variants
Named variants or optimizations with a one‑line difference each (1–3).
- Variant 1: description
- Variant 2: description

### When to use vs avoid
Differentiators that help choose this algorithm over alternatives.
- Use when:
- Avoid when:

### Related
Links to similar or related algorithms
- [Related algorithm](./related.md)
