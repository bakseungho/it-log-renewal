#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GNB 메뉴에 스마트 건설현장 안전 플랫폼 추가 스크립트
- AI 영상 방송 관제 시스템 다음에 추가
"""

import os
import re
from pathlib import Path

def add_smart_safety_to_gnb(file_path, is_root=False):
    """파일의 GNB에 스마트 건설현장 안전 플랫폼 메뉴 추가"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = []
        
        # 상대 경로 설정
        if is_root:
            smart_safety_link = "solutions/smart-safety.html"
        else:
            smart_safety_link = "../solutions/smart-safety.html"
        
        # 1. 데스크탑 메뉴에 추가 (AI 영상 방송 관제 시스템 다음)
        pattern1 = r'(<li><a href="[^"]*ai-surveillance\.html" class="header-dropdown-item">AI 영상 방송 관제 시스템</a></li>)'
        replacement1 = r'\1\n              <li><a href="' + smart_safety_link + r'" class="header-dropdown-item">스마트 건설현장 안전 플랫폼</a></li>'
        
        # smart-safety.html이 메뉴에 없고, AI 영상 방송 관제 시스템이 있으면 추가
        if re.search(pattern1, content) and 'header-dropdown-item">스마트 건설현장 안전 플랫폼' not in content:
            content = re.sub(pattern1, replacement1, content)
            changes.append("스마트 건설현장 안전 플랫폼 메뉴 추가 (데스크탑)")
        
        # 2. 모바일 메뉴에 추가
        pattern2 = r'(<a href="[^"]*ai-surveillance\.html" class="header-mobile-submenu-item">AI 영상 방송 관제 시스템</a>)'
        replacement2 = r'\1\n            <a href="' + smart_safety_link + r'" class="header-mobile-submenu-item">스마트 건설현장 안전 플랫폼</a>'
        
        if re.search(pattern2, content) and 'header-mobile-submenu-item">스마트 건설현장 안전 플랫폼' not in content:
            content = re.sub(pattern2, replacement2, content)
            changes.append("스마트 건설현장 안전 플랫폼 메뉴 추가 (모바일)")
        
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
        
        updated, changes = add_smart_safety_to_gnb(html_file, is_root)
        
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
    print("스마트 건설현장 안전 플랫폼 메뉴 추가 시작")
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
