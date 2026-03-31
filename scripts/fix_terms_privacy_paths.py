#!/usr/bin/env python3
"""
이용약관과 개인정보처리방침 페이지의 경로 수정 스크립트
web/dark/ 루트에 있는 파일이므로 ../ 경로를 제거
"""

from pathlib import Path

def fix_paths():
    files = [
        Path('web/dark/terms.html'),
        Path('web/dark/privacy.html')
    ]
    
    for file_path in files:
        if not file_path.exists():
            print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
            continue
        
        content = file_path.read_text(encoding='utf-8')
        original_content = content
        
        # 이미지 경로 수정: ../images/ -> images/
        content = content.replace('src="../images/', 'src="images/')
        
        # 링크 경로 수정: ../terms.html -> terms.html, ../privacy.html -> privacy.html
        content = content.replace('href="../terms.html"', 'href="terms.html"')
        content = content.replace('href="../privacy.html"', 'href="privacy.html"')
        
        # JS 경로는 이미 올바름 (js/로 시작)
        
        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            print(f"✅ 수정: {file_path}")
        else:
            print(f"ℹ️  변경사항 없음: {file_path}")
    
    print("\n✨ 완료!")

if __name__ == '__main__':
    fix_paths()
