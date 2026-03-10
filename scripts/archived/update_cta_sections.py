#!/usr/bin/env python3
"""
모든 서브페이지의 CTA 섹션을 통일된 내용으로 수정하는 스크립트
"""

import re
from pathlib import Path

def update_cta_section(file_path):
    """CTA 섹션을 통일된 내용으로 교체"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # CTA 섹션 찾기 (contact-section 또는 solution-cta)
    # 패턴: <section class="contact-section"> 또는 <section class="solution-cta">
    # 부터 </section>까지
    
    # 새로운 CTA 섹션 HTML
    new_cta = '''  <!-- CTA Section -->
  <section class="contact-section">
    <div class="container">
      <h2 class="contact-title">안전을 위한 기술, 고객의 만족을 실현합니다.</h2>
      <p class="contact-description">더 스마트하고 안전한 인프라, 지금 영업팀에 문의하여 귀사만의 맞춤형 솔루션을 설계하세요.</p>
      <div class="contact-actions">
        <a href="mailto:ok@it-log.co.kr" class="btn btn-primary btn-lg">문의하기</a>
      </div>
    </div>
  </section>'''
    
    # 패턴 1: contact-section
    pattern1 = r'<section class="contact-section">.*?</section>'
    if re.search(pattern1, content, re.DOTALL):
        content = re.sub(pattern1, new_cta, content, flags=re.DOTALL)
    
    # 패턴 2: solution-cta
    pattern2 = r'<section class="solution-cta">.*?</section>'
    if re.search(pattern2, content, re.DOTALL):
        content = re.sub(pattern2, new_cta, content, flags=re.DOTALL)
    
    # 변경사항이 있는 경우에만 파일 저장
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """메인 실행 함수"""
    template3_dir = Path('web/template3')
    
    # 처리할 HTML 파일 목록
    html_files = []
    
    # 서브페이지들
    subdirs = ['about', 'solutions', 'support', 'projects']
    for subdir in subdirs:
        subdir_path = template3_dir / subdir
        if subdir_path.exists():
            html_files.extend(subdir_path.glob('*.html'))
    
    updated_count = 0
    
    print("CTA 섹션 업데이트 시작...\n")
    
    for file_path in html_files:
        if file_path.exists():
            if update_cta_section(file_path):
                print(f"✓ Updated: {file_path}")
                updated_count += 1
            else:
                print(f"  Skipped: {file_path} (CTA 섹션 없음 또는 변경사항 없음)")
    
    print(f"\n완료: {updated_count}개 파일이 업데이트되었습니다.")
    print("\n새로운 CTA 내용:")
    print("- 타이틀: 안전을 위한 기술, 고객의 만족을 실현합니다.")
    print("- 설명: 더 스마트하고 안전한 인프라, 지금 영업팀에 문의하여 귀사만의 맞춤형 솔루션을 설계하세요.")
    print("- 버튼: 문의하기 (mailto:ok@it-log.co.kr)")

if __name__ == '__main__':
    main()
