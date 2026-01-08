# Fast Exponentiation (Binary Exponentiation)
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Number Theory`

### Topics
**Topics:** `exponentiation by squaring`, `modular arithmetic`, `matrix exponentiation`, `Fibonacci`

### Definition
Compute a^n in O(log n) time by exploiting the binary representation of the exponent. Also known as exponentiation by squaring or binary exponentiation.

### Use cases
- Large power computations
- Modular exponentiation (cryptography)
- Matrix exponentiation (Fibonacci, recurrences)
- Computing large factorials mod p
- RSA encryption

### Prerequisites
- Binary representation
- Modular arithmetic
- Basic recursion

### Step-by-step
**Key insight:**
- a^n = a^(n/2) × a^(n/2) if n is even
- a^n = a × a^(n-1) if n is odd

**Iterative approach:**
1. Convert n to binary
2. For each bit from LSB to MSB:
   - If bit is 1, multiply result by current power of a
   - Square a for next iteration

### In code
```python
def fast_pow(base, exp):
    """
    Compute base^exp in O(log exp) time.
    """
    if exp < 0:
        return 1 / fast_pow(base, -exp)

    result = 1
    while exp > 0:
        if exp & 1:  # If last bit is 1
            result *= base
        base *= base
        exp >>= 1

    return result

