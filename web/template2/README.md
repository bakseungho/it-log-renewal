# (주)아이티로그 홈페이지 - Template2

## 프로젝트 개요

**프로젝트명**: (주)아이티로그 홈페이지 리뉴얼 (Template2)  
**디자인 테마**: Trendy & Simple (트렌디하고 심플한)  
**기술 스택**: HTML5, CSS3, JavaScript (ES6+)  
**개발 기간**: 2024

## 디자인 컨셉

- **Primary Color**: Electric Blue (#0066FF)
- **Secondary Color**: Cyan Accent (#00D9FF)
- **폰트**: Pretendard (한글), Inter (영문)
- **스타일**: 미니멀하고 현대적인 디자인
- **반응형**: Mobile First 접근

## 프로젝트 구조

```
web/template2/
├── index.html                 # 메인 페이지
├── about/                     # 회사소개 (5개 페이지)
│   ├── company.html          # 회사소개
│   ├── ceo-message.html      # CEO 인사말
│   ├── history.html          # 회사연혁
│   ├── certifications.html   # 인증 및 특허
│   └── location.html         # 오시는 길
├── solutions/                 # 솔루션 (6개 페이지)
│   ├── smart-safety.html     # 스마트 현장안전 시스템
│   ├── tower-crane.html      # 타워크레인 통합안전 시스템
│   ├── ai-surveillance.html  # AI 영상 방송 관제시스템
│   ├── environment-sensor.html # 스마트 환경센서 시스템
│   └── access-control.html   # 스마트 출입통제 시스템
├── support/                   # 고객지원 (2개 페이지)
│   ├── remote-support.html   # 원격지원
│   └── contact.html          # 문의하기
├── css/                       # 스타일시트
│   ├── reset.css             # CSS 리셋
│   ├── variables.css         # CSS 변수
│   ├── common.css            # 공통 스타일
│   ├── components.css        # 컴포넌트
│   ├── header.css            # 헤더
│   ├── footer.css            # 푸터
│   └── pages/                # 페이지별 스타일
│       ├── home.css
│       ├── subpage.css
│       └── solutions.css
├── js/                        # JavaScript
│   ├── utils.js              # 유틸리티 함수
│   ├── components.js         # UI 컴포넌트
│   └── main.js               # 메인 초기화
└── assets/                    # 에셋
    ├── images/               # 이미지
    │   ├── logo.png
    │   ├── hero/
    │   ├── icons/
    │   ├── clients/
    │   └── projects/
    └── fonts/                # 폰트 (선택)
```

## 주요 기능

### 1. 반응형 네비게이션
- 데스크톱: 드롭다운 메뉴
- 모바일: 햄버거 메뉴 (전체 화면 오버레이)
- 스크롤 시 헤더 고정 (Sticky Header)

### 2. 히어로 섹션 슬라이더
- 4개 슬라이드 자동 재생 (5초 간격)
- 좌우 화살표 및 인디케이터
- 모바일 스와이프 제스처 지원

### 3. 솔루션 카드
- 4대 핵심 솔루션 표시
- 호버 효과 (확대 + 그림자)
- 스크롤 애니메이션

### 4. 숫자 카운트업 애니메이션
- 스크롤 시 숫자 카운트업
- GSAP 라이브러리 활용

### 5. 스크롤 애니메이션
- 페이드인 + 슬라이드업 효과
- Intersection Observer API 활용

### 6. 문의 폼
- 유효성 검사
- 개인정보 수집 동의
- 메일 발송 기능 (FormSubmit 연동 가능)

### 7. Back to Top 버튼
- 스크롤 일정 거리 이상 시 표시
- 스무스 스크롤

## 외부 라이브러리 (CDN)

### GSAP (애니메이션)
```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>
```

### Swiper.js (슬라이더)
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
```

### Pretendard 폰트
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css">
```

### 카카오맵 API (오시는 길 페이지)
```html
<script src="//dapi.kakao.com/v2/maps/sdk.js?appkey=YOUR_APP_KEY"></script>
```

## 브라우저 지원

- Chrome (최신 버전)
- Firefox (최신 버전)
- Safari (최신 버전)
- Edge (최신 버전)
- 모바일 브라우저 (iOS Safari, Chrome)

## 반응형 브레이크포인트

- **모바일**: 320px - 767px
- **태블릿**: 768px - 1023px
- **데스크톱**: 1024px 이상

## 성능 최적화

### 이미지 최적화
- WebP 형식 사용 권장
- 레이지 로딩 (`loading="lazy"`)
- 반응형 이미지 (`<picture>`, srcset)

### CSS/JS 최적화
- CSS 파일 분리 (페이지별)
- JavaScript 비동기 로딩
- 사용하지 않는 코드 제거

### 캐싱
- 정적 에셋 장기 캐싱
- HTML 짧은 캐싱

## 접근성 (WCAG 2.1 AA)

- 시맨틱 HTML 사용
- 키보드 네비게이션 지원
- 스크린 리더 호환
- 색상 대비 4.5:1 이상
- ARIA 레이블 적절히 사용

## SEO 최적화

### 메타 태그
- 페이지별 고유 title 및 description
- Open Graph 태그
- Schema.org 마크업

### 사이트맵
- sitemap.xml 생성
- robots.txt 작성

## 개발 가이드

### 1. 로컬 개발 환경 설정

```bash
# 프로젝트 클론
git clone [repository-url]

# 디렉토리 이동
cd web/template2

# 로컬 서버 실행 (Python)
python -m http.server 8000

# 또는 (Node.js)
npx http-server -p 8000
```

브라우저에서 `http://localhost:8000` 접속

### 2. 이미지 추가

1. `assets/images/` 폴더에 이미지 추가
2. HTML에서 경로 참조: `assets/images/your-image.jpg`
3. 이미지 최적화 권장 (TinyPNG, ImageOptim 등)

### 3. 콘텐츠 수정

#### 텍스트 수정
- HTML 파일에서 직접 수정

#### 스타일 수정
- `css/variables.css`: 색상, 폰트, 간격 등 변수 수정
- `css/common.css`: 공통 스타일 수정
- `css/pages/`: 페이지별 스타일 수정

#### 기능 수정
- `js/components.js`: 컴포넌트 로직 수정
- `js/main.js`: 초기화 및 전역 설정 수정

### 4. 새 페이지 추가

1. 기존 페이지 복사 (예: `about/company.html`)
2. 콘텐츠 수정
3. 네비게이션 메뉴에 링크 추가 (header 부분)

## 배포 가이드

### 정적 호스팅 (권장)

#### Netlify
1. Netlify 계정 생성
2. 프로젝트 폴더 드래그 앤 드롭
3. 자동 배포 완료

#### Vercel
1. Vercel 계정 생성
2. GitHub 저장소 연결
3. 자동 배포 설정

#### GitHub Pages
1. GitHub 저장소 생성
2. `web/template2` 폴더 푸시
3. Settings > Pages에서 배포 설정

### 일반 웹 호스팅

1. FTP 클라이언트로 파일 업로드
2. 도메인 연결
3. SSL 인증서 설정

## 유지보수 가이드

### 정기 업데이트

#### 콘텐츠 업데이트
- 솔루션 정보: 분기별
- 시공사례: 월별
- 회사연혁: 연별
- 인증 및 특허: 수시

#### 기술 유지보수
- 라이브러리 버전 업데이트: 분기별
- 보안 패치: 수시
- 성능 모니터링: 월별

### 문제 해결

#### 슬라이더가 작동하지 않을 때
- Swiper.js CDN 로드 확인
- 콘솔 에러 확인
- 브라우저 캐시 삭제

#### 애니메이션이 작동하지 않을 때
- GSAP CDN 로드 확인
- ScrollTrigger 플러그인 로드 확인
- 요소에 `.fade-in-up` 클래스 추가 확인

#### 모바일 메뉴가 작동하지 않을 때
- JavaScript 에러 확인
- 햄버거 버튼 클래스 확인
- 이벤트 리스너 등록 확인

## 추가 개발 필요 사항

### 콘텐츠
- [ ] 실제 회사 정보 (주소, 연락처, 사업자번호)
- [ ] CEO 인사말 전문
- [ ] 회사연혁 상세 (2010-2025)
- [ ] 인증서 및 특허 이미지
- [ ] 고객사 CI 로고 이미지
- [ ] 시공사례 이미지 및 설명
- [ ] 솔루션별 시스템 구성도 이미지

### 기능
- [ ] 문의 폼 메일 발송 기능 (FormSubmit 또는 서버 사이드)
- [ ] 카카오맵 API 키 설정 및 좌표 입력
- [ ] 원격지원 외부 링크 URL 설정
- [ ] Google Analytics 설정
- [ ] sitemap.xml 생성
- [ ] robots.txt 작성

### 이미지
- [ ] 히어로 섹션 배경 이미지 (4개)
- [ ] 솔루션 아이콘 (4개)
- [ ] 시공사례 이미지 (최소 9개)
- [ ] 고객사 로고 (6개 이상)
- [ ] 로고 이미지 (컬러, 화이트)
- [ ] Favicon

## 라이선스

이 프로젝트는 (주)아이티로그의 소유입니다.

## 문의

프로젝트 관련 문의: info@itlog.co.kr

---

**개발 완료일**: 2024  
**버전**: 1.0  
**개발자**: Frontend Developer
