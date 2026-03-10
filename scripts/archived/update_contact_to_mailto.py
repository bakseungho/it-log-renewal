#!/usr/bin/env python3
"""
모든 페이지의 GNB 메뉴에서 문의하기 링크를 mailto로 변경하는 스크립트
"""

import re
from pathlib import Path

def update_contact_link(file_path):
    """GNB 메뉴의 문의하기 링크를 mailto로 변경"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 패턴 1: 헤더 드롭다운 메뉴의 문의하기 링크
    # <li><a href="../support/contact.html" class="header-dropdown-item">문의하기</a></li>
    # -> <li><a href="mailto:ok@it-log.co.kr" class="header-dropdown-item">문의하기</a></li>
    
    # 상대 경로 패턴들
    patterns = [
        (r'<a href="\.\.\/support\/contact\.html" class="header-dropdown-item">문의하기</a>',
         '<a href="mailto:ok@it-log.co.kr" class="header-dropdown-item">문의하기</a>'),
        (r'<a href="support\/contact\.html" class="header-dropdown-item">문의하기</a>',
         '<a href="mailto:ok@it-log.co.kr" class="header-dropdown-item">문의하기</a>'),
        (r'<a href="contact\.html" class="header-dropdown-item">문의하기</a>',
         '<a href="mailto:ok@it-log.co.kr" class="header-dropdown-item">문의하기</a>'),
    ]
    
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    # 변경사항이 있는 경우에만 파일 저장
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """메인 실행 함수"""
    template3_dir = Path('web/template3')
    
    # 처리할 HTML 파일 목록
    html_files = []
    
    # 메인 페이지
    html_files.append(template3_dir / 'index.html')
    
    # 기타 루트 페이지들
    for file in ['404.html', 'privacy.html', 'terms.html']:
        file_path = template3_dir / file
        if file_path.exists():
            html_files.append(file_path)
    
    # 서브페이지들
    subdirs = ['about', 'solutions', 'support', 'projects']
    for subdir in subdirs:
        subdir_path = template3_dir / subdir
        if subdir_path.exists():
            html_files.extend(subdir_path.glob('*.html'))
    
    updated_count = 0
    
    print("GNB 메뉴 문의하기 링크 업데이트 시작...\n")
    
    for file_path in html_files:
        if file_path.exists():
            if update_contact_link(file_path):
                print(f"✓ Updated: {file_path}")
                updated_count += 1
            else:
                print(f"  Skipped: {file_path} (변경사항 없음)")
    
    print(f"\n완료: {updated_count}개 파일이 업데이트되었습니다.")
    print("GNB 메뉴의 문의하기 링크가 mailto:ok@it-log.co.kr로 변경되었습니다.")

if __name__ == '__main__':
    main()
