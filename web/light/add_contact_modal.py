"""모든 서브페이지에 문의하기 모달 + EmailJS CDN 일괄 추가"""
import os, glob

LIGHT_DIR = os.path.dirname(os.path.abspath(__file__))

# privacy.html 경로는 페이지 깊이에 따라 다름
def get_privacy_path(depth):
    return "../" * depth + "privacy.html"

def get_modal_html(privacy_path):
    return f'''
  <!-- Contact Modal -->
  <div class="contact-modal-overlay" id="contactModal" role="dialog" aria-modal="true" aria-labelledby="contactModalTitle">
    <div class="contact-modal">
      <button class="contact-modal-close" id="contactModalClose" aria-label="닫기">&times;</button>
      <h2 class="contact-modal-title" id="contactModalTitle">문의하기</h2>
      <form id="contactForm" class="contact-modal-form">
        <div class="contact-modal-field">
          <label for="contact-subject">제목 <span class="required">*</span></label>
          <input type="text" id="contact-subject" name="subject" required placeholder="문의 제목을 입력해주세요">
        </div>
        <div class="contact-modal-field">
          <label for="contact-name">이름 <span class="required">*</span></label>
          <input type="text" id="contact-name" name="name" required placeholder="이름을 입력해주세요">
        </div>
        <div class="contact-modal-field">
          <label for="contact-phone">전화번호 <span class="required">*</span></label>
          <input type="tel" id="contact-phone" name="phone" required placeholder="010-0000-0000">
        </div>
        <div class="contact-modal-field">
          <label for="contact-email">이메일 <span class="required">*</span></label>
          <input type="email" id="contact-email" name="email" required placeholder="example@email.com">
        </div>
        <div class="contact-modal-field">
          <label for="contact-message">내용 <span class="required">*</span></label>
          <textarea id="contact-message" name="message" rows="5" required placeholder="문의 내용을 입력해주세요"></textarea>
        </div>
        <div class="contact-modal-field contact-modal-agree">
          <label><input type="checkbox" id="contact-agree" required> <a href="{privacy_path}" target="_blank">개인정보처리방침</a>에 동의합니다. <span class="required">*</span></label>
        </div>
        <button type="submit" class="btn btn-primary btn-lg contact-modal-submit" id="contactSubmitBtn">문의하기</button>
      </form>
    </div>
  </div>
'''

EMAILJS_CDN = '  <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>'

# 서브페이지 목록 (index.html 제외 - 이미 적용됨)
html_files = []
for pattern in ["pages/**/*.html"]:
    html_files.extend(glob.glob(os.path.join(LIGHT_DIR, pattern), recursive=True))

# terms.html, privacy.html도 추가
for f in ["terms.html", "privacy.html", "404.html"]:
    fp = os.path.join(LIGHT_DIR, f)
    if os.path.exists(fp):
        html_files.append(fp)

updated = []
skipped = []

for filepath in sorted(html_files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 이미 모달이 있으면 스킵
    if 'contactModal' in content:
        skipped.append(filepath)
        continue
    
    # </footer> 뒤, <!-- Scripts --> 전에 모달 삽입
    if '</footer>' not in content or '<!-- Scripts -->' not in content:
        skipped.append(filepath)
        continue
    
    # 깊이 계산 (light/ 기준)
    rel = os.path.relpath(filepath, LIGHT_DIR)
    depth = rel.count(os.sep)
    privacy_path = get_privacy_path(depth)
    modal_html = get_modal_html(privacy_path)
    
    # <!-- Scripts --> 앞에 모달 삽입
    content = content.replace('  <!-- Scripts -->', modal_html + '  <!-- Scripts -->')
    
    # EmailJS CDN 추가 (<!-- Scripts --> 다음 줄)
    content = content.replace('  <!-- Scripts -->\r\n', f'  <!-- Scripts -->\r\n{EMAILJS_CDN}\r\n')
    content = content.replace('  <!-- Scripts -->\n', f'  <!-- Scripts -->\n{EMAILJS_CDN}\n')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    updated.append(os.path.relpath(filepath, LIGHT_DIR))

print(f"Updated {len(updated)} files:")
for f in updated:
    print(f"  ✅ {f}")
if skipped:
    print(f"\nSkipped {len(skipped)} files (already has modal or no footer/scripts):")
    for f in skipped:
        print(f"  ⏭️  {os.path.relpath(f, LIGHT_DIR)}")
