#!/usr/bin/env python3
"""
3개 템플릿의 모든 HTML 파일에 '시공사례' 메뉴를 추가하는 스크립트
각 템플릿의 네비게이션 구조에 맞게 처리
"""

import os
import re
from pathlib import Path

def add_projects_to_template1(file_path):
    """Template1 파일에 시공사례 메뉴 추가"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 이미 시공사례가 있는지 확인
    if '시공사례' in content:
        return False, "이미 시공사례 메뉴 존재"
    
    is_root = file_path.name == 'index.html' and 'template1' in str(file_path.parent)
    projects_link = '#projects' if is_root else '../index.html#projects'
    
    original = content
    
    # 데스크톱 네비게이션 업데이트
    desktop_pattern = r'(</ul>\s*</li>\s*<li class="nav-list__item">\s*<a href="#" class="nav-list__link nav-list__link--dropdown">\s*고객지원)'
    desktop_replacement = f'''</ul>
                        </li>
                        <li class="nav-list__item">
                            <a href="{projects_link}" class="nav-list__link">시공사례</a>
                        </li>
                        <li class="nav-list__item">
                            <a href="#" class="nav-list__link nav-list__link--dropdown">
                                고객지원'''
    content = re.sub(desktop_pattern, desktop_replacement, content, flags=re.DOTALL)
    
    # 모바일 네비게이션 업데이트
    mobile_pattern = r'(</div>\s*</li>\s*<li class="mobile-menu__item">\s*<button class="mobile-menu__link"[^>]*>\s*고객지원)'
    mobile_replacement = f'''</div>
                </li>
                <li class="mobile-menu__item">
                    <a href="{projects_link}" class="mobile-menu__link">시공사례</a>
                </li>
                <li class="mobile-menu__item">
                    <button class="mobile-menu__link" aria-expanded="false">
                        고객지원'''
    content = re.sub(mobile_pattern, mobile_replacement, content, flags=re.DOTALL)
    
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "업데이트 완료"
    
    return False, "패턴을 찾지 못함"

def add_projects_to_template2(file_path):
    """Template2 파일에 시공사례 메뉴 추가"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 이미 시공사례가 있는지 확인
    if '시공사례' in content:
        return False, "이미 시공사례 메뉴 존재"
    
    is_root = file_path.name == 'index.html' and 'template2' in str(file_path.parent)
    projects_link = '#projects' if is_root else '../index.html#projects'
    
    original = content
    
    # 데스크톱 네비게이션 업데이트
    desktop_pattern = r'(</ul>\s*</li>\s*<li class="nav-item">\s*<a href="#" class="nav-link">\s*고객지원)'
    desktop_replacement = f'''</ul>
          </li>

          <li class="nav-item">
            <a href="{projects_link}" class="nav-link">시공사례</a>
          </li>
          
          <li class="nav-item">
            <a href="#" class="nav-link">
              고객지원'''
    content = re.sub(desktop_pattern, desktop_replacement, content, flags=re.DOTALL)
    
    # 모바일 네비게이션 업데이트
    mobile_pattern = r'(</ul>\s*</li>\s*<li class="mobile-nav-item">\s*<div class="mobile-nav-link">\s*고객지원)'
    mobile_replacement = f'''</ul>
      </li>
      
      <li class="mobile-nav-item">
        <a href="{projects_link}" class="mobile-nav-link">시공사례</a>
      </li>
      
      <li class="mobile-nav-item">
        <div class="mobile-nav-link">
          고객지원'''
    content = re.sub(mobile_pattern, mobile_replacement, content, flags=re.DOTALL)
    
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "업데이트 완료"
    
    return False, "패턴을 찾지 못함"

def add_projects_to_template3(file_path):
    """Template3 파일에 시공사례 메뉴 추가"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 이미 시공사례가 있는지 확인
    if '시공사례' in content:
        return False, "이미 시공사례 메뉴 존재"
    
    is_root = file_path.name == 'index.html' and 'template3' in str(file_path.parent)
    projects_link = '#projects' if is_root else '../index.html#projects'
    
    original = content
    
    # 데스크톱 네비게이션 업데이트
    desktop_pattern = r'(</ul>\s*</li>\s*<li class="header-dropdown">\s*<a href="[^"]*" class="header-menu-item">고객지원</a>)'
    desktop_replacement = f'''</ul>
          </li>
          <li class="header-dropdown">
            <a href="{projects_link}" class="header-menu-item">시공사례</a>
          </li>
          <li class="header-dropdown">
            <a href="support/contact.html" class="header-menu-item">고객지원</a>'''
    
    # 서브페이지의 경우 경로 조정
    if not is_root:
        desktop_replacement = desktop_replacement.replace('support/contact.html', '../support/contact.html')
    
    content = re.sub(desktop_pattern, desktop_replacement, content, flags=re.DOTALL)
    
    # 모바일 네비게이션 업데이트
    mobile_pattern = r'(</div>\s*<a href="[^"]*" class="header-mobile-menu-item">고객지원</a>)'
    mobile_replacement = f'''</div>
      
      <a href="{projects_link}" class="header-mobile-menu-item">시공사례</a>
      
      <a href="{'support/contact.html' if is_root else '../support/contact.html'}" class="header-mobile-menu-item">고객지원</a>'''
    content = re.sub(mobile_pattern, mobile_replacement, content, flags=re.DOTALL)
    
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "업데이트 완료"
    
    return False, "패턴을 찾지 못함"

def process_template(template_dir, template_name):
    """템플릿 디렉토리의 모든 HTML 파일 처리"""
    print(f"\n{'='*60}")
    print(f"📁 {template_name} 처리 중...")
    print(f"{'='*60}")
    
    # 처리할 함수 선택
    if template_name == 'template1':
        process_func = add_projects_to_template1
    elif template_name == 'template2':
        process_func = add_projects_to_template2
    elif template_name == 'template3':
        process_func = add_projects_to_template3
    else:
        print(f"⚠ 알 수 없는 템플릿: {template_name}")
        return 0
    
    # HTML 파일 찾기
    html_files = []
    
    # 루트 index.html
    root_index = template_dir / 'index.html'
    if root_index.exists():
        html_files.append(root_index)
    
    # 서브 디렉토리의 HTML 파일들
    for subdir in ['about', 'solutions', 'support']:
        subdir_path = template_dir / subdir
        if subdir_path.exists():
            html_files.extend(subdir_path.glob('*.html'))
    
    # 각 파일 처리
    updated_count = 0
    for html_file in html_files:
        relative_path = html_file.relative_to(template_dir)
        print(f"\n처리 중: {relative_path}")
        
        success, message = process_func(html_file)
        if success:
            updated_count += 1
            print(f"  ✓ {message}")
        else:
            print(f"  - {message}")
    
    print(f"\n{template_name}: {updated_count}/{len(html_files)}개 파일 업데이트 완료")
    return updated_count

def main():
    """메인 함수"""
    base_dir = Path(__file__).parent / 'web'
    templates = ['template1', 'template2', 'template3']
    
    print("=" * 60)
    print("3개 템플릿에 '시공사례' 메뉴 추가 시작")
    print("=" * 60)
    
    total_updated = 0
    
    for template in templates:
        template_dir = base_dir / template
        
        if not template_dir.exists():
            print(f"\n⚠ {template} 디렉토리를 찾을 수 없습니다.")
            continue
        
        updated = process_template(template_dir, template)
        total_updated += updated
    
    print(f"\n{'='*60}")
    print(f"✅ 전체 작업 완료")
    print(f"   총 {total_updated}개 파일 업데이트")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
