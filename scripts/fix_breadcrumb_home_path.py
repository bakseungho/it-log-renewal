#!/usr/bin/env python3
"""
브레드크럼브 홈 링크 경로 수정
pages/about/, pages/solutions/, pages/support/, pages/projects/ 하위 파일에서
href="../index.html" → href="../../index.html" 로 수정
(page-header-breadcrumb 내부의 홈 링크만 대상)
"""

import os
import glob

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # breadcrumb 내 홈 링크: ../index.html → ../../index.html
    # 이미 ../../index.html인 경우는 건드리지 않음
    content = content.replace(
        'page-header-breadcrumb">\n        <a href="../index.html">',
        'page-header-breadcrumb">\n        <a href="../../index.html">'
    )
    # certifications 등 breadcrumb-item 패턴
    content = content.replace(
        '<a href="../index.html" class="breadcrumb-item">',
        '<a href="../../index.html" class="breadcrumb-item">'
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  Fixed: {filepath}')
        return True
    else:
        print(f'  Skipped: {filepath}')
        return False

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    patterns = [
        os.path.join(base_dir, 'web', 'dark', 'pages', '**', '*.html'),
        os.path.join(base_dir, 'web', 'light', 'pages', '**', '*.html'),
    ]
    
    updated = 0
    total = 0
    
    for pattern in patterns:
        files = glob.glob(pattern, recursive=True)
        for filepath in sorted(files):
            total += 1
            if fix_file(filepath):
                updated += 1
    
    print(f'\nDone: {updated}/{total} files fixed.')

if __name__ == '__main__':
    main()
