# (주)아이티로그 홈페이지 리뉴얼 프로젝트

건설 현장 안전 솔루션 전문 기업 (주)아이티로그의 공식 홈페이지 리뉴얼 프로젝트입니다.

## 프로젝트 개요

- **프로젝트명**: (주)아이티로그 홈페이지 리뉴얼
- **기술 스택**: HTML5, CSS3, JavaScript (ES6+)
- **라이브러리**: Swiper.js, CountUp.js, AOS, GLightbox
- **개발 기간**: 8주 (2024)
- **목표**: B2B 건설 현장 안전 솔루션 웹사이트 구축

## 주요 기능

- ✅ 반응형 디자인 (모바일, 태블릿, 데스크톱)
- ✅ 접근성 준수 (WCAG 2.1 AA)
- ✅ SEO 최적화
- ✅ 성능 최적화 (Lighthouse 90+)
- ✅ 4개 슬라이드 Hero 섹션
- ✅ 주요 솔루션 소개 (4개)
- ✅ 실시간 통계 카운터
- ✅ 고객사 및 시공사례 갤러리

## 빠른 시작

### 1. 프로젝트 클론
```bash
git clone [repository-url]
cd renewal2
```

### 2. 로컬 서버 실행
```bash
# web/template1 폴더로 이동
cd web/template1

# Python 3
python -m http.server 8000

# Node.js (http-server)
npx http-server -p 8000
```

### 3. 브라우저에서 확인
```
http://localhost:8000
```

## 프로젝트 구조

```
project-root/
├── .kiro/                 # Kiro 설정 파일
├── .vscode/               # VS Code 설정
├── docs/                  # 프로젝트 문서
│   ├── README.md         # 문서 가이드
│   └── template1/        # Template1 관련 문서 (45개)
│       ├── 기획 문서 (PM)
│       ├── 디자인 문서 (UX)
│       ├── 웹 기획 문서
│       ├── 개발 문서 (Frontend)
│       ├── 테스트 문서
│       └── 완료 보고서
├── web/                   # 웹 템플릿 폴더
│   ├── README.md         # 템플릿 가이드
│   └── template1/        # 메인 웹사이트
│       ├── index.html     # 메인 페이지
│       ├── 404.html       # 에러 페이지
│       ├── terms.html     # 이용약관
│       ├── privacy.html   # 개인정보처리방침
│       ├── robots.txt     # 검색엔진 크롤링 규칙
│       ├── sitemap.xml    # 사이트맵
│       ├── about/         # 회사소개 페이지 (5개)
│       ├── solutions/     # 솔루션 페이지 (5개)
│       ├── support/       # 고객지원 페이지 (2개)
│       ├── pages/         # 추가 페이지
│       └── assets/
│           ├── css/
│           │   ├── reset.css      # CSS 리셋
│           │   ├── variables.css  # CSS 변수 (디자인 토큰)
│           │   ├── common.css     # 공통 스타일
│           │   ├── components.css # 컴포넌트 스타일
│           │   ├── header.css     # 헤더 스타일
│           │   ├── footer.css     # 푸터 스타일
│           │   └── pages/         # 페이지별 스타일
│           ├── js/
│           │   ├── utils.js       # 유틸리티 함수
│           │   ├── components.js  # 컴포넌트 로직
│           │   └── main.js        # 메인 스크립트
│           ├── images/            # 이미지 파일
│           └── fonts/             # 웹폰트 (Pretendard CDN)
├── .gitignore
├── README.md              # 이 파일
├── SETUP.md
├── DEVELOPMENT-LOG.md
├── CHANGELOG.md
└── PROJECT-STRUCTURE.md   # 상세 구조 설명
```

**상세 구조**: [`PROJECT-STRUCTURE.md`](PROJECT-STRUCTURE.md) 참조

## 디자인 시스템

### 색상
- **Primary**: Industrial Blue (#1A4D8F)
- **Accent**: Safety Orange (#FF6B35)
- **Secondary**: Steel Gray (#5A6C7D)

### 타이포그래피
- **폰트**: Pretendard (CDN)
- **크기**: 12px ~ 64px (8단계)
- **굵기**: 400 (Regular), 500 (Medium), 600 (SemiBold), 700 (Bold)

### 브레이크포인트
- **모바일**: < 768px
- **태블릿**: 768px ~ 1023px
- **데스크톱**: ≥ 1024px

## 개발 현황

### ✅ Week 1-2: 공통 요소 및 디자인 시스템 (완료)
- CSS 변수 및 디자인 시스템 구축
- 헤더/푸터 컴포넌트
- 공통 컴포넌트 (버튼, 카드, 폼 등)
- 메인 페이지 HTML 구조
- JavaScript 컴포넌트 로직

### ✅ Week 3-4: 메인 페이지 및 이미지 통합 (완료)
- jQuery CDN 추가
- 이미지 디렉토리 구조 생성
- 임시 로고 SVG 생성
- 플레이스홀더 이미지 설정
- 초기 테스트 수행

### ✅ Week 5-6: 서브페이지 개발 (완료)
- 회사소개 5개 페이지 개발
- 솔루션 5개 페이지 개발
- 고객지원 2개 페이지 개발
- 시공사례 갤러리 (GLightbox)
- 탭/아코디언 컴포넌트

### ✅ Week 7-8: 통합 테스트 및 배포 준비 (완료)
- 전체 15개 페이지 통합 테스트
- 이용약관/개인정보처리방침 페이지 추가
- SEO 최적화 (sitemap.xml, robots.txt)
- 구조화된 데이터 추가 (Schema.org)
- 최종 문서 정리

### 📊 프로젝트 완료 상태: 95% (배포 대기)

## 문서

### 프로젝트 문서
- **프로젝트 구조**: `PROJECT-STRUCTURE.md` - 상세 디렉터리 구조
- **개발 로그**: `DEVELOPMENT-LOG.md` - 8주간의 개발 기록
- **설정 가이드**: `SETUP.md` - 개발 환경 설정
- **변경 이력**: `CHANGELOG.md` - 버전별 변경사항

### Template1 문서 (docs/template1/)
- **문서 가이드**: `docs/README.md` - 문서 구조 및 읽는 순서
- **최종 요약**: `docs/template1/FINAL-SUMMARY.md`
- **기술 명세**: `docs/template1/frontend-technical-spec.md`
- **디자인 핸드오프**: `docs/template1/ux-design-handoff.md`
- **테스트 체크리스트**: `docs/template1/TESTING-CHECKLIST.md`
- **완료 보고서**: `docs/template1/WEEK-7-8-COMPLETION-REPORT.md`

**전체 문서 목록**: [`docs/README.md`](docs/README.md) 참조 (45개 문서)

## 품질 기준

- **Lighthouse Performance**: 90+
- **Lighthouse Accessibility**: 95+
- **Lighthouse Best Practices**: 90+
- **Lighthouse SEO**: 95+
- **WCAG 2.1 AA**: 준수

## 브라우저 지원

- Chrome (최신 2개 버전)
- Firefox (최신 2개 버전)
- Safari (최신 2개 버전)
- Edge (최신 2개 버전)
- iOS Safari (최신 2개 버전)
- Chrome Mobile (최신 2개 버전)

## 라이선스

© 2024 (주)아이티로그. All rights reserved.

## 문의

- **이메일**: info@itlog.co.kr
- **전화**: 02-1234-5678
- **주소**: 서울특별시 강남구 테헤란로 123
