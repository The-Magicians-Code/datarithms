# XOR Tricks and Bit Manipulation
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Bit Manipulation`

### Topics
**Topics:** `XOR properties`, `bit tricks`, `single number`, `missing number`

### Definition
A collection of techniques using XOR (exclusive or) and other bitwise operations to solve problems efficiently. XOR has special properties: a^a=0, a^0=a, and is commutative/associative.

### Use cases
- Finding single/missing numbers
- Swapping without temp variable
- Detecting duplicates
- Error detection (parity)
- Cryptography basics

### Prerequisites
- Binary number system
- Bitwise operators (&, |, ^, ~, <<, >>)
- XOR truth table

### Step-by-step
**Key XOR properties:**
- a ^ a = 0 (cancellation)
- a ^ 0 = a (identity)
- a ^ b = b ^ a (commutative)
- (a ^ b) ^ c = a ^ (b ^ c) (associative)
- a ^ b ^ b = a (double XOR cancels)

### In code
```python
def single_number(nums):
    """
    Find the element that appears once (others appear twice).
    Classic XOR problem.
    """
    result = 0
    for num in nums:
        result ^= num
    return result

def single_number_three_times(nums):
    """
    Find element appearing once when others appear three times.
    Uses bit counting approach.
    """
    result = 0
    for i in range(32):
        bit_sum = 0
        for num in nums:
            bit_sum += (num >> i) & 1
        result |= (bit_sum % 3) << i

    # Handle negative numbers
    if result >= 2**31:
        result -= 2**32

    return result

def two_single_numbers(nums):
    """
    Find two elements that appear once (others appear twice).
    """
    # XOR all: result = a ^ b where a, b are the two singles
    xor_all = 0
    for num in nums:
        xor_all ^= num

    # Find rightmost set bit (where a and b differ)
    rightmost_bit = xor_all & (-xor_all)

    # Partition numbers and XOR separately
    a, b = 0, 0
    for num in nums:
        if num & rightmost_bit:
            a ^= num
        else:
            b ^= num

    return a, b

def missing_number(nums):
    """
    Find missing number in [0, n] where array has n elements.
    XOR all indices with all values.
    """
    n = len(nums)
    result = n

    for i, num in enumerate(nums):
        result ^= i ^ num

    return result

def find_duplicate(nums):
    """
    Find duplicate in array where each number appears once or twice.
    Array contains numbers 1 to n.
    """
    n = len(nums)
    expected_xor = 0
    actual_xor = 0

    for i in range(1, n):
        expected_xor ^= i

    for num in nums:
        actual_xor ^= num

    # If all unique, expected_xor == actual_xor
    # The difference reveals the duplicate (appears extra time)
    return expected_xor ^ actual_xor

def swap_without_temp(a, b):
    """Swap two variables without temporary variable"""
    a = a ^ b
    b = a ^ b  # b = (a^b)^b = a
    a = a ^ b  # a = (a^b)^a = b
    return a, b

def count_bits(n):
    """Count number of 1 bits (Hamming weight)"""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def count_bits_optimized(n):
    """Brian Kernighan's algorithm - O(number of 1 bits)"""
    count = 0
    while n:
        n &= n - 1  # Clear rightmost set bit
        count += 1
    return count

def is_power_of_two(n):
    """Check if n is a power of 2"""
    return n > 0 and (n & (n - 1)) == 0

def next_power_of_two(n):
    """Find next power of 2 >= n"""
    if n <= 0:
        return 1
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return n + 1

def get_rightmost_set_bit(n):
    """Get rightmost set bit position (0-indexed)"""
    if n == 0:
        return -1
    return (n & -n).bit_length() - 1

def clear_rightmost_set_bit(n):
    """Clear the rightmost set bit"""
    return n & (n - 1)

def set_bit(n, i):
    """Set i-th bit to 1"""
    return n | (1 << i)

def clear_bit(n, i):
    """Clear i-th bit to 0"""
    return n & ~(1 << i)

def toggle_bit(n, i):
    """Toggle i-th bit"""
    return n ^ (1 << i)

def get_bit(n, i):
    """Get i-th bit value"""
    return (n >> i) & 1

def hamming_distance(x, y):
    """Count differing bits between two numbers"""
    return count_bits_optimized(x ^ y)

def reverse_bits(n, num_bits=32):
    """Reverse bits of a number"""
    result = 0
    for i in range(num_bits):
        result <<= 1
        result |= n & 1
        n >>= 1
    return result

def max_xor_pair(nums):
    """
    Find maximum XOR of any two numbers in array.
    Uses trie-based approach for O(n * 32).
    """
    max_xor = 0

    for i in range(31, -1, -1):
        max_xor <<= 1
        # Check if we can have this bit set
        prefixes = set()
        for num in nums:
            prefixes.add(num >> i)

        for prefix in prefixes:
            # Try to find complement that gives us max_xor | 1
            if (max_xor | 1) ^ prefix in prefixes:
                max_xor |= 1
                break

    return max_xor

def xor_range(a, b):
    """
    XOR of all numbers from a to b inclusive.
    Uses pattern: XOR(0 to n) has period of 4.
    """
    def xor_to_n(n):
        mod = n % 4
        if mod == 0: return n
        if mod == 1: return 1
        if mod == 2: return n + 1
        return 0  # mod == 3

    return xor_to_n(b) ^ xor_to_n(a - 1)

def count_pairs_with_xor(nums, k):
    """Count pairs where XOR equals k"""
    from collections import Counter
    count = Counter(nums)
    result = 0

    for num in count:
        target = num ^ k
        if target in count:
            if target == num:
                result += count[num] * (count[num] - 1)
            else:
                result += count[num] * count[target]

    return result // 2

# Usage
# Single number
nums = [4, 1, 2, 1, 2]
print(f"Single number: {single_number(nums)}")  # 4

# Two single numbers
nums = [1, 2, 1, 3, 2, 5]
print(f"Two singles: {two_single_numbers(nums)}")  # (3, 5)

# Missing number
nums = [3, 0, 1]
print(f"Missing: {missing_number(nums)}")  # 2

# Bit operations
print(f"Bits in 11: {count_bits_optimized(11)}")  # 3
print(f"Is 16 power of 2: {is_power_of_two(16)}")  # True
print(f"Hamming distance 1,4: {hamming_distance(1, 4)}")  # 2

# XOR range
print(f"XOR(1 to 5): {xor_range(1, 5)}")  # 1^2^3^4^5 = 1
```

### Time complexity

| Operation | Complexity |
|-----------|------------|
| Single number | O(n) |
| Count bits | O(log n) or O(k) where k = set bits |
| Max XOR pair | O(n × 32) |

Most operations are O(n) or O(log n).

### Space complexity
O(1) for most operations. O(n) for hash-based approaches.

### Edge cases
- Empty array
- All same numbers
- Negative numbers (handle sign bit)
- Integer overflow

### Variants
- **Gray code**: Adjacent numbers differ by 1 bit
- **Bit parity**: Even/odd number of set bits
- **Bit interleaving**: Morton codes for spatial hashing

### When to use vs avoid
- **Use when**: Dealing with duplicates, missing numbers, can exploit XOR properties, need O(1) space
- **Avoid when**: Complex relationships beyond pairing, need to preserve all values, floating point numbers

### Related
- [Bitmask DP](./bitmaskDP.md)
- [Binary Search](../searching/binarySearch.md)
