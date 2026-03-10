#!/usr/bin/env python3
"""
3개 템플릿의 모든 HTML 파일에 '시공사례' 메뉴를 추가하는 스크립트
"""

import os
import re
from pathlib import Path

def update_template1_desktop(content, is_root):
    """Template1 데스크톱 네비게이션 업데이트"""
    projects_link = '#projects' if is_root else '../index.html#projects'
    
    pattern = r'(</ul>\s*</li>\s*<li class="nav-list__item">\s*<a href="#" class="nav-list__link nav-list__link--dropdown">\s*고객지원)'
    
    replacement = f'''</ul>
                        </li>
                        <li class="nav-list__item">
                            <a href="{projects_link}" class="nav-list__link">시공사례</a>
                        </li>
                        <li class="nav-list__item">
                            <a href="#" class="nav-list__link nav-list__link--dropdown">
                                고객지원'''
    
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def update_template1_mobile(content, is_root):
    """Template1 모바일 네비게이션 업데이트"""
    projects_link = '#projects' if is_root else '../index.html#projects'
    
    pattern = r'(</div>\s*</li>\s*<li class="mobile-menu__item">\s*<button class="mobile-menu__link js-mobile-submenu-toggle" aria-expanded="false">\s*고객지원)'
    
    replacement = f'''</div>
                        </li>
                        <li class="mobile-menu__item">
                            <a href="{projects_link}" class="mobile-menu__link">시공사례</a>
                        </li>
                        <li class="mobile-menu__item">
                            <button class="mobile-menu__link js-mobile-submenu-toggle" aria-expanded="false">
                                고객지원'''
    
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def update_template2_desktop(content, is_root):
    """Template2 데스크톱 네비게이션 업데이트"""
    projects_link = '#projects' if is_root else '../index.html#projects'
    
    pattern = r'(</ul>\s*</li>\s*<li class="nav-item">\s*<a href="#" class="nav-link">\s*고객지원)'
    
    replacement = f'''</ul>
          </li>

          <li class="nav-item">
            <a href="{projects_link}" class="nav-link">시공사례</a>
          </li>
          
          <li class="nav-item">
            <a href="#" class="nav-link">
              고객지원'''
    
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def update_template2_mobile(content, is_root):
    """Template2 모바일 네비게이션 업데이트"""
    projects_link = '#projects' if is_root else '../index.html#projects'
    
    pattern = r'(</ul>\s*</li>\s*<li class="mobile-nav-item">\s*<div class="mobile-nav-link">\s*고객지원)'
    
    replacement = f'''</ul>
      </li>
      
      <li class="mobile-nav-item">
        <a href="{projects_link}" class="mobile-nav-link">시공사례</a>
      </li>
      
      <li class="mobile-nav-item">
        <div class="mobile-nav-link">
          고객지원'''
    
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def update_template3_desktop(content, is_root):
    """Template3 데스크톱 네비게이션 업데이트"""
    projects_link = '#projects' if is_root else '../index.html#projects'
    
    pattern = r'(</ul>\s*</li>\s*<li class="header-dropdown">\s*<a href="[^"]*" class="header-menu-item">고객지원</a>)'
    
    replacement = f'''</ul>
          </li>
          <li class="header-dropdown">
            <a href="{projects_link}" class="header-menu-item">시공사례</a>
          </li>
          <li class="header-dropdown">
            <a href="support/contact.html" class="header-menu-item">고객지원</a>'''
    
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def update_template3_mobile(content, is_root):
    """Template3 모바일 네비게이션 업데이트"""
    projects_link = '#projects' if is_root else '../index.html#projects'
    
    pattern = r'(</div>\s*<a href="[^"]*" class="header-mobile-menu-item">고객지원</a>)'
    
    replacement = f'''</div>
      
      <a href="{projects_link}" class="header-mobile-menu-item">시공사례</a>
      
      <a href="support/contact.html" class="header-mobile-menu-item">고객지원</a>'''
    
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def update_desktop_nav(content, template_name, is_root):
    """데스크톱 네비게이션에 시공사례 메뉴 추가"""
    
    # 이미 시공사례가 있는지 확인
    if '시공사례' in content:
        print(f"  ✓ 이미 시공사례 메뉴가 존재합니다.")
        return content
    
    original = content
    
    if template_name == 'template1':
        content = update_template1_desktop(content, is_root)
    elif template_name == 'template2':
        content = update_template2_desktop(content, is_root)
    elif template_name == 'template3':
        content = update_template3_desktop(content, is_root)
    
    if content != original:
        print(f"  ✓ 데스크톱 네비게이션 업데이트 완료")
    else:
        print(f"  ⚠ 데스크톱 네비게이션 패턴을 찾지 못했습니다.")
    
    return content

def update_mobile_nav(content, template_name, is_root):
    """모바일 네비게이션에 시공사례 메뉴 추가"""
    
    # 이미 시공사례가 있는지 확인 (모바일 메뉴 영역에서)
    mobile_menu_section = content[content.find('mobile'):] if 'mobile' in content else content
    if '시공사례' in mobile_menu_section:
        print(f"  ✓ 이미 모바일 시공사례 메뉴가 존재합니다.")
        return content
    
    original = content
    
    if template_name == 'template1':
        content = update_template1_mobile(content, is_root)
    elif template_name == 'template2':
        content = update_template2_mobile(content, is_root)
    elif template_name == 'template3':
        content = update_template3_mobile(content, is_root)
    
    if content != original:
        print(f"  ✓ 모바일 네비게이션 업데이트 완료")
    else:
        print(f"  ⚠ 모바일 네비게이션 패턴을 찾지 못했습니다.")
    
    return content

def process_html_file(file_path, template_name):
    """HTML 파일 처리"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 파일 타입 확인
        is_root = file_path.name == 'index.html' and file_path.parent.name.startswith('template')
        
        original_content = content
        
        # 데스크톱 네비게이션 업데이트
        content = update_desktop_nav(content, template_name, is_root)
        
        # 모바일 네비게이션 업데이트
        content = update_mobile_nav(content, template_name, is_root)
        
        # 변경사항이 있으면 파일 저장
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        else:
            return False
            
    except Exception as e:
        print(f"  ✗ 오류 발생: {e}")
        return False

def main():
    """메인 함수"""
    base_dir = Path(__file__).parent / 'web'
    templates = ['template1', 'template2', 'template3']
    
    print("=" * 60)
    print("3개 템플릿에 '시공사례' 메뉴 추가 시작")
    print("=" * 60)
    
    total_updated = 0
    total_files = 0
    
    for template in templates:
        template_dir = base_dir / template
        
        if not template_dir.exists():
            print(f"\n⚠ {template} 디렉토리를 찾을 수 없습니다.")
            continue
        
        print(f"\n{'='*60}")
        print(f"📁 {template} 처리 중...")
        print(f"{'='*60}")
        
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
        template_updated = 0
        for html_file in html_files:
            relative_path = html_file.relative_to(template_dir)
            print(f"\n처리 중: {relative_path}")
            
            if process_html_file(html_file, template):
                template_updated += 1
                print(f"  ✓ 업데이트 완료")
            else:
                print(f"  - 변경사항 없음")
            
            total_files += 1
        
        total_updated += template_updated
        print(f"\n{template}: {template_updated}개 파일 업데이트 완료")
    
    print(f"\n{'='*60}")
    print(f"✅ 전체 작업 완료")
    print(f"   총 {total_files}개 파일 중 {total_updated}개 파일 업데이트")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
