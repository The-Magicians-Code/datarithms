# Trie (Prefix Tree)
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Trees`

### Topics
**Topics:** `autocomplete`, `prefix queries`, `lexicographic search`, `spell checking`

### Definition
A tree-like data structure for storing strings where each node represents a character, enabling efficient prefix-based operations in O(L) time where L is the string length.

### Use cases
- Autocomplete and typeahead suggestions
- Spell checkers and dictionary lookups
- IP routing tables (longest prefix matching)
- Word games (finding valid words)
- Prefix-based search engines

### Attributes
- Each node represents a character
- Root is empty, paths from root to marked nodes form words
- Children stored as hash map or array of 26 (for lowercase letters)
- End-of-word marker indicates complete words

### Common operations

| Operation        | Time  | Description |
|------------------|-------|-------------|
| Insert           | O(L)  | Add word of length L |
| Search           | O(L)  | Find exact word |
| Prefix search    | O(P)  | Check if prefix exists |
| Autocomplete     | O(P+S)| Find S suggestions with prefix P |
| Delete           | O(L)  | Remove word |

### In code
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert word - O(L)"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        """Search exact word - O(L)"""
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        """Check if any word starts with prefix - O(P)"""
        return self._find_node(prefix) is not None

    def _find_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def autocomplete(self, prefix):
        """Get all words with prefix - O(P + S)"""
        node = self._find_node(prefix)
        if not node:
            return []
        results = []
        self._dfs(node, prefix, results)
        return results

    def _dfs(self, node, path, results):
        if node.is_end:
            results.append(path)
        for char, child in node.children.items():
            self._dfs(child, path + char, results)

# Usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("application")

trie.search("app")       # True
trie.starts_with("app")  # True
trie.autocomplete("app") # ["app", "apple", "application"]
```

### Time complexity
- **Insert/Search/Delete**: O(L) where L is word length
- **Prefix check**: O(P) where P is prefix length
- **Autocomplete**: O(P + S) where S is total characters in suggestions
- **All operations are independent of total words stored**

### Space complexity
O(N * L) worst case where N is number of words and L is average length. With prefix sharing, actual space is often much less. Each node stores a hash map of children.

### Trade-offs
**Pros:**
- O(L) operations independent of dictionary size
- Efficient prefix queries
- Natural alphabetical ordering
- No hash collisions

**Cons:**
- High memory usage (one node per character)
- Not cache-friendly (pointer chasing)
- Overkill for exact-match-only lookups (use hash map)

### Variants
- **Compressed trie (Radix tree)**: Merge single-child chains to save space
- **Ternary search trie**: Three children (less, equal, greater) - more space efficient
- **Suffix trie**: Store all suffixes for pattern matching
- **DAWG**: Directed acyclic word graph - shares suffixes too

### When to use vs avoid
- **Use when**: Need prefix operations, autocomplete, dictionary with partial matching, lexicographic ordering
- **Avoid when**: Only need exact match (hash map is simpler), memory constrained, few strings to store

### Related
- [Binary Search Tree](./bst.md)
- [Hash Map](../hashBased/hashmap.md)
