#!/usr/bin/env python3
"""Extract and test Python code blocks from markdown files."""

import re
import sys
from pathlib import Path


def extract_code_blocks(md_file):
    """Extract all Python code blocks from a markdown file."""
    content = md_file.read_text()
    pattern = r'```python\n(.*?)```'
    return re.findall(pattern, content, re.DOTALL)


def test_code_block(code, filename, block_num):
    """Execute a code block and return success/failure."""
    try:
        # Create isolated namespace for each execution
        exec(code, {'__name__': '__main__'})
        return True, None
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


def main():
    root = Path(__file__).parent
    md_files = sorted(
        list(root.glob('algorithms/**/*.md')) +
        list(root.glob('datastructs/**/*.md')) +
        [root / 'bigO.md']  # Include root-level Big O guide
    )

    passed, failed = 0, []

    for md_file in md_files:
        blocks = extract_code_blocks(md_file)
        if not blocks:
            continue

        for i, code in enumerate(blocks, 1):
            success, error = test_code_block(code, md_file.name, i)
            rel_path = md_file.relative_to(root)

            if success:
                passed += 1
                print(f"✓ {rel_path} (block {i})")
            else:
                failed.append((rel_path, i, error))
                print(f"✗ {rel_path} (block {i})")

    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {len(failed)} failed")
    print(f"{'='*50}")

    if failed:
        print("\nFailures:")
        for path, block_num, error in failed:
            print(f"\n  {path} (block {block_num}):")
            print(f"    {error}")

    sys.exit(len(failed))


if __name__ == '__main__':
    main()
