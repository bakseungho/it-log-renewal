#!/usr/bin/env python3
"""
Comment out components section in solution pages (except ai-surveillance_2.html and one-stop-solution.html)
"""

import os
import re

def comment_components_section(file_path):
    """Comment out the components section"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match the components section
        # Looking for <div class="components-section"> ... </div>
        pattern = r'(\s*<div class="components-section">.*?</div>\s*</div>)'
        
        # Check if pattern exists and is not already commented
        if re.search(pattern, content, re.DOTALL):
            # Replace with commented version
            new_content = re.sub(
                pattern,
                r'<!-- \1 -->',
                content,
                flags=re.DOTALL
            )
            
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
    # Solution pages to process (excluding ai-surveillance_2.html and one-stop-solution.html)
    solution_files = [
        'ai-surveillance.html',
        'smart-safety.html',
        'tower-crane.html',
        'access-control.html',
        'environment-sensor.html'
    ]
    
    themes = ['dark', 'light']
    modified_count = 0
    
    for theme in themes:
        for filename in solution_files:
            file_path = f'web/{theme}/pages/solutions/{filename}'
            
            if os.path.exists(file_path):
                if comment_components_section(file_path):
                    print(f"Modified: {file_path}")
                    modified_count += 1
                else:
                    print(f"No changes needed: {file_path}")
            else:
                print(f"File not found: {file_path}")
    
    print(f"\nTotal files modified: {modified_count}")

if __name__ == '__main__':
    main()
