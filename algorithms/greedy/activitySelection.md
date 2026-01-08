# Activity Selection
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Greedy Algorithms`

### Topics
**Topics:** `scheduling`, `optimization`, `greedy choice`, `proof of correctness`

### Definition
Select the maximum number of non-overlapping activities from a set of activities with start and finish times, using a greedy approach that always picks the activity that finishes earliest.

### Use cases
- Event scheduling
- Job scheduling
- Resource allocation
- Classroom scheduling
- CPU task selection

### Prerequisites
- Sorting
- Understanding of greedy algorithms
- Optimal substructure concept

### Step-by-step
1. Sort activities by finish time
2. Select first activity (earliest finish)
3. For each remaining activity:
   - If start time >= finish time of last selected activity
   - Include this activity
4. This greedy choice produces optimal solution

**Why it works:**
- Choosing earliest finish leaves maximum room for other activities
- Can be proven by exchange argument

### In code
```python
def activity_selection(activities):
    """
    Select maximum non-overlapping activities.
    activities: list of (start, finish) or (start, finish, name)

    Returns list of selected activities.
    """
    if not activities:
        return []

    # Handle both formats
    if len(activities[0]) == 2:
        activities = [(s, f, i) for i, (s, f) in enumerate(activities)]

    # Sort by finish time (greedy choice)
    sorted_activities = sorted(activities, key=lambda x: x[1])

    selected = [sorted_activities[0]]
    last_finish = sorted_activities[0][1]

    for start, finish, name in sorted_activities[1:]:
        if start >= last_finish:
            selected.append((start, finish, name))
            last_finish = finish

    return selected

def activity_selection_recursive(activities, k=0, n=None):
    """
    Recursive greedy implementation.
    k: index of last selected activity
    """
    if n is None:
        activities = sorted(activities, key=lambda x: x[1])
        n = len(activities)

    m = k + 1

    # Find first activity that starts after activity k finishes
    while m < n and activities[m][0] < activities[k][1]:
        m += 1

    if m < n:
        return [activities[m]] + activity_selection_recursive(activities, m, n)
    else:
        return []

def weighted_activity_selection(activities):
    """
    Maximum weight subset of non-overlapping activities.
    activities: list of (start, finish, weight)
    Uses DP since greedy doesn't work for weighted version.
    """
    if not activities:
        return 0, []

    n = len(activities)
    # Sort by finish time
    activities = sorted(activities, key=lambda x: x[1])

    # Binary search to find last non-conflicting activity
    def find_last_non_conflict(idx):
        target = activities[idx][0]
        lo, hi = 0, idx - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if activities[mid][1] <= target:
                if mid + 1 <= idx - 1 and activities[mid + 1][1] <= target:
                    lo = mid + 1
                else:
                    return mid
            else:
                hi = mid - 1

        return -1

    # DP arrays
    dp = [0] * n
    dp[0] = activities[0][2]

    for i in range(1, n):
        # Include current activity
        include = activities[i][2]
        last = find_last_non_conflict(i)
        if last != -1:
            include += dp[last]

        # Exclude current activity
        exclude = dp[i - 1]

        dp[i] = max(include, exclude)

    # Reconstruct solution
    selected = []
    i = n - 1
    while i >= 0:
        include = activities[i][2]
        last = find_last_non_conflict(i)
        if last != -1:
            include += dp[last]

        if i == 0 or include >= dp[i - 1]:
            selected.append(activities[i])
            i = last
        else:
            i -= 1

    return dp[n - 1], selected[::-1]

def minimum_platforms(arrivals, departures):
    """
    Minimum platforms needed at a train station.
    Similar concept to activity selection but minimizing resources.
    """
    events = []
    for arr in arrivals:
        events.append((arr, 'A'))
    for dep in departures:
        events.append((dep, 'D'))

    events.sort(key=lambda x: (x[0], x[1] == 'A'))  # Departure before arrival at same time

    max_platforms = 0
    current = 0

    for time, event_type in events:
        if event_type == 'A':
            current += 1
            max_platforms = max(max_platforms, current)
        else:
            current -= 1

    return max_platforms

