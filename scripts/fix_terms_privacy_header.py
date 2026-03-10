#!/usr/bin/env python3
"""
이용약관과 개인정보처리방침 페이지의 헤더 메뉴를 드롭다운 구조로 수정
"""

from pathlib import Path
import re

# 올바른 헤더 메뉴 구조
correct_header_nav = '''      <nav class="header-nav">
        <ul class="header-menu">
          <li class="header-dropdown">
            <a href="pages/about/company.html" class="header-menu-item">회사소개</a>
            <ul class="header-dropdown-menu">
              <li><a href="pages/about/company.html" class="header-dropdown-item">회사소개</a></li>
              <li><a href="pages/about/ceo-message.html" class="header-dropdown-item">인사말</a></li>
              <li><a href="pages/about/history.html" class="header-dropdown-item">회사연혁</a></li>
              <li><a href="pages/about/safety-policy.html" class="header-dropdown-item">안전보건 경영방침과 목표</a></li>
              <li><a href="pages/about/location.html" class="header-dropdown-item">오시는 길</a></li>
            </ul>
          </li>
          <li class="header-dropdown">
            <a href="#" class="header-menu-item">제품 솔루션</a>
            <ul class="header-dropdown-menu">
              <li><a href="pages/solutions/one-stop-solution.html" class="header-dropdown-item">원스탑 산업관리 스마트 솔루션</a></li>
              <li><a href="pages/solutions/ai-surveillance.html" class="header-dropdown-item">AI 영상 방송 관제 시스템</a></li>
              <li><a href="pages/solutions/smart-safety.html" class="header-dropdown-item">스마트 건설현장 안전 플랫폼</a></li>
              <li><a href="pages/solutions/tower-crane.html" class="header-dropdown-item">타워크레인 통합 안전 시스템</a></li>
              <li><a href="pages/solutions/access-control.html" class="header-dropdown-item">스마트 출입통제 시스템</a></li>
              <li><a href="pages/solutions/environment-sensor.html" class="header-dropdown-item">스마트 환경센서 시스템</a></li>
            </ul>
          </li>
          <li class="header-dropdown">
            <a href="pages/projects/index.html" class="header-menu-item">시공사례</a>
          </li>
          <li class="header-dropdown">
            <a href="pages/support/remote-support.html" class="header-menu-item">고객지원</a>
            <ul class="header-dropdown-menu">
              <li><a href="pages/support/remote-support.html" class="header-dropdown-item">원격지원</a></li>
              <li><a href="mailto:ok@it-log.co.kr" class="header-dropdown-item">문의하기</a></li>
            </ul>
          </li>
        </ul>
      </nav>'''

def fix_header():
    files = [
        Path('web/dark/terms.html'),
        Path('web/dark/privacy.html')
    ]
    
    for file_path in files:
        if not file_path.exists():
            print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
            continue
        
        content = file_path.read_text(encoding='utf-8')
        
        # 기존 header-nav 부분을 찾아서 교체
        pattern = r'<nav class="header-nav">.*?</nav>'
        
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, correct_header_nav, content, flags=re.DOTALL)
            file_path.write_text(content, encoding='utf-8')
            print(f"✅ 수정: {file_path}")
        else:
            print(f"⚠️  헤더 메뉴를 찾을 수 없습니다: {file_path}")
    
    print("\n✨ 완료!")

if __name__ == '__main__':
    fix_header()
