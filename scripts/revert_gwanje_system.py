#!/usr/bin/env python3
"""Revert '관제시스템' back to '관제 시스템' for proper Korean spacing."""
import glob

files = glob.glob('web/**/*.html', recursive=True)
total = 0

for filepath in sorted(files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    count = content.count('관제시스템')
    if count > 0:
        new_content = content.replace('관제시스템', '관제 시스템')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        total += count
        print(f"  {filepath}: {count} replacements")

print(f"\nTotal: {total} replacements")