def fast_pow_recursive(base, exp):
    """Recursive version"""
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / fast_pow_recursive(base, -exp)

    if exp & 1:
        return base * fast_pow_recursive(base, exp - 1)
    else:
        half = fast_pow_recursive(base, exp // 2)
        return half * half

def mod_pow(base, exp, mod):
    """
    Compute (base^exp) mod mod in O(log exp) time.
    Essential for cryptography and large number computations.
    """
    result = 1
    base = base % mod

    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1

    return result

def matrix_multiply(A, B, mod=None):
    """Multiply two matrices"""
    n = len(A)
    m = len(B[0])
    k = len(B)

    C = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for p in range(k):
                C[i][j] += A[i][p] * B[p][j]
                if mod:
                    C[i][j] %= mod

    return C

def matrix_pow(M, n, mod=None):
    """
    Compute M^n for square matrix M.
    Uses binary exponentiation on matrices.
    """
    size = len(M)
    # Identity matrix
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    while n > 0:
        if n & 1:
            result = matrix_multiply(result, M, mod)
        M = matrix_multiply(M, M, mod)
        n >>= 1

    return result

def fibonacci(n, mod=10**9 + 7):
    """
    Compute n-th Fibonacci number in O(log n) using matrix exponentiation.
    [F(n+1)]   [1 1]^n   [F(1)]
    [F(n)  ] = [1 0]   * [F(0)]
    """
    if n <= 1:
        return n

    M = [[1, 1], [1, 0]]
    result = matrix_pow(M, n, mod)

    return result[0][1]  # F(n)

def linear_recurrence(coeffs, init_values, n, mod=10**9 + 7):
    """
    Solve linear recurrence in O(k^3 log n).
    f(n) = c[0]*f(n-1) + c[1]*f(n-2) + ... + c[k-1]*f(n-k)

    coeffs: [c[0], c[1], ..., c[k-1]]
    init_values: [f(0), f(1), ..., f(k-1)]
    """
    k = len(coeffs)

    if n < k:
        return init_values[n]

    # Build transformation matrix
    M = [[0] * k for _ in range(k)]

    # First row is coefficients
    for i in range(k):
        M[0][i] = coeffs[i]

    # Shift matrix for other rows
    for i in range(1, k):
        M[i][i - 1] = 1

    # Compute M^(n-k+1)
    result = matrix_pow(M, n - k + 1, mod)

    # Multiply by initial values (reversed)
    ans = 0
    for i in range(k):
        ans += result[0][i] * init_values[k - 1 - i]
        ans %= mod

    return ans

def fermat_little_theorem_inverse(a, p):
    """
    Compute modular inverse using Fermat's little theorem.
    For prime p: a^(-1) ≡ a^(p-2) (mod p)
    """
    return mod_pow(a, p - 2, p)

def factorial_mod(n, p):
    """Compute n! mod p"""
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % p
    return result

def nCr_mod(n, r, p):
    """
    Compute C(n, r) mod p using Fermat's little theorem.
    Requires p to be prime.
    """
    if r > n or r < 0:
        return 0

    num = factorial_mod(n, p)
    denom = (factorial_mod(r, p) * factorial_mod(n - r, p)) % p

    return (num * fermat_little_theorem_inverse(denom, p)) % p

def lucas_theorem(n, r, p):
    """
    Compute C(n, r) mod p for very large n using Lucas' theorem.
    p must be prime.
    """
    if r == 0:
        return 1

    ni = n % p
    ri = r % p

    return (lucas_theorem(n // p, r // p, p) * nCr_mod(ni, ri, p)) % p

def mod_pow_large_exp(base, exp_str, mod):
    """
    Compute base^exp mod mod where exp is given as string (very large).
    Uses Euler's theorem: a^φ(n) ≡ 1 (mod n) when gcd(a,n)=1
    """
    # For simplicity, compute exp mod φ(mod) when possible
    # Here we compute directly
    result = 1
    base = base % mod

    for digit in exp_str:
        # result = result^10 * base^digit
        result = mod_pow(result, 10, mod)
        result = (result * mod_pow(base, int(digit), mod)) % mod

    return result

def tetration(a, b, mod):
    """
    Compute a^^b (a raised to itself b times) mod mod.
    a^^3 = a^(a^a)
    Uses recursive modular exponentiation.
    """
    if b == 0:
        return 1 % mod
    if b == 1:
        return a % mod

    exp = tetration(a, b - 1, mod)
    return mod_pow(a, exp, mod)

# Usage
# Basic fast power
print(f"2^10 = {fast_pow(2, 10)}")  # 1024
print(f"2^100 mod 1000 = {mod_pow(2, 100, 1000)}")  # 376

# Fibonacci
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}", end="  ")
print()  # 0 1 1 2 3 5 8 13 21 34

# Linear recurrence: f(n) = 2*f(n-1) + 3*f(n-2), f(0)=1, f(1)=2
# This gives sequence: 1, 2, 7, 20, 61, 182, ...
coeffs = [2, 3]
init = [1, 2]
print(f"f(5) = {linear_recurrence(coeffs, init, 5)}")  # 182

# Combinatorics
p = 10**9 + 7
print(f"C(10, 3) mod p = {nCr_mod(10, 3, p)}")  # 120
print(f"10! mod p = {factorial_mod(10, p)}")  # 3628800

# Matrix power
M = [[1, 2], [3, 4]]
M_cubed = matrix_pow(M, 3)
print(f"Matrix^3: {M_cubed}")
```

### Time complexity

| Operation | Complexity |
|-----------|------------|
| fast_pow | O(log n) |
| mod_pow | O(log n) |
| matrix_pow | O(k³ log n) |
| fibonacci | O(log n) |

### Space complexity
O(1) for iterative scalar exponentiation. O(k²) for matrix operations.

### Edge cases
- Exponent is 0 (return 1)
- Negative exponent (return inverse)
- Base is 0 (return 0 for positive exp)
- Very large exponents (use modular)

### Variants
- **Matrix exponentiation**: For linear recurrences
- **Modular exponentiation**: For cryptography
- **Exponentiation with negative exponents**: Return inverse

### When to use vs avoid
- **Use when**: Computing large powers, need O(log n), modular arithmetic, solving recurrences
- **Avoid when**: Small exponents (simple loop suffices), need exact large numbers (precision issues)

### Related
- [GCD](./gcd.md)
- [Sieve of Eratosthenes](./sieve.md)
