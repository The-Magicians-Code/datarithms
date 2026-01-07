---
title: Data structures
---
# Data structures
[Back](../index.md)

### All data structures

{%- assign datastructs = site.pages | where_exp: "page", "page.path contains 'datastructs/'" | where_exp: "page", "page.path != 'datastructs/summary.md'" | sort: "name" -%}
{%- for page in datastructs %}
- [{{ page.title | default: page.name | replace: '.md', '' | capitalize }}]({{ page.url | relative_url }})
{%- endfor %}

# Comparisons of data structures

## Measures for Data Structures

### Space Complexity
- Memory usage (bytes, kilobytes)
- Overhead per element stored
- Cache locality/efficiency

### Time Complexity of Operations
- **Access**: How fast can you retrieve an element? O(1), O(n), O(log n), etc.
- **Search**: How fast can you find an element?
- **Insertion/Deletion**: Cost of modifying the structure
- **Traversal**: Cost of visiting all elements
