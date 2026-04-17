import glob, os

base = os.path.dirname(os.path.abspath(__file__))
files = glob.glob(os.path.join(base, '**/*.html'), recursive=True)

replacements = [
    ('>원스탑 솔루션</a>', '>원스탑 산업관리 스마트 솔루션</a>'),
    ('>AI 영상 관제</a>', '>AI 영상 방송 관제 시스템</a>'),
    ('>타워크레인</a>', '>타워크레인 통합안전 시스템</a>'),
    ('>출입통제</a>', '>스마트 출입통제 시스템</a>'),
    ('>환경센서</a>', '>스마트 환경센서 시스템</a>'),
]

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    original = content
    for old, new in replacements:
        # footer-sitemap-link 내에서만 치환
        content = content.replace(f'class="footer-sitemap-link"{old}', f'class="footer-sitemap-link"{new}')
    if content != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print(f'✅ {os.path.relpath(f, base)}')

print('\n완료!')
