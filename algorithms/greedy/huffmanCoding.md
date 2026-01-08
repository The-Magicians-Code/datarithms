# Huffman Coding
[Back](../summary.md)
[Home](../../index.md)

### Category
**Category:** `Greedy Algorithms`

### Topics
**Topics:** `compression`, `prefix codes`, `binary tree`, `entropy encoding`

### Definition
A lossless data compression algorithm that assigns variable-length codes to characters based on their frequencies, with more frequent characters getting shorter codes.

### Use cases
- File compression (ZIP, GZIP)
- Image compression (JPEG uses similar ideas)
- Network data compression
- Fax machines
- Text compression

### Prerequisites
- Binary trees
- Priority queues (min-heap)
- Prefix-free codes concept

### Step-by-step
1. Create leaf node for each character with its frequency
2. Build a min-heap of all nodes
3. While heap has more than one node:
   - Extract two minimum frequency nodes
   - Create new internal node with these as children
   - Frequency = sum of children's frequencies
   - Insert new node back to heap
4. Root of tree is the Huffman tree
5. Left edge = 0, Right edge = 1
6. Code for character = path from root to leaf

### In code
```python
import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    """
    Build Huffman tree from character frequencies.
    frequencies: dict of {char: frequency}
    """
    # Create leaf nodes and build min-heap
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Build tree
    while len(heap) > 1:
        # Extract two minimum
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create internal node
        internal = HuffmanNode(None, left.freq + right.freq)
        internal.left = left
        internal.right = right

        heapq.heappush(heap, internal)

    return heap[0] if heap else None

def generate_codes(root):
    """Generate Huffman codes from tree"""
    codes = {}

    def traverse(node, code):
        if node is None:
            return

        if node.char is not None:  # Leaf node
            codes[node.char] = code if code else '0'
            return

        traverse(node.left, code + '0')
        traverse(node.right, code + '1')

    traverse(root, '')
    return codes

def huffman_encode(text):
    """Encode text using Huffman coding"""
    if not text:
        return '', {}, None

    # Count frequencies
    frequencies = Counter(text)

    # Build tree
    root = build_huffman_tree(frequencies)

    # Generate codes
    codes = generate_codes(root)

    # Encode text
    encoded = ''.join(codes[char] for char in text)

    return encoded, codes, root

def huffman_decode(encoded, root):
    """Decode Huffman encoded string"""
    if not encoded or root is None:
        return ''

    # Handle single character case
    if root.char is not None:
        return root.char * len(encoded)

    decoded = []
    node = root

    for bit in encoded:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.char is not None:  # Leaf
            decoded.append(node.char)
            node = root

    return ''.join(decoded)

def calculate_compression_ratio(original, encoded):
    """Calculate compression ratio"""
    original_bits = len(original) * 8  # Assuming 8 bits per char
    encoded_bits = len(encoded)

    return {
        'original_bits': original_bits,
        'encoded_bits': encoded_bits,
        'compression_ratio': original_bits / encoded_bits if encoded_bits > 0 else 0,
        'space_savings': (1 - encoded_bits / original_bits) * 100 if original_bits > 0 else 0
    }

def serialize_tree(root):
    """Serialize Huffman tree for storage"""
    if root is None:
        return ''

    result = []

    def preorder(node):
        if node.char is not None:  # Leaf
            result.append(f'1{node.char}')
        else:
            result.append('0')
            preorder(node.left)
            preorder(node.right)

    preorder(root)
    return ''.join(result)

def deserialize_tree(data):
    """Deserialize Huffman tree"""
    if not data:
        return None

    idx = [0]

    def build():
        if idx[0] >= len(data):
            return None

        if data[idx[0]] == '1':  # Leaf
            idx[0] += 1
            char = data[idx[0]]
            idx[0] += 1
            return HuffmanNode(char, 0)
        else:  # Internal node
            idx[0] += 1
            node = HuffmanNode(None, 0)
            node.left = build()
            node.right = build()
            return node

    return build()

def canonical_huffman_codes(frequencies):
    """
    Generate canonical Huffman codes.
    Canonical codes are easier to transmit - only need code lengths.
    """
    # Build regular Huffman tree and get code lengths
    root = build_huffman_tree(frequencies)
    regular_codes = generate_codes(root)

    # Get code lengths
    code_lengths = {char: len(code) for char, code in regular_codes.items()}

    # Sort by length, then alphabetically
    sorted_chars = sorted(code_lengths.keys(), key=lambda x: (code_lengths[x], x))

    # Generate canonical codes
    canonical = {}
    code = 0
    prev_length = 0

    for char in sorted_chars:
        length = code_lengths[char]

        if prev_length > 0:
            code = (code + 1) << (length - prev_length)

        canonical[char] = format(code, f'0{length}b')
        prev_length = length

    return canonical

def adaptive_huffman_encode(text):
    """
    Simplified adaptive Huffman encoding concept.
    Tree is updated as characters are processed.
    """
    # This is a simplified demonstration
    # Full implementation uses FGK or Vitter algorithm
    encoded = []
    frequencies = {}

    for char in text:
        if char in frequencies:
            # Use current code
            tree = build_huffman_tree(frequencies)
            codes = generate_codes(tree)
            encoded.append(codes.get(char, char))
        else:
            # New character - send literal
            encoded.append(f'NEW:{char}')

        frequencies[char] = frequencies.get(char, 0) + 1

    return encoded

# Usage
text = "this is an example for huffman encoding"

# Encode
encoded, codes, root = huffman_encode(text)
print("Huffman Codes:")
for char, code in sorted(codes.items()):
    print(f"  '{char}': {code}")

print(f"\nOriginal: {text}")
print(f"Encoded: {encoded[:50]}...")  # Show first 50 bits

# Decode
decoded = huffman_decode(encoded, root)
print(f"Decoded: {decoded}")
print(f"Match: {decoded == text}")

# Compression stats
stats = calculate_compression_ratio(text, encoded)
print(f"\nCompression ratio: {stats['compression_ratio']:.2f}x")
print(f"Space savings: {stats['space_savings']:.1f}%")
```

### Time complexity

| Operation | Complexity |
|-----------|------------|
| Build tree | O(n log n) |
| Generate codes | O(n) |
| Encode text | O(m) |
| Decode text | O(m) |

Where n = unique characters, m = text length.

### Space complexity
O(n) for the tree and codes. O(m) for encoded/decoded output.

### Edge cases
- Empty text
- Single character repeated
- All characters same frequency
- Very skewed frequencies (one dominant character)

### Variants
- **Adaptive Huffman**: Updates tree as data is processed
- **Canonical Huffman**: Standardized code assignment
- **Shannon-Fano**: Similar but divides recursively (less optimal)
- **Arithmetic Coding**: More efficient but complex

### When to use vs avoid
- **Use when**: Data has varying character frequencies, need prefix-free codes, lossless compression required
- **Avoid when**: Data is uniform (no compression benefit), need real-time streaming (use adaptive), extreme compression needed (use arithmetic coding)

### Related
- [Activity Selection](./activitySelection.md)
- [Heap](../../datastructs/trees/heap.md)
