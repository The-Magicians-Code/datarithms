# Reservoir Sampling
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Streaming Algorithms`

### Topics
**Topics:** `random sampling`, `streaming data`, `probability`, `online algorithms`

### Definition
A family of randomized algorithms for choosing k samples from a stream of n items, where n is either unknown or too large to fit in memory, with each item having equal probability of being selected.

### Use cases
- Random sampling from large datasets
- A/B testing
- Log sampling
- Streaming data analysis
- Memory-constrained environments

### Prerequisites
- Basic probability
- Random number generation
- Understanding of uniform distribution

### Step-by-step
**Algorithm R (k=1):**
1. Keep first item in reservoir
2. For i-th item (i > 1):
   - Generate random j in [1, i]
   - If j == 1, replace reservoir with current item
3. Final reservoir is uniform random sample

**Algorithm R (general k):**
1. Fill reservoir with first k items
2. For i-th item (i > k):
   - Generate random j in [1, i]
   - If j <= k, replace reservoir[j-1] with current item

### In code
```python
import random

def reservoir_sample_one(stream):
    """
    Select one random element from stream.
    Each element has 1/n probability of being chosen.
    """
    result = None

    for i, item in enumerate(stream, 1):
        # Select with probability 1/i
        if random.randint(1, i) == 1:
            result = item

    return result

def reservoir_sample_k(stream, k):
    """
    Select k random elements from stream (Algorithm R).
    Each element has k/n probability of being in final sample.
    """
    reservoir = []

    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            # Select with probability k/(i+1)
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = item

    return reservoir

def weighted_reservoir_sample(stream, k):
    """
    Weighted reservoir sampling (Algorithm A-ES).
    stream: iterator of (item, weight) pairs
    Items with higher weights have higher probability.
    """
    import heapq

    reservoir = []  # Min-heap of (key, item)

    for item, weight in stream:
        if weight <= 0:
            continue

        # Key = random^(1/weight) - higher weight = higher key
        key = random.random() ** (1.0 / weight)

        if len(reservoir) < k:
            heapq.heappush(reservoir, (key, item))
        elif key > reservoir[0][0]:
            heapq.heapreplace(reservoir, (key, item))

    return [item for _, item in reservoir]

def reservoir_sample_with_replacement(stream, k):
    """
    Sample k items with replacement.
    Each sample is independent uniform random.
    """
    result = [None] * k
    count = 0

    for item in stream:
        count += 1
        for i in range(k):
            if random.randint(1, count) == 1:
                result[i] = item

    return result

class ReservoirSampler:
    """
    Online reservoir sampler that can be updated incrementally.
    """
    def __init__(self, k):
        self.k = k
        self.reservoir = []
        self.count = 0

    def add(self, item):
        """Add item to stream"""
        self.count += 1

        if len(self.reservoir) < self.k:
            self.reservoir.append(item)
        else:
            j = random.randint(0, self.count - 1)
            if j < self.k:
                self.reservoir[j] = item

    def get_sample(self):
        """Return current sample"""
        return self.reservoir.copy()

    def reset(self):
        """Reset sampler"""
        self.reservoir = []
        self.count = 0

def reservoir_sample_optimized(stream, k):
    """
    Optimized version that skips items using geometric distribution.
    Faster for large streams when k << n.
    """
    import math

    reservoir = []

    # Fill reservoir
    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            break
    else:
        return reservoir  # Stream exhausted before k items

    # Main sampling loop
    w = math.exp(math.log(random.random()) / k)

    try:
        while True:
            # Skip items
            skip = int(math.log(random.random()) / math.log(1 - w)) + 1

            for _ in range(skip):
                item = next(stream)

            # Replace random item in reservoir
            reservoir[random.randint(0, k - 1)] = item

            w *= math.exp(math.log(random.random()) / k)
    except StopIteration:
        pass

    return reservoir

def random_node_from_linked_list(head):
    """
    Select random node from linked list in single pass.
    Classic reservoir sampling application.
    """
    result = None
    current = head
    i = 1

    while current:
        if random.randint(1, i) == 1:
            result = current.val
        current = current.next
        i += 1

    return result

def shuffle_stream(stream, k):
    """
    Generate random permutation of first k items from stream.
    Uses variant of reservoir sampling.
    """
    reservoir = []

    for i, item in enumerate(stream):
        if i < k:
            # Insert at random position
            j = random.randint(0, i)
            reservoir.insert(j, item)
        else:
            break

    return reservoir

def stratified_reservoir_sample(stream, k, get_stratum):
    """
    Stratified sampling - maintain proportional representation.
    stream: items
    get_stratum: function that returns stratum for item
    """
    from collections import defaultdict

    strata_counts = defaultdict(int)
    strata_samples = defaultdict(list)

    for i, item in enumerate(stream, 1):
        stratum = get_stratum(item)
        strata_counts[stratum] += 1
        count = strata_counts[stratum]

        # Reservoir sample within each stratum
        if len(strata_samples[stratum]) < k:
            strata_samples[stratum].append(item)
        else:
            j = random.randint(1, count)
            if j <= k:
                strata_samples[stratum][j - 1] = item

    return dict(strata_samples)

# Usage
# Basic sampling
stream = range(1, 1001)  # Numbers 1 to 1000
sample = reservoir_sample_k(iter(stream), 10)
print(f"Random sample of 10 from 1-1000: {sorted(sample)}")

# Verify uniformity (run many times)
counts = [0] * 100
for _ in range(10000):
    stream = range(100)
    sample = reservoir_sample_k(iter(stream), 1)
    counts[sample[0]] += 1
print(f"Sample counts (should be ~uniform): {counts[:10]}...")

# Weighted sampling
weighted_stream = [('a', 10), ('b', 5), ('c', 1), ('d', 1)]
weighted_sample = weighted_reservoir_sample(iter(weighted_stream), 2)
print(f"Weighted sample: {weighted_sample}")  # 'a' most likely

# Online sampler
sampler = ReservoirSampler(5)
for x in range(100):
    sampler.add(x)
print(f"Online sample: {sampler.get_sample()}")

# Single item
single = reservoir_sample_one(range(1000))
print(f"Single random item: {single}")
```

### Time complexity

| Operation | Complexity |
|-----------|------------|
| Sample k from n | O(n) |
| Optimized (Algorithm L) | O(k(1 + log(n/k))) |
| Weighted sampling | O(n log k) |

### Space complexity
O(k) - only stores the reservoir.

### Edge cases
- Stream shorter than k
- k = 0 (empty sample)
- All items identical
- Stream is infinite (works!)

### Variants
- **Weighted Reservoir Sampling**: Items have different selection probabilities
- **Algorithm L**: Optimized for k << n
- **Distributed Reservoir Sampling**: Across multiple machines
- **Min-wise Sampling**: For set similarity

### When to use vs avoid
- **Use when**: Unknown or very large stream, memory constrained, need uniform random sample
- **Avoid when**: Can fit all data in memory, need exact distribution, weighted sampling with negative weights

### Related
- [Count-Min Sketch](./countMinSketch.md)
- [HyperLogLog](./hyperLogLog.md)
