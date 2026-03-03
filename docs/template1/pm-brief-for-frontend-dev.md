# 프론트엔드 개발자를 위한 작업 지시서

## 문서 개요

**프로젝트명**: (주)아이티로그 홈페이지 리뉴얼 프로젝트  
**대상**: 프론트엔드 개발자 (frontend-dev-website)  
**작성일**: 2024  
**작성자**: PM (Product Manager)  
**버전**: 2.0 (업데이트)

---

## 1. 프로젝트 배경 및 목표

### 1.1 회사 소개
- **회사명**: (주)아이티로그
- **사업 분야**: 건설 현장 제품 솔루션 설치 및 시공
- **주요 솔루션**:
  - 현장 안전 플랫폼 (스마트 현장안전, 타워크레인 통합안전)
  - 스마트 관제·제어 (AI 영상 방송 관제)
  - 환경·출입관리 (환경센서, 출입통제)

### 1.2 프로젝트 목표
1. **기술 목표**
   - 정적 웹사이트 (HTML/CSS/JavaScript)
   - 모바일 최적화 및 반응형 디자인
   - 접근성 준수 (WCAG 2.1 AA)
   - 빠른 페이지 로딩 속도 (3초 이내)
   - Lighthouse 점수 90점 이상 (모든 항목)

2. **성능 목표**
   - LCP (Largest Contentful Paint): 2.5초 이하
   - FID (First Input Delay): 100ms 이하
   - CLS (Cumulative Layout Shift): 0.1 이하
   - 이미지 최적화 (WebP, Lazy Loading)

3. **품질 목표**
   - 크로스 브라우저 호환성 (Chrome, Firefox, Safari, Edge)
   - 시맨틱 HTML 사용
   - 접근성 테스트 통과 (WAVE 에러 0개)
   - 코드 품질 및 유지보수성

### 1.3 기술 스택
- **마크업**: HTML5 (시맨틱 태그)
- **스타일**: CSS3 (Flexbox, Grid, CSS Variables)
- **스크립트**: JavaScript (ES6+), jQuery 3.x (선택 사항)
- **라이브러리**:
  - Swiper.js (슬라이더/캐러셀)
  - AOS (Animate On Scroll)
  - GLightbox (이미지 갤러리)
  - jQuery Validation (폼 검증, 선택 사항)

### 1.4 프로젝트 제약사항
- **정적 웹사이트**: 데이터베이스 없음, 서버 사이드 로직 없음
- **제외 기능**: 로그인, 회원가입, 게시판, 실시간 채팅
- **포함 기능**: 문의 폼, 검색, 다운로드, 지도 연동
- **데이터 관리**: JSON 파일 활용 (제품 정보, 실적 등)

---

## 2. 페이지 구조 개요

### 2.1 주요 페이지 목록
1. **메인 페이지** (`index.html`)
2. **회사소개** (`about/index.html`)
   - CEO 인사말 (`about/ceo-message.html`)
   - 회사연혁 (`about/history.html`)
   - 인증 및 특허 (`about/certifications.html`)
   - 오시는 길 (`about/location.html`)
3. **솔루션 페이지**
   - 현장 안전 플랫폼 (`solutions/safety-platform.html`)
   - 스마트 관제·제어 (`solutions/smart-control.html`)
   - 환경·출입관리 (`solutions/environment-access.html`)
   - 솔루션 상세 (각 솔루션별 상세 페이지)
4. **고객지원**
   - 문의하기 (`contact/index.html`)
   - 원격지원 (외부 링크)

### 2.2 공통 요소
- **Header**: 로고, 메뉴, 검색, 문의하기 버튼
- **Footer**: 회사 정보, 이용약관, 개인정보처리방침, 문의처
- **Back to Top 버튼**

---

## 3. 담당 업무 및 산출물

### 3.1 Week 5: 프로젝트 셋업 및 HTML/CSS 마크업 (1차)

#### 3.1.1 프로젝트 셋업 (Week 5 초반)
**목표**: 개발 환경 구축 및 프로젝트 구조 설정

**작업 내용**:
1. **디렉토리 구조 설정**

