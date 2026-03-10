#!/usr/bin/env python3
"""
Fix the features section layout in all solution pages.
Move the features-section-title outside of overview-features div for proper centering.
"""

import os
import re

def fix_features_layout(file_path):
    """Fix the features section layout in a solution page."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find the features section with title inside overview-features
    pattern = r'(<div class="overview-features">)\s*<h3 class="features-section-title">(.*?)</h3>'
    
    # Check if the pattern exists
    if re.search(pattern, content):
        # Move the title outside and before the overview-features div
        content = re.sub(
            pattern,
            r'<h3 class="features-section-title">\2</h3>\n      \1',
            content
        )
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    
    return False

def main():
    """Process all solution pages."""
    solutions_dir = 'web/template3/solutions'
    
    # List of solution pages to process
    solution_files = [
        'ai-surveillance.html',
        'access-control.html',
        'tower-crane.html',
        'environment-sensor.html'
    ]
    
    fixed_count = 0
    
    for filename in solution_files:
        file_path = os.path.join(solutions_dir, filename)
        
        if os.path.exists(file_path):
            if fix_features_layout(file_path):
                print(f"✓ Fixed: {filename}")
                fixed_count += 1
            else:
                print(f"- Skipped (already correct): {filename}")
        else:
            print(f"✗ Not found: {filename}")
    
    print(f"\nTotal files fixed: {fixed_count}")

if __name__ == '__main__':
    main()
