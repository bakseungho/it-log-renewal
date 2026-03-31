#!/usr/bin/env python3
"""
Fix header logo links in pages/ subdirectories
Change from ../index.html to ../../index.html
"""

import os
import re
from pathlib import Path

def fix_logo_link(file_path):
    """Fix logo link in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix logo link: ../index.html -> ../../index.html
        content = re.sub(
            r'<a href="\.\./index\.html" class="header-logo-link">',
            r'<a href="../../index.html" class="header-logo-link">',
            content
        )
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")
        return False

def process_template(template_name):
    """Process all HTML files in pages/ subdirectories"""
    template_dir = Path(f'web/{template_name}')
    pages_dir = template_dir / 'pages'
    
    if not pages_dir.exists():
        print(f"✗ Pages directory not found: {pages_dir}")
        return
    
    print(f"\n{'='*60}")
    print(f"Processing {template_name.upper()} template")
    print(f"{'='*60}\n")
    
    updated_count = 0
    
    # Process all HTML files in pages subdirectories
    for html_file in pages_dir.rglob('*.html'):
        if fix_logo_link(html_file):
            print(f"✓ Fixed {html_file.relative_to(template_dir)}")
            updated_count += 1
    
    print(f"\nTotal updated: {updated_count} files")

def main():
    """Main function"""
    print("Fixing header logo links in pages/ subdirectories\n")
    
    # Process both templates
    for template in ['dark', 'light']:
        if os.path.exists(f'web/{template}'):
            process_template(template)
    
    print(f"\n{'='*60}")
    print("Logo link fix complete!")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
