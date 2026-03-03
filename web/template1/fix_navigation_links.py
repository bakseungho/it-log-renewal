#!/usr/bin/env python3
"""
Fix navigation links in template1 HTML files.
Convert absolute paths to relative paths based on file location.
"""

import os
import re
from pathlib import Path

# Define the base directory
BASE_DIR = Path(__file__).parent

# Link replacements for files in subfolders (about/, solutions/, support/)
SUBFOLDER_REPLACEMENTS = {
    'href="/"': 'href="../index.html"',
    'href="/about/company.html"': 'href="company.html"',  # For about/ folder
    'href="/about/ceo-message.html"': 'href="ceo-message.html"',  # For about/ folder
    'href="/about/history.html"': 'href="history.html"',  # For about/ folder
    'href="/about/certifications.html"': 'href="certifications.html"',  # For about/ folder
    'href="/about/location.html"': 'href="location.html"',  # For about/ folder
    'href="/solutions/smart-safety.html"': 'href="../solutions/smart-safety.html"',
    'href="/solutions/tower-crane.html"': 'href="../solutions/tower-crane.html"',
    'href="/solutions/ai-surveillance.html"': 'href="../solutions/ai-surveillance.html"',
    'href="/solutions/environment-sensor.html"': 'href="../solutions/environment-sensor.html"',
    'href="/solutions/access-control.html"': 'href="../solutions/access-control.html"',
    'href="/support/remote-support.html"': 'href="../support/remote-support.html"',
    'href="/support/contact.html"': 'href="../support/contact.html"',
}

# Special replacements for about/ folder files
ABOUT_FOLDER_REPLACEMENTS = {
    'href="/about/company.html"': 'href="company.html"',
    'href="/about/ceo-message.html"': 'href="ceo-message.html"',
    'href="/about/history.html"': 'href="history.html"',
    'href="/about/certifications.html"': 'href="certifications.html"',
    'href="/about/location.html"': 'href="location.html"',
}

# Special replacements for solutions/ folder files
SOLUTIONS_FOLDER_REPLACEMENTS = {
    'href="/solutions/smart-safety.html"': 'href="smart-safety.html"',
    'href="/solutions/tower-crane.html"': 'href="tower-crane.html"',
    'href="/solutions/ai-surveillance.html"': 'href="ai-surveillance.html"',
    'href="/solutions/environment-sensor.html"': 'href="environment-sensor.html"',
    'href="/solutions/access-control.html"': 'href="access-control.html"',
}

# Special replacements for support/ folder files
SUPPORT_FOLDER_REPLACEMENTS = {
    'href="/support/remote-support.html"': 'href="remote-support.html"',
    'href="/support/contact.html"': 'href="contact.html"',
}

def fix_file(file_path):
    """Fix navigation links in a single HTML file."""
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Determine which replacements to use based on file location
    folder = file_path.parent.name
    
    # Apply common replacements first
    content = content.replace('href="/"', 'href="../index.html"')
    
    # Apply folder-specific replacements
    if folder == 'about':
        for old, new in ABOUT_FOLDER_REPLACEMENTS.items():
            content = content.replace(old, new)
        # For other folders, use relative paths
        for old, new in SOLUTIONS_FOLDER_REPLACEMENTS.items():
            new_path = new.replace('href="', 'href="../solutions/')
            content = content.replace(old, new_path)
        for old, new in SUPPORT_FOLDER_REPLACEMENTS.items():
            new_path = new.replace('href="', 'href="../support/')
            content = content.replace(old, new_path)
    
    elif folder == 'solutions':
        for old, new in SOLUTIONS_FOLDER_REPLACEMENTS.items():
            content = content.replace(old, new)
        # For other folders, use relative paths
        for old, new in ABOUT_FOLDER_REPLACEMENTS.items():
            new_path = new.replace('href="', 'href="../about/')
            content = content.replace(old, new_path)
        for old, new in SUPPORT_FOLDER_REPLACEMENTS.items():
            new_path = new.replace('href="', 'href="../support/')
            content = content.replace(old, new_path)
    
    elif folder == 'support':
        for old, new in SUPPORT_FOLDER_REPLACEMENTS.items():
            content = content.replace(old, new)
        # For other folders, use relative paths
        for old, new in ABOUT_FOLDER_REPLACEMENTS.items():
            new_path = new.replace('href="', 'href="../about/')
            content = content.replace(old, new_path)
        for old, new in SOLUTIONS_FOLDER_REPLACEMENTS.items():
            new_path = new.replace('href="', 'href="../solutions/')
            content = content.replace(old, new_path)
    
    # Write back if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Fixed {file_path}")
        return True
    else:
        print(f"  - No changes needed for {file_path}")
        return False

def main():
    """Main function to process all HTML files."""
    print("Fixing navigation links in template1 HTML files...\n")
    
    # Process files in subfolders
    folders = ['about', 'solutions', 'support']
    fixed_count = 0
    
    for folder in folders:
        folder_path = BASE_DIR / folder
        if folder_path.exists():
            print(f"\nProcessing {folder}/ folder:")
            for html_file in folder_path.glob('*.html'):
                if fix_file(html_file):
                    fixed_count += 1
    
    print(f"\n✓ Complete! Fixed {fixed_count} files.")

if __name__ == '__main__':
    main()
