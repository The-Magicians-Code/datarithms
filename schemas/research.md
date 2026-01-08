# Research: Interview-Relevant Algorithms and Data Structures

This list focuses on commonly asked topics in software interviews and maps them to categories and keywords that describe where they show up in real systems. It was validated against publicly available university syllabi (see Sources), with a last validation date of 2026-01-08.

## Data Structures

### Sequence Types
- Arrays
  - Keywords: indexing, cache locality, dynamic programming, sliding window
- Dynamic Arrays (e.g., vector, ArrayList)
  - Keywords: amortized analysis, resizing, contiguous storage
- Linked Lists (singly/doubly)
  - Keywords: pointer manipulation, LRU caches, memory-constrained systems
- Strings
  - Keywords: pattern matching, encoding, parsing, text processing

### Hash-Based
- Hash Map / Dictionary
  - Keywords: key-value storage, caching, indexing, frequency counting
- Hash Set
  - Keywords: membership testing, deduplication, graph visited sets

### Tree-Based
- Binary Search Tree (BST)
  - Keywords: ordered data, range queries, in-order traversal
- Balanced BSTs (AVL, Red-Black)
  - Keywords: ordered maps/sets, consistent performance
- Heap / Priority Queue
  - Keywords: scheduling, top-k, Dijkstra, event simulation
- Trie (Prefix Tree)
  - Keywords: autocomplete, prefix queries, lexicographic search
- Segment Tree
  - Keywords: range queries, interval updates
- Fenwick Tree (Binary Indexed Tree)
  - Keywords: prefix sums, point updates

### Graph-Based
- Graphs (adjacency list/matrix)
  - Keywords: networks, dependencies, routing, social graphs
- Union-Find (Disjoint Set Union)
  - Keywords: connectivity, Kruskal, clustering

### Specialized / Systems
- Queue / Deque
  - Keywords: BFS, streaming, task queues
- Stack
  - Keywords: parsing, recursion, monotonic stack
- Circular Buffer
  - Keywords: streaming, low-latency systems, telemetry
- Bloom Filter
  - Keywords: probabilistic membership, caching, distributed systems
- LRU / LFU Cache (often as a combination of hash map + linked list / heap)
  - Keywords: caching, memory efficiency, eviction policies

## Algorithms

### Sorting and Selection
- Quick Sort
  - Keywords: average-case performance, in-place sorting
- Merge Sort
  - Keywords: stable sort, linked lists, external sorting
- Heap Sort
  - Keywords: worst-case bounds, in-place
- Counting / Radix Sort
  - Keywords: integer keys, linear-time sorting
- Quickselect (Kth element)
  - Keywords: top-k, median, order statistics

### Searching
- Binary Search (and variants)
  - Keywords: monotonic predicates, sorted data, search on answer
- Two Pointers / Sliding Window
  - Keywords: subarrays, string processing, streaming data
- Hashing-based lookup
  - Keywords: O(1) expected lookup

### Graph Algorithms
- BFS / DFS
  - Keywords: shortest path in unweighted graphs, connectivity
- Dijkstra
  - Keywords: shortest path, routing, weighted graphs
- Bellman-Ford
  - Keywords: negative weights, arbitrage detection
- Floyd-Warshall
  - Keywords: all-pairs shortest path
- Topological Sort
  - Keywords: dependency resolution, build systems, DAGs
- Minimum Spanning Tree (Kruskal, Prim)
  - Keywords: network design, clustering, cost optimization
- A* Search
  - Keywords: pathfinding, game AI, heuristics

### Dynamic Programming
- Knapsack (0/1, unbounded)
  - Keywords: resource allocation, budgeting
- Longest Common Subsequence / Edit Distance
  - Keywords: diff tools, DNA alignment, version control
- LIS (Longest Increasing Subsequence)
  - Keywords: sequence analysis
- Matrix DP (grid paths)
  - Keywords: robotics, path counting

### String Algorithms
- KMP (Knuth-Morris-Pratt)
  - Keywords: pattern matching, text search
- Rabin-Karp
  - Keywords: rolling hash, plagiarism detection
- Z-Algorithm
  - Keywords: pattern matching, string preprocessing
- Trie-based search
  - Keywords: autocomplete, prefix matching

### Greedy
- Interval Scheduling / Merge Intervals
  - Keywords: scheduling, resource allocation
- Huffman Coding
  - Keywords: compression, entropy coding
- Activity Selection
  - Keywords: optimization under constraints

### Recursion / Backtracking
- Subsets / Permutations / Combinations
  - Keywords: state space search, combinatorics
- N-Queens / Sudoku
  - Keywords: constraint satisfaction
- DFS with pruning
  - Keywords: search optimization

### Bit Manipulation
- Bitmask DP
  - Keywords: combinatorial optimization
- XOR tricks
  - Keywords: parity, deduplication, error detection

### Numeric / Math
- GCD / LCM (Euclid)
  - Keywords: number theory, modular arithmetic
- Fast Exponentiation
  - Keywords: cryptography, modular arithmetic
- Sieve of Eratosthenes
  - Keywords: prime generation

### Data Streaming / Approximate
- Reservoir Sampling
  - Keywords: streaming, randomized algorithms
- Count-Min Sketch
  - Keywords: frequency estimation, streaming analytics
- HyperLogLog
  - Keywords: cardinality estimation, distributed systems

## Category Keywords (Example Cross-References)

### Networking
- Graphs, shortest paths, MST, queues, hashing

### Security / Cryptography
- Hashing, bit operations, fast exponentiation, GCD, string search

### Distributed Systems
- Hashing (consistent hashing), Bloom filters, queues, graphs, caching

### Load Balancing
- Hashing, priority queues, heaps, weighted selection

### Databases / Storage
- B-Trees (mentioned here as common in practice), hashing, segment trees, indexing, LSM structures

### ML / Data Processing
- Sorting, heaps (top-k), prefix sums, dynamic programming

## Interview Emphasis Notes
- Expect heavy focus on arrays/strings, hash maps/sets, stacks/queues, trees, graphs, and dynamic programming.
- Emphasis is on correctness, complexity analysis, and clean implementation.

## Sources (Validation)
Last validated: 2026-01-08

University syllabi and course descriptions:
- MIT 6.006 Introduction to Algorithms (Spring 2020 syllabus): `https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/syllabus`
- Stanford CS161 Design and Analysis of Algorithms (course description): `https://bulletin.stanford.edu/courses/1056871`
- Stanford CS161 Design and Analysis of Algorithms (Fall 2025 course page): `https://cs161-stanford.github.io/`
- Princeton COS 226 Algorithms and Data Structures (Spring 2025 syllabus): `https://www.cs.princeton.edu/courses/archive/spring25/cos226/`