```
project-root/
├── index.html
├── about/
│   ├── index.html
│   ├── ceo-message.html
│   ├── history.html
│   ├── certifications.html
│   └── location.html
├── solutions/
│   ├── safety-platform.html
│   ├── smart-control.html
│   └── environment-access.html
├── contact/
│   └── index.html
├── assets/
│   ├── css/
│   │   ├── reset.css
│   │   ├── variables.css
│   │   ├── common.css
│   │   ├── components.css
│   │   └── pages/
│   ├── js/
│   │   ├── vendor/
│   │   ├── common.js
│   │   ├── components/
│   │   └── pages/
│   ├── images/
│   ├── fonts/
│   └── data/
├── favicon.ico
├── robots.txt
└── sitemap.xml
```

2. **개발 환경 구축**
   - Git 저장소 초기화
   - .gitignore 파일 작성
   - 코드 에디터 설정 (VS Code 권장)
   - 브라우저 개발자 도구 설정

3. **CSS 변수 및 공통 스타일 작성**
   - `assets/css/variables.css`: 색상, 폰트, 간격 등
   - `assets/css/reset.css`: CSS 리셋
   - `assets/css/common.css`: 공통 스타일 (헤더, 푸터, 버튼 등)
   - `assets/css/components.css`: 재사용 가능한 컴포넌트

4. **외부 라이브러리 설치**
   - Swiper.js (CDN 또는 로컬)
   - AOS (Animate On Scroll)
   - GLightbox (이미지 갤러리)
   - jQuery (선택 사항)

**산출물**: 프로젝트 구조 및 기본 파일

---

#### 3.1.2 HTML/CSS 마크업 - 공통 요소 (Week 5 초중반)
**목표**: 모든 페이지에서 사용되는 공통 요소 개발

**작업 내용**:
1. **Header 개발**
   - 로고
   - 글로벌 네비게이션 (GNB)
   - 검색 버튼
   - 문의하기 버튼
   - Sticky Header (스크롤 시 상단 고정)
   - 모바일 햄버거 메뉴

2. **Footer 개발**
   - 회사 기본정보 (CI, 주소, 전화번호, 팩스, 사업자번호)
   - 이용약관, 개인정보처리방침 링크
   - 저작권 표기
   - 문의하기 링크

3. **Back to Top 버튼**
   - 스크롤 시 표시
   - 클릭 시 부드럽게 상단 이동

**고려사항**:
- 시맨틱 HTML 사용 (`<header>`, `<nav>`, `<footer>`)
- 접근성 (ARIA 속성, 키보드 네비게이션)
- 반응형 디자인 (Mobile First)

**산출물**: Header, Footer, Back to Top 버튼

---

#### 3.1.3 HTML/CSS 마크업 - 메인 페이지 (Week 5 중후반)
**목표**: 메인 페이지 마크업 및 스타일링

**작업 내용**:
1. **히어로 섹션**
   - 슬라이더 (4개 슬라이드)
   - 각 슬라이드: 배경 이미지, 서브타이틀, 제목, 서브 문구, CTA 버튼
   - 자동 재생, 수동 조작 (화살표, 인디케이터)

2. **주요 솔루션 섹션**
   - 4개 솔루션 카드 (그리드 레이아웃)
   - 각 카드: 아이콘/이미지, 제목, 간단한 설명, 상세보기 버튼
   - 호버 효과

3. **숫자로 보는 신뢰 섹션**
   - 3-4개 통계 카드
   - 숫자 카운터 애니메이션 (스크롤 시 작동)

4. **고객사 섹션**
   - 고객사 로고 그리드 또는 슬라이더

5. **주요 시공사례 섹션**
   - 프로젝트 카드 그리드 (3-6개)
   - 각 카드: 썸네일 이미지, 프로젝트명, 발주처, 간단한 설명

6. **고객문의 섹션**
   - CS 정보 (전화번호, 이메일)
   - 원격지원 버튼
   - 문의하기 버튼

**고려사항**:
- UX 디자이너의 와이어프레임 및 디자인 시스템 반영
- 반응형 레이아웃 (모바일: 1컬럼, 태블릿: 2컬럼, 데스크톱: 3-4컬럼)
- 이미지 최적화 (WebP, Lazy Loading)
- 스크롤 애니메이션 (AOS)

**산출물**: 메인 페이지 (`index.html`)

---

### 3.2 Week 6: HTML/CSS 마크업 (2차) - 서브 페이지

