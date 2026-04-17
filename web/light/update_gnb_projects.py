import glob, os, re

base = os.path.dirname(os.path.abspath(__file__))
files = glob.glob(os.path.join(base, '**/*.html'), recursive=True)

# index.html은 이미 드롭다운이 있으므로 제외
skip = os.path.join(base, 'index.html')

for f in files:
    if f == skip:
        continue
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()

    # 시공사례 링크의 href 추출
    m = re.search(r'<a href="([^"]+)" class="header-menu-item">시공사례</a>\s*</li>', content)
    if not m:
        continue

    href = m.group(1)
    old = m.group(0)
    new = (
        f'<a href="{href}" class="header-menu-item">시공사례</a>\n'
        f'            <ul class="header-dropdown-menu">\n'
        f'              <li><a href="{href}" class="header-dropdown-item">시공사례</a></li>\n'
        f'            </ul>\n'
        f'          </li>'
    )

    if old in content:
        content = content.replace(old, new)
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print(f'✅ {os.path.relpath(f, base)}')

print('\n완료!')
