# (주)아이티로그 홈페이지 리뉴얼 프로젝트

건설 현장 안전 솔루션 전문 기업 (주)아이티로그의 공식 홈페이지 리뉴얼 프로젝트입니다.

## 프로젝트 개요

- **프로젝트명**: (주)아이티로그 홈페이지 리뉴얼
- **기술 스택**: HTML5, CSS3, JavaScript (ES6+)
- **라이브러리**: Swiper.js, GSAP, ScrollTrigger
- **개발 기간**: 2024
- **목표**: B2B 건설 현장 안전 솔루션 웹사이트 구축

## 주요 기능

- ✅ 반응형 디자인 (모바일, 태블릿, 데스크톱)
- ✅ 접근성 준수 (WCAG 2.1 AAA)
- ✅ SEO 최적화
- ✅ 성능 최적화
- ✅ 4개 슬라이드 Hero 섹션 (자동재생/정지 기능)
- ✅ 주요 솔루션 소개
- ✅ 실시간 통계 카운터
- ✅ 스크롤 애니메이션 (GSAP)
- ✅ 다크/라이트 모드 지원

## 빠른 시작

### 1. 프로젝트 클론
```bash
git clone [repository-url]
cd renewal2
```

### 2. 로컬 서버 실행
```bash
# 다크 모드
cd web/dark
python -m http.server 8000

# 라이트 모드
cd web/light
python -m http.server 8000
```

### 3. 브라우저에서 확인
```
http://localhost:8000
```

## 프로젝트 구조

```
renewal2/
├── web/
│   ├── light/              # 라이트 모드 템플릿
│   └── dark/               # 다크 모드 템플릿
├── docs/                   # 프로젝트 문서
│   ├── README.md
│   ├── renewal_content.md
│   └── template1/          # 템플릿 문서
├── scripts/                # 유틸리티 스크립트
│   ├── completed/          # 최근 완료된 스크립트
│   └── archived/           # 과거 스크립트 보관
├── .kiro/                  # AI 에이전트 설정
│   └── agents/             # 커스텀 에이전트
├── README.md               # 이 파일
├── SETUP.md                # 설치 가이드
└── PROJECT-STRUCTURE.md    # 상세 구조 문서
```

## 템플릿 구조

### Template 1 - Light Mode
- 밝은 배경, 어두운 텍스트
- 깔끔하고 모던한 디자인
- 접근성 최적화

### Template 2 - Dark Mode (메인)
- 어두운 배경, 밝은 텍스트
- 프리미엄 다크 테마
- WCAG AAA 접근성 준수
- GSAP 애니메이션
- Swiper 슬라이더

## 디자인 시스템

### 색상 (Template 2 - Dark Mode)
- **Primary**: #4D9FFF (다크모드 최적화, 대비율 7.2:1)
- **Background**: 다크 그라데이션 (#0a0a0a ~ #1a1a1a)
- **Text**: 밝은 색상 계열
- **Accent**: 시안 계열

### 타이포그래피
- **폰트**: Pretendard (CDN)
- **크기**: 12px ~ 64px
- **굵기**: 400 (Regular), 500 (Medium), 600 (SemiBold), 700 (Bold)

### 브레이크포인트
- **모바일**: < 768px
- **태블릿**: 768px ~ 1023px
- **데스크톱**: ≥ 1024px

## 페이지 구조

### 공통 페이지
- 메인 페이지 (index.html)
- 404 페이지
- 이용약관
- 개인정보처리방침

### 회사소개 (about/)
- 회사소개
- 인사말
- 회사연혁
- 안전보건 경영방침과 목표
- 오시는 길

### 제품 솔루션 (solutions/)
- 원스탑 산업관리 스마트 솔루션
- AI 영상 방송 관제 시스템
- 스마트 건설현장 안전 플랫폼
- 타워크레인 통합 안전 시스템
- 스마트 출입통제 시스템
- 스마트 환경센서 시스템

### 시공사례 (projects/)
- 시공사례 목록 (필터링 기능)

### 고객지원 (support/)
- 원격지원
- 문의하기 (mailto)

## 주요 기능

### 히어로 슬라이더
- Swiper.js 기반 슬라이더
- 자동 재생/정지 토글 버튼
- 프로그레스 바 애니메이션
- 페이드 전환 효과
- 4개 슬라이드 (5초/6초 duration)

### 스크롤 애니메이션
- GSAP ScrollTrigger
- Fade-in, Scale-in 효과
- 카운터 애니메이션
- Parallax 효과 (선택적)

### 반응형 디자인
- 모바일 최적화
- 태블릿 레이아웃
- 데스크톱 레이아웃
- 터치 제스처 지원

## 접근성

- WCAG 2.1 AAA 레벨 준수
- 다크모드 최적화 컬러 (대비율 7.2:1)
- 키보드 네비게이션 지원
- 스크린 리더 호환
- ARIA 레이블 적용

## 문서

### 핵심 문서
- **[web/README.md](web/README.md)** - 템플릿 가이드
- **[docs/renewal_content.md](docs/renewal_content.md)** - 리뉴얼 콘텐츠
- **[scripts/README.md](scripts/README.md)** - 스크립트 관리 가이드

### 개발 가이드
- **[SETUP.md](SETUP.md)** - 개발 환경 설정
- **[PROJECT-STRUCTURE.md](PROJECT-STRUCTURE.md)** - 프로젝트 구조 상세
- **[web/dark/DEVELOPMENT-GUIDE.md](web/dark/DEVELOPMENT-GUIDE.md)** - 개발 가이드

## 품질 기준

- **Lighthouse Performance**: 90+
- **Lighthouse Accessibility**: 95+
- **Lighthouse Best Practices**: 90+
- **Lighthouse SEO**: 95+
- **WCAG 2.1 AAA**: 준수

## 브라우저 지원

- Chrome (최신 버전)
- Firefox (최신 버전)
- Safari (최신 버전)
- Edge (최신 버전)
- 모바일 브라우저

## 스크립트 관리

프로젝트 유틸리티 스크립트는 `scripts/` 디렉토리에서 관리됩니다.

- `scripts/completed/` - 최근 완료된 재사용 가능한 스크립트
- `scripts/archived/` - 과거 사용된 참고용 스크립트

자세한 내용은 [scripts/README.md](scripts/README.md)를 참조하세요.

## 라이선스

© 2024 (주)아이티로그. All rights reserved.

## 문의

- **이메일**: ok@it-log.co.kr
- **주소**: 서울특별시 구로구 디지털로33길 28 우림이비즈센터 1차 308호
