#!/usr/bin/env python3
"""
GNB 메뉴를 renewal_content.md의 사이트맵에 맞게 업데이트하는 스크립트
"""
import os
import re
from pathlib import Path

# 데스크톱 네비게이션 (메인 페이지용 - 상대 경로)
DESKTOP_NAV_MAIN = '''                <!-- Desktop Navigation -->
                <nav class="header__nav" role="navigation" aria-label="주 메뉴">
                    <ul class="nav-list">
                        <li class="nav-list__item">
                            <a href="#" class="nav-list__link nav-list__link--dropdown">
                                회사소개
                                <svg class="dropdown-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                </svg>
                            </a>
                            <ul class="dropdown-menu">
                                <li class="dropdown-menu__item"><a href="about/company.html" class="dropdown-menu__link">회사소개</a></li>
                                <li class="dropdown-menu__item"><a href="about/ceo-message.html" class="dropdown-menu__link">인사말</a></li>
                                <li class="dropdown-menu__item"><a href="about/history.html" class="dropdown-menu__link">회사연혁</a></li>
                                <li class="dropdown-menu__item"><a href="#" class="dropdown-menu__link">안전보건 경영방침과 목표</a></li>
                                <li class="dropdown-menu__item"><a href="about/certifications.html" class="dropdown-menu__link">인증 및 특허</a></li>
                                <li class="dropdown-menu__item"><a href="about/location.html" class="dropdown-menu__link">오시는 길</a></li>
                            </ul>
                        </li>
                        <li class="nav-list__item">
                            <a href="#" class="nav-list__link nav-list__link--dropdown">
                                제품 솔루션
                                <svg class="dropdown-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                </svg>
                            </a>
                            <ul class="dropdown-menu">
                                <li class="dropdown-menu__item"><a href="#" class="dropdown-menu__link">원스탑 산업관리 스마트 솔루션</a></li>
                                <li class="dropdown-menu__item"><a href="solutions/ai-surveillance.html" class="dropdown-menu__link">AI 영상 방송 관제 시스템</a></li>
                                <li class="dropdown-menu__item"><a href="solutions/tower-crane.html" class="dropdown-menu__link">타워크레인 통합 안전 시스템</a></li>
                                <li class="dropdown-menu__item"><a href="solutions/access-control.html" class="dropdown-menu__link">스마트 출입통제 시스템</a></li>
                                <li class="dropdown-menu__item"><a href="solutions/environment-sensor.html" class="dropdown-menu__link">스마트 환경센서 시스템</a></li>
                            </ul>
                        </li>
                        <li class="nav-list__item">
                            <a href="#" class="nav-list__link nav-list__link--dropdown">
                                고객지원
                                <svg class="dropdown-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                </svg>
                            </a>
                            <ul class="dropdown-menu">
                                <li class="dropdown-menu__item"><a href="support/remote-support.html" class="dropdown-menu__link">원격지원</a></li>
                                <li class="dropdown-menu__item"><a href="support/contact.html" class="dropdown-menu__link">문의하기</a></li>
                            </ul>
                        </li>
                    </ul>
                </nav>'''

