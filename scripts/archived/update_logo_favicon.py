#!/usr/bin/env python3
"""
모든 서브페이지의 헤더 로고와 favicon을 메인페이지와 동일하게 맞추는 스크립트
"""

import re
from pathlib import Path

def update_logo_and_favicon(file_path):
    """헤더 로고와 favicon 업데이트"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 상대 경로 계산
    depth = len(Path(file_path).relative_to('web/template3').parts) - 1
    prefix = '../' * depth if depth > 0 else ''
    
    # 1. Favicon 업데이트
    # 기존 favicon 관련 태그 제거
    content = re.sub(r'<link rel="icon"[^>]*>', '', content)
    content = re.sub(r'<link rel="shortcut icon"[^>]*>', '', content)
    content = re.sub(r'<!-- Favicon -->.*?(?=<link|<meta|<title)', '', content, flags=re.DOTALL)
    
    # 새로운 favicon 추가 (head 태그 안, title 태그 앞에)
    favicon_html = f'''  <!-- 라이트 모드용 (어두운 색상의 파비콘) -->
  <link rel="icon" href="{prefix}images/common/favicon_light.ico" media="(prefers-color-scheme: light)" />
  <!-- 다크 모드용 (밝은 색상의 파비콘) -->
  <link rel="icon" href="{prefix}images/common/favicon_dark.ico" media="(prefers-color-scheme: dark)" />
  
'''
    
    # title 태그 앞에 favicon 삽입
    content = re.sub(r'(\s*<title)', favicon_html + r'\1', content, count=1)
    
    # 2. 헤더 로고 업데이트
    # 기존 로고 이미지 경로를 새 경로로 변경
    logo_patterns = [
        (r'<img src="\.\.\/images\/logo-white\.png"', f'<img src="{prefix}images/common/header_logo.png"'),
        (r'<img src="images\/logo-white\.png"', f'<img src="{prefix}images/common/header_logo.png"'),
        (r'<img src="\.\.\/images\/common\/header_logo\.png"', f'<img src="{prefix}images/common/header_logo.png"'),
    ]
    
    for pattern, replacement in logo_patterns:
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
    
    # 처리할 HTML 파일 목록 (메인 페이지 제외)
    html_files = []
    
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
    
    print("헤더 로고 및 Favicon 업데이트 시작...\n")
    
    for file_path in html_files:
        if file_path.exists():
            if update_logo_and_favicon(file_path):
                print(f"✓ Updated: {file_path}")
                updated_count += 1
            else:
                print(f"  Skipped: {file_path} (변경사항 없음)")
    
    print(f"\n완료: {updated_count}개 파일이 업데이트되었습니다.")
    print("\n변경사항:")
    print("1. 헤더 로고: images/common/header_logo.png")
    print("2. Favicon (라이트 모드): images/common/favicon_light.ico")
    print("3. Favicon (다크 모드): images/common/favicon_dark.ico")

if __name__ == '__main__':
    main()
