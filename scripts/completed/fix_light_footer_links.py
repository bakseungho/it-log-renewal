#!/usr/bin/env python3
"""
라이트 모드 서브페이지의 이용약관/개인정보처리방침 링크 경로 수정
"""

import os
import re

def fix_footer_links(file_path):
    """파일의 푸터 링크 경로 수정"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # ../terms.html -> ../../terms.html
        content = content.replace('href="../terms.html"', 'href="../../terms.html"')
        
        # 이미 ../../privacy.html로 되어 있는 것은 그대로 유지
        # (일부는 이미 올바른 경로)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        else:
            return False
            
    except Exception as e:
        print(f"  ❌ 오류 발생: {file_path} - {str(e)}")
        return False

def main():
    """메인 함수"""
    base_dir = 'web/light/pages'
    
    # 모든 HTML 파일 찾기
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"🔍 {len(html_files)}개의 HTML 파일 발견\n")
    
    updated_count = 0
    for file_path in sorted(html_files):
        print(f"📝 처리 중: {file_path}")
        if fix_footer_links(file_path):
            updated_count += 1
            print(f"  ✅ 링크 경로 수정 완료")
        else:
            print(f"  ⚠️  변경 사항 없음")
        print()
    
    print(f"\n{'='*60}")
    print(f"✨ 완료: {updated_count}/{len(html_files)}개 파일 업데이트")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
