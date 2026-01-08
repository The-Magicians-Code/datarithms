# Dictionary
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Hash-based`

### Topics
**Topics:** `key-value storage`, `JSON parsing`, `configuration`, `object representation`

### Definition
Python's built-in hash map implementation that stores key-value pairs with O(1) average access time, preserving insertion order as of Python 3.7+.

### Use cases
- Storing configuration settings
- JSON/API response handling
- Grouping and aggregating data
- Function keyword arguments (*kwargs)
- Counting and frequency analysis

### Attributes
- Keys must be hashable (strings, numbers, tuples of immutables)
- Values can be any type
- Maintains insertion order (Python 3.7+)
- Dynamic resizing as elements are added

### Common operations

| Operation      | Average | Worst | Description |
|----------------|---------|-------|-------------|
| d[key]         | O(1)    | O(n)  | Get value, raises KeyError if missing |
| d.get(key)     | O(1)    | O(n)  | Get value or default |
| d[key] = val   | O(1)    | O(n)  | Set or update value |
| del d[key]     | O(1)    | O(n)  | Remove key-value pair |
| key in d       | O(1)    | O(n)  | Check key existence |
| len(d)         | O(1)    | O(1)  | Number of items |
| d.keys()       | O(1)    | O(1)  | View of keys |
| d.values()     | O(1)    | O(1)  | View of values |
| d.items()      | O(1)    | O(1)  | View of key-value pairs |

### In code
```python
# Creation
d = {"name": "Alice", "age": 30}
d = dict(name="Alice", age=30)

# Access
name = d["name"]           # KeyError if missing
age = d.get("age", 0)      # Returns default if missing

# Modification
d["city"] = "NYC"          # Add or update
d.update({"age": 31})      # Merge another dict
d.setdefault("country", "USA")  # Set only if missing

# Deletion
del d["city"]              # Remove key
val = d.pop("age", None)   # Remove and return value

# Iteration (maintains insertion order)
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}

# Common patterns
from collections import defaultdict, Counter

# Auto-initialize missing keys
word_count = defaultdict(int)
for word in ["a", "b", "a"]:
    word_count[word] += 1

# Count frequencies
freq = Counter(["a", "b", "a"])  # {'a': 2, 'b': 1}
```

### Time complexity
- **Lookup/Insert/Delete**: O(1) average, O(n) worst case
- **Iteration**: O(n) - must visit all items
- **Copy**: O(n) - shallow copy of all items
- **Merge (|)**: O(n + m) - combines two dicts (Python 3.9+)

### Space complexity
O(n) for n key-value pairs. Python over-allocates to maintain fast access, typically using 1/3 empty slots. Memory per entry includes key, value, and hash.

### Trade-offs
**Pros:**
- O(1) average operations
- Flexible value types
- Preserves insertion order
- Rich standard library support (defaultdict, Counter)

**Cons:**
- Keys must be hashable
- Memory overhead higher than lists for simple data
- No direct indexing by position

### Variants
- **OrderedDict**: Explicit ordering with move_to_end() support
- **defaultdict**: Auto-initializes missing keys with factory function
- **Counter**: Specialized for counting hashable objects
- **ChainMap**: Views multiple dicts as one (for scope chains)

### When to use vs avoid
- **Use when**: Need key-based lookup, storing heterogeneous data, JSON-like structures, counting
- **Avoid when**: Need numeric indexing, keys are not hashable, memory-constrained simple lists suffice

### Related
- [Hash Map](./hashmap.md)
- [Set](./set.md)
