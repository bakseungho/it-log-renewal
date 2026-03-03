# Web Templates

이 폴더는 웹사이트 템플릿을 포함합니다.

## 폴더 구조

```
web/
└── template1/          # 메인 웹사이트 (아이티로그 홈페이지)
    ├── index.html      # 메인 페이지
    ├── 404.html        # 에러 페이지
    ├── terms.html      # 이용약관
    ├── privacy.html    # 개인정보처리방침
    ├── robots.txt      # 검색엔진 크롤링 규칙
    ├── sitemap.xml     # 사이트맵
    ├── about/          # 회사소개 페이지 (5개)
    ├── solutions/      # 솔루션 페이지 (5개)
    ├── support/        # 고객지원 페이지 (2개)
    ├── pages/          # 추가 페이지
    └── assets/         # 정적 리소스 (CSS, JS, 이미지)
```

## Template1 - 아이티로그 홈페이지

### 개요
- **프로젝트**: (주)아이티로그 홈페이지 리뉴얼
- **타입**: B2B 건설 현장 안전 솔루션 웹사이트
- **기술**: HTML5, CSS3, JavaScript (ES6+)
- **완료 상태**: 95% (배포 대기)

### 페이지 목록 (15개)
1. 메인 페이지 (index.html)
2. 회사소개 (about/company.html)
3. CEO 인사말 (about/ceo-message.html)
4. 회사연혁 (about/history.html)
5. 인증 및 특허 (about/certifications.html)
6. 오시는 길 (about/location.html)
7. 스마트 현장안전 시스템 (solutions/smart-safety.html)
8. 타워크레인 통합안전 시스템 (solutions/tower-crane.html)
9. AI 영상 방송 관제시스템 (solutions/ai-surveillance.html)
10. 스마트 환경센서 시스템 (solutions/environment-sensor.html)
11. 스마트 출입통제 시스템 (solutions/access-control.html)
12. 원격지원 (support/remote-support.html)
13. 문의하기 (support/contact.html)
14. 이용약관 (terms.html)
15. 개인정보처리방침 (privacy.html)

### 주요 기능
- ✅ 반응형 디자인 (모바일/태블릿/데스크톱)
- ✅ 접근성 준수 (WCAG 2.1 AA)
- ✅ SEO 최적화
- ✅ Hero 슬라이더 (Swiper.js)
- ✅ 통계 카운터 (CountUp.js)
- ✅ 스크롤 애니메이션 (AOS)
- ✅ 이미지 라이트박스 (GLightbox)
- ✅ 지도 (Kakao Map API)

### 로컬 실행 방법

```bash
# template1 폴더로 이동
cd template1

# Python 서버 실행
python -m http.server 8000

# 브라우저에서 확인
# http://localhost:8000
```

### 배포 전 필수 작업
1. Kakao Map API 키 설정 (about/location.html)
2. 문의 폼 API 연동 (support/contact.html)
3. 실제 이미지 교체 (고객사 로고, CEO 사진, 인증서 등)
4. 회사 정보 업데이트 (주소, 전화번호, 이메일)
5. 이용약관/개인정보처리방침 법무팀 검토

### 관련 문서
- 프로젝트 개요: `/README.md`
- 설정 가이드: `/SETUP.md`
- 개발 로그: `/DEVELOPMENT-LOG.md`
- 기획/디자인 문서: `/docs/`

---

## 향후 템플릿 추가 계획

이 폴더에 추가 웹사이트 템플릿을 추가할 수 있습니다:

```
web/
├── template1/    # 아이티로그 홈페이지 (현재)
├── template2/    # 향후 추가 템플릿
└── template3/    # 향후 추가 템플릿
```

각 템플릿은 독립적으로 관리되며, 자체 README.md를 포함해야 합니다.
