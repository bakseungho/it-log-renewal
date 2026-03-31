#!/usr/bin/env python3
"""Unify terminology across all HTML files in web/ directory."""
import glob

# (old, new) - order matters for some patterns
patterns = [
    ('원-스탑', '원스탑'),
    ('타워 크레인', '타워크레인'),
    ('환경 센서', '환경센서'),
    ('통합 안전 시스템', '통합안전 시스템'),  # product name only
]

files = glob.glob('web/**/*.html', recursive=True)
total = 0

for filepath in sorted(files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    file_count = 0
    for old, new in patterns:
        c = new_content.count(old)
        if c > 0:
            new_content = new_content.replace(old, new)
            file_count += c
    
    if file_count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        total += file_count
        print(f"  {filepath}: {file_count} replacements")

print(f"\nTotal: {total} replacements in {len(files)} files scanned")
