#!/usr/bin/env python3
"""
Batch fix navigation links in all template1 HTML files.
Converts absolute paths to relative paths based on file location.
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def fix_links_in_file(file_path, replacements):
    """Apply link replacements to a file."""
    print(f"Processing: {file_path.relative_to(BASE_DIR)}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = 0
        
        for old_pattern, new_pattern in replacements.items():
            if old_pattern in content:
                count = content.count(old_pattern)
                content = content.replace(old_pattern, new_pattern)
                changes_made += count
                if count > 0:
                    print(f"  - Replaced '{old_pattern}' → '{new_pattern}' ({count} times)")
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Fixed {changes_made} links in {file_path.name}\n")
            return True
        else:
            print(f"  - No changes needed\n")
            return False
            
    except Exception as e:
        print(f"  ✗ Error: {e}\n")
        return False

def get_about_folder_replacements():
    """Get replacements for files in about/ folder."""
    return {
        'href="/"': 'href="../index.html"',
        'href="/about/company.html"': 'href="company.html"',
        'href="/about/ceo-message.html"': 'href="ceo-message.html"',
        'href="/about/history.html"': 'href="history.html"',
        'href="/about/certifications.html"': 'href="certifications.html"',
        'href="/about/location.html"': 'href="location.html"',
        'href="/solutions/smart-safety.html"': 'href="../solutions/smart-safety.html"',
        'href="/solutions/tower-crane.html"': 'href="../solutions/tower-crane.html"',
        'href="/solutions/ai-surveillance.html"': 'href="../solutions/ai-surveillance.html"',
        'href="/solutions/environment-sensor.html"': 'href="../solutions/environment-sensor.html"',
        'href="/solutions/access-control.html"': 'href="../solutions/access-control.html"',
        'href="/support/remote-support.html"': 'href="../support/remote-support.html"',
        'href="/support/contact.html"': 'href="../support/contact.html"',
    }

def get_solutions_folder_replacements():
    """Get replacements for files in solutions/ folder."""
    return {
        'href="/"': 'href="../index.html"',
        'href="/about/company.html"': 'href="../about/company.html"',
        'href="/about/ceo-message.html"': 'href="../about/ceo-message.html"',
        'href="/about/history.html"': 'href="../about/history.html"',
        'href="/about/certifications.html"': 'href="../about/certifications.html"',
        'href="/about/location.html"': 'href="../about/location.html"',
        'href="/solutions/smart-safety.html"': 'href="smart-safety.html"',
        'href="/solutions/tower-crane.html"': 'href="tower-crane.html"',
        'href="/solutions/ai-surveillance.html"': 'href="ai-surveillance.html"',
        'href="/solutions/environment-sensor.html"': 'href="environment-sensor.html"',
        'href="/solutions/access-control.html"': 'href="access-control.html"',
        'href="/support/remote-support.html"': 'href="../support/remote-support.html"',
        'href="/support/contact.html"': 'href="../support/contact.html"',
    }

def get_support_folder_replacements():
    """Get replacements for files in support/ folder."""
    return {
        'href="/"': 'href="../index.html"',
        'href="/about/company.html"': 'href="../about/company.html"',
        'href="/about/ceo-message.html"': 'href="../about/ceo-message.html"',
        'href="/about/history.html"': 'href="../about/history.html"',
        'href="/about/certifications.html"': 'href="../about/certifications.html"',
        'href="/about/location.html"': 'href="../about/location.html"',
        'href="/solutions/smart-safety.html"': 'href="../solutions/smart-safety.html"',
        'href="/solutions/tower-crane.html"': 'href="../solutions/tower-crane.html"',
        'href="/solutions/ai-surveillance.html"': 'href="../solutions/ai-surveillance.html"',
        'href="/solutions/environment-sensor.html"': 'href="../solutions/environment-sensor.html"',
        'href="/solutions/access-control.html"': 'href="../solutions/access-control.html"',
        'href="/support/remote-support.html"': 'href="remote-support.html"',
        'href="/support/contact.html"': 'href="contact.html"',
    }

def get_root_folder_replacements():
    """Get replacements for files in root folder."""
    return {
        'href="/"': 'href="index.html"',
        'href="/about/company.html"': 'href="about/company.html"',
        'href="/about/ceo-message.html"': 'href="about/ceo-message.html"',
        'href="/about/history.html"': 'href="about/history.html"',
        'href="/about/certifications.html"': 'href="about/certifications.html"',
        'href="/about/location.html"': 'href="about/location.html"',
        'href="/solutions/smart-safety.html"': 'href="solutions/smart-safety.html"',
        'href="/solutions/tower-crane.html"': 'href="solutions/tower-crane.html"',
        'href="/solutions/ai-surveillance.html"': 'href="solutions/ai-surveillance.html"',
        'href="/solutions/environment-sensor.html"': 'href="solutions/environment-sensor.html"',
        'href="/solutions/access-control.html"': 'href="solutions/access-control.html"',
        'href="/support/remote-support.html"': 'href="support/remote-support.html"',
        'href="/support/contact.html"': 'href="support/contact.html"',
    }

def main():
    """Main function to process all HTML files."""
    print("=" * 70)
    print("Batch Fixing Navigation Links in Template1")
    print("=" * 70)
    print()
    
    fixed_count = 0
    skipped_files = ['index.html', 'about/history.html']  # Already fixed
    
    # Fix about/ folder files
    print("📁 Processing about/ folder files:")
    print("-" * 70)
    about_folder = BASE_DIR / 'about'
    if about_folder.exists():
        replacements = get_about_folder_replacements()
        for html_file in sorted(about_folder.glob('*.html')):
            if f'about/{html_file.name}' not in skipped_files:
                if fix_links_in_file(html_file, replacements):
                    fixed_count += 1
    
    # Fix solutions/ folder files
    print("\n📁 Processing solutions/ folder files:")
    print("-" * 70)
    solutions_folder = BASE_DIR / 'solutions'
    if solutions_folder.exists():
        replacements = get_solutions_folder_replacements()
        for html_file in sorted(solutions_folder.glob('*.html')):
            if fix_links_in_file(html_file, replacements):
                fixed_count += 1
    
    # Fix support/ folder files
    print("\n📁 Processing support/ folder files:")
    print("-" * 70)
    support_folder = BASE_DIR / 'support'
    if support_folder.exists():
        replacements = get_support_folder_replacements()
        for html_file in sorted(support_folder.glob('*.html')):
            if fix_links_in_file(html_file, replacements):
                fixed_count += 1
    
    # Fix root folder files (except index.html which is already fixed)
    print("\n📁 Processing root folder files:")
    print("-" * 70)
    replacements = get_root_folder_replacements()
    for html_file in sorted(BASE_DIR.glob('*.html')):
        if html_file.name not in skipped_files:
            if fix_links_in_file(html_file, replacements):
                fixed_count += 1
    
    print("\n" + "=" * 70)
    print(f"✅ Complete! Fixed {fixed_count} files.")
    print("=" * 70)
    print("\n💡 Next steps:")
    print("1. Open index.html in a browser")
    print("2. Test all navigation links")
    print("3. Verify pages load correctly")
    print()

if __name__ == '__main__':
    main()
