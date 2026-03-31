#!/usr/bin/env python3
"""
솔루션 페이지에서 중복된 solution-hero 섹션 제거
"""

import os
import re
from pathlib import Path

def remove_solution_hero(file_path):
    """solution-hero 섹션 제거"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # solution-hero 섹션 전체 제거 (주석 포함)
    pattern = r'  <!-- Solution Hero -->.*?</section>\n\n'
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ Fixed: {file_path}')

def main():
    base_dir = Path('web/template3/solutions')
    
    # 모든 솔루션 HTML 파일 처리
    for html_file in base_dir.glob('*.html'):
        remove_solution_hero(html_file)
    
    print('\n모든 솔루션 페이지 수정 완료!')

if __name__ == '__main__':
    main()
