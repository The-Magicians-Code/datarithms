# ROT13
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Cryptography`

### Topics
**Topics:** `substitution cipher`, `Caesar cipher`, `encoding`, `obfuscation`

### Definition
A simple letter substitution cipher that replaces each letter with the letter 13 positions after it in the alphabet. Since the alphabet has 26 letters, applying ROT13 twice returns the original text.

### Use cases
- Hiding spoilers or puzzle answers online
- Simple text obfuscation (not secure encryption)
- Encoding offensive content with warning
- Classic cryptography education
- Unix `tr` command demonstrations

### Prerequisites
- ASCII character codes
- Modular arithmetic basics

### Step-by-step
1. For each character in the input:
2. If it's a letter (A-Z or a-z):
   - Find its position in the alphabet (0-25)
   - Add 13 and take modulo 26
   - Convert back to the corresponding letter
3. If not a letter, keep it unchanged
4. ROT13 is its own inverse: encode = decode

### In code
```python
def rot13(text):
    """
    Apply ROT13 cipher to text.
    Letters are rotated 13 positions, other characters unchanged.
    """
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            # Lowercase: rotate within a-z
            rotated = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            result.append(rotated)
        elif 'A' <= char <= 'Z':
            # Uppercase: rotate within A-Z
            rotated = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            result.append(rotated)
        else:
            # Non-letters unchanged
            result.append(char)

    return ''.join(result)


def rot13_using_translate(text):
    """ROT13 using str.translate() - more Pythonic."""
    import string

    rot13_table = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
        string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
    )

    return text.translate(rot13_table)


def rot_n(text, n):
    """Generalized rotation cipher (Caesar cipher)."""
    result = []
    n = n % 26  # Normalize rotation

    for char in text:
        if 'a' <= char <= 'z':
            rotated = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
            result.append(rotated)
        elif 'A' <= char <= 'Z':
            rotated = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            result.append(rotated)
        else:
            result.append(char)

    return ''.join(result)


def crack_caesar(ciphertext):
    """Try all 26 rotations to crack a Caesar cipher."""
    results = []
    for n in range(26):
        decrypted = rot_n(ciphertext, n)
        results.append((n, decrypted))
    return results


# Usage examples
text = "Hello, World!"
encoded = rot13(text)
print(f"Original: {text}")
print(f"ROT13:    {encoded}")

# ROT13 is self-inverse
decoded = rot13(encoded)
print(f"Decoded:  {decoded}")

# Verify self-inverse property
assert rot13(rot13(text)) == text

# Using translate method
encoded2 = rot13_using_translate(text)
print(f"\nUsing translate: {encoded2}")

# Caesar cipher with different rotations
print(f"\nROT1:  {rot_n(text, 1)}")
print(f"ROT5:  {rot_n(text, 5)}")
print(f"ROT13: {rot_n(text, 13)}")

# Crack example
secret = rot_n("attack at dawn", 7)
print(f"\nCracking '{secret}':")
for n, attempt in crack_caesar(secret)[:5]:
    print(f"  ROT{n}: {attempt}")
```

### Time complexity

| Operation | Complexity |
|-----------|------------|
| Encode/Decode | O(n) |
| Crack Caesar | O(26n) = O(n) |

Where n = length of text. Single pass through the string.

### Space complexity
O(n) for the output string. Can be O(1) if modifying in place (in languages that allow it).

### Edge cases
- Empty string
- Non-alphabetic characters (numbers, punctuation, spaces)
- Mixed case preservation
- Unicode characters (typically left unchanged)

### Variants
- **Caesar cipher**: General rotation by any amount (ROT13 is ROT with n=13)
- **ROT5**: For digits (0-4 become 5-9 and vice versa)
- **ROT47**: Rotates ASCII printable characters (33-126)
- **Vigenere cipher**: Uses a keyword for variable rotation

### When to use vs avoid
- **Use when**: Hiding spoilers, simple obfuscation, educational purposes, reversible encoding needed
- **Avoid when**: Any real security is needed (trivially breakable), protecting sensitive data, need actual encryption

### Related
- Caesar Cipher (generalization)
- Substitution Ciphers

