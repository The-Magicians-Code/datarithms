# Interval Scheduling
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Greedy Algorithms`

### Topics
**Topics:** `scheduling`, `interval problems`, `optimization`, `resource allocation`

### Definition
A family of problems involving selection, partitioning, or covering of intervals on a line, typically solved optimally using greedy strategies.

### Use cases
- Meeting room scheduling
- CPU task scheduling
- Bandwidth allocation
- Calendar applications
- Resource booking systems

### Prerequisites
- Sorting algorithms
- Understanding of intervals (start, end)
- Greedy choice property

### Step-by-step
**Maximum Non-overlapping Intervals:**
1. Sort intervals by end time
2. Select first interval
3. For each subsequent interval:
   - If it doesn't overlap with last selected, include it
4. This greedy choice is provably optimal

**Minimum Rooms (Interval Partitioning):**
1. Sort by start time
2. Use min-heap for end times of active rooms
3. For each interval, assign to existing room or create new

### In code
```python
import heapq

def max_non_overlapping(intervals):
    """
    Find maximum number of non-overlapping intervals.
    intervals: list of (start, end) tuples
    Returns count and selected intervals.
    """
    if not intervals:
        return 0, []

    # Sort by end time (greedy choice)
    sorted_intervals = sorted(intervals, key=lambda x: x[1])

    selected = [sorted_intervals[0]]
    last_end = sorted_intervals[0][1]

    for start, end in sorted_intervals[1:]:
        if start >= last_end:  # No overlap
            selected.append((start, end))
            last_end = end

    return len(selected), selected

def min_intervals_to_remove(intervals):
    """
    Minimum intervals to remove for non-overlapping set.
    Equivalent to: total - max_non_overlapping
    """
    if not intervals:
        return 0

    count, _ = max_non_overlapping(intervals)
    return len(intervals) - count

def min_meeting_rooms(intervals):
    """
    Minimum number of rooms needed to schedule all meetings.
    Uses min-heap to track room availability.
    """
    if not intervals:
        return 0

    # Sort by start time
    intervals = sorted(intervals, key=lambda x: x[0])

    # Min-heap of end times (rooms in use)
    rooms = []

    for start, end in intervals:
        # If earliest ending room is free, reuse it
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)

        heapq.heappush(rooms, end)

    return len(rooms)

def min_meeting_rooms_sweep(intervals):
    """
    Alternative using line sweep / event processing.
    Often easier to understand.
    """
    events = []
    for start, end in intervals:
        events.append((start, 1))   # Meeting starts
        events.append((end, -1))    # Meeting ends

    events.sort()

    max_rooms = 0
    current_rooms = 0

    for time, delta in events:
        current_rooms += delta
        max_rooms = max(max_rooms, current_rooms)

    return max_rooms

def merge_intervals(intervals):
    """Merge overlapping intervals"""
    if not intervals:
        return []

    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:  # Overlap
            merged[-1] = (merged[-1][0], max(last_end, end))
        else:
            merged.append((start, end))

    return merged

def insert_interval(intervals, new_interval):
    """Insert interval and merge if necessary"""
    result = []
    i = 0
    n = len(intervals)
    start, end = new_interval

    # Add all intervals before new_interval
    while i < n and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1

    result.append((start, end))

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

def interval_intersection(list1, list2):
    """Find intersection of two lists of intervals"""
    result = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        start = max(list1[i][0], list2[j][0])
        end = min(list1[i][1], list2[j][1])

        if start <= end:
            result.append((start, end))

        # Move pointer for interval that ends first
        if list1[i][1] < list2[j][1]:
            i += 1
        else:
            j += 1

    return result

def weighted_interval_scheduling(intervals):
    """
    Maximum weight subset of non-overlapping intervals.
    intervals: list of (start, end, weight)
    Requires DP, not pure greedy.
    """
    if not intervals:
        return 0

    n = len(intervals)
    intervals = sorted(intervals, key=lambda x: x[1])

    # Find last non-conflicting interval for each
    def find_last_non_conflict(idx):
        for j in range(idx - 1, -1, -1):
            if intervals[j][1] <= intervals[idx][0]:
                return j
        return -1

    # DP
    dp = [0] * n
    dp[0] = intervals[0][2]

    for i in range(1, n):
        include = intervals[i][2]
        last = find_last_non_conflict(i)
        if last != -1:
            include += dp[last]

        dp[i] = max(include, dp[i - 1])

    return dp[n - 1]

def can_attend_all(intervals):
    """Check if a person can attend all meetings"""
    intervals = sorted(intervals, key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True

# Usage
intervals = [(1, 4), (2, 3), (3, 5), (7, 8)]

# Maximum non-overlapping
count, selected = max_non_overlapping(intervals)
print(f"Max non-overlapping: {count}")  # 3
print(f"Selected: {selected}")  # [(2, 3), (3, 5), (7, 8)]

# Minimum rooms
meetings = [(0, 30), (5, 10), (15, 20)]
rooms = min_meeting_rooms(meetings)
print(f"Minimum rooms needed: {rooms}")  # 2

# Merge intervals
intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
merged = merge_intervals(intervals)
print(f"Merged: {merged}")  # [(1, 6), (8, 10), (15, 18)]
```

### Time complexity

| Operation | Complexity |
|-----------|------------|
| Max non-overlapping | O(n log n) |
| Min rooms | O(n log n) |
| Merge intervals | O(n log n) |

Dominated by sorting.

### Space complexity
O(n) for storing results. O(1) extra for some operations.

### Edge cases
- Empty interval list
- Single interval
- All intervals overlap
- No intervals overlap
- Intervals with same start/end time

### Variants
- **Weighted Interval Scheduling**: Each interval has weight (requires DP)
- **Interval Partitioning**: Assign intervals to minimum resources
- **Interval Covering**: Minimum intervals to cover a range

### When to use vs avoid
- **Use when**: Scheduling problems, resource allocation, calendar conflicts
- **Avoid when**: Intervals have weights (use DP), need to minimize gaps, complex constraints

### Related
- [Activity Selection](./activitySelection.md)
- [Huffman Coding](./huffmanCoding.md)