# 데스크톱 네비게이션 (서브 페이지용 - ../ 경로)
DESKTOP_NAV_SUB = '''                <!-- Desktop Navigation -->
                <nav class="header__nav" role="navigation" aria-label="주 메뉴">
                    <ul class="nav-list">
                        <li class="nav-list__item">
                            <a href="#" class="nav-list__link nav-list__link--dropdown">
                                회사소개
                                <svg class="dropdown-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                </svg>
                            </a>
                            <ul class="dropdown-menu">
                                <li class="dropdown-menu__item"><a href="../about/company.html" class="dropdown-menu__link">회사소개</a></li>
                                <li class="dropdown-menu__item"><a href="../about/ceo-message.html" class="dropdown-menu__link">인사말</a></li>
                                <li class="dropdown-menu__item"><a href="../about/history.html" class="dropdown-menu__link">회사연혁</a></li>
                                <li class="dropdown-menu__item"><a href="#" class="dropdown-menu__link">안전보건 경영방침과 목표</a></li>
                                <li class="dropdown-menu__item"><a href="../about/certifications.html" class="dropdown-menu__link">인증 및 특허</a></li>
                                <li class="dropdown-menu__item"><a href="../about/location.html" class="dropdown-menu__link">오시는 길</a></li>
                            </ul>
                        </li>
                        <li class="nav-list__item">
                            <a href="#" class="nav-list__link nav-list__link--dropdown">
                                제품 솔루션
                                <svg class="dropdown-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                </svg>
                            </a>
                            <ul class="dropdown-menu">
                                <li class="dropdown-menu__item"><a href="#" class="dropdown-menu__link">원스탑 산업관리 스마트 솔루션</a></li>
                                <li class="dropdown-menu__item"><a href="../solutions/ai-surveillance.html" class="dropdown-menu__link">AI 영상 방송 관제 시스템</a></li>
                                <li class="dropdown-menu__item"><a href="../solutions/tower-crane.html" class="dropdown-menu__link">타워크레인 통합 안전 시스템</a></li>
                                <li class="dropdown-menu__item"><a href="../solutions/access-control.html" class="dropdown-menu__link">스마트 출입통제 시스템</a></li>
                                <li class="dropdown-menu__item"><a href="../solutions/environment-sensor.html" class="dropdown-menu__link">스마트 환경센서 시스템</a></li>
                            </ul>
                        </li>
                        <li class="nav-list__item">
                            <a href="#" class="nav-list__link nav-list__link--dropdown">
                                고객지원
                                <svg class="dropdown-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                </svg>
                            </a>
                            <ul class="dropdown-menu">
                                <li class="dropdown-menu__item"><a href="../support/remote-support.html" class="dropdown-menu__link">원격지원</a></li>
                                <li class="dropdown-menu__item"><a href="../support/contact.html" class="dropdown-menu__link">문의하기</a></li>
                            </ul>
                        </li>
                    </ul>
                </nav>'''

# 모바일 네비게이션 (메인 페이지용)
MOBILE_NAV_MAIN = '''        <!-- Mobile Navigation -->
        <div id="mobile-menu" class="mobile-menu js-mobile-menu">
            <div class="mobile-menu__container">
                <nav role="navigation" aria-label="모바일 메뉴">
                    <ul class="mobile-menu__list">
                        <li class="mobile-menu__item">
                            <button class="mobile-menu__link js-mobile-submenu-toggle" aria-expanded="false">
                                회사소개
                                <svg class="mobile-menu__toggle-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                </svg>
                            </button>
                            <div class="mobile-submenu">
                                <ul class="mobile-submenu__list">
                                    <li><a href="about/company.html" class="mobile-submenu__link">회사소개</a></li>
                                    <li><a href="about/ceo-message.html" class="mobile-submenu__link">인사말</a></li>
                                    <li><a href="about/history.html" class="mobile-submenu__link">회사연혁</a></li>
                                    <li><a href="#" class="mobile-submenu__link">안전보건 경영방침과 목표</a></li>
                                    <li><a href="about/certifications.html" class="mobile-submenu__link">인증 및 특허</a></li>
                                    <li><a href="about/location.html" class="mobile-submenu__link">오시는 길</a></li>
                                </ul>
                            </div>
                        </li>
                        <li class="mobile-menu__item">
                            <button class="mobile-menu__link js-mobile-submenu-toggle" aria-expanded="false">
                                제품 솔루션
                                <svg class="mobile-menu__toggle-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                </svg>
                            </button>
                            <div class="mobile-submenu">
                                <ul class="mobile-submenu__list">
                                    <li><a href="#" class="mobile-submenu__link">원스탑 산업관리 스마트 솔루션</a></li>
                                    <li><a href="solutions/ai-surveillance.html" class="mobile-submenu__link">AI 영상 방송 관제 시스템</a></li>
                                    <li><a href="solutions/tower-crane.html" class="mobile-submenu__link">타워크레인 통합 안전 시스템</a></li>
                                    <li><a href="solutions/access-control.html" class="mobile-submenu__link">스마트 출입통제 시스템</a></li>
                                    <li><a href="solutions/environment-sensor.html" class="mobile-submenu__link">스마트 환경센서 시스템</a></li>
                                </ul>
                            </div>
                        </li>
                        <li class="mobile-menu__item">
                            <button class="mobile-menu__link js-mobile-submenu-toggle" aria-expanded="false">
                                고객지원
                                <svg class="mobile-menu__toggle-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                </svg>
                            </button>
                            <div class="mobile-submenu">
                                <ul class="mobile-submenu__list">
                                    <li><a href="support/remote-support.html" class="mobile-submenu__link">원격지원</a></li>
                                    <li><a href="support/contact.html" class="mobile-submenu__link">문의하기</a></li>
                                </ul>
                            </div>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>'''

