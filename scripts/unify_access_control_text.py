#!/usr/bin/env python3
"""Unify '출입 통제' -> '출입통제' across all HTML files in web/dark and web/light."""
import glob

patterns = [
    ('출입 통제', '출입통제'),
]

files = glob.glob('web/**/*.html', recursive=True)
total = 0

for filepath in sorted(files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    count = 0
    for old, new in patterns:
        c = new_content.count(old)
        if c > 0:
            new_content = new_content.replace(old, new)
            count += c
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        total += count
        print(f"  {filepath}: {count} replacements")

print(f"\nTotal: {total} replacements")
