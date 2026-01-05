# Summary of algorithms
[Back](../index.md)

Alphabetical:
- [Bubblesort](./sorting/bubble.md)
- [Quicksort](./sorting/quick.md)

### All algorithms

{%- assign algorithms = site.pages | where_exp: "page", "page.path contains 'algorithms/'" | where_exp: "page", "page.path != 'algorithms/summary.md'" | sort: "name" -%}
{%- for page in algorithms %}
- [{{ page.title | default: page.name | replace: '.md', '' | capitalize }}]({{ page.url | relative_url }})
{%- endfor %}

### The Big-O notation
Also known as Space-time complexity

## Measures for Algorithms

### Time Complexity (Big O Notation)
- Measures how runtime scales with input size
- Common classes: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ)
- Expressed in terms of *number of operations* as a function of input size n

### Space Complexity
- Additional memory required beyond input
- Auxiliary space usage

### Other Considerations
- Best/Average/Worst case performance
- Stability (for sorting algorithms)
- Correctness and termination guarantees
