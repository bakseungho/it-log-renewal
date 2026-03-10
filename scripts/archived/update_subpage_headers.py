#!/usr/bin/env python3
"""
서브페이지 헤더 레이아웃을 새로운 구조로 변경하는 스크립트
- 큰 배경 이미지 제거
- 브레드크럼브 → 타이틀 → 서브문구 → 배경 이미지 순서로 변경
"""

import os
import re
from pathlib import Path

# 페이지 정보 (경로, 브레드크럼브, 타이틀, 서브문구)
PAGES = {
    'about/company.html': {
        'breadcrumb': ['Home', '회사소개', '회사소개'],
        'title': '기술과 신뢰로 안전을 만듭니다',
        'description': '건설 현장 스마트 안전 솔루션 전문 기업',
        'image': '../images/about/company-bg.jpg'
    },
    'about/ceo-message.html': {
        'breadcrumb': ['Home', '회사소개', '인사말'],
        'title': 'CEO 인사말',
        'description': '안전한 건설 현장을 위한 아이티로그의 약속',
        'image': '../images/about/ceo-bg.jpg'
    },
    'about/history.html': {
        'breadcrumb': ['Home', '회사소개', '회사연혁'],
        'title': '회사연혁',
        'description': '16년간 쌓아온 기술력과 신뢰의 역사',
        'image': '../images/about/history-bg.jpg'
    },
    'about/safety-policy.html': {
        'breadcrumb': ['Home', '회사소개', '안전보건 경영방침과 목표'],
        'title': '안전보건 경영방침과 목표',
        'description': '안전을 최우선으로 하는 아이티로그의 경영 철학',
        'image': '../images/about/safety-bg.jpg'
    },
    'about/location.html': {
        'breadcrumb': ['Home', '회사소개', '오시는 길'],
        'title': '오시는 길',
        'description': '아이티로그 본사 위치 안내',
        'image': '../images/about/location-bg.jpg'
    },
    'solutions/one-stop-solution.html': {
        'breadcrumb': ['Home', '제품 솔루션', '원스탑 산업관리 스마트 솔루션'],
        'title': '원스탑 산업관리 스마트 솔루션',
        'description': '건설 현장의 모든 안전 시스템을 하나로 통합',
        'image': '../images/solutions/onestop-bg.jpg'
    },
    'solutions/ai-surveillance.html': {
        'breadcrumb': ['Home', '제품 솔루션', 'AI 영상 방송 관제 시스템'],
        'title': 'AI 영상 방송 관제 시스템',
        'description': '실시간 위험 감지 및 즉각 대응 시스템',
        'image': '../images/solutions/ai-bg.jpg'
    },
    'solutions/smart-safety.html': {
        'breadcrumb': ['Home', '제품 솔루션', '스마트 건설현장 안전 플랫폼'],
        'title': '스마트 건설현장 안전 플랫폼',
        'description': '안전교육부터 방문자 관리까지 통합 플랫폼',
        'image': '../images/solutions/safety-bg.jpg'
    },
    'solutions/tower-crane.html': {
        'breadcrumb': ['Home', '제품 솔루션', '타워크레인 통합 안전 시스템'],
        'title': '타워크레인 통합 안전 시스템',
        'description': '타워크레인 작업의 안전성을 극대화하는 통합 솔루션',
        'image': '../images/solutions/crane-bg.jpg'
    },
    'solutions/access-control.html': {
        'breadcrumb': ['Home', '제품 솔루션', '스마트 출입통제 시스템'],
        'title': '스마트 출입통제 시스템',
        'description': '안면인식 기반 출입 관리 및 통합 차량 관제',
        'image': '../images/solutions/access-bg.jpg'
    },
    'solutions/environment-sensor.html': {
        'breadcrumb': ['Home', '제품 솔루션', '스마트 환경센서 시스템'],
        'title': '스마트 환경센서 시스템',
        'description': '미세먼지, 소음, 온습도 등 실시간 환경 모니터링',
        'image': '../images/solutions/sensor-bg.jpg'
    },
    'projects/index.html': {
        'breadcrumb': ['Home', '시공사례'],
        'title': '주요 시공사례',
        'description': '대한민국 대표 건설사와 함께한 프로젝트',
        'image': '../images/projects/projects-bg.jpg'
    },
    'support/remote-support.html': {
        'breadcrumb': ['Home', '고객지원', '원격지원'],
        'title': '원격지원',
        'description': '신속하고 정확한 원격 기술 지원 서비스',
        'image': '../images/support/remote-bg.jpg'
    },
    'support/contact.html': {
        'breadcrumb': ['Home', '고객지원', '문의하기'],
        'title': '문의하기',
        'description': '궁금하신 사항을 남겨주시면 빠르게 답변드리겠습니다',
        'image': '../images/support/contact-bg.jpg'
    }
}

def create_new_header(page_info):
    """새로운 헤더 HTML 생성"""
    breadcrumb_items = page_info['breadcrumb']
    breadcrumb_html = []
    
    for i, item in enumerate(breadcrumb_items):
        if i == 0:
            breadcrumb_html.append(f'<a href="../index.html">{item}</a>')
        elif i == len(breadcrumb_items) - 1:
            breadcrumb_html.append(f'<span class="active">{item}</span>')
        else:
            breadcrumb_html.append(f'<span>{item}</span>')
        
        if i < len(breadcrumb_items) - 1:
            breadcrumb_html.append('<span class="separator">></span>')
    
    breadcrumb_str = '\n        '.join(breadcrumb_html)
    
    return f'''  <!-- Page Header -->
  <section class="page-header">
    <div class="page-header-content">
      <div class="page-header-breadcrumb">
        {breadcrumb_str}
      </div>
      <h1 class="page-header-title">{page_info['title']}</h1>
      <p class="page-header-description">{page_info['description']}</p>
      <div class="page-header-image">
        <img src="{page_info['image']}" alt="{page_info['title']}">
      </div>
    </div>
  </section>'''

def update_page(file_path, page_info):
    """페이지 헤더 업데이트"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 기존 Page Header와 Breadcrumb 섹션 찾기 및 제거
    # Page Header 섹션 제거
    pattern1 = r'  <!-- Page Header -->.*?</section>'
    content = re.sub(pattern1, '', content, flags=re.DOTALL)
    
    # Breadcrumb 섹션 제거
    pattern2 = r'  <!-- Breadcrumb -->.*?</section>'
    content = re.sub(pattern2, '', content, flags=re.DOTALL)
    
    # 새로운 헤더 삽입 (</header> 다음에)
    new_header = create_new_header(page_info)
    content = content.replace('</header>', f'</header>\n\n{new_header}')
    
    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ Updated: {file_path}')

def main():
    base_dir = Path('web/template3')
    
    for page_path, page_info in PAGES.items():
        file_path = base_dir / page_path
        if file_path.exists():
            update_page(file_path, page_info)
        else:
            print(f'✗ Not found: {file_path}')
    
    print('\n모든 서브페이지 헤더 업데이트 완료!')

if __name__ == '__main__':
    main()
