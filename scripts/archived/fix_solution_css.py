#!/usr/bin/env python3
"""
솔루션 페이지의 CSS 링크를 solutions.css에서 subpage.css로 변경
"""

import os
from pathlib import Path

def fix_css_link(file_path):
    """CSS 링크 수정"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # solutions.css를 subpage.css로 변경
    content = content.replace(
        '<link rel="stylesheet" href="../css/pages/solutions.css">',
        '<link rel="stylesheet" href="../css/pages/subpage.css">'
    )
    
    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ Fixed: {file_path}')

def main():
    base_dir = Path('web/template3/solutions')
    
    # 모든 솔루션 HTML 파일 처리
    for html_file in base_dir.glob('*.html'):
        fix_css_link(html_file)
    
    print('\n모든 솔루션 페이지 CSS 링크 수정 완료!')

if __name__ == '__main__':
    main()
