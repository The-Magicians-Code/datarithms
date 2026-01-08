# Sieve of Eratosthenes
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Number Theory`

### Topics
**Topics:** `prime numbers`, `factorization`, `number theory`, `preprocessing`

### Definition
An ancient algorithm for finding all prime numbers up to a given limit by iteratively marking the multiples of each prime starting from 2.

### Use cases
- Prime number generation
- Prime factorization preprocessing
- Competitive programming
- Cryptography
- Mathematical computations

### Prerequisites
- Understanding of prime numbers
- Array manipulation
- Basic number theory

### Step-by-step
1. Create boolean array of size n+1, initially all true
2. Mark 0 and 1 as not prime
3. For each unmarked number p starting from 2:
   - Mark all multiples of p as not prime (start from p²)
4. All remaining unmarked numbers are prime

### In code
```python
def sieve_of_eratosthenes(n):
    """
    Find all primes up to n.
    Time: O(n log log n)
    Space: O(n)
    """
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Only need to check up to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples starting from i*i
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(n + 1) if is_prime[i]]

def sieve_optimized(n):
    """
    Memory-optimized sieve (only odd numbers).
    Halves memory usage.
    """
    if n < 2:
        return []
    if n == 2:
        return [2]

    # is_prime[i] represents (2*i + 1)
    size = (n - 1) // 2
    is_prime = [True] * (size + 1)

    for i in range(1, int(n**0.5) // 2 + 1):
        if is_prime[i]:
            # Number represented: 2*i + 1
            p = 2 * i + 1
            # Start marking from p*p
            start = (p * p - 1) // 2
            for j in range(start, size + 1, p):
                is_prime[j] = False

    primes = [2]
    for i in range(1, size + 1):
        if is_prime[i]:
            primes.append(2 * i + 1)

    return primes

def segmented_sieve(n):
    """
    Find primes up to n using segmented sieve.
    Memory efficient for large n.
    """
    import math

    limit = int(math.sqrt(n)) + 1
    base_primes = sieve_of_eratosthenes(limit)

    primes = base_primes[:]
    segment_size = max(limit, 32768)

    low = limit + 1
    while low <= n:
        high = min(low + segment_size - 1, n)
        is_prime = [True] * (high - low + 1)

        for p in base_primes:
            # Find first multiple of p >= low
            start = ((low + p - 1) // p) * p
            if start == p:
                start += p

            for j in range(start, high + 1, p):
                is_prime[j - low] = False

        for i in range(high - low + 1):
            if is_prime[i]:
                primes.append(low + i)

        low = high + 1

    return primes

def smallest_prime_factor(n):
    """
    Compute smallest prime factor for all numbers up to n.
    Useful for fast factorization.
    """
    spf = list(range(n + 1))  # spf[i] = i initially

    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:  # i is prime
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i

    return spf

def prime_factorization_with_spf(n, spf):
    """
    Factorize n using precomputed smallest prime factors.
    Time: O(log n) per query.
    """
    factors = []
    while n > 1:
        factors.append(spf[n])
        n //= spf[n]
    return factors

def count_divisors(n, spf):
    """
    Count divisors of n using prime factorization.
    If n = p1^a1 * p2^a2 * ..., divisors = (a1+1) * (a2+1) * ...
    """
    count = 1
    while n > 1:
        prime = spf[n]
        exp = 0
        while spf[n] == prime:
            n //= prime
            exp += 1
        count *= (exp + 1)
    return count

def sum_of_divisors(n, spf):
    """Sum of all divisors of n"""
    result = 1
    while n > 1:
        prime = spf[n]
        exp = 0
        while spf[n] == prime:
            n //= prime
            exp += 1
        # Sum of geometric series: (p^(e+1) - 1) / (p - 1)
        result *= (prime ** (exp + 1) - 1) // (prime - 1)
    return result

def euler_phi_sieve(n):
    """
    Compute Euler's totient for all numbers up to n.
    """
    phi = list(range(n + 1))

    for i in range(2, n + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i

    return phi

def mobius_function_sieve(n):
    """
    Compute Mobius function for all numbers up to n.
    μ(n) = 0 if n has squared prime factor
    μ(n) = (-1)^k if n is product of k distinct primes
    """
    mobius = [0] * (n + 1)
    mobius[1] = 1

    is_prime = [True] * (n + 1)

    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i, n + 1, i):
                is_prime[j] = False if j > i else is_prime[j]
                mobius[j] -= mobius[j // i]

    # Correct approach
    mobius = [0] * (n + 1)
    mobius[1] = 1
    spf = smallest_prime_factor(n)

    for i in range(2, n + 1):
        p = spf[i]
        if spf[i // p] == p:  # Squared factor
            mobius[i] = 0
        else:
            mobius[i] = -mobius[i // p]

    return mobius

def is_prime(n):
    """
    Check if n is prime (for single query).
    For multiple queries, use sieve.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

def prime_count_approximation(n):
    """
    Approximate number of primes up to n.
    π(n) ≈ n / ln(n) (Prime Number Theorem)
    """
    import math
    if n < 2:
        return 0
    return int(n / math.log(n))

def nth_prime_approximation(n):
    """
    Approximate n-th prime number.
    p_n ≈ n * ln(n)
    """
    import math
    if n < 6:
        return [2, 3, 5, 7, 11][n - 1] if n > 0 else 0
    return int(n * (math.log(n) + math.log(math.log(n))))

# Usage
# Basic sieve
primes = sieve_of_eratosthenes(50)
print(f"Primes up to 50: {primes}")

# Count primes
print(f"Number of primes up to 100: {len(sieve_of_eratosthenes(100))}")  # 25

# Prime factorization with SPF
n = 1000
spf = smallest_prime_factor(n)
print(f"Prime factors of 360: {prime_factorization_with_spf(360, spf)}")  # [2, 2, 2, 3, 3, 5]
print(f"Divisor count of 360: {count_divisors(360, spf)}")  # 24
print(f"Sum of divisors of 360: {sum_of_divisors(360, spf)}")  # 1170

# Euler's phi
phi = euler_phi_sieve(20)
print(f"φ(1-20): {phi[1:21]}")

# Prime checking
print(f"Is 997 prime? {is_prime(997)}")  # True
print(f"Is 999 prime? {is_prime(999)}")  # False

# Approximations
print(f"~Primes up to 10^6: {prime_count_approximation(10**6)}")  # ~72382 (actual: 78498)
```

### Time complexity

| Operation | Complexity |
|-----------|------------|
| Sieve | O(n log log n) |
| SPF computation | O(n log log n) |
| Factorization (with SPF) | O(log n) |
| Euler phi sieve | O(n log log n) |

### Space complexity
O(n) for basic sieve. O(√n) for segmented sieve working memory.

### Edge cases
- n < 2 (no primes)
- n = 2 (only one prime)
- Very large n (use segmented sieve)

### Variants
- **Segmented Sieve**: For very large ranges
- **Linear Sieve**: Exactly O(n) time
- **Sieve of Sundaram**: Different approach
- **Wheel Sieve**: Skip multiples of small primes

### When to use vs avoid
- **Use when**: Need all primes up to n, multiple factorization queries, number theory problems
- **Avoid when**: Only checking few numbers for primality, n is very large without segmentation

### Related
- [GCD](./gcd.md)
- [Fast Exponentiation](./fastExpo.md)
