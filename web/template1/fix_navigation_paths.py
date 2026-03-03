#!/usr/bin/env python3
"""
Template1 네비게이션 경로 수정 스크립트
절대 경로(/)를 상대 경로로 변경
"""

import os
import re
from pathlib import Path

def fix_navigation_paths(file_path, is_subpage=True):
    """HTML 파일의 네비게이션 경로를 수정"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    if is_subpage:
        # 서브페이지: / -> ../
        replacements = [
            (r'href="/about/', 'href="../about/'),
            (r'href="/solutions/', 'href="../solutions/'),
            (r'href="/support/', 'href="../support/'),
            (r'href="/">', 'href="../index.html">'),
            (r'<a href="/"', '<a href="../index.html"'),
        ]
    else:
        # 메인 페이지: / -> 상대 경로
        replacements = [
            (r'href="/about/', 'href="about/'),
            (r'href="/solutions/', 'href="solutions/'),
            (r'href="/support/', 'href="support/'),
        ]
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    """메인 실행 함수"""
    
    base_dir = Path(__file__).parent
    modified_files = []
    
    # 서브페이지 처리
    subdirs = ['about', 'solutions', 'support']
    
    for subdir in subdirs:
        subdir_path = base_dir / subdir
        if subdir_path.exists():
            for html_file in subdir_path.glob('*.html'):
                if fix_navigation_paths(html_file, is_subpage=True):
                    modified_files.append(str(html_file.relative_to(base_dir)))
                    print(f"✓ 수정됨: {html_file.name}")
    
    # 메인 페이지 처리 (index.html, terms.html, privacy.html, 404.html)
    main_pages = ['index.html', 'terms.html', 'privacy.html', '404.html']
    for page in main_pages:
        page_path = base_dir / page
        if page_path.exists():
            if fix_navigation_paths(page_path, is_subpage=False):
                modified_files.append(page)
                print(f"✓ 수정됨: {page}")
    
    print(f"\n총 {len(modified_files)}개 파일 수정 완료")
    
    if modified_files:
        print("\n수정된 파일 목록:")
        for file in modified_files:
            print(f"  - {file}")

if __name__ == '__main__':
    main()