#### 3.2.1 회사소개 페이지 (Week 6 초반)
**작업 내용**:
1. **회사소개 메인** (`about/index.html`)
   - 기업정보 섹션
   - 사업분야 섹션
   - 고객사 섹션

2. **CEO 인사말** (`about/ceo-message.html`)
   - 인사말 텍스트
   - CEO 서명 이미지

3. **회사연혁** (`about/history.html`)
   - 타임라인 레이아웃 (2010-2025)
   - 연도별 주요 성과

4. **인증 및 특허** (`about/certifications.html`)
   - 이미지 갤러리 (그리드 레이아웃)
   - 라이트박스 기능

5. **오시는 길** (`about/location.html`)
   - 지도 API 연동 (Kakao Map 또는 Google Maps)
   - 주소 정보 (도로명/지번)
   - 대중교통 이용 안내

**산출물**: 회사소개 관련 5개 페이지

---

#### 3.2.2 솔루션 페이지 (Week 6 중반)
**작업 내용**:
1. **솔루션 카테고리 페이지** (3개)
   - 현장 안전 플랫폼 (`solutions/safety-platform.html`)
   - 스마트 관제·제어 (`solutions/smart-control.html`)
   - 환경·출입관리 (`solutions/environment-access.html`)

2. **각 페이지 공통 구조**:
   - 시스템 개요 섹션
   - 시스템 구성도 (이미지/일러스트)
   - 주요 시공사례 섹션 (카드 그리드)
   - 관련 솔루션 추천
   - 문의하기 CTA

**고려사항**:
- 템플릿 방식으로 개발 (재사용 가능한 구조)
- JSON 데이터 활용 (솔루션 정보, 시공사례)

**산출물**: 솔루션 페이지 3개

---

#### 3.2.3 고객지원 페이지 (Week 6 후반)
**작업 내용**:
1. **문의하기 페이지** (`contact/index.html`)
   - 문의 폼
     - 이름 (필수)
     - 회사명 (필수)
     - 연락처 (필수)
     - 이메일 (필수)
     - 문의 유형 (드롭다운)
     - 문의 내용 (텍스트 영역)
   - 연락처 정보
   - 원격지원 링크

**고려사항**:
- 폼 접근성 (레이블, 에러 메시지)
- 반응형 폼 레이아웃

**산출물**: 문의하기 페이지

---

### 3.3 Week 7: JavaScript 기능 구현 및 통합

#### 3.3.1 공통 JavaScript 기능 (Week 7 초반)
**작업 내용**:
1. **Header 기능**
   - Sticky Header (스크롤 시 상단 고정)
   - 모바일 햄버거 메뉴 토글
   - 메뉴 호버 시 드롭다운 (데스크톱)

2. **검색 기능**
   - 검색창 확장/축소
   - 실시간 검색 (JSON 데이터 기반)
   - 자동완성
   - 검색 결과 표시

3. **Back to Top 버튼**
   - 스크롤 위치에 따라 표시/숨김
   - 클릭 시 부드럽게 상단 이동

4. **Smooth Scroll**
   - 앵커 링크 클릭 시 부드러운 스크롤

**산출물**: `assets/js/common.js`

---

#### 3.3.2 메인 페이지 JavaScript (Week 7 초중반)
**작업 내용**:
1. **히어로 슬라이더** (Swiper.js)
   - 자동 재생 (5초 간격)
   - 수동 조작 (화살표, 인디케이터)
   - 페이드 효과
   - 접근성 (키보드 네비게이션)

2. **숫자 카운터 애니메이션**
   - 스크롤 시 숫자 증가 애니메이션
   - Intersection Observer 활용

3. **고객사 로고 슬라이더** (Swiper.js)
   - 자동 재생
   - 무한 루프

4. **스크롤 애니메이션** (AOS)
   - 섹션별 페이드 인 효과

**산출물**: `assets/js/pages/home.js`

---

#### 3.3.3 서브 페이지 JavaScript (Week 7 중반)
**작업 내용**:
1. **이미지 갤러리** (GLightbox)
   - 인증 및 특허 페이지
   - 시공사례 이미지
   - 라이트박스 팝업
   - 이전/다음 네비게이션

2. **지도 연동** (Kakao Map 또는 Google Maps)
   - 오시는 길 페이지
   - 지도 표시
   - 마커 표시
   - 길찾기 링크

