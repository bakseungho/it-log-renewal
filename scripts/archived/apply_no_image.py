#!/usr/bin/env python3
"""
모든 페이지의 이미지를 no_image.png로 교체하는 스크립트
제외: 서브페이지 상단 배경 이미지 (page-header-image)
"""

import os
import re
from pathlib import Path

def get_relative_path(from_file, to_file='images/common/no_image.png'):
    """파일 위치에 따른 상대 경로 계산"""
    from_path = Path(from_file)
    from_dir = from_path.parent
    
    # 파일이 web/template3/ 루트에 있는 경우
    if from_dir == Path('web/template3'):
        return to_file
    
    # 파일이 하위 폴더에 있는 경우 (about/, solutions/, support/, projects/)
    depth = len(from_dir.relative_to('web/template3').parts)
    prefix = '../' * depth
    return prefix + to_file

def update_images_in_file(file_path):
    """HTML 파일의 이미지를 no_image.png로 교체"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    relative_path = get_relative_path(file_path)
    
    # 1. 히어로 슬라이드 배경 이미지 (메인 페이지)
    # <div class="hero-background" style="background-image: url('...');">
    pattern1 = r'(<div class="hero-background"[^>]*style="background-image:\s*url\([\'"]?)([^\'")]+)([\'"]?\);?"[^>]*>)'
    content = re.sub(pattern1, rf'\1{relative_path}\3', content)
    
    # 2. 일반 img 태그 (page-header-image 클래스 제외)
    # <img src="..." alt="..." class="...">
    # page-header-image 내부의 img는 제외
    def replace_img(match):
        full_match = match.group(0)
        # page-header-image 내부인지 확인 (앞뒤 컨텍스트 확인)
        return full_match  # 일단 그대로 반환, 아래에서 처리
    
    # page-header-image가 아닌 img 태그만 교체
    lines = content.split('\n')
    new_lines = []
    in_page_header_image = False
    
    for line in lines:
        # page-header-image 섹션 시작
        if 'class="page-header-image"' in line or 'page-header-image' in line:
            in_page_header_image = True
            new_lines.append(line)
            continue
        
        # page-header-image 섹션 종료 (닫는 div)
        if in_page_header_image and '</div>' in line:
            in_page_header_image = False
            new_lines.append(line)
            continue
        
        # page-header-image 내부가 아닌 경우에만 img src 교체
        if not in_page_header_image and '<img' in line and 'src=' in line:
            # 로고 이미지는 제외
            if 'logo' not in line.lower():
                # src 속성 교체
                line = re.sub(r'src=["\']([^"\']+)["\']', f'src="{relative_path}"', line)
        
        new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    # 3. 카드 이미지 (card-project, card-solution 등)
    # <div class="card-image">...<img src="...">
    # 이미 위에서 처리됨
    
    # 4. 갤러리 이미지
    # <img class="gallery-image" src="...">
    # 이미 위에서 처리됨
    
    # 5. case-image, component-image 등
    # 이미 위에서 처리됨
    
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
    
    # 서브페이지들
    subdirs = ['about', 'solutions', 'support', 'projects']
    for subdir in subdirs:
        subdir_path = template3_dir / subdir
        if subdir_path.exists():
            html_files.extend(subdir_path.glob('*.html'))
    
    updated_count = 0
    
    print("이미지 교체 시작...\n")
    
    for file_path in html_files:
        if file_path.exists():
            if update_images_in_file(file_path):
                print(f"✓ Updated: {file_path}")
                updated_count += 1
            else:
                print(f"  Skipped: {file_path} (변경사항 없음)")
    
    print(f"\n완료: {updated_count}개 파일이 업데이트되었습니다.")
    print("서브페이지 상단 배경 이미지(page-header-image)는 제외되었습니다.")

if __name__ == '__main__':
    main()
