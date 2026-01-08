# Bellman-Ford Algorithm
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Shortest Path`

### Topics
**Topics:** `negative weights`, `arbitrage detection`, `dynamic programming`, `cycle detection`

### Definition
A shortest path algorithm that finds the shortest path from a source to all vertices, handling negative edge weights and detecting negative cycles, by relaxing all edges V-1 times.

### Use cases
- Graphs with negative edge weights
- Currency arbitrage detection
- Routing protocols (RIP, BGP)
- Detecting negative cycles
- When Dijkstra cannot be used

### Prerequisites
- Graph representation (edge list)
- Understanding of relaxation
- Handling of negative weights

### Step-by-step
1. Initialize distances: source = 0, all others = infinity
2. Repeat V-1 times: relax all edges
3. Relaxation: if dist[u] + weight < dist[v], update dist[v]
4. One more pass: if any edge can still be relaxed, negative cycle exists
5. Return distances (or report negative cycle)

### In code
```python
def bellman_ford(vertices, edges, source):
    """
    Find shortest paths from source to all vertices.
    vertices: list of vertex names
    edges: list of (u, v, weight) tuples
    """
    # Initialize distances
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0
    predecessor = {v: None for v in vertices}

    # Relax all edges V-1 times
    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                predecessor[v] = u

    # Check for negative cycles
    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            raise ValueError("Graph contains negative cycle")

    return dist, predecessor

def bellman_ford_with_path(vertices, edges, source, target):
    """Get shortest path to specific target"""
    dist, predecessor = bellman_ford(vertices, edges, source)

    # Reconstruct path
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = predecessor[current]

    path.reverse()

    if path[0] != source:
        return float('inf'), []

    return dist[target], path

def detect_negative_cycle(vertices, edges):
    """Detect if graph has any negative cycle reachable from any vertex"""
    # Use a super source connected to all vertices with weight 0
    super_source = '__super__'
    new_edges = edges.copy()
    for v in vertices:
        new_edges.append((super_source, v, 0))

    new_vertices = vertices + [super_source]

    try:
        bellman_ford(new_vertices, new_edges, super_source)
        return False
    except ValueError:
        return True

def find_negative_cycle(vertices, edges):
    """Find and return a negative cycle if it exists"""
    dist = {v: 0 for v in vertices}  # Start all at 0
    predecessor = {v: None for v in vertices}

    # Relax V times (one extra to detect cycle)
    cycle_vertex = None
    for i in range(len(vertices)):
        for u, v, weight in edges:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                predecessor[v] = u
                if i == len(vertices) - 1:
                    cycle_vertex = v

    if cycle_vertex is None:
        return []

    # Find the cycle
    # Go back V times to ensure we're in the cycle
    for _ in range(len(vertices)):
        cycle_vertex = predecessor[cycle_vertex]

    cycle = []
    current = cycle_vertex
    while True:
        cycle.append(current)
        current = predecessor[current]
        if current == cycle_vertex:
            break

    cycle.append(cycle_vertex)
    cycle.reverse()
    return cycle

# Currency arbitrage detection
def find_arbitrage(exchange_rates):
    """
    exchange_rates: dict of {(from, to): rate}
    Example: {('USD', 'EUR'): 0.85, ('EUR', 'GBP'): 0.88, ...}
    """
    import math

    currencies = set()
    for (c1, c2) in exchange_rates:
        currencies.add(c1)
        currencies.add(c2)

    currencies = list(currencies)

    # Convert to negative log for shortest path
    # If rate1 * rate2 * ... > 1, then -log(rate1) - log(rate2) - ... < 0
    edges = []
    for (c1, c2), rate in exchange_rates.items():
        edges.append((c1, c2, -math.log(rate)))

    return detect_negative_cycle(currencies, edges)

# Usage
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'C', -3), ('B', 'D', 2),
    ('C', 'D', 3), ('D', 'E', 2),
    ('E', 'B', -1)
]

try:
    dist, pred = bellman_ford(vertices, edges, 'A')
    print(dist)  # {'A': 0, 'B': 4, 'C': 1, 'D': 4, 'E': 6}
except ValueError as e:
    print(e)
```

### Time complexity

| Case | Complexity |
|------|------------|
| All  | O(V × E)   |

Where V = number of vertices, E = number of edges.

V-1 iterations, each relaxing E edges.

### Space complexity
O(V) for distance and predecessor arrays.

### Edge cases
- Negative cycle (detect and report)
- Disconnected vertices (remain at infinity)
- All positive weights (works, but Dijkstra faster)
- Single vertex

### Variants
- **SPFA (Shortest Path Faster Algorithm)**: Queue-based optimization, faster in practice
- **Yen's k-shortest paths**: Find k best paths
- **Johnson's algorithm**: Use Bellman-Ford to reweight, then Dijkstra

### When to use vs avoid
- **Use when**: Graph has negative edge weights, need to detect negative cycles, arbitrage detection
- **Avoid when**: No negative weights (Dijkstra is faster), very large graphs, real-time applications

### Related
- [Dijkstra](./dijkstra.md)
- [Floyd-Warshall](./floydWarshall.md)
