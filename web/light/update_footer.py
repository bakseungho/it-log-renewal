import glob, os

base = os.path.dirname(os.path.abspath(__file__))
files = glob.glob(os.path.join(base, '**/*.html'), recursive=True)

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    original = content
    # 카피라이트 연도 수정 (footer 내 copyright만 대상)
    content = content.replace(
        'Copyright © 2024 ITLOG. All rights reserved.',
        'Copyright © 2026 ITLOG. All rights reserved.'
    )
    # 사이트맵 링크 텍스트 수정
    content = content.replace('>건설안전 플랫폼</a>', '>건설안전 시스템</a>')
    
    if content != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print(f'✅ {os.path.relpath(f, base)}')

print('\n완료!')
