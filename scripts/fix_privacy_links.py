#!/usr/bin/env python3
"""
개인정보처리방침 링크 경로 수정 스크립트
pages/ 폴더 내의 모든 HTML 파일에서 ../privacy.html을 ../../privacy.html로 수정
"""

from pathlib import Path

def fix_privacy_links():
    # pages 폴더 내의 모든 HTML 파일 찾기
    pages_dir = Path('web/dark/pages')
    html_files = list(pages_dir.rglob('*.html'))
    
    fixed_count = 0
    
    for html_file in html_files:
        content = html_file.read_text(encoding='utf-8')
        original_content = content
        
        # ../privacy.html을 ../../privacy.html로 변경
        content = content.replace('href="../privacy.html"', 'href="../../privacy.html"')
        
        # 변경사항이 있으면 저장
        if content != original_content:
            html_file.write_text(content, encoding='utf-8')
            fixed_count += 1
            print(f"✅ 수정: {html_file}")
    
    print(f"\n✨ 완료! {fixed_count}개 파일의 개인정보처리방침 링크를 수정했습니다.")

if __name__ == '__main__':
    fix_privacy_links()