# 모바일 네비게이션 (서브 페이지용)
MOBILE_NAV_SUB = '''        <!-- Mobile Navigation -->
        <div id="mobile-menu" class="mobile-menu js-mobile-menu">
            <div class="mobile-menu__container">
                <nav role="navigation" aria-label="모바일 메뉴">
                    <ul class="mobile-menu__list">
                        <li class="mobile-menu__item">
                            <button class="mobile-menu__link js-mobile-submenu-toggle" aria-expanded="false">
                                회사소개
                                <svg class="mobile-menu__toggle-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                </svg>
                            </button>
                            <div class="mobile-submenu">
                                <ul class="mobile-submenu__list">
                                    <li><a href="../about/company.html" class="mobile-submenu__link">회사소개</a></li>
                                    <li><a href="../about/ceo-message.html" class="mobile-submenu__link">인사말</a></li>
                                    <li><a href="../about/history.html" class="mobile-submenu__link">회사연혁</a></li>
                                    <li><a href="#" class="mobile-submenu__link">안전보건 경영방침과 목표</a></li>
                                    <li><a href="../about/certifications.html" class="mobile-submenu__link">인증 및 특허</a></li>
                                    <li><a href="../about/location.html" class="mobile-submenu__link">오시는 길</a></li>
                                </ul>
                            </div>
                        </li>
                        <li class="mobile-menu__item">
                            <button class="mobile-menu__link js-mobile-submenu-toggle" aria-expanded="false">
                                제품 솔루션
                                <svg class="mobile-menu__toggle-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                </svg>
                            </button>
                            <div class="mobile-submenu">
                                <ul class="mobile-submenu__list">
                                    <li><a href="#" class="mobile-submenu__link">원스탑 산업관리 스마트 솔루션</a></li>
                                    <li><a href="../solutions/ai-surveillance.html" class="mobile-submenu__link">AI 영상 방송 관제 시스템</a></li>
                                    <li><a href="../solutions/tower-crane.html" class="mobile-submenu__link">타워크레인 통합 안전 시스템</a></li>
                                    <li><a href="../solutions/access-control.html" class="mobile-submenu__link">스마트 출입통제 시스템</a></li>
                                    <li><a href="../solutions/environment-sensor.html" class="mobile-submenu__link">스마트 환경센서 시스템</a></li>
                                </ul>
                            </div>
                        </li>
                        <li class="mobile-menu__item">
                            <button class="mobile-menu__link js-mobile-submenu-toggle" aria-expanded="false">
                                고객지원
                                <svg class="mobile-menu__toggle-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                </svg>
                            </button>
                            <div class="mobile-submenu">
                                <ul class="mobile-submenu__list">
                                    <li><a href="../support/remote-support.html" class="mobile-submenu__link">원격지원</a></li>
                                    <li><a href="../support/contact.html" class="mobile-submenu__link">문의하기</a></li>
                                </ul>
                            </div>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>'''


def update_navigation(file_path, is_main_page=False):
    """HTML 파일의 네비게이션을 업데이트"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 데스크톱 네비게이션 패턴
    desktop_pattern = r'<!-- Desktop Navigation -->.*?</nav>'
    # 모바일 네비게이션 패턴
    mobile_pattern = r'<!-- Mobile Navigation -->.*?</div>\s*</div>'
    
    # 적절한 네비게이션 선택
    desktop_nav = DESKTOP_NAV_MAIN if is_main_page else DESKTOP_NAV_SUB
    mobile_nav = MOBILE_NAV_MAIN if is_main_page else MOBILE_NAV_SUB
    
    # 데스크톱 네비게이션 교체
    content = re.sub(desktop_pattern, desktop_nav, content, flags=re.DOTALL)
    
    # 모바일 네비게이션 교체
    content = re.sub(mobile_pattern, mobile_nav, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated: {file_path}")


def main():
    """메인 실행 함수"""
    base_dir = Path(__file__).parent
    
    # 메인 페이지 업데이트
    update_navigation(base_dir / 'index.html', is_main_page=True)
    
    # 서브 페이지 업데이트
    subdirs = ['about', 'solutions', 'support']
    
    for subdir in subdirs:
        subdir_path = base_dir / subdir
        if subdir_path.exists():
            for html_file in subdir_path.glob('*.html'):
                update_navigation(html_file, is_main_page=False)
    
    print("\n✅ All navigation menus updated successfully!")


if __name__ == '__main__':
    main()
