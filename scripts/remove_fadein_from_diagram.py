#!/usr/bin/env python3
"""Remove fade-in class from diagram-container elements in solution pages."""
import re
import glob

files = glob.glob('web/*/pages/solutions/*.html')
total_replacements = 0

for filepath in sorted(files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('diagram-container fade-in', 'diagram-container')
    
    count = content.count('diagram-container fade-in') - new_content.count('diagram-container fade-in')
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        total_replacements += count
        print(f"  {filepath}: {count} replacements")

print(f"\nTotal: {total_replacements} replacements in {len(files)} files scanned")
