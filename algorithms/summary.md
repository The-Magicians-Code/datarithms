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