3. **문의 폼 검증 및 제출**
   - 실시간 입력 검증
   - 에러 메시지 표시
   - 폼 제출 (FormSpree 또는 EmailJS)
   - 성공/실패 메시지

**산출물**: 
- `assets/js/components/gallery.js`
- `assets/js/components/map.js`
- `assets/js/components/contact-form.js`

---

#### 3.3.4 데이터 관리 (Week 7 중후반)
**작업 내용**:
1. **JSON 데이터 파일 작성**
   - `assets/data/solutions.json`: 솔루션 정보
   - `assets/data/projects.json`: 시공사례 정보
   - `assets/data/search-index.json`: 검색 인덱스

2. **데이터 로드 및 렌더링**
   - Fetch API 활용
   - 동적 콘텐츠 렌더링
   - 에러 처리

**산출물**: JSON 데이터 파일 및 렌더링 스크립트

---

### 3.4 Week 7 후반: 성능 최적화

#### 3.4.1 이미지 최적화
**작업 내용**:
1. **이미지 포맷 최적화**
   - WebP 형식 사용 (Fallback: JPG/PNG)
   - 적절한 이미지 크기 및 압축

2. **Lazy Loading**
   - 이미지 지연 로딩 (`loading="lazy"`)
   - Intersection Observer 활용

3. **Responsive Images**
   - `srcset` 및 `sizes` 속성 활용
   - 디바이스별 최적 이미지 제공

**산출물**: 최적화된 이미지 및 코드

---

#### 3.4.2 코드 최적화
**작업 내용**:
1. **CSS 최적화**
   - 불필요한 스타일 제거
   - CSS 압축 (minify)
   - Critical CSS 인라인 (선택 사항)

2. **JavaScript 최적화**
   - 코드 압축 (minify)
   - 불필요한 코드 제거
   - 비동기 로딩 (`async`, `defer`)

3. **캐싱 전략**
   - CSS/JS 파일에 버전 쿼리 추가
   - 브라우저 캐싱 활용

**산출물**: 최적화된 CSS/JS 파일

---

#### 3.4.3 SEO 최적화
**작업 내용**:
1. **메타 태그 작성**
   - 각 페이지별 Title, Description
   - Open Graph 태그
   - Twitter Card 태그

2. **구조화된 데이터** (Schema.org)
   - 조직 정보
   - 제품 정보
   - Breadcrumb

3. **sitemap.xml 및 robots.txt**
   - 사이트맵 생성
   - 검색 엔진 크롤링 설정

**산출물**: SEO 최적화된 HTML 및 sitemap.xml

---

### 3.5 Week 8: 테스트 및 배포

#### 3.5.1 기능 테스트 (Week 8 초반)
**테스트 항목**:
- [ ] 모든 링크 작동 확인
- [ ] 네비게이션 메뉴 (데스크톱/모바일)
- [ ] 검색 기능
- [ ] 문의 폼 제출 및 검증
- [ ] 슬라이더/캐러셀 동작
- [ ] 이미지 갤러리 라이트박스
- [ ] 지도 표시 및 인터랙션
- [ ] Back to Top 버튼

**산출물**: 테스트 체크리스트 및 버그 리포트

---

#### 3.5.2 반응형 및 브라우저 테스트 (Week 8 초중반)
**테스트 디바이스**:
- iPhone SE (375px)
- iPhone 12/13 (390px)
- Samsung Galaxy S21 (360px)
- iPad (768px)
- iPad Pro (1024px)
- Desktop (1920px)

**테스트 브라우저**:
- Chrome (최신)
- Firefox (최신)
- Safari (최신)
- Edge (최신)
- iOS Safari
- Chrome Mobile

**산출물**: 브라우저 호환성 리포트

---

#### 3.5.3 성능 및 접근성 테스트 (Week 8 중반)
**성능 테스트**:
- Google Lighthouse (목표: 90점 이상)
- PageSpeed Insights
- Core Web Vitals 측정

**접근성 테스트**:
- WAVE 도구 (목표: 에러 0개)
- 키보드 네비게이션 테스트
- 스크린 리더 테스트 (NVDA, VoiceOver)
- 색상 대비 검사

**산출물**: 성능 및 접근성 리포트

---

