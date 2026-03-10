#!/usr/bin/env python3
"""
솔루션 페이지의 구성품 이미지 placeholder를 실제 이미지로 교체하는 스크립트
"""

import os
import re
from pathlib import Path

def update_component_images(file_path):
    """구성품 placeholder를 img 태그로 교체"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # component-image-placeholder를 img 태그로 교체
    # <div class="component-image-placeholder">이미지</div>
    # -> <img src="../images/common/no_image.png" alt="구성품" class="component-image">
    
    pattern = r'<div class="component-image-placeholder">[^<]*</div>'
    replacement = '<img src="../images/common/no_image.png" alt="구성품" class="component-image">'
    
    content = re.sub(pattern, replacement, content)
    
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
    
    print("구성품 이미지 교체 시작...\n")
    
    for file_path in html_files:
        if file_path.exists():
            if update_component_images(file_path):
                print(f"✓ Updated: {file_path}")
                updated_count += 1
            else:
                print(f"  Skipped: {file_path} (변경사항 없음)")
    
    print(f"\n완료: {updated_count}개 파일이 업데이트되었습니다.")

if __name__ == '__main__':
    main()
