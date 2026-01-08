# GCD (Greatest Common Divisor) & LCM
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Number Theory`

### Topics
**Topics:** `Euclidean algorithm`, `modular arithmetic`, `fractions`, `extended GCD`

### Definition
The Greatest Common Divisor (GCD) of two numbers is the largest positive integer that divides both. The Least Common Multiple (LCM) is the smallest positive integer divisible by both.

### Use cases
- Simplifying fractions
- Cryptography (RSA)
- Modular arithmetic
- Solving Diophantine equations
- Synchronization problems

### Prerequisites
- Division and remainder
- Understanding of divisibility
- Basic modular arithmetic

### Step-by-step
**Euclidean Algorithm:**
1. If b = 0, return a
2. Otherwise, return gcd(b, a mod b)
3. Based on property: gcd(a, b) = gcd(b, a mod b)

**Extended Euclidean:**
1. Find gcd and coefficients x, y where ax + by = gcd(a, b)
2. Used for modular inverse and Diophantine equations

### In code
```python
def gcd(a, b):
    """
    Euclidean algorithm for GCD.
    Time: O(log(min(a, b)))
    """
    while b:
        a, b = b, a % b
    return a

def gcd_recursive(a, b):
    """Recursive version"""
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def lcm(a, b):
    """
    Least Common Multiple.
    LCM(a, b) = |a * b| / GCD(a, b)
    """
    return abs(a * b) // gcd(a, b)

def gcd_multiple(numbers):
    """GCD of multiple numbers"""
    from functools import reduce
    return reduce(gcd, numbers)

def lcm_multiple(numbers):
    """LCM of multiple numbers"""
    from functools import reduce
    return reduce(lcm, numbers)

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm.
    Returns (gcd, x, y) where ax + by = gcd(a, b)
    """
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return g, x, y

def mod_inverse(a, m):
    """
    Find modular multiplicative inverse of a mod m.
    Returns x where (a * x) mod m = 1.
    Exists only if gcd(a, m) = 1.
    """
    g, x, _ = extended_gcd(a, m)

    if g != 1:
        raise ValueError(f"Inverse doesn't exist for {a} mod {m}")

    return (x % m + m) % m

def solve_linear_diophantine(a, b, c):
    """
    Solve ax + by = c.
    Solution exists iff gcd(a, b) divides c.
    Returns (x0, y0) - one particular solution.
    General solution: x = x0 + (b/g)*t, y = y0 - (a/g)*t for any integer t.
    """
    g, x, y = extended_gcd(a, b)

    if c % g != 0:
        return None  # No solution

    # Scale to actual c
    x *= c // g
    y *= c // g

    return x, y

def chinese_remainder_theorem(remainders, moduli):
    """
    Solve system of congruences:
    x ≡ r[i] (mod m[i]) for all i

    Returns (x, M) where M = product of all moduli.
    Solution is x mod M.
    """
    from functools import reduce

    M = reduce(lambda a, b: a * b, moduli)
    x = 0

    for ri, mi in zip(remainders, moduli):
        Mi = M // mi
        yi = mod_inverse(Mi, mi)
        x += ri * Mi * yi

    return x % M, M

def simplify_fraction(numerator, denominator):
    """Reduce fraction to lowest terms"""
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")

    g = gcd(abs(numerator), abs(denominator))

    # Handle signs
    sign = -1 if (numerator < 0) ^ (denominator < 0) else 1

    return sign * abs(numerator) // g, abs(denominator) // g

def add_fractions(n1, d1, n2, d2):
    """Add two fractions and simplify"""
    num = n1 * d2 + n2 * d1
    den = d1 * d2
    return simplify_fraction(num, den)

def coprime(a, b):
    """Check if a and b are coprime (relatively prime)"""
    return gcd(a, b) == 1

def euler_phi(n):
    """
    Euler's totient function.
    Count of integers in [1, n] that are coprime with n.
    """
    result = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            # Remove all factors of p
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    if n > 1:  # n is a prime factor
        result -= result // n

    return result

def bezout_identity(a, b):
    """
    Find coefficients for Bezout's identity: ax + by = gcd(a, b)
    """
    return extended_gcd(a, b)

def solve_congruence(a, b, m):
    """
    Solve ax ≡ b (mod m)
    Returns all solutions in [0, m) or empty list if no solution.
    """
    g = gcd(a, m)

    if b % g != 0:
        return []  # No solution

    # Reduce to simpler equation
    a //= g
    b //= g
    m //= g

    x0 = (mod_inverse(a, m) * b) % m

    # All g solutions
    return [(x0 + i * m) % (m * g) for i in range(g)]

# Binary GCD (Stein's algorithm) - more efficient for large numbers
def binary_gcd(a, b):
    """
    Binary GCD algorithm using only shifts and subtractions.
    Avoids expensive division operations.
    """
    if a == 0:
        return b
    if b == 0:
        return a

    # Find common factors of 2
    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1

    # Remove factors of 2 from a
    while (a & 1) == 0:
        a >>= 1

    while b:
        # Remove factors of 2 from b
        while (b & 1) == 0:
            b >>= 1

        # Swap if necessary so a <= b
        if a > b:
            a, b = b, a

        b -= a

    return a << shift

# Usage
# Basic GCD/LCM
print(f"GCD(48, 18): {gcd(48, 18)}")  # 6
print(f"LCM(48, 18): {lcm(48, 18)}")  # 144

# Extended GCD
g, x, y = extended_gcd(48, 18)
print(f"48*{x} + 18*{y} = {g}")  # 48*(-1) + 18*3 = 6

# Modular inverse
print(f"Inverse of 3 mod 7: {mod_inverse(3, 7)}")  # 5 (3*5 = 15 ≡ 1 mod 7)

# Simplify fraction
n, d = simplify_fraction(48, 18)
print(f"48/18 simplified: {n}/{d}")  # 8/3

# Diophantine equation
sol = solve_linear_diophantine(3, 5, 7)
print(f"3x + 5y = 7, one solution: {sol}")  # (4, -1) since 3*4 + 5*(-1) = 7

# Chinese Remainder Theorem
x, m = chinese_remainder_theorem([2, 3, 2], [3, 5, 7])
print(f"x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7): x = {x}")  # 23
```

### Time complexity

| Operation | Complexity |
|-----------|------------|
| GCD | O(log(min(a, b))) |
| Extended GCD | O(log(min(a, b))) |
| LCM | O(log(min(a, b))) |
| Euler phi | O(√n) |

### Space complexity
O(1) for iterative, O(log n) for recursive versions (stack).

### Edge cases
- One number is 0 (gcd(a, 0) = a)
- Both numbers are 0 (undefined, often return 0)
- Negative numbers (take absolute values)
- Coprime numbers (gcd = 1)

### Variants
- **Binary GCD (Stein's)**: Uses only shifts/subtractions
- **Polynomial GCD**: For polynomials
- **GCD in other domains**: Gaussian integers, etc.

### When to use vs avoid
- **Use when**: Simplifying fractions, finding modular inverse, cryptographic computations
- **Avoid when**: Built-in functions available (Python's math.gcd), working with floats

### Related
- [Fast Exponentiation](./fastExpo.md)
- [Sieve of Eratosthenes](./sieve.md)
