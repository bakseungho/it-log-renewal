#!/usr/bin/env python3
"""
솔루션 페이지의 구성도 이미지 캡션 제거 스크립트
"""

import re
from pathlib import Path

def remove_diagram_caption(file_path):
    """diagram-caption 제거"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # <p class="diagram-caption">클릭하여 확대 보기</p> 제거
    pattern = r'\s*<p class="diagram-caption">[^<]*</p>'
    content = re.sub(pattern, '', content)
    
    # 변경사항이 있는 경우에만 파일 저장
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """메인 실행 함수"""
    solutions_dir = Path('web/template3/solutions')
    
    # 솔루션 페이지 HTML 파일들
    html_files = list(solutions_dir.glob('*.html'))
    
    updated_count = 0
    
    print("구성도 캡션 제거 시작...\n")
    
    for file_path in html_files:
        if file_path.exists():
            if remove_diagram_caption(file_path):
                print(f"✓ Updated: {file_path}")
                updated_count += 1
            else:
                print(f"  Skipped: {file_path} (캡션 없음)")
    
    print(f"\n완료: {updated_count}개 파일이 업데이트되었습니다.")

if __name__ == '__main__':
    main()
