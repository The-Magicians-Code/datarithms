# Data structures
[Back](../index.md)\
By category:
- graphs
- trees

Alphabetical:
- [Array](./sequenceTypes/array.md)
- [List](./sequenceTypes/list.md)

### All data structures

{% assign datastructs = site.pages | where_exp: "page", "page.path contains 'datastructs/'" | where_exp: "page", "page.path != 'datastructs/summary.md'" %}
{% for page in datastructs %}
- [{{ page.title | default: page.name | replace: '.md', '' }}]({{ page.url | relative_url }})
{% endfor %}

# Comparisons of data structures