def job_sequencing_with_deadlines(jobs):
    """
    Maximize profit by scheduling jobs before their deadlines.
    jobs: list of (job_id, deadline, profit)
    Each job takes 1 unit of time.
    """
    # Sort by profit (descending)
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * (max_deadline + 1)  # slot[i] = job at time i

    total_profit = 0
    scheduled = []

    for job_id, deadline, profit in jobs:
        # Find latest available slot before deadline
        for slot in range(deadline, 0, -1):
            if slots[slot] == -1:
                slots[slot] = job_id
                total_profit += profit
                scheduled.append((job_id, slot, profit))
                break

    return total_profit, scheduled

def activity_selection_with_k_persons(activities, k):
    """
    Select activities when k persons can do activities in parallel.
    Each person can do one activity at a time.
    """
    if not activities:
        return []

    activities = sorted(activities, key=lambda x: x[1])

    # Use min-heap to track when each person becomes free
    import heapq
    free_times = [0] * k
    heapq.heapify(free_times)

    selected = []

    for start, finish in activities:
        earliest_free = free_times[0]

        if start >= earliest_free:
            selected.append((start, finish))
            heapq.heappop(free_times)
            heapq.heappush(free_times, finish)

    return selected

def count_max_activities(activities):
    """Just count maximum activities (optimized)"""
    if not activities:
        return 0

    activities = sorted(activities, key=lambda x: x[1])
    count = 1
    last_finish = activities[0][1]

    for start, finish in activities[1:]:
        if start >= last_finish:
            count += 1
            last_finish = finish

    return count

# Usage
activities = [
    (1, 4),   # Activity 0
    (3, 5),   # Activity 1
    (0, 6),   # Activity 2
    (5, 7),   # Activity 3
    (3, 9),   # Activity 4
    (5, 9),   # Activity 5
    (6, 10),  # Activity 6
    (8, 11),  # Activity 7
    (8, 12),  # Activity 8
    (2, 14),  # Activity 9
    (12, 16)  # Activity 10
]

selected = activity_selection(activities)
print(f"Selected {len(selected)} activities:")
for s, f, idx in selected:
    print(f"  Activity {idx}: ({s}, {f})")

# Weighted version
weighted_activities = [
    (1, 4, 50),   # (start, finish, profit)
    (3, 5, 20),
    (0, 6, 100),
    (5, 7, 30),
    (5, 9, 60),
    (7, 8, 10)
]

max_profit, selected_weighted = weighted_activity_selection(weighted_activities)
print(f"\nMax profit: {max_profit}")

# Job sequencing
jobs = [
    ('a', 4, 20),
    ('b', 1, 10),
    ('c', 1, 40),
    ('d', 1, 30)
]

profit, scheduled = job_sequencing_with_deadlines(jobs)
print(f"\nJob scheduling profit: {profit}")
print(f"Scheduled jobs: {scheduled}")
```

### Time complexity

| Operation | Complexity |
|-----------|------------|
| Basic selection | O(n log n) |
| Weighted selection | O(n log n) |
| Job sequencing | O(n²) or O(n log n) with Union-Find |

Dominated by sorting.

### Space complexity
O(n) for storing selected activities and sorted array.

### Edge cases
- Empty activity list
- All activities overlap
- No activities overlap
- Activities with same finish time
- Single activity

### Variants
- **Weighted Activity Selection**: Each activity has weight/profit (requires DP)
- **k-Person Activity Selection**: Multiple people can do activities in parallel
- **Job Sequencing with Deadlines**: Jobs have deadlines and profits
- **Minimum Platforms**: Minimize resources for overlapping activities

### When to use vs avoid
- **Use when**: Maximizing count of non-overlapping activities, simple scheduling, proof of optimality exists
- **Avoid when**: Activities have different values/weights (use DP), complex constraints, need to consider dependencies

### Related
- [Interval Scheduling](./intervalScheduling.md)
- [Huffman Coding](./huffmanCoding.md)
