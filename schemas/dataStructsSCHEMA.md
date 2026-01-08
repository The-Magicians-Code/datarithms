# Name

This section must only contain two navigation paths:
- Back - to return to the summary.md file
- Home - to return to the index.md file

Make sure that the relative paths are valid, depending on where the data structure file is located.

**Example for files directly in datastructs/:**
```
[Back](./summary.md)
[Home](../index.md)
```

**Example for files inside a subfolder within datastructs/:**
```
[Back](../summary.md)
[Home](../../index.md)
```

### Category
Primary classification of this data structure (pick one).

Example categories:
- Sequence types (arrays, lists, strings)
- Hash-based (hashmap, dictionary, set)
- Trees (binary tree, BST, heap)
- Graphs
- Stacks & Queues

**Category:** `category-name`

### Topics
Application domains where this data structure is commonly used (2–4 items).

Example topics:
- Distributed systems
- Caching
- Databases
- Networking
- Security
- Web development
- Operating systems
- Game development

**Topics:** `topic1`, `topic2`, `topic3`

### Definition
One‑sentence description of what it stores and how it is accessed.

### Use cases
Specific scenarios where this structure is a good fit (2–4 bullets).
- Scenario 1
- Scenario 2

### Attributes
Characteristic behavior that differentiates it (2–4 bullets).
- Methods (adding, removing values)
- How does it behave?

### Common operations

| Operation | Time Complexity | Description |
|-----------|-----------------|-------------|
| Access    | O(?)            |             |
| Search    | O(?)            |             |
| Insert    | O(?)            |             |
| Delete    | O(?)            |             |

### In code
Simple, short, readable implementation in Python (keep it minimal).
````python
````

### Time complexity
Big O notation; note average vs worst when different.

### Space complexity
Big O notation; state extra space only (not input).

### Trade-offs
**Pros:**
-

**Cons:**
-

### Variants
Different implementations or variations of this structure (1–3).
- Variant 1: description
- Variant 2: description

### When to use vs avoid
Differentiators that help choose this structure over alternatives.
- Use when:
- Avoid when:

### Related
Links to similar or related data structures
- [Related structure](./related.md)