#### 3.5.4 배포 (Week 8 후반)
**작업 내용**:
1. **배포 전 최종 점검**
   - 모든 테스트 통과 확인
   - 프로덕션 빌드 (코드 압축)
   - 환경 변수 설정 (API 키 등)

2. **배포**
   - 호스팅 서비스 선택 (Netlify, Vercel, GitHub Pages 등)
   - 도메인 연결
   - SSL 인증서 설정

3. **배포 후 모니터링**
   - 실제 환경에서 기능 테스트
   - 성능 모니터링
   - 에러 로깅

**산출물**: 배포된 웹사이트 및 배포 가이드

---

## 4. 작업 가이드라인

### 4.1 코딩 표준
1. **HTML**
   - 시맨틱 태그 사용
   - 들여쓰기: 2 스페이스
   - 속성 순서: class, id, data-*, src, href, type, value
   - 대체 텍스트 필수 (이미지)

2. **CSS**
   - BEM 네이밍 컨벤션
   - Mobile First 접근
   - CSS 변수 활용
   - 들여쓰기: 2 스페이스

3. **JavaScript**
   - ES6+ 문법 사용
   - camelCase 네이밍
   - 'use strict' 모드
   - 주석 작성 (복잡한 로직)

### 4.2 접근성 가이드
- 모든 이미지에 alt 속성
- 폼 요소에 레이블 연결
- 키보드 네비게이션 지원
- ARIA 속성 적절히 사용
- 색상 대비 4.5:1 이상

### 4.3 성능 가이드
- 이미지 최적화 (WebP, 압축)
- Lazy Loading 적용
- CSS/JS 압축
- 불필요한 라이브러리 제거
- 캐싱 전략 활용

---

## 5. 참고 자료

### 5.1 필수 참고 문서
- `docs/hopage_renewal_content.md` - 콘텐츠 요구사항
- `docs/ux-wireframes.md` - 와이어프레임 (Week 3 말 제공)
- `docs/ux-design-system.md` - 디자인 시스템 (Week 4 말 제공)
- `docs/ux-design-handoff.md` - 디자인 핸드오프 (Week 4 말 제공)
- `docs/pm-requirements-for-frontend.md` - 프론트엔드 요구사항 (기존 문서)

### 5.2 기술 문서
- MDN Web Docs: https://developer.mozilla.org/
- Swiper.js: https://swiperjs.com/
- AOS: https://michalsnik.github.io/aos/
- GLightbox: https://biati-digital.github.io/glightbox/

### 5.3 도구
- VS Code (코드 에디터)
- Chrome DevTools (디버깅)
- Lighthouse (성능 측정)
- WAVE (접근성 검사)

---

## 6. 산출물 제출 가이드

### 6.1 산출물 목록 및 제출 기한
| 산출물 | 제출 기한 | 형식 |
|--------|-----------|------|
| 프로젝트 구조 및 공통 요소 | Week 5 수요일 | 코드 |
| 메인 페이지 | Week 5 금요일 | 코드 |
| 회사소개 페이지 | Week 6 화요일 | 코드 |
| 솔루션 페이지 | Week 6 목요일 | 코드 |
| 고객지원 페이지 | Week 6 금요일 | 코드 |
| JavaScript 기능 구현 | Week 7 수요일 | 코드 |
| 성능 최적화 완료 | Week 7 금요일 | 코드 + 리포트 |
| 테스트 완료 | Week 8 수요일 | 테스트 리포트 |
| 최종 배포 | Week 8 금요일 | 배포 URL + 가이드 |

### 6.2 코드 제출 방법
- **Git 저장소**: GitHub 또는 GitLab
- **브랜치 전략**: main (프로덕션), develop (개발)
- **커밋 메시지**: 명확하고 구체적으로 작성
- **Pull Request**: 주요 기능 완성 시 PR 생성

### 6.3 검토 프로세스
1. **코드 리뷰**: PM 및 팀원 검토
2. **피드백 반영**: 1-2일 내 수정
3. **테스트**: 기능, 반응형, 브라우저 호환성
4. **승인**: PM 최종 승인 후 배포

---

## 7. 협업 가이드

### 7.1 커뮤니케이션
- **정기 미팅**: 매주 월요일 오전 10시 (전체 팀)
- **일일 스탠드업**: 매일 오전 9시 30분 (개발 단계부터)
- **진행 상황 공유**: 매일 오전 Slack 채널에 업데이트
- **질문 및 이슈**: Slack 또는 이메일로 PM에게 즉시 문의

