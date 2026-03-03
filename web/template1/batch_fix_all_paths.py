#!/usr/bin/env python3
"""
Template1 모든 경로 일괄 수정 스크립트
- 헤더 로고 링크
- 네비게이션 메뉴 링크
- 모바일 메뉴 링크
- 푸터 링크
- Breadcrumb 링크
"""

import os
import re
from pathlib import Path

def fix_all_paths_in_file(file_path, folder_name=None):
    """HTML 파일의 모든 경로를 수정"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 파일이 어느 폴더에 있는지 확인
    if folder_name:  # 서브페이지 (about, solutions, support)
        # 절대 경로를 상대 경로로 변경
        replacements = [
            # 같은 폴더 내 링크
            (rf'href="/{folder_name}/([^"]+)"', r'href="\1"'),
            # 다른 폴더로의 링크
            (r'href="/about/', 'href="../about/'),
            (r'href="/solutions/', 'href="../solutions/'),
            (r'href="/support/', 'href="../support/'),
            # 홈 링크
            (r'href="/">', 'href="../index.html">'),
            (r'<a href="/"', '<a href="../index.html"'),
        ]
    else:  # 메인 페이지 (index.html, terms.html, privacy.html)
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
    
    print("=" * 60)
    print("Template1 경로 일괄 수정 시작")
    print("=" * 60)
    
    # 서브페이지 처리
    subdirs = {
        'about': 'about',
        'solutions': 'solutions',
        'support': 'support'
    }
    
    for folder_name, folder_path in subdirs.items():
        subdir_path = base_dir / folder_path
        if subdir_path.exists():
            print(f"\n[{folder_name}] 폴더 처리 중...")
            for html_file in sorted(subdir_path.glob('*.html')):
                if fix_all_paths_in_file(html_file, folder_name):
                    modified_files.append(str(html_file.relative_to(base_dir)))
                    print(f"  ✓ {html_file.name}")
    
    # 메인 페이지 처리
    print(f"\n[메인 페이지] 처리 중...")
    main_pages = ['index.html', 'terms.html', 'privacy.html', '404.html']
    for page in main_pages:
        page_path = base_dir / page
        if page_path.exists():
            if fix_all_paths_in_file(page_path, None):
                modified_files.append(page)
                print(f"  ✓ {page}")
    
    print("\n" + "=" * 60)
    print(f"작업 완료: 총 {len(modified_files)}개 파일 수정")
    print("=" * 60)
    
    if modified_files:
        print("\n수정된 파일 목록:")
        for file in modified_files:
            print(f"  - {file}")
    else:
        print("\n수정할 파일이 없습니다. (이미 모두 수정됨)")

if __name__ == '__main__':
    main()
