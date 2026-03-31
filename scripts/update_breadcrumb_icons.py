#!/usr/bin/env python3
"""
브레드크럼브 업데이트 스크립트
- Home 텍스트를 SVG 홈 아이콘으로 교체
- 부등호(>) 구분자를 가운데 점(·)으로 교체
- 다크/라이트 테마 모두 적용
"""

import os
import re
import glob

# Dark theme: fill color white (rgba)
DARK_HOME_SVG = '<svg class="breadcrumb-home-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none"><mask id="mask0_home" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="24" height="24"><rect width="24" height="24" fill="#D9D9D9"/></mask><g mask="url(#mask0_home)"><path d="M4 21V9L12 3L20 9V21H14V14H10V21H4Z" fill="currentColor"/></g></svg>'

# page-header-breadcrumb pattern: <a href="...">Home</a>
PATTERN_HOME_LINK = re.compile(r'(<a\s+href="[^"]*">)\s*Home\s*(</a>)')

# separator pattern: <span class="separator">></span>
PATTERN_SEPARATOR = re.compile(r'(<span\s+class="separator">)\s*>\s*(</span>)')

# breadcrumb-separator pattern (certifications): <span class="breadcrumb-separator">></span>
PATTERN_BREADCRUMB_SEP = re.compile(r'(<span\s+class="breadcrumb-separator">)\s*>\s*(</span>)')

# breadcrumb-item Home link: <a href="..." class="breadcrumb-item">Home</a>
PATTERN_BREADCRUMB_ITEM_HOME = re.compile(r'(<a\s+href="[^"]*"\s+class="breadcrumb-item">)\s*Home\s*(</a>)')


def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Replace Home text with SVG icon
    content = PATTERN_HOME_LINK.sub(rf'\1{DARK_HOME_SVG}\2', content)
    content = PATTERN_BREADCRUMB_ITEM_HOME.sub(rf'\1{DARK_HOME_SVG}\2', content)
    
    # Replace > separator with · 
    content = PATTERN_SEPARATOR.sub(r'\1·\2', content)
    content = PATTERN_BREADCRUMB_SEP.sub(r'\1·\2', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  Updated: {filepath}')
        return True
    else:
        print(f'  Skipped (no changes): {filepath}')
        return False


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Find all HTML files in dark and light pages
    patterns = [
        os.path.join(base_dir, 'web', 'dark', 'pages', '**', '*.html'),
        os.path.join(base_dir, 'web', 'light', 'pages', '**', '*.html'),
    ]
    
    updated = 0
    total = 0
    
    for pattern in patterns:
        files = glob.glob(pattern, recursive=True)
        for filepath in sorted(files):
            total += 1
            if update_file(filepath):
                updated += 1
    
    print(f'\nDone: {updated}/{total} files updated.')


if __name__ == '__main__':
    main()
