"""서브페이지 문의하기 링크를 모달 열기로 일괄 변경"""
import os, glob, re

LIGHT_DIR = os.path.dirname(os.path.abspath(__file__))

html_files = glob.glob(os.path.join(LIGHT_DIR, "pages/**/*.html"), recursive=True)
# 루트 파일도 포함
for f in ["terms.html", "privacy.html"]:
    fp = os.path.join(LIGHT_DIR, f)
    if os.path.exists(fp):
        html_files.append(fp)

updated = []

for filepath in sorted(html_files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. GNB 드롭다운 문의하기 → 모달 열기
    content = content.replace(
        '<a href="mailto:ok@it-log.co.kr" class="header-dropdown-item">문의하기</a>',
        '<a href="#" class="header-dropdown-item open-contact-modal">문의하기</a>'
    )
    
    # 2. CTA 버튼 문의하기 → 모달 열기 (btn btn-primary btn-lg)
    content = re.sub(
        r'<a href="mailto:ok@it-log\.co\.kr" class="btn btn-primary btn-lg"[^>]*>문의하기</a>',
        '<button type="button" class="btn btn-primary btn-lg open-contact-modal">문의하기</button>',
        content
    )
    
    # 3. 푸터 사이트맵 문의하기도 모달로
    content = content.replace(
        '<a href="mailto:ok@it-log.co.kr" class="footer-sitemap-link">문의하기</a>',
        '<a href="#" class="footer-sitemap-link open-contact-modal">문의하기</a>'
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated.append(os.path.relpath(filepath, LIGHT_DIR))

print(f"Updated {len(updated)} files:")
for f in updated:
    print(f"  ✅ {f}")
