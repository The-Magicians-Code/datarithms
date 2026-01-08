# Algorithms
[Back](../index.md)

## By Category

### Sorting & Selection
- [Quick Sort](./sorting/quickSort.md) - O(n log n) average, divide and conquer
- [Merge Sort](./sorting/mergeSort.md) - O(n log n), stable, divide and conquer
- [Heap Sort](./sorting/heapSort.md) - O(n log n) guaranteed, in-place
- [Counting Sort](./sorting/countingSort.md) - O(n + k), linear for integers
- [Radix Sort](./sorting/radixSort.md) - O(d(n + k)), linear for fixed digits
- [Quickselect](./sorting/quickselect.md) - O(n) average, k-th element selection

### Searching
- [Binary Search](./searching/binarySearch.md) - O(log n), sorted arrays
- [Two Pointers](./searching/twoPointers.md) - O(n), linear traversal patterns
- [Sliding Window](./searching/slidingWindow.md) - O(n), contiguous subarray problems

### Graph Algorithms
- [BFS](./graphs/bfs.md) - O(V + E), shortest path unweighted
- [DFS](./graphs/dfs.md) - O(V + E), traversal and cycle detection
- [Dijkstra](./graphs/dijkstra.md) - O(E log V), shortest path weighted
- [Bellman-Ford](./graphs/bellmanFord.md) - O(VE), handles negative weights
- [Floyd-Warshall](./graphs/floydWarshall.md) - O(V³), all-pairs shortest path
- [Topological Sort](./graphs/topologicalSort.md) - O(V + E), DAG ordering
- [MST (Kruskal/Prim)](./graphs/mst.md) - O(E log E), minimum spanning tree
- [A* Search](./graphs/aStar.md) - O(b^d), heuristic pathfinding

### Dynamic Programming
- [Knapsack](./dp/knapsack.md) - O(nW), subset selection optimization
- [LCS](./dp/lcs.md) - O(mn), longest common subsequence
- [Edit Distance](./dp/editDistance.md) - O(mn), string similarity
- [LIS](./dp/lis.md) - O(n log n), longest increasing subsequence
- [Matrix DP](./dp/matrixDP.md) - O(mn), grid-based problems

### String Algorithms
- [KMP](./strings/kmp.md) - O(n + m), pattern matching
- [Rabin-Karp](./strings/rabinKarp.md) - O(n + m) avg, rolling hash
- [Z-Algorithm](./strings/zAlgorithm.md) - O(n), prefix matching

### Greedy Algorithms
- [Interval Scheduling](./greedy/intervalScheduling.md) - O(n log n), non-overlapping intervals
- [Huffman Coding](./greedy/huffmanCoding.md) - O(n log n), optimal prefix codes
- [Activity Selection](./greedy/activitySelection.md) - O(n log n), maximum activities

### Backtracking
- [Subsets](./backtracking/subsets.md) - O(n × 2^n), power set generation
- [Permutations](./backtracking/permutations.md) - O(n × n!), all arrangements
- [N-Queens](./backtracking/nQueens.md) - O(n!), constraint satisfaction

### Bit Manipulation & Math
- [Bitmask DP](./bitmath/bitmaskDP.md) - O(n² × 2^n), subset state DP
- [XOR Tricks](./bitmath/xorTricks.md) - O(n), duplicate/missing detection
- [GCD/LCM](./bitmath/gcd.md) - O(log n), Euclidean algorithm
- [Fast Exponentiation](./bitmath/fastExpo.md) - O(log n), power computation
- [Sieve of Eratosthenes](./bitmath/sieve.md) - O(n log log n), prime generation

### Streaming Algorithms
- [Reservoir Sampling](./streaming/reservoirSampling.md) - O(n), random sampling from stream
- [Count-Min Sketch](./streaming/countMinSketch.md) - O(1), frequency estimation
- [HyperLogLog](./streaming/hyperLogLog.md) - O(1), cardinality estimation

---

## Complexity Reference

### Time Complexity Classes
| Class | Name | Example |
|-------|------|---------|
| O(1) | Constant | Hash table lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Array scan |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Nested loops |
| O(2^n) | Exponential | Subset enumeration |
| O(n!) | Factorial | Permutation enumeration |

### Common Patterns

**Divide and Conquer**: Split problem, solve recursively, combine
- Quick Sort, Merge Sort, Binary Search

**Dynamic Programming**: Optimal substructure + overlapping subproblems
- Knapsack, LCS, Edit Distance

**Greedy**: Local optimal choices lead to global optimum
- Huffman, Interval Scheduling, Dijkstra

**Backtracking**: Try all possibilities with pruning
- N-Queens, Subsets, Permutations

### Choosing an Algorithm

| Problem Type | Consider |
|-------------|----------|
| Sorted array search | Binary Search |
| Shortest path | BFS (unweighted), Dijkstra (weighted) |
| String matching | KMP, Rabin-Karp |
| Optimization with constraints | DP, Greedy |
| All combinations | Backtracking |
| Streaming data | Reservoir Sampling, Count-Min, HLL |
