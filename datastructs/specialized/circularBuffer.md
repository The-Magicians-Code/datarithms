# Circular Buffer (Ring Buffer)
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Specialized`

### Topics
**Topics:** `streaming`, `low-latency systems`, `telemetry`, `real-time data`

### Definition
A fixed-size buffer that wraps around when full, overwriting the oldest data with new data, providing O(1) operations for streaming data scenarios.

### Use cases
- Audio/video streaming buffers
- Log rotation (keeping last N entries)
- Real-time data collection (sensors, telemetry)
- Network packet buffering
- Producer-consumer patterns with bounded memory

### Attributes
- Fixed capacity - never grows beyond initial size
- Head and tail pointers wrap around using modulo
- Overwrites oldest data when full (or blocks/rejects)
- O(1) read and write operations

### Common operations

| Operation | Time | Description |
|-----------|------|-------------|
| Write     | O(1) | Add element (may overwrite oldest) |
| Read      | O(1) | Remove and return oldest element |
| Peek      | O(1) | View oldest without removing |
| IsFull    | O(1) | Check if buffer is at capacity |
| IsEmpty   | O(1) | Check if buffer has no elements |

### In code
```python
class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0  # Write position
        self.tail = 0  # Read position
        self.size = 0

    def write(self, item):
        """Add item, overwriting oldest if full - O(1)"""
        if self.is_full():
            # Overwrite oldest - move tail forward
            self.tail = (self.tail + 1) % self.capacity
        else:
            self.size += 1
        self.buffer[self.head] = item
        self.head = (self.head + 1) % self.capacity

    def read(self):
        """Remove and return oldest item - O(1)"""
        if self.is_empty():
            raise IndexError("Buffer is empty")
        item = self.buffer[self.tail]
        self.buffer[self.tail] = None
        self.tail = (self.tail + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        """View oldest item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Buffer is empty")
        return self.buffer[self.tail]

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

# Using collections.deque with maxlen (simpler)
from collections import deque

# Fixed-size deque acts as circular buffer
recent_logs = deque(maxlen=100)
recent_logs.append("log entry 1")
recent_logs.append("log entry 2")
# When 101st item added, oldest is automatically discarded

# Use for sliding window
def moving_average(stream, window_size):
    buffer = deque(maxlen=window_size)
    for value in stream:
        buffer.append(value)
        if len(buffer) == window_size:
            yield sum(buffer) / window_size

# NumPy ring buffer for numerical data
import numpy as np

class NumPyRingBuffer:
    def __init__(self, capacity, dtype=float):
        self.buffer = np.zeros(capacity, dtype=dtype)
        self.capacity = capacity
        self.index = 0
        self.is_full = False

    def append(self, value):
        self.buffer[self.index] = value
        self.index = (self.index + 1) % self.capacity
        if self.index == 0:
            self.is_full = True

    def get_ordered(self):
        """Get elements in insertion order"""
        if not self.is_full:
            return self.buffer[:self.index]
        return np.concatenate([
            self.buffer[self.index:],
            self.buffer[:self.index]
        ])
```

### Time complexity
- **Write/Read/Peek**: O(1) - direct index access with modulo
- **IsFull/IsEmpty**: O(1) - simple size comparison
- **Access middle**: O(1) with proper indexing

### Space complexity
O(n) where n is the fixed capacity. No additional memory allocated after initialization. Memory usage is constant regardless of how many items pass through.

### Trade-offs
**Pros:**
- Constant memory usage
- O(1) all operations
- Cache-friendly (contiguous memory)
- No memory allocation after initialization

**Cons:**
- Fixed size - cannot grow
- Loses old data when full (by design)
- Accessing arbitrary positions requires index calculation

### Variants
- **Blocking ring buffer**: Blocks writer when full instead of overwriting
- **Lock-free ring buffer**: For concurrent access without locks
- **SPSC buffer**: Single Producer Single Consumer - optimized for one reader/writer
- **MPMC buffer**: Multiple Producer Multiple Consumer - thread-safe

### When to use vs avoid
- **Use when**: Need fixed-size buffer, streaming data, recent history only, memory-bounded logging
- **Avoid when**: Need to keep all data, size is unpredictable, random access is frequent

### Related
- [Deque](../deque.md)
- [Queue](../queue.md)
