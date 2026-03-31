#!/usr/bin/env python3
"""
모든 페이지의 footer 레이아웃을 수정하는 스크립트
1. CI 로고 이미지 길이 140px
2. footer-bottom 요소 제거
3. 주소 위에 이용약관, 개인정보처리방침 메뉴 이동
4. 이메일 주소 아래 저작권 문구 적용
"""

import re
from pathlib import Path

def update_footer(file_path):
    """Footer 레이아웃 수정"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 상대 경로 계산
    depth = len(Path(file_path).relative_to('web/template3').parts) - 1
    prefix = '../' * depth if depth > 0 else ''
    
    # 새로운 footer HTML
    new_footer = f'''  <!-- Footer -->
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-content">
        <div class="footer-info">
          <img src="{prefix}images/common/footer_logo.png" alt="아이티로그" class="footer-logo">
          <p class="footer-company-name">(주)아이티로그</p>
          <div class="footer-policy-links">
            <a href="{prefix}terms.html" class="footer-policy-link">이용약관</a>
            <span class="footer-policy-separator">|</span>
            <a href="{prefix}privacy.html" class="footer-policy-link">개인정보처리방침</a>
          </div>
          <div class="footer-details">
            <p><strong>주소:</strong> 서울특별시 구로구 디지털로33길 28 우림이비즈센터 1차 308호</p>
            <p><strong>이메일:</strong> ok@it-log.co.kr</p>
            <p class="footer-copyright">Copyright © 2024 ITLOG. All rights reserved.</p>
          </div>
        </div>
        
        <div class="footer-sitemap">
          <div class="footer-sitemap-column">
            <h3 class="footer-sitemap-title">회사소개</h3>
            <a href="{prefix}about/company.html" class="footer-sitemap-link">회사소개</a>
            <a href="{prefix}about/ceo-message.html" class="footer-sitemap-link">인사말</a>
            <a href="{prefix}about/history.html" class="footer-sitemap-link">회사연혁</a>
            <a href="{prefix}about/safety-policy.html" class="footer-sitemap-link">안전보건 경영방침</a>
            <a href="{prefix}about/location.html" class="footer-sitemap-link">오시는 길</a>
          </div>
          
          <div class="footer-sitemap-column">
            <h3 class="footer-sitemap-title">제품 솔루션</h3>
            <a href="{prefix}solutions/one-stop-solution.html" class="footer-sitemap-link">원스탑 솔루션</a>
            <a href="{prefix}solutions/ai-surveillance.html" class="footer-sitemap-link">AI 영상 관제</a>
            <a href="{prefix}solutions/smart-safety.html" class="footer-sitemap-link">건설안전 플랫폼</a>
            <a href="{prefix}solutions/tower-crane.html" class="footer-sitemap-link">타워크레인</a>
            <a href="{prefix}solutions/access-control.html" class="footer-sitemap-link">출입통제</a>
            <a href="{prefix}solutions/environment-sensor.html" class="footer-sitemap-link">환경센서</a>
          </div>
          
          <div class="footer-sitemap-column">
            <h3 class="footer-sitemap-title">시공사례</h3>
            <a href="{prefix}projects/index.html" class="footer-sitemap-link">시공사례</a>
          </div>
          
          <div class="footer-sitemap-column">
            <h3 class="footer-sitemap-title">고객지원</h3>
            <a href="{prefix}support/remote-support.html" class="footer-sitemap-link">원격지원</a>
            <a href="mailto:ok@it-log.co.kr" class="footer-sitemap-link">문의하기</a>
          </div>
        </div>
      </div>
    </div>
  </footer>'''
    
    # footer 전체를 교체
    pattern = r'<footer class="footer">.*?</footer>'
    content = re.sub(pattern, new_footer, content, flags=re.DOTALL)
    
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
    
    # 메인 페이지
    html_files.append(template3_dir / 'index.html')
    
    # 기타 루트 페이지들
    for file in ['404.html', 'privacy.html', 'terms.html']:
        file_path = template3_dir / file
        if file_path.exists():
            html_files.append(file_path)
    
    # 서브페이지들
    subdirs = ['about', 'solutions', 'support', 'projects']
    for subdir in subdirs:
        subdir_path = template3_dir / subdir
        if subdir_path.exists():
            html_files.extend(subdir_path.glob('*.html'))
    
    updated_count = 0
    
    print("Footer 레이아웃 업데이트 시작...\n")
    
    for file_path in html_files:
        if file_path.exists():
            if update_footer(file_path):
                print(f"✓ Updated: {file_path}")
                updated_count += 1
            else:
                print(f"  Skipped: {file_path} (변경사항 없음)")
    
    print(f"\n완료: {updated_count}개 파일이 업데이트되었습니다.")
    print("\nFooter 변경사항:")
    print("1. CI 로고 이미지 길이 140px")
    print("2. footer-bottom 요소 제거")
    print("3. 주소 위에 이용약관, 개인정보처리방침 메뉴 이동")
    print("4. 이메일 주소 아래 저작권 문구 적용")

if __name__ == '__main__':
    main()
