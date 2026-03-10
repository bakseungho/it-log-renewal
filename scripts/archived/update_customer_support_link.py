#!/usr/bin/env python3
"""
Update customer support link in GNB menu to point to remote-support page.
Change from support/contact.html to support/remote-support.html
"""

import os
import re

def update_support_link(file_path):
    """Update the customer support link in a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern to find the customer support menu item link
    # Looking for: <a href="...support/contact.html" class="header-menu-item">고객지원</a>
    patterns = [
        (r'(<a href="[^"]*)(support/contact\.html)(" class="header-menu-item">고객지원</a>)', 
         r'\1support/remote-support.html\3'),
        (r'(<a href="[^"]*)(\.\.\/support\/contact\.html)(" class="header-menu-item">고객지원</a>)', 
         r'\1../support/remote-support.html\3'),
    ]
    
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    """Process all HTML files in template3."""
    base_dir = 'web/template3'
    
    # Find all HTML files
    html_files = []
    
    # Root level
    for file in os.listdir(base_dir):
        if file.endswith('.html'):
            html_files.append(os.path.join(base_dir, file))
    
    # Subdirectories
    subdirs = ['about', 'solutions', 'support', 'projects']
    for subdir in subdirs:
        subdir_path = os.path.join(base_dir, subdir)
        if os.path.exists(subdir_path):
            for file in os.listdir(subdir_path):
                if file.endswith('.html'):
                    html_files.append(os.path.join(subdir_path, file))
    
    updated_count = 0
    
    for file_path in sorted(html_files):
        if update_support_link(file_path):
            rel_path = os.path.relpath(file_path, 'web/template3')
            print(f"✓ Updated: {rel_path}")
            updated_count += 1
    
    print(f"\nTotal files updated: {updated_count}")

if __name__ == '__main__':
    main()
