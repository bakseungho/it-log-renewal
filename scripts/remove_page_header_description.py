#!/usr/bin/env python3
"""
Remove page-header-description from all subpages in dark and light themes
"""

import os
import re
from pathlib import Path

def remove_description_line(file_path):
    """Remove the page-header-description line from HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match the entire line with page-header-description
        pattern = r'\s*<p class="page-header-description">.*?</p>\s*\n'
        
        # Remove the line
        new_content = re.sub(pattern, '', content)
        
        # Only write if content changed
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    # Base directories
    base_dirs = [
        'web/dark/pages',
        'web/light/pages'
    ]
    
    modified_count = 0
    
    for base_dir in base_dirs:
        if not os.path.exists(base_dir):
            print(f"Directory not found: {base_dir}")
            continue
            
        # Find all HTML files recursively
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file.endswith('.html'):
                    file_path = os.path.join(root, file)
                    if remove_description_line(file_path):
                        print(f"Modified: {file_path}")
                        modified_count += 1
    
    print(f"\nTotal files modified: {modified_count}")

if __name__ == '__main__':
    main()
