#!/usr/bin/env python3
"""
Comprehensive sync from dark theme to light theme
Follows the rules in docs/README.md:
1. Copy content structure from dark to light
2. Copy layout/structure changes
3. Keep image paths as-is (don't copy image files)
4. Adjust colors for light theme (CSS variables)
"""

import os
import shutil
import re

def sync_css_files():
    """Sync CSS files from dark to light (excluding variables.css)"""
    css_files = [
        'reset.css',
        'common.css',
        'components.css',
        'header.css',
        'footer.css',
        'pages/home.css',
        'pages/subpage.css',
        'pages/solutions.css'
    ]
    
    synced = []
    
    for css_file in css_files:
        dark_path = f'web/dark/css/{css_file}'
        light_path = f'web/light/css/{css_file}'
        
        if os.path.exists(dark_path):
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(light_path), exist_ok=True)
            
            # Copy file
            shutil.copy2(dark_path, light_path)
            synced.append(css_file)
            print(f"✓ Synced CSS: {css_file}")
        else:
            print(f"✗ Not found: {dark_path}")
    
    return synced

def fix_light_theme_colors():
    """Fix hardcoded dark colors in light theme CSS files"""
    
    fixes = []
    
    # Fix header.css
    header_path = 'web/light/css/header.css'
    if os.path.exists(header_path):
        with open(header_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace dark theme comment
        content = content.replace(
            '/* Header - Dark & Premium Theme */',
            '/* Header - Light & Professional Theme */'
        )
        
        # Replace scrolled background
        content = re.sub(
            r'background: rgba\(10, 10, 10, 0\.95\);',
            'background: rgba(255, 255, 255, 0.95);',
            content
        )
        
        # Replace shadow
        content = re.sub(
            r'box-shadow: 0 2px 16px rgba\(0, 0, 0, 0\.5\);',
            'box-shadow: 0 2px 16px var(--color-line-regular);',
            content
        )
        
        with open(header_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        fixes.append('header.css')
        print(f"✓ Fixed colors: header.css")
    
    # Fix footer.css
    footer_path = 'web/light/css/footer.css'
    if os.path.exists(footer_path):
        with open(footer_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace dark theme comment
        content = content.replace(
            '/* Footer - Dark & Premium Theme',
            '/* Footer - Light & Professional Theme'
        )
        
        # Replace background gradient
        content = re.sub(
            r'background: linear-gradient\(135deg, #0a0a0a 0%, #1a1a1a 100%\);',
            'background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);',
            content
        )
        
        # Replace border
        content = re.sub(
            r'border-top: 1px solid rgba\(255, 255, 255, 0\.1\);',
            'border-top: 1px solid var(--color-line-regular);',
            content
        )
        
        with open(footer_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        fixes.append('footer.css')
        print(f"✓ Fixed colors: footer.css")
    
    # Fix subpage.css (timeline-tabs background)
    subpage_path = 'web/light/css/pages/subpage.css'
    if os.path.exists(subpage_path):
        with open(subpage_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace timeline-tabs background
        content = re.sub(
            r'background: rgb\(10, 10, 10\);',
            'background: rgb(255, 255, 255);',
            content
        )
        
        with open(subpage_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        fixes.append('subpage.css')
        print(f"✓ Fixed colors: subpage.css")
    
    return fixes

def sync_js_files():
    """Sync JavaScript files from dark to light"""
    js_files = [
        'main.js',
        'utils.js',
        'components.js'
    ]
    
    synced = []
    
    for js_file in js_files:
        dark_path = f'web/dark/js/{js_file}'
        light_path = f'web/light/js/{js_file}'
        
        if os.path.exists(dark_path):
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(light_path), exist_ok=True)
            
            # Copy file
            shutil.copy2(dark_path, light_path)
            synced.append(js_file)
            print(f"✓ Synced JS: {js_file}")
        else:
            print(f"✗ Not found: {dark_path}")
    
    return synced

def sync_html_structure():
    """Sync HTML structure changes (ai-surveillance_2.html)"""
    
    # Check if ai-surveillance_2.html exists in dark theme
    dark_file = 'web/dark/pages/solutions/ai-surveillance_2.html'
    light_file = 'web/light/pages/solutions/ai-surveillance_2.html'
    
    if os.path.exists(dark_file):
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(light_file), exist_ok=True)
        
        # Copy file
        shutil.copy2(dark_file, light_file)
        print(f"✓ Synced HTML: ai-surveillance_2.html")
        return True
    else:
        print(f"✗ Not found: {dark_file}")
        return False

def main():
    print("=" * 60)
    print("다크 테마 → 라이트 테마 포괄적 동기화")
    print("=" * 60)
    print()
    
    print("📋 규칙:")
    print("  1. 내용 구성: 다크 테마와 동일하게 복제")
    print("  2. 레이아웃/구조: 다크 테마와 동일하게 복제")
    print("  3. 색상/스타일: 라이트 테마에 맞게 조정")
    print("  4. 이미지 경로: 그대로 복제 (파일은 복제 안 함)")
    print()
    
    print("=" * 60)
    print("1단계: CSS 파일 동기화")
    print("=" * 60)
    css_synced = sync_css_files()
    print()
    
    print("=" * 60)
    print("2단계: 라이트 테마 색상 수정")
    print("=" * 60)
    color_fixes = fix_light_theme_colors()
    print()
    
    print("=" * 60)
    print("3단계: JavaScript 파일 동기화")
    print("=" * 60)
    js_synced = sync_js_files()
    print()
    
    print("=" * 60)
    print("4단계: HTML 구조 동기화")
    print("=" * 60)
    html_synced = sync_html_structure()
    print()
    
    print("=" * 60)
    print("📊 동기화 완료 요약")
    print("=" * 60)
    print(f"✓ CSS 파일: {len(css_synced)}개")
    print(f"✓ 색상 수정: {len(color_fixes)}개")
    print(f"✓ JS 파일: {len(js_synced)}개")
    print(f"✓ HTML 파일: {'1개' if html_synced else '0개'}")
    print()
    print("⚠️  참고:")
    print("  - variables.css는 동기화되지 않음 (테마별 색상 변수)")
    print("  - 이미지 파일은 복제되지 않음 (경로만 복사)")
    print("  - 추가 색상 조정이 필요할 수 있음")
    print()

if __name__ == '__main__':
    main()
