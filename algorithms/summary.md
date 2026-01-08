# Algorithms
[Back](../index.md)

## By Category

{%- assign algorithms = site.pages | where_exp: "page", "page.path contains 'algorithms/'" | where_exp: "page", "page.path != 'algorithms/summary.md'" | sort: "name" -%}

{%- assign categories = "sorting,searching,graphs,dp,strings,greedy,backtracking,bitmath,streaming" | split: "," -%}

{%- assign category_names = "Sorting & Selection,Searching,Graph Algorithms,Dynamic Programming,String Algorithms,Greedy Algorithms,Backtracking,Bit Manipulation & Math,Streaming Algorithms" | split: "," -%}

{%- for cat in categories -%}
{%- assign cat_pages = algorithms | where_exp: "page", "page.path contains cat" -%}
{%- if cat_pages.size > 0 %}

### {{ category_names[forloop.index0] }}
{%- for page in cat_pages %}
- [{{ page.name | replace: '.md', '' }}]({{ page.url | relative_url }})
{%- endfor %}
{%- endif -%}
{%- endfor %}

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
