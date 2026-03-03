# Template3 - Dark & Premium Website

## 프로젝트 개요

**디자인 테마**: Dark & Premium  
**참고 사이트**: https://www.dwce.co.kr/  
**기술 스택**: HTML5, CSS3, Vanilla JavaScript, jQuery  
**애니메이션**: GSAP 3.12+, Swiper.js  
**컬러 테마**: 다크 모드 (#0a0a0a, #1a1a1a) + 골드(#d4af37) + 시안(#00d9ff)

## 주요 특징

### 디자인
- ✅ 다크 모드 기반 프리미엄 디자인
- ✅ 풀스크린 히어로 슬라이더 (4개 슬라이드)
- ✅ 대형 타이포그래피 (60-120px)
- ✅ 골드 + 시안 듀얼 포인트 컬러
- ✅ 넉넉한 여백 (최소 80px)

### 인터랙션
- ✅ GSAP ScrollTrigger 스크롤 애니메이션
- ✅ 패럴랙스 효과
- ✅ 호버 시 스케일 + 글로우 효과
- ✅ 숫자 카운트업 애니메이션
- ✅ 부드러운 페이지 전환

### 기능
- ✅ 반응형 디자인 (320px, 768px, 1024px, 1366px)
- ✅ 다크 테마 네비게이션 (투명 → 불투명)
- ✅ 모바일 햄버거 메뉴
- ✅ 이미지 레이지 로딩
- ✅ 폼 유효성 검사
- ✅ 라이트박스 이미지 갤러리

## 파일 구조

```
web/template3/
├── index.html                 # 메인 페이지
├── about/                     # 회사소개 (5개)
│   ├── company.html
│   ├── ceo-message.html
│   ├── history.html
│   ├── certifications.html
│   └── location.html
├── solutions/                 # 솔루션 (5개)
│   ├── smart-safety.html
│   ├── tower-crane.html
│   ├── ai-surveillance.html
│   ├── environment-sensor.html
│   └── access-control.html
├── support/                   # 고객지원 (2개)
│   ├── remote-support.html
│   └── contact.html
├── 404.html
├── terms.html
├── privacy.html
├── css/
│   ├── reset.css
│   ├── variables.css
│   ├── common.css
│   ├── components.css
│   ├── header.css
│   ├── footer.css
│   └── pages/
│       ├── home.css
│       ├── subpage.css
│       └── solutions.css
├── js/
│   ├── utils.js
│   ├── components.js
│   └── main.js
├── images/
│   ├── logo-white.png
│   ├── hero/
│   ├── clients/
│   ├── projects/
│   └── solutions/
├── README.md
└── DEVELOPMENT-GUIDE.md
```

## 페이지 목록

### 메인 페이지 (1개)
- `index.html` - 풀스크린 히어로 슬라이더, 주요 솔루션, 통계, 고객사, 시공사례

### 회사소개 (5개)
- `about/company.html` - 기업 정보, 비전, 사업분야
- `about/ceo-message.html` - CEO 인사말
- `about/history.html` - 타임라인 (2010-2025)
- `about/certifications.html` - 인증서 및 특허 갤러리
- `about/location.html` - 카카오맵 + 주소

### 솔루션 (5개)
- `solutions/smart-safety.html` - 스마트 현장안전 시스템
- `solutions/tower-crane.html` - 타워크레인 통합안전 시스템
- `solutions/ai-surveillance.html` - AI 영상 방송 관제시스템
- `solutions/environment-sensor.html` - 스마트 환경센서 시스템
- `solutions/access-control.html` - 스마트 출입통제 시스템

### 고객지원 (2개)
- `support/remote-support.html` - 원격지원 안내
- `support/contact.html` - 문의 폼

### 기타 (3개)
- `404.html` - 에러 페이지
- `terms.html` - 이용약관
- `privacy.html` - 개인정보처리방침

## 사용된 라이브러리 (CDN)

### CSS
- **Pretendard Font**: 한글 웹폰트
- **Swiper.js 11**: 히어로 슬라이더

### JavaScript
- **GSAP 3.12+**: 스크롤 애니메이션
  - ScrollTrigger: 스크롤 기반 애니메이션
  - ScrollToPlugin: 부드러운 스크롤
- **Swiper.js 11**: 터치 슬라이더

## 브라우저 지원

- Chrome (최신 2개 버전)
- Firefox (최신 2개 버전)
- Safari (최신 2개 버전)
- Edge (최신 2개 버전)

## 반응형 브레이크포인트

- **모바일**: 320px - 767px
- **태블릿**: 768px - 1023px
- **노트북**: 1024px - 1365px
- **데스크톱**: 1366px 이상

## 성능 목표

- **페이지 로딩**: 2초 이내
- **애니메이션**: 60fps 유지
- **Lighthouse 점수**: 95점 이상
- **접근성**: WCAG 2.1 AA 준수

## 컬러 팔레트

### 다크 배경
- Primary: `#0a0a0a`
- Secondary: `#1a1a1a`
- Tertiary: `#2a2a2a`
- Black: `#000000`

### 포인트 컬러
- Gold: `#d4af37` (프리미엄, 신뢰)
- Cyan: `#00d9ff` (기술력, 혁신)

### 텍스트
- Primary: `#ffffff`
- Secondary: `#a0a0a0`
- Tertiary: `#707070`

## 타이포그래피

### 폰트
- Primary: Pretendard (한글)
- Secondary: Inter (영문, 숫자)

### 사이즈
- Display 1: 120px (히어로 제목)
- Display 2: 80px (히어로 부제목)
- H1: 60px (페이지 제목)
- H2: 48px (섹션 제목)
- Body: 16-18px (본문)

## 개발 가이드

자세한 개발 가이드는 `DEVELOPMENT-GUIDE.md`를 참고하세요.

## 라이선스

© 2024 ITLOG. All rights reserved.

## 문의

- **이메일**: contact@itlog.co.kr
- **전화**: 02-XXXX-XXXX
