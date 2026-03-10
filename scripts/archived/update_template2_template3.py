#!/usr/bin/env python3
"""
template2와 template3의 서브페이지에 시공사례 메뉴 추가
"""

import re
from pathlib import Path

def update_template2_files():
    """Template2의 모든 서브페이지 업데이트"""
    base_dir = Path('web/template2')
    
    # 데스크톱 패턴
    desktop_pattern = r'(</ul>\s*</li>\s*<li class="nav-item">\s*<a href="#" class="nav-link">\s*고객지원)'
    desktop_replacement = '''</ul>
          </li>

          <li class="nav-item">
            <a href="../index.html#projects" class="nav-link">시공사례</a>
          </li>
          
          <li class="nav-item">
            <a href="#" class="nav-link">
              고객지원'''
    
    # 모바일 패턴
    mobile_pattern = r'(</ul>\s*</li>\s*<li class="mobile-nav-item">\s*<div class="mobile-nav-link">\s*고객지원)'
    mobile_replacement = '''</ul>
      </li>
      
      <li class="mobile-nav-item">
        <a href="../index.html#projects" class="mobile-nav-link">시공사례</a>
      </li>
      
      <li class="mobile-nav-item">
        <div class="mobile-nav-link">
          고객지원'''
    
    updated = 0
    for subdir in ['about', 'solutions', 'support']:
        subdir_path = base_dir / subdir
        if not subdir_path.exists():
            continue
            
        for html_file in subdir_path.glob('*.html'):
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if '시공사례' in content:
                print(f"  - {html_file.name}: 이미 존재")
                continue
            
            original = content
            content = re.sub(desktop_pattern, desktop_replacement, content, flags=re.DOTALL)
            content = re.sub(mobile_pattern, mobile_replacement, content, flags=re.DOTALL)
            
            if content != original:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✓ {html_file.name}: 업데이트 완료")
                updated += 1
            else:
                print(f"  ⚠ {html_file.name}: 패턴 찾지 못함")
    
    return updated

def update_template3_files():
    """Template3의 모든 서브페이지 업데이트"""
    base_dir = Path('web/template3')
    
    # 데스크톱 패턴
    desktop_pattern = r'(</ul>\s*</li>\s*<li class="header-dropdown">\s*<a href="[^"]*" class="header-menu-item">고객지원</a>)'
    desktop_replacement = '''</ul>
          </li>
          <li class="header-dropdown">
            <a href="../index.html#projects" class="header-menu-item">시공사례</a>
          </li>
          <li class="header-dropdown">
            <a href="../support/contact.html" class="header-menu-item">고객지원</a>'''
    
    # 모바일 패턴
    mobile_pattern = r'(</div>\s*<a href="[^"]*" class="header-mobile-menu-item">고객지원</a>)'
    mobile_replacement = '''</div>
      
      <a href="../index.html#projects" class="header-mobile-menu-item">시공사례</a>
      
      <a href="../support/contact.html" class="header-mobile-menu-item">고객지원</a>'''
    
    updated = 0
    for subdir in ['about', 'solutions', 'support']:
        subdir_path = base_dir / subdir
        if not subdir_path.exists():
            continue
            
        for html_file in subdir_path.glob('*.html'):
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if '시공사례' in content:
                print(f"  - {html_file.name}: 이미 존재")
                continue
            
            original = content
            content = re.sub(desktop_pattern, desktop_replacement, content, flags=re.DOTALL)
            content = re.sub(mobile_pattern, mobile_replacement, content, flags=re.DOTALL)
            
            if content != original:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✓ {html_file.name}: 업데이트 완료")
                updated += 1
            else:
                print(f"  ⚠ {html_file.name}: 패턴 찾지 못함")
    
    return updated

def main():
    print("=" * 60)
    print("Template2와 Template3 서브페이지 업데이트")
    print("=" * 60)
    
    print("\n📁 Template2 처리 중...")
    t2_updated = update_template2_files()
    print(f"Template2: {t2_updated}개 파일 업데이트 완료")
    
    print("\n📁 Template3 처리 중...")
    t3_updated = update_template3_files()
    print(f"Template3: {t3_updated}개 파일 업데이트 완료")
    
    print(f"\n{'='*60}")
    print(f"✅ 전체 작업 완료: 총 {t2_updated + t3_updated}개 파일 업데이트")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
