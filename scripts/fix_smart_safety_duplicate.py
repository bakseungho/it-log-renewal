#!/usr/bin/env python3
"""
Remove duplicate content after </html> tag in smart-safety.html files
"""

import os

def fix_duplicate_content(file_path):
    """Remove content after first </html> tag"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the first </html> tag
        first_html_end = content.find('</html>')
        
        if first_html_end == -1:
            print(f"No </html> tag found in {file_path}")
            return False
        
        # Check if there's content after </html>
        end_position = first_html_end + len('</html>')
        remaining_content = content[end_position:].strip()
        
        if remaining_content:
            # Keep only content up to and including first </html>
            new_content = content[:end_position] + '\n'
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Fixed: {file_path}")
            print(f"  Removed {len(remaining_content)} characters after </html>")
            return True
        else:
            print(f"No duplicate content in {file_path}")
            return False
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    files = [
        'web/dark/pages/solutions/smart-safety.html',
        'web/light/pages/solutions/smart-safety.html'
    ]
    
    for file_path in files:
        if os.path.exists(file_path):
            fix_duplicate_content(file_path)
        else:
            print(f"File not found: {file_path}")

if __name__ == '__main__':
    main()