### 7.2 UX 디자이너와 협업
- Week 4 말: 디자인 핸드오프 미팅
- Figma 파일 접근 권한 확보
- 디자인 QA: 개발 중 디자인 검증 요청
- 불명확한 부분: 즉시 UX 디자이너에게 문의

### 7.3 웹 기획자와 협업
- 기능 명세 확인
- 불명확한 기능: 웹 기획자에게 문의
- 기술적 제약: PM 및 웹 기획자와 협의

---

## 8. 품질 체크리스트

### 8.1 HTML 체크리스트
- [ ] 시맨틱 HTML 사용
- [ ] 모든 이미지에 alt 속성
- [ ] 폼 요소에 레이블 연결
- [ ] 메타 태그 작성 (Title, Description)
- [ ] Open Graph 태그

### 8.2 CSS 체크리스트
- [ ] BEM 네이밍 컨벤션
- [ ] CSS 변수 활용
- [ ] 반응형 디자인 (Mobile First)
- [ ] 크로스 브라우저 호환성
- [ ] 코드 압축 (프로덕션)

### 8.3 JavaScript 체크리스트
- [ ] ES6+ 문법 사용
- [ ] 에러 처리
- [ ] 접근성 (키보드 네비게이션)
- [ ] 성능 최적화 (Lazy Loading)
- [ ] 코드 압축 (프로덕션)

### 8.4 성능 체크리스트
- [ ] Lighthouse 점수 90점 이상
- [ ] 이미지 최적화 (WebP, 압축)
- [ ] Lazy Loading 적용
- [ ] CSS/JS 압축
- [ ] 캐싱 전략

### 8.5 접근성 체크리스트
- [ ] WAVE 에러 0개
- [ ] 키보드 네비게이션 가능
- [ ] 색상 대비 4.5:1 이상
- [ ] 스크린 리더 호환
- [ ] 포커스 인디케이터 명확

---

## 9. 성공 기준

### 9.1 기술 품질 기준
- 시맨틱 HTML 사용
- 반응형 디자인 완벽 구현
- 크로스 브라우저 호환성
- Lighthouse 점수 90점 이상
- 접근성 테스트 통과

### 9.2 성능 기준
- 페이지 로딩 속도 3초 이내
- LCP 2.5초 이하
- FID 100ms 이하
- CLS 0.1 이하

### 9.3 프로젝트 기여도
- 고품질 코드로 유지보수 용이
- 성능 최적화로 사용자 경험 향상
- 접근성 준수로 더 많은 사용자 포용
- 일정 준수로 프로젝트 성공

---

## 10. 다음 단계

### 10.1 즉시 실행 항목
1. `docs/hopage_renewal_content.md` 파일 정독
2. UX 디자이너 산출물 대기 (Week 4 말 제공)
3. 개발 환경 구축 (VS Code, Git)
4. 기술 스택 검토 및 라이브러리 조사

### 10.2 Week 5 목표
- **월요일**: UX 디자이너 핸드오프 미팅, 프로젝트 셋업
- **화요일-수요일**: 공통 요소 개발 (Header, Footer)
- **목요일-금요일**: 메인 페이지 마크업

### 10.3 Week 6-7 목표
- Week 6: 서브 페이지 마크업 완료
- Week 7: JavaScript 기능 구현 및 성능 최적화

---

## 11. 연락처 및 지원

### 11.1 PM 연락처
- **이름**: [PM 이름]
- **이메일**: [PM 이메일]
- **Slack**: @pm-website-renewal
- **근무 시간**: 평일 09:00 - 18:00

### 11.2 질문 및 지원
- **일반 질문**: Slack 채널 #homepage-renewal
- **긴급 이슈**: PM에게 직접 연락
- **디자인 문의**: UX 디자이너와 협의
- **기획 문의**: 웹 기획자와 협의

---

**작업 시작 전 이 문서를 반드시 숙지하시고, 질문 사항이 있으면 PM에게 문의해 주세요.**

**문서 버전**: 2.0 (업데이트)  
**작성일**: 2024  
**작성자**: PM (Product Manager)  
**검토자**: 프로젝트 팀  

**고품질 코드와 훌륭한 사용자 경험을 기대합니다!**
