#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GNB 링크 활성화 및 '인증 및 특허' 메뉴 제거 스크립트
- 안전보건 경영방침과 목표: href="#" → "about/safety-policy.html" 또는 "../about/safety-policy.html"
- 시공사례: href="#projects" → "projects/index.html" 또는 "../projects/index.html"
- 인증 및 특허 메뉴 제거
"""

import os
import re
from pathlib import Path

def update_gnb_in_file(file_path, is_root=False):
    """파일의 GNB 링크를 업데이트하고 인증 및 특허 메뉴 제거"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = []
        
        # 상대 경로 설정
        if is_root:
            safety_link = "about/safety-policy.html"
            projects_link = "projects/index.html"
        else:
            safety_link = "../about/safety-policy.html"
            projects_link = "../projects/index.html"
        
        # 1. 안전보건 경영방침과 목표 링크 활성화 (데스크탑)
        pattern1 = r'<li><a href="#" class="header-dropdown-item">안전보건 경영방침과 목표</a></li>'
        replacement1 = f'<li><a href="{safety_link}" class="header-dropdown-item">안전보건 경영방침과 목표</a></li>'
        if re.search(pattern1, content):
            content = re.sub(pattern1, replacement1, content)
            changes.append("안전보건 경영방침 링크 활성화 (데스크탑)")
        
        # 2. 안전보건 경영방침과 목표 링크 활성화 (모바일)
        pattern2 = r'<a href="#" class="header-mobile-submenu-item">안전보건 경영방침과 목표</a>'
        replacement2 = f'<a href="{safety_link}" class="header-mobile-submenu-item">안전보건 경영방침과 목표</a>'
        if re.search(pattern2, content):
            content = re.sub(pattern2, replacement2, content)
            changes.append("안전보건 경영방침 링크 활성화 (모바일)")
        
        # 3. 시공사례 링크 업데이트 (데스크탑) - #projects → projects/index.html
        pattern3 = r'<a href="[^"]*#projects" class="header-menu-item">시공사례</a>'
        replacement3 = f'<a href="{projects_link}" class="header-menu-item">시공사례</a>'
        if re.search(pattern3, content):
            content = re.sub(pattern3, replacement3, content)
            changes.append("시공사례 링크 업데이트 (데스크탑)")
        
        # 4. 시공사례 링크 업데이트 (모바일)
        pattern4 = r'<a href="[^"]*#projects" class="header-mobile-menu-item">시공사례</a>'
        replacement4 = f'<a href="{projects_link}" class="header-mobile-menu-item">시공사례</a>'
        if re.search(pattern4, content):
            content = re.sub(pattern4, replacement4, content)
            changes.append("시공사례 링크 업데이트 (모바일)")
        
        # 5. 인증 및 특허 메뉴 제거 (데스크탑)
        pattern5 = r'\s*<li><a href="[^"]*certifications\.html" class="header-dropdown-item">인증 및 특허</a></li>'
        if re.search(pattern5, content):
            content = re.sub(pattern5, '', content)
            changes.append("인증 및 특허 메뉴 제거 (데스크탑)")
        
        # 6. 인증 및 특허 메뉴 제거 (모바일)
        pattern6 = r'\s*<a href="[^"]*certifications\.html" class="header-mobile-submenu-item">인증 및 특허</a>'
        if re.search(pattern6, content):
            content = re.sub(pattern6, '', content)
            changes.append("인증 및 특허 메뉴 제거 (모바일)")
        
        # 변경사항이 있으면 파일 저장
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes
        
        return False, []
        
    except Exception as e:
        print(f"  ❌ 오류 발생: {e}")
        return False, []

def process_template(template_path):
    """템플릿 폴더의 모든 HTML 파일 처리"""
    template_name = os.path.basename(template_path)
    print(f"\n{'='*60}")
    print(f"📁 {template_name} 처리 중...")
    print(f"{'='*60}\n")
    
    updated_count = 0
    
    # HTML 파일 찾기
    html_files = list(Path(template_path).rglob("*.html"))
    
    for html_file in html_files:
        rel_path = html_file.relative_to(template_path)
        print(f"처리 중: {rel_path}")
        
        # 루트 레벨 파일인지 확인
        is_root = len(html_file.relative_to(template_path).parts) == 1
        
        updated, changes = update_gnb_in_file(html_file, is_root)
        
        if updated:
            for change in changes:
                print(f"  ✓ {change}")
            updated_count += 1
        else:
            print(f"  - 변경사항 없음")
        print()
    
    print(f"{template_name}: {updated_count}개 파일 업데이트 완료")
    return updated_count

def main():
    """메인 함수"""
    print("="*60)
    print("GNB 링크 활성화 및 '인증 및 특허' 메뉴 제거 시작")
    print("="*60)
    
    # 현재 스크립트 위치 기준으로 web 폴더 찾기
    script_dir = Path(__file__).parent
    web_dir = script_dir / "web"
    
    if not web_dir.exists():
        print(f"❌ web 폴더를 찾을 수 없습니다: {web_dir}")
        return
    
    total_updated = 0
    
    # template3만 처리
    template3_path = web_dir / "template3"
    if template3_path.exists():
        count = process_template(template3_path)
        total_updated += count
    else:
        print(f"⚠ template3 폴더를 찾을 수 없습니다: {template3_path}")
    
    print("\n" + "="*60)
    print(f"✅ 전체 작업 완료")
    print(f"   총 {total_updated}개 파일 업데이트")
    print("="*60)

if __name__ == "__main__":
    main()
