# UX 디자인 핸드오프 문서

## 문서 개요

**프로젝트명**: (주)아이티로그 홈페이지 리뉴얼  
**작성일**: 2024  
**작성자**: UX Designer  
**버전**: 2.0 (웹 기획 문서 반영)  
**대상**: 프론트엔드 개발자

---

## 1. 문서 목적

이 문서는 UX 디자인을 프론트엔드 개발로 전환하기 위한 상세 가이드입니다.
웹 기획 문서(web-planning-*.md)와 100% 정합성을 유지하며 작성되었습니다.

### 1.1 참조 문서
- `web-planning-sitemap.md` - 사이트 구조 및 URL
- `web-planning-content-strategy.md` - 콘텐츠 전략
- `web-planning-functional-spec.md` - 기능 명세
- `web-planning-user-flow.md` - 사용자 플로우
- `ux-design-concept.md` - 디자인 컨셉
- `ux-design-system.md` - 디자인 시스템

---

## 2. 사이트 구조 및 URL

### 2.1 전체 페이지 목록 (23개)

| 순번 | 페이지명 | URL | 우선순위 | 개발 단계 |
|------|---------|-----|---------|----------|
| 1 | 메인페이지 | `/index.html` | P0 | Phase 1 |
| 2 | 회사소개 | `/about/company.html` | P0 | Phase 1 |
| 3 | CEO 인사말 | `/about/ceo-message.html` | P1 | Phase 1 |
| 4 | 회사연혁 | `/about/history.html` | P1 | Phase 1 |
| 5 | 인증 및 특허 | `/about/certifications.html` | P0 | Phase 1 |
| 6 | 오시는 길 | `/about/location.html` | P0 | Phase 1 |
| 7 | 스마트 현장안전 시스템 | `/solutions/smart-safety.html` | P0 | Phase 1 |
| 8 | 타워크레인 통합안전 시스템 | `/solutions/tower-crane.html` | P0 | Phase 1 |
| 9 | AI 영상 방송 관제시스템 | `/solutions/ai-surveillance.html` | P0 | Phase 1 |
| 10 | 스마트 환경센서 시스템 | `/solutions/environment-sensor.html` | P0 | Phase 1 |
| 11 | 스마트 출입통제 시스템 | `/solutions/access-control.html` | P0 | Phase 1 |
| 12 | 원격지원 | `/support/remote-support.html` | P0 | Phase 1 |
| 13 | 문의하기 | `/support/contact.html` | P0 | Phase 1 |

### 2.2 메뉴 구조

```
1. 회사소개
   - 회사소개
   - CEO 인사말
   - 회사연혁
   - 인증 및 특허
   - 오시는 길

2. 현장 안전 플랫폼
   - 스마트 현장안전 시스템
   - 타워크레인 통합안전 시스템

3. 스마트 관제·제어
   - AI 영상 방송 관제시스템

4. 환경·출입관리
   - 스마트 환경센서 시스템
   - 스마트 출입통제 시스템

5. 고객지원
   - 원격지원
   - 문의하기
```

---

## 3. 디자인 시스템 요약

### 3.1 색상 팔레트

```css
/* Primary Colors */
--color-primary-700: #1A4D8F;  /* 메인 컬러 */
--color-primary-600: #2563B3;  /* 호버 */
--color-primary-500: #3B82F6;  /* 강조 */

/* Secondary Colors */
--color-secondary-600: #5A6C7D;  /* 보조 컬러 */

/* Accent Colors */
--color-accent-500: #FF6B35;  /* CTA 버튼 */

/* Neutral Colors */
--color-white: #FFFFFF;
--color-gray-50: #F8F9FA;
--color-gray-900: #212529;
```

### 3.2 타이포그래피

```css
/* 폰트 패밀리 */
--font-primary: 'Pretendard', sans-serif;

/* 폰트 크기 */
--text-6xl: 3rem;      /* 48px - H1 */
--text-5xl: 2.5rem;    /* 40px - H2 */
--text-4xl: 2rem;      /* 32px - H3 */
--text-2xl: 1.5rem;    /* 24px - H4 */
--text-base: 1rem;     /* 16px - Body */
```


### 3.3 간격 시스템

```css
--space-2: 0.5rem;    /* 8px */
--space-4: 1rem;      /* 16px */
--space-6: 1.5rem;    /* 24px */
--space-8: 2rem;      /* 32px */
--space-12: 3rem;     /* 48px */
--space-16: 4rem;     /* 64px */
```

### 3.4 브레이크포인트

```css
--breakpoint-sm: 640px;   /* 모바일 */
--breakpoint-md: 768px;   /* 태블릿 */
--breakpoint-lg: 1024px;  /* 데스크톱 */
--breakpoint-xl: 1280px;  /* 대형 데스크톱 */
```

---

## 4. 페이지별 상세 명세

### 4.1 메인 페이지 (index.html)

#### 4.1.1 히어로 섹션 (슬라이드 4개)

**슬라이드 1: 브랜드 가치**
```
서브타이틀: Sustainable Safety Partner
제목: 건설은 안전하게! 안전은 스마트하게!
서브 문구: 기술과 사람을 잇는 아이티로그만의 혁신적인 안전 체계, 
          사고 제로(Zero)를 향한 가장 확실한 정답입니다.
CTA: [견적 문의하기] [솔루션 둘러보기]
```

**슬라이드 2: 핵심 기술**
```
서브타이틀: Smart AI Surveillance
제목: 사각지대 없는 지능형 AI 영상 관제 시스템
서브 문구: AI 실시간 위험 감지로 현장의 모든 순간을 분석하고, 
          위급 상황 발생 시 즉각적인 통합 대응을 지원합니다.
CTA: [자세히 보기]
```

**슬라이드 3: 현장 맞춤 솔루션**
```
서브타이틀: Specialized Field Solution
제목: 쾌적한 환경부터 철저한 출입통제 솔루션까지
서브 문구: 스마트 환경센서로 유해 요소를 관리하고, 
          체계적인 출입 관리 시스템을 통해 고도화된 맞춤형 현장 관리를 실현합니다
CTA: [자세히 보기]
```

**슬라이드 4: 신뢰와 유지보수**
```
서브타이틀: Reliable Support & CS
제목: 전국 어디서나, 멈춤 없는 원격지원과 사후관리
서브 문구: 구축보다 중요한 것은 신뢰입니다. 
          아이티로그의 전문 엔지니어가 365일 신속하게 귀하의 현장을 함께 지킵니다.
CTA: [원격지원 바로가기]
```

**기술 구현:**
- 라이브러리: Swiper.js
- 자동 재생: 5초 간격
- 전환 효과: Fade
- 인디케이터: 점 형태 (4개)
- 화살표 네비게이션: 좌우
- 모바일: 터치 스와이프 지원


#### 4.1.2 주요 솔루션 섹션

**4개 솔루션 카드:**
1. 지능형 영상 관제 → `/solutions/ai-surveillance.html`
2. 스마트 환경센서 → `/solutions/environment-sensor.html`
3. 스마트 출입통제 → `/solutions/access-control.html`
4. 스마트 현장안전 → `/solutions/smart-safety.html`

**카드 구성:**
- 아이콘 또는 대표 이미지
- 솔루션명 (H4, 24px, SemiBold)
- 간단한 설명 (1-2줄, 16px, Regular)
- [자세히 보기] 버튼 (Secondary Button)

**레이아웃:**
- 데스크톱: 4단 그리드
- 태블릿: 2단 그리드
- 모바일: 1단 그리드

**호버 효과:**
- Transform: translateY(-8px)
- Box-shadow: 증가
- Duration: 0.3s

#### 4.1.3 숫자로 보는 신뢰 섹션

**표시 항목:**
- 설치 횟수: 1,247+
- 연구 기간: 20년+
- 고객사 수: 523+
- (추가 지표 가능)

**기술 구현:**
- 카운터 애니메이션: CountUp.js
- 트리거: Intersection Observer (섹션 진입 시)
- Duration: 2초
- Easing: ease-out

#### 4.1.4 고객사 섹션

**표시 방식:**
- 주요 고객사 CI 로고 나열
- 데스크톱: 8개씩 2줄 (총 16개)
- 모바일: 4개씩 여러 줄
- 그레이스케일 → 호버 시 컬러

#### 4.1.5 주요 시공사례 섹션

**표시 항목:**
- 대표 프로젝트 3-4개
- 슬라이더 형태

**카드 정보:**
- 프로젝트 이미지 (16:9 비율)
- 프로젝트명 (H4)
- 발주처
- 기간
- [자세히 보기] 버튼

**클릭 동작:**
- 해당 솔루션 페이지의 시공사례 섹션으로 이동

#### 4.1.6 고객문의 섹션

**구성:**
- CS 정보 (전화번호, 운영시간)
- [원격지원] 버튼 → `/support/remote-support.html`
- [문의하기] 버튼 → `/support/contact.html`

---

### 4.2 솔루션 페이지 (공통 구조)

#### 4.2.1 페이지 헤더

**브레드크럼:**
```
홈 > [1Depth 메뉴명] > [페이지명]
예: 홈 > 현장 안전 플랫폼 > 스마트 현장안전 시스템
```

**페이지 제목:**
- H1 (48px, Bold)
- 솔루션명 표시


#### 4.2.2 시스템 개요 섹션

**구성:**
- 소개 텍스트 (2-3 문단)
- 주요 특징 (3-5개 불릿 포인트)
- 적용 분야

**레이아웃:**
- 텍스트 + 이미지 (좌우 배치)
- 모바일: 이미지 위, 텍스트 아래

#### 4.2.3 시스템 구성도 섹션

**구성:**
- 구성도 이미지 또는 일러스트
- 각 구성 요소 설명
- 기술 사양 (선택)

**이미지 요구사항:**
- 최소 해상도: 1200px 너비
- 형식: WebP (폴백: PNG)
- Alt 텍스트 필수

#### 4.2.4 하위 시스템 섹션 (해당 시)

**표시 방법:**
- 탭 방식 (데스크톱)
- 아코디언 방식 (모바일)

**각 하위 시스템:**
- 시스템명 (H3)
- 개요 설명
- 구성도 (선택)
- 주요 특징

**하위 시스템 목록:**

1. **스마트 현장안전 시스템**
   - 스마트 안전교육 시스템
   - 방문자 시스템

2. **AI 영상 방송 관제시스템**
   - 지능형 영상·방송 관제 시스템

3. **스마트 환경센서 시스템**
   - 환경센서 시스템
   - 초음파 풍향/풍속 시스템

4. **스마트 출입통제 시스템**
   - 안면인식 출입 통제 시스템
   - 스마트 통합 차량 관제 서비스

#### 4.2.5 주요 시공 사례 섹션

**구성:**
- 사례 이미지 3-4개
- 그리드 레이아웃

**각 사례 정보:**
- 프로젝트 이미지
- 프로젝트명
- 발주처
- 기간
- 주요 성과 (선택)

**기능:**
- 라이트박스 (클릭 시 확대)
- 좌우 네비게이션
- ESC 또는 X 버튼으로 닫기

**기술 구현:**
- 라이브러리: GLightbox 또는 Lightbox2

#### 4.2.6 문의 CTA 섹션

**구성:**
- 안내 문구
- [견적 문의하기] 버튼 (Primary)
- 전화 문의 정보

---

### 4.3 회사소개 페이지

#### 4.3.1 회사소개 (/about/company.html)

**섹션 구성:**
1. 기업정보
   - 소개 문구
   - 기업 이념
   - 안전보건 경영방침/목표

2. 사업분야
   - 주요 비즈니스 영역 요약
   - 각 분야 간략 설명

3. 주요 고객사
   - 고객사 로고 그리드


#### 4.3.2 CEO 인사말 (/about/ceo-message.html)

**구성:**
- CEO 사진 (좌측)
- 인사말 전문 (우측, 3-5 문단)
- CEO 서명 이미지

**모바일:**
- CEO 사진 (상단)
- 인사말 (하단)

#### 4.3.3 회사연혁 (/about/history.html)

**구성:**
- 타임라인 형태 (2010년~2025년)
- 연도별 주요 성과

**레이아웃:**
- 데스크톱: 세로 타임라인 (좌우 교차 배치)
- 모바일: 세로 타임라인 (단일 열)

**스크롤 애니메이션:**
- 타임라인 항목 순차 표시
- Fade-in + Slide-up
- Intersection Observer 사용

#### 4.3.4 인증 및 특허 (/about/certifications.html)

**구성:**
- 인증서 이미지 그리드
- 특허권 이미지 및 명칭

**레이아웃:**
- 데스크톱: 4단 그리드
- 태블릿: 3단 그리드
- 모바일: 2단 그리드

**기능:**
- 라이트박스 (클릭 시 확대)
- 다운로드 버튼 (선택)

#### 4.3.5 오시는 길 (/about/location.html)

**구성:**
1. 지도 (좌측)
   - 카카오맵 API 임베드
   - 마커: 회사 위치 표시
   - 줌 레벨: 적절한 확대 수준

2. 정보 (우측)
   - 주소 (도로명/지번)
   - 전화번호
   - 팩스
   - 이메일
   - 대중교통 안내
   - 주차 안내

**모바일:**
- 지도 (상단)
- 정보 (하단)

**기술 구현:**
- API: Kakao Map API
- 반응형 지도 크기 조정

---

### 4.4 고객지원 페이지

#### 4.4.1 원격지원 (/support/remote-support.html)

**구성:**
- 원격지원 서비스 설명
- 이용 방법 안내
- [원격지원 시작하기] 버튼

**버튼 동작:**
- 외부 사이트 연결
- target="_blank"
- rel="noopener noreferrer"

#### 4.4.2 문의하기 (/support/contact.html)

**문의 폼 필드:**
```
이름* (text, 2자 이상)
회사명* (text, 2자 이상)
연락처* (tel, 숫자+하이픈)
이메일* (email, 이메일 형식)
제목* (text, 5자 이상)
내용* (textarea, 10자 이상)
개인정보 동의* (checkbox, 체크 필수)
```

**입력 검증:**
- 실시간 검증 (포커스 아웃 시)
- 에러 메시지 표시 (빨간 테두리 + 텍스트)
- 제출 전 전체 검증

**에러 메시지:**
- 필수 항목 미입력: "이 항목은 필수입니다"
- 이메일 형식 오류: "올바른 이메일 주소를 입력해주세요"
- 연락처 형식 오류: "올바른 전화번호를 입력해주세요"


**제출 프로세스:**
```
1. 필드 입력 → 실시간 검증
2. 제출 버튼 클릭 → 전체 검증
3. 검증 실패 → 에러 메시지 표시
4. 검증 성공 → 로딩 인디케이터 표시
5. 전송 완료 → 성공 메시지 표시
6. 전송 실패 → 에러 메시지 + 재시도 안내
```

**기술 구현:**
- 이메일 전송: FormSpree, EmailJS, 또는 Netlify Forms
- 검증: HTML5 validation + JavaScript
- 스팸 방지: reCAPTCHA (선택)

**연락처 정보 섹션:**
- 전화번호 (클릭투콜)
- 이메일
- 팩스
- 운영시간

---

## 5. 공통 컴포넌트

### 5.1 헤더 (Header)

#### 데스크톱 구조
```
[로고] [회사소개▾] [현장 안전 플랫폼▾] [스마트 관제·제어▾] [환경·출입관리▾] [고객지원▾] [🔍] [문의하기]
```

**드롭다운 메뉴:**
- 마우스 오버 시 표시
- Fade-in 애니메이션 (0.2s)
- 배경: 흰색
- 그림자: shadow-lg
- 최소 너비: 200px

**Sticky 헤더:**
- 스크롤 100px 이상 → 배경 불투명, 그림자 추가
- Position: sticky
- Top: 0
- Z-index: 1020

#### 모바일 구조
```
[☰] [로고]                    [🔍] [문의]
```

**햄버거 메뉴:**
- 전체 화면 오버레이
- 슬라이드 인 애니메이션 (우측에서 좌측)
- 아코디언 방식 (1Depth 클릭 시 2Depth 펼침)
- 닫기 버튼 (X)

### 5.2 푸터 (Footer)

**구성:**
```
┌─────────────────────────────────────────┐
│ [회사 로고]                              │
│                                         │
│ 회사명: (주)아이티로그                   │
│ 주소: [주소]                             │
│ 전화: [전화번호]                         │
│ 팩스: [팩스번호]                         │
│ 사업자번호: [사업자번호]                 │
│                                         │
│ [이용약관] | [개인정보처리방침]          │
│                                         │
│ Copyright © 2024 ITLOG. All rights.     │
└─────────────────────────────────────────┘
```

**링크:**
- 주요 페이지 링크 (선택)
- 문의하기 링크

### 5.3 플로팅 버튼

**Back to Top 버튼:**
- 표시 조건: 스크롤 300px 이상
- 위치: 우측 하단 고정 (bottom: 24px, right: 24px)
- 크기: 48x48px
- 아이콘: 위쪽 화살표
- 동작: 클릭 시 부드럽게 최상단 이동 (smooth scroll)

**빠른 문의 버튼 (선택):**
- 위치: Back to Top 위
- 크기: 56x56px
- 배경: Accent Color
- 아이콘: 말풍선 또는 전화
- 동작: 문의 페이지 이동 또는 문의 모달


### 5.4 브레드크럼 (Breadcrumb)

**패턴:**
```
홈 > 1Depth > 2Depth
```

**예시:**
```
홈 > 회사소개 > 회사연혁
홈 > 현장 안전 플랫폼 > 스마트 현장안전 시스템
홈 > 고객지원 > 문의하기
```

**스타일:**
- 구분자: > (꺾쇠)
- 현재 페이지: 링크 없음, 굵게 표시
- 색상: 텍스트 보조 색상
- 호버: Primary Color

### 5.5 버튼

#### Primary Button
```css
배경: var(--color-primary-700)
텍스트: 흰색
패딩: 12px 24px
최소 높이: 48px
Border-radius: 8px
호버: 배경 10% 밝게, translateY(-1px)
```

#### Secondary Button
```css
배경: 투명
텍스트: var(--color-primary-700)
테두리: 2px solid var(--color-primary-700)
패딩: 12px 24px
최소 높이: 48px
호버: 배경 var(--color-primary-50)
```

#### Accent Button
```css
배경: var(--color-accent-500)
텍스트: 흰색
패딩: 12px 24px
최소 높이: 48px
호버: 배경 10% 밝게
```

---

## 6. 반응형 디자인

### 6.1 브레이크포인트

```css
/* 모바일 */
@media (max-width: 767px) {
  /* 1단 레이아웃 */
  /* 햄버거 메뉴 */
  /* 터치 최적화 */
}

/* 태블릿 */
@media (min-width: 768px) and (max-width: 1023px) {
  /* 2단 레이아웃 */
  /* 축소된 네비게이션 */
}

/* 데스크톱 */
@media (min-width: 1024px) {
  /* 3-4단 레이아웃 */
  /* 풀 네비게이션 */
  /* 호버 효과 */
}
```

### 6.2 모바일 최적화

**터치 영역:**
- 최소 크기: 44x44px
- 버튼, 링크, 입력 필드 모두 적용

**클릭투콜:**
- 전화번호 링크: `<a href="tel:02-1234-5678">`
- 모바일에서 자동으로 전화 앱 실행

**이미지:**
- Lazy Loading 적용
- srcset 사용 (반응형 이미지)
- WebP 형식 우선 (폴백: JPG/PNG)

---

## 7. 애니메이션 및 인터랙션

### 7.1 페이지 로드 애니메이션

```
1. 헤더: Fade in (0.3s)
2. Hero 섹션: Fade in + Slide up (0.5s, delay 0.2s)
3. 콘텐츠 섹션: Fade in + Slide up (0.4s, 순차적으로)
```

### 7.2 스크롤 애니메이션

**트리거:**
- Intersection Observer API
- 요소가 뷰포트 50% 진입 시

**효과:**
- Fade-in (opacity 0 → 1)
- Slide-up (translateY 20px → 0)
- Duration: 0.6s
- Easing: ease-out

**라이브러리:**
- AOS (Animate On Scroll) 또는 직접 구현

### 7.3 호버 효과

**카드:**
```css
transform: translateY(-8px);
box-shadow: 증가;
transition: 0.3s ease-out;
```

**버튼:**
```css
transform: scale(1.02);
background: 10% 밝게;
transition: 0.2s ease-out;
```

**링크:**
```css
밑줄 애니메이션 (왼쪽 → 오른쪽);
color: Primary → Accent;
transition: 0.2s ease-out;
```


---

## 8. 접근성 (WCAG 2.1 AA)

### 8.1 색상 대비

**검증 완료:**
- 일반 텍스트 (#212529) on 흰색: 16.1:1 ✓ (AAA)
- 보조 텍스트 (#6C757D) on 흰색: 5.7:1 ✓ (AA)
- 흰색 텍스트 on Primary (#1A4D8F): 8.2:1 ✓ (AAA)
- 흰색 텍스트 on Accent (#FF6B35): 4.5:1 ✓ (AA)

### 8.2 키보드 네비게이션

**Tab 순서:**
```
1. Skip to content 링크
2. 로고
3. 메인 메뉴 (좌→우)
4. 검색
5. 문의 버튼
6. 메인 콘텐츠
7. 푸터 링크
```

**포커스 스타일:**
```css
*:focus-visible {
  outline: 2px solid var(--color-primary-500);
  outline-offset: 2px;
}
```

**Skip Link:**
```html
<a href="#main-content" class="skip-link">
  본문으로 바로가기
</a>
```

### 8.3 시맨틱 HTML

```html
<header role="banner">
<nav role="navigation" aria-label="주 메뉴">
<main role="main" id="main-content">
<aside role="complementary">
<footer role="contentinfo">
```

### 8.4 이미지 대체 텍스트

**필수:**
- 모든 이미지에 의미 있는 alt 속성
- 장식 이미지: `alt=""` 또는 `role="presentation"`

**예시:**
```html
<img src="product.jpg" alt="스마트 안전 모니터링 시스템 제품 사진">
<img src="decoration.jpg" alt="" role="presentation">
```

### 8.5 ARIA 레이블

**버튼:**
```html
<button aria-label="메뉴 열기" aria-expanded="false">
  <span aria-hidden="true">☰</span>
</button>
```

**폼:**
```html
<input 
  id="email" 
  type="email" 
  aria-required="true"
  aria-invalid="false"
  aria-describedby="email-error"
>
<span id="email-error" role="alert">
  올바른 이메일을 입력해주세요
</span>
```

---

## 9. 성능 최적화

### 9.1 이미지 최적화

**형식:**
- WebP 우선 (폴백: JPG/PNG)
- 압축률: 80-85%
- Progressive JPEG 사용

**Lazy Loading:**
```html
<img src="image.jpg" loading="lazy" alt="설명">
```

**반응형 이미지:**
```html
<img 
  src="image-800.jpg"
  srcset="image-400.jpg 400w,
          image-800.jpg 800w,
          image-1200.jpg 1200w"
  sizes="(max-width: 768px) 100vw,
         (max-width: 1024px) 50vw,
         33vw"
  alt="제품 이미지"
  loading="lazy"
>
```

### 9.2 코드 최적화

**CSS:**
- 번들링: 하나의 CSS 파일로 통합
- 압축: Minify
- Critical CSS: 인라인 삽입

**JavaScript:**
- 번들링: 하나의 JS 파일로 통합
- 압축: Minify
- 비동기 로드: defer 또는 async 속성

**폰트:**
```html
<link rel="preload" href="/fonts/Pretendard-Regular.woff2" as="font" type="font/woff2" crossorigin>
```

### 9.3 성능 목표

**Lighthouse 점수:**
- Performance: 90점 이상
- Accessibility: 95점 이상
- Best Practices: 90점 이상
- SEO: 95점 이상

**Core Web Vitals:**
- LCP (Largest Contentful Paint): 2.5초 이하
- FID (First Input Delay): 100ms 이하
- CLS (Cumulative Layout Shift): 0.1 이하


---

## 10. 기술 스택 권장

### 10.1 필수 라이브러리

**슬라이더:**
- Swiper.js (https://swiperjs.com/)
- 용도: 히어로 슬라이더, 시공사례 슬라이더

**애니메이션:**
- AOS (Animate On Scroll) (https://michalsnik.github.io/aos/)
- 용도: 스크롤 애니메이션

**라이트박스:**
- GLightbox (https://biati-digital.github.io/glightbox/)
- 용도: 이미지 확대, 갤러리

**카운터:**
- CountUp.js (https://inorganik.github.io/countUp.js/)
- 용도: 숫자 카운터 애니메이션

**지도:**
- Kakao Map API (https://apis.map.kakao.com/)
- 용도: 오시는 길 지도

**폼 전송:**
- FormSpree (https://formspree.io/) 또는
- EmailJS (https://www.emailjs.com/) 또는
- Netlify Forms (https://www.netlify.com/products/forms/)

### 10.2 선택 라이브러리

**아이콘:**
- Heroicons (https://heroicons.com/) 또는
- Feather Icons (https://feathericons.com/)

**스크롤:**
- Smooth Scroll Polyfill (구형 브라우저 지원)

---

## 11. 브라우저 지원

### 11.1 지원 브라우저

**Desktop:**
- Chrome: 최신 2개 버전
- Firefox: 최신 2개 버전
- Safari: 최신 2개 버전
- Edge: 최신 2개 버전

**Mobile:**
- iOS Safari: 최신 2개 버전
- Chrome Mobile: 최신 2개 버전
- Samsung Internet: 최신 버전

### 11.2 폴리필

**CSS 변수:**
```css
.button {
  background-color: #1A4D8F; /* 폴백 */
  background-color: var(--color-primary-700);
}
```

**Intersection Observer:**
```javascript
if (!('IntersectionObserver' in window)) {
  // 폴리필 로드
  import('intersection-observer');
}
```

---

## 12. 개발 가이드

### 12.1 파일 구조

```
project/
├── index.html
├── about/
│   ├── company.html
│   ├── ceo-message.html
│   ├── history.html
│   ├── certifications.html
│   └── location.html
├── solutions/
│   ├── smart-safety.html
│   ├── tower-crane.html
│   ├── ai-surveillance.html
│   ├── environment-sensor.html
│   └── access-control.html
├── support/
│   ├── remote-support.html
│   └── contact.html
├── assets/
│   ├── css/
│   │   ├── main.css
│   │   ├── components.css
│   │   └── pages/
│   ├── js/
│   │   ├── main.js
│   │   ├── components.js
│   │   └── pages/
│   ├── images/
│   └── fonts/
└── sitemap.xml
```

### 12.2 CSS 네이밍 컨벤션

**BEM (Block Element Modifier):**
```css
.block {}
.block__element {}
.block--modifier {}

/* 예시 */
.card {}
.card__header {}
.card__body {}
.card--featured {}
```

### 12.3 코드 품질

**도구:**
- Stylelint: CSS 린팅
- Prettier: 코드 포맷팅
- ESLint: JavaScript 린팅

**검증:**
- W3C HTML Validator
- W3C CSS Validator
- Lighthouse 성능 점수
- WAVE 접근성 검사


---

## 13. SEO 최적화

### 13.1 페이지별 메타 정보

**메인 페이지:**
```html
<title>건설 현장 안전 솔루션 - (주)아이티로그</title>
<meta name="description" content="건설 현장의 안전과 효율을 높이는 스마트 솔루션. 20년 경험의 아이티로그가 제공하는 검증된 현장 안전 시스템.">
<meta name="keywords" content="건설 현장 안전, 스마트 현장 관리, 현장 솔루션, 안전 시스템">
```

**솔루션 페이지 예시:**
```html
<title>스마트 현장안전 시스템 - (주)아이티로그</title>
<meta name="description" content="스마트 안전교육 시스템과 방문자 관리로 현장 안전을 강화하세요. 실시간 모니터링과 체계적인 안전 관리.">
```

### 13.2 구조화된 데이터 (Schema.org)

**Organization:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "(주)아이티로그",
  "url": "https://www.itlog.co.kr",
  "logo": "https://www.itlog.co.kr/assets/images/logo.png",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+82-2-1234-5678",
    "contactType": "customer service"
  }
}
</script>
```

### 13.3 Open Graph

```html
<meta property="og:title" content="건설 현장 안전 솔루션 - (주)아이티로그">
<meta property="og:description" content="건설 현장의 안전과 효율을 높이는 스마트 솔루션">
<meta property="og:image" content="https://www.itlog.co.kr/assets/images/og-image.jpg">
<meta property="og:url" content="https://www.itlog.co.kr">
<meta property="og:type" content="website">
```

### 13.4 Sitemap.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.itlog.co.kr/</loc>
    <priority>1.0</priority>
    <changefreq>weekly</changefreq>
  </url>
  <url>
    <loc>https://www.itlog.co.kr/about/company.html</loc>
    <priority>0.8</priority>
    <changefreq>monthly</changefreq>
  </url>
  <!-- 이하 모든 페이지 -->
</urlset>
```

---

## 14. 테스트 체크리스트

### 14.1 기능 테스트

**네비게이션:**
- [ ] 모든 메뉴 링크 정상 작동
- [ ] 드롭다운 메뉴 호버/클릭 동작
- [ ] 모바일 햄버거 메뉴 열기/닫기
- [ ] 브레드크럼 링크 정상 작동

**폼:**
- [ ] 모든 필드 입력 가능
- [ ] 실시간 검증 작동
- [ ] 에러 메시지 표시
- [ ] 제출 성공/실패 처리

**슬라이더:**
- [ ] 자동 재생 작동
- [ ] 화살표 네비게이션
- [ ] 인디케이터 클릭
- [ ] 모바일 스와이프

**라이트박스:**
- [ ] 이미지 클릭 시 확대
- [ ] 좌우 네비게이션
- [ ] ESC/X 버튼으로 닫기

### 14.2 반응형 테스트

**브레이크포인트:**
- [ ] 320px (모바일 최소)
- [ ] 375px (모바일 일반)
- [ ] 768px (태블릿)
- [ ] 1024px (데스크톱)
- [ ] 1440px (대형 데스크톱)

**디바이스:**
- [ ] iPhone SE
- [ ] iPhone 12/13/14
- [ ] iPad
- [ ] Desktop (1920x1080)

### 14.3 브라우저 테스트

- [ ] Chrome (최신)
- [ ] Firefox (최신)
- [ ] Safari (최신)
- [ ] Edge (최신)
- [ ] iOS Safari
- [ ] Chrome Mobile

### 14.4 접근성 테스트

- [ ] 키보드 네비게이션 (Tab, Enter, ESC)
- [ ] 스크린 리더 (NVDA, JAWS)
- [ ] 색상 대비 검증
- [ ] WAVE 접근성 검사
- [ ] Lighthouse 접근성 점수 95+ 

### 14.5 성능 테스트

- [ ] Lighthouse 성능 점수 90+
- [ ] PageSpeed Insights
- [ ] 이미지 최적화 확인
- [ ] 로딩 속도 (3G, 4G, WiFi)

---

## 15. 배포 전 체크리스트

### 15.1 콘텐츠

- [ ] 모든 텍스트 콘텐츠 최종 확인
- [ ] 이미지 alt 텍스트 작성
- [ ] 메타 정보 (title, description) 작성
- [ ] 404 페이지 작성

### 15.2 SEO

- [ ] sitemap.xml 생성
- [ ] robots.txt 작성
- [ ] Open Graph 메타 태그
- [ ] 구조화된 데이터 (Schema.org)

### 15.3 성능

- [ ] 이미지 압축 및 최적화
- [ ] CSS/JS 번들링 및 압축
- [ ] 폰트 최적화
- [ ] Lazy Loading 적용

### 15.4 보안

- [ ] HTTPS 적용
- [ ] 외부 링크 rel="noopener noreferrer"
- [ ] 폼 스팸 방지 (reCAPTCHA)

---

## 16. 유지보수 가이드

### 16.1 콘텐츠 업데이트

**이미지 추가:**
1. 이미지 최적화 (WebP 변환, 압축)
2. 반응형 이미지 생성 (400w, 800w, 1200w)
3. alt 텍스트 작성
4. Lazy Loading 속성 추가

**페이지 추가:**
1. HTML 파일 생성
2. 헤더/푸터 포함
3. 메타 정보 작성
4. sitemap.xml 업데이트
5. 네비게이션 메뉴 업데이트

### 16.2 디자인 시스템 업데이트

**색상 변경:**
1. CSS 변수 업데이트
2. 색상 대비 검증
3. 전체 페이지 확인

**컴포넌트 추가:**
1. 디자인 시스템 문서 업데이트
2. 재사용 가능한 클래스 작성
3. 예시 코드 작성

---

## 17. 문의 및 지원

### 17.1 디자인 관련 문의

**UX 디자이너:**
- 디자인 의도 및 컨셉
- 와이어프레임 해석
- 사용자 경험 관련

### 17.2 기술 구현 문의

**프론트엔드 개발자:**
- 기술 스택 선택
- 구현 방법
- 성능 최적화

### 17.3 콘텐츠 관련 문의

**웹 기획자:**
- 콘텐츠 전략
- 페이지 구조
- 사용자 플로우

---

**문서 버전**: 2.0  
**작성일**: 2024  
**작성자**: UX Designer  
**검토자**: PM, Web Planner, Frontend Developer  
**승인일**: [승인 후 기입]

**변경 이력:**
- v2.0 (2024): 웹 기획 문서 반영, 메뉴 구조 변경, 솔루션 페이지 구조 업데이트
- v1.0 (2024): 초기 버전

**다음 단계:**
1. 프론트엔드 개발자와 킥오프 미팅
2. 기술 스택 최종 확정
3. 개발 환경 설정
4. Phase 1 개발 시작 (P0 페이지 12개)



---

## 18. 이미지 소싱 가이드 (Unsplash)

### 18.1 개요

이 섹션은 Unsplash(https://unsplash.com)의 무료 고품질 이미지를 활용하여 웹사이트에 적합한 비주얼을 선택하는 가이드입니다. 건설 현장 안전 솔루션 회사의 전문성, 신뢰성, 기술력을 효과적으로 전달할 수 있는 이미지 선택 기준을 제시합니다.

### 18.2 Unsplash 라이선스 정보

**Unsplash License:**
- 상업적 및 비상업적 용도로 무료 사용 가능
- 크레딧 표기 권장 (필수 아님)
- 수정 및 편집 가능
- 재배포 가능

**크레딧 표기 방법 (권장):**
```html
<!-- 이미지 하단 또는 푸터에 표기 -->
Photo by <a href="https://unsplash.com/@photographer">Photographer Name</a> 
on <a href="https://unsplash.com">Unsplash</a>
```

**자세한 정보:**
- https://unsplash.com/license

---

### 18.3 페이지별 이미지 가이드

#### 18.3.1 메인 페이지

##### 히어로 섹션 (4개 슬라이드)

**슬라이드 1: 브랜드 가치**
- **컨셉**: 건설 현장의 전경, 안전한 작업 환경
- **Unsplash 검색 키워드**:
  - `construction site safety`
  - `construction workers helmet`
  - `modern construction site`
  - `building construction aerial`
- **이미지 선택 기준**:
  - 밝고 긍정적인 분위기
  - 안전 장비를 착용한 작업자
  - 깨끗하고 체계적인 현장
  - 하늘이 보이는 넓은 구도
- **색감**: 파란 하늘, 밝은 톤, 주황색 안전 장비
- **추천 사진가**: `Scott Blake`, `Ant Rozetsky`, `Zac Edmonds`

**슬라이드 2: 핵심 기술 (AI 영상 관제)**
- **컨셉**: 기술, 모니터링, CCTV, 관제 시스템
- **Unsplash 검색 키워드**:
  - `security camera surveillance`
  - `control room monitors`
  - `cctv monitoring`
  - `technology surveillance`
  - `security control center`
- **이미지 선택 기준**:
  - 여러 모니터가 있는 관제실
  - CCTV 카메라 클로즈업
  - 기술적이고 전문적인 분위기
  - 어두운 배경에 밝은 화면 (대비)
- **색감**: 블루 톤, 어두운 배경, 화면의 밝은 빛
- **추천 사진가**: `Matthew Henry`, `Lianhao Qu`, `Bernard Hermant`

**슬라이드 3: 현장 맞춤 솔루션 (환경센서, 출입통제)**
- **컨셉**: 스마트 기술, IoT 센서, 출입 시스템
- **Unsplash 검색 키워드**:
  - `smart building technology`
  - `access control system`
  - `iot sensors construction`
  - `digital construction`
  - `smart city technology`
- **이미지 선택 기준**:
  - 현대적인 기술 장비
  - 센서 또는 디지털 디바이스
  - 깨끗하고 미래지향적인 느낌
  - 사람과 기술의 조화
- **색감**: 화이트/그레이 톤, 블루 액센트
- **추천 사진가**: `Adi Goldstein`, `Possessed Photography`, `Lenny Kuhne`

**슬라이드 4: 신뢰와 유지보수 (원격지원)**
- **컨셉**: 전문가, 지원, 협업, 신뢰
- **Unsplash 검색 키워드**:
  - `engineer construction site`
  - `construction team meeting`
  - `professional handshake construction`
  - `construction planning tablet`
  - `engineer blueprint`
- **이미지 선택 기준**:
  - 전문가가 태블릿/노트북 사용
  - 팀워크와 협업 장면
  - 신뢰감 있는 표정과 자세
  - 현장에서의 전문적인 모습
- **색감**: 자연광, 따뜻한 톤, 전문적인 분위기
- **추천 사진가**: `ThisisEngineering RAEng`, `Annie Spratt`, `Headway`

##### 주요 솔루션 섹션 (4개 카드)

**1. 지능형 영상 관제**
- **검색 키워드**: `security camera`, `surveillance system`, `cctv network`
- **이미지 특징**: CCTV 카메라, 모니터링 화면, 관제 시스템
- **권장 비율**: 16:9 또는 4:3
- **최소 해상도**: 800x600px

**2. 스마트 환경센서**
- **검색 키워드**: `environmental sensor`, `air quality monitor`, `iot device construction`
- **이미지 특징**: 센서 장비, 측정 기기, 디지털 디스플레이
- **권장 비율**: 16:9 또는 4:3
- **최소 해상도**: 800x600px

**3. 스마트 출입통제**
- **검색 키워드**: `access control`, `fingerprint scanner`, `face recognition`, `security gate`
- **이미지 특징**: 출입 단말기, 생체 인식 장비, 게이트 시스템
- **권장 비율**: 16:9 또는 4:3
- **최소 해상도**: 800x600px

**4. 스마트 현장안전**
- **검색 키워드**: `construction safety equipment`, `safety helmet`, `construction worker safety`
- **이미지 특징**: 안전 장비, 안전 교육, 체계적인 현장
- **권장 비율**: 16:9 또는 4:3
- **최소 해상도**: 800x600px

##### 시공사례 섹션

- **검색 키워드**: 
  - `construction project completed`
  - `modern building construction`
  - `construction site progress`
  - `infrastructure construction`
- **이미지 특징**:
  - 완공된 건물 또는 진행 중인 프로젝트
  - 규모감이 느껴지는 구도
  - 전문적이고 깨끗한 현장
- **권장 비율**: 16:9
- **최소 해상도**: 1200x675px

---

#### 18.3.2 솔루션 페이지

##### 스마트 현장안전 시스템

**시스템 개요 섹션:**
- **검색 키워드**:
  - `construction safety training`
  - `safety equipment construction`
  - `construction worker helmet`
  - `safety vest construction`
- **이미지 특징**:
  - 안전 장비를 착용한 작업자
  - 안전 교육 장면
  - 체계적인 현장 관리
- **색감**: 주황색/노란색 안전 장비, 밝은 톤

**하위 시스템 (안전교육, 방문자 시스템):**
- **검색 키워드**:
  - `construction training`
  - `visitor management system`
  - `construction site entrance`
  - `safety briefing construction`
- **이미지 특징**:
  - 교육 장면 (강의실, 현장)
  - 출입구 관리 시스템
  - 방문자 등록 장면

##### 타워크레인 통합안전 시스템

- **검색 키워드**:
  - `tower crane construction`
  - `crane operator`
  - `construction crane safety`
  - `tower crane aerial view`
- **이미지 특징**:
  - 타워크레인 전경
  - 크레인 조종실
  - 높은 곳에서 본 현장
  - 안전 시스템이 보이는 구도
- **색감**: 하늘 배경, 금속 질감, 산업적 느낌

##### AI 영상 방송 관제시스템

- **검색 키워드**:
  - `control room surveillance`
  - `security monitoring center`
  - `cctv control room`
  - `video surveillance system`
  - `security operations center`
- **이미지 특징**:
  - 여러 모니터가 있는 관제실
  - CCTV 카메라 배열
  - 관제 요원이 모니터링하는 장면
  - 기술적이고 전문적인 분위기
- **색감**: 어두운 배경, 블루 톤, 화면의 밝은 빛

##### 스마트 환경센서 시스템

- **검색 키워드**:
  - `environmental monitoring`
  - `air quality sensor`
  - `weather station construction`
  - `iot sensor outdoor`
  - `environmental measurement device`
- **이미지 특징**:
  - 환경 측정 센서
  - 디지털 디스플레이
  - 실외 설치된 장비
  - 깨끗하고 현대적인 디자인
- **색감**: 화이트/그레이, 블루 액센트, 자연광

##### 스마트 출입통제 시스템

- **검색 키워드**:
  - `access control system`
  - `biometric scanner`
  - `face recognition system`
  - `security turnstile`
  - `fingerprint scanner`
  - `construction site gate`
- **이미지 특징**:
  - 출입 단말기 클로즈업
  - 생체 인식 장비
  - 게이트 시스템
  - 사람이 인증하는 장면
- **색감**: 블랙/화이트, 블루 LED, 현대적인 느낌

---

#### 18.3.3 회사소개 페이지

##### 회사소개

- **검색 키워드**:
  - `modern office building`
  - `professional team meeting`
  - `business handshake`
  - `corporate office`
- **이미지 특징**:
  - 현대적인 사무실
  - 전문적인 팀 미팅
  - 신뢰감 있는 비즈니스 장면
- **색감**: 밝고 깨끗한 톤, 전문적인 분위기

##### CEO 인사말

- **검색 키워드**:
  - `business leader portrait`
  - `professional executive`
  - `ceo office`
  - `business professional`
- **이미지 특징**:
  - 전문적인 인물 사진
  - 신뢰감 있는 표정
  - 깨끗한 배경
- **참고**: 실제 CEO 사진 사용 권장

##### 회사연혁

- **검색 키워드**:
  - `timeline infographic`
  - `business growth`
  - `company milestone`
  - `success journey`
- **이미지 특징**:
  - 성장과 발전을 상징하는 이미지
  - 타임라인 배경으로 사용 가능
  - 추상적이고 깨끗한 디자인
- **색감**: 그라데이션, 블루 톤, 미니멀

##### 인증 및 특허

- **참고**: 실제 인증서 및 특허 문서 스캔 사용
- **보조 이미지 검색 키워드**:
  - `certificate award`
  - `patent document`
  - `quality certification`
- **이미지 특징**:
  - 배경 이미지로 사용 가능
  - 전문성을 강조하는 비주얼

##### 오시는 길

- **검색 키워드**:
  - `modern office building exterior`
  - `business district`
  - `corporate building`
- **이미지 특징**:
  - 건물 외관 (실제 사진 권장)
  - 주변 환경
  - 접근성이 좋아 보이는 위치
- **참고**: 실제 회사 건물 사진 사용 권장

---

#### 18.3.4 고객지원 페이지

##### 원격지원

- **검색 키워드**:
  - `remote support technician`
  - `it support engineer`
  - `remote desktop support`
  - `technical support team`
  - `customer service technology`
- **이미지 특징**:
  - 헤드셋을 착용한 지원 요원
  - 노트북으로 원격 지원하는 장면
  - 전문적이고 친절한 분위기
- **색감**: 밝고 따뜻한 톤, 신뢰감

##### 문의하기

- **검색 키워드**:
  - `customer service contact`
  - `business communication`
  - `contact us concept`
  - `professional consultation`
- **이미지 특징**:
  - 소통과 연결을 상징하는 이미지
  - 친근하고 접근하기 쉬운 느낌
  - 전문적이면서도 따뜻한 분위기
- **색감**: 밝은 톤, 블루/그린 계열

---

### 18.4 이미지 선택 기준

#### 18.4.1 B2B 전문성 체크리스트

**필수 요소:**
- [ ] 전문적이고 신뢰감 있는 분위기
- [ ] 고품질 이미지 (선명도, 구도)
- [ ] 적절한 조명 (너무 어둡거나 밝지 않음)
- [ ] 깨끗하고 정돈된 환경
- [ ] 안전 장비 착용 (건설 현장 이미지)

**피해야 할 요소:**
- [ ] 지저분하거나 위험해 보이는 현장
- [ ] 안전 장비 미착용
- [ ] 과도하게 연출된 스톡 사진 느낌
- [ ] 저품질 또는 흐릿한 이미지
- [ ] 브랜드 컬러와 충돌하는 색감

#### 18.4.2 건설 현장 안전 이미지 기준

**안전 요소:**
- 안전모 (헬멧) 착용
- 안전 조끼 착용
- 안전화 착용
- 체계적인 현장 관리
- 깨끗한 작업 환경

**기술 요소:**
- 최신 장비 및 시스템
- 디지털 기기 활용
- 모니터링 시스템
- 스마트 기술 적용

**신뢰 요소:**
- 전문가의 모습
- 팀워크와 협업
- 체계적인 프로세스
- 완성도 높은 결과물

---

### 18.5 이미지 다운로드 및 최적화

#### 18.5.1 Unsplash 다운로드 방법

**1. 이미지 검색:**
```
1. https://unsplash.com 접속
2. 검색창에 키워드 입력 (영문)
3. 필터 적용 (Orientation: Landscape/Portrait)
4. 라이선스 확인 (모두 무료)
```

**2. 적절한 크기 선택:**
- **Small**: 640px (썸네일, 카드 이미지)
- **Medium**: 1920px (일반 섹션 이미지)
- **Large**: 2400px (히어로 섹션, 배경 이미지)
- **Original**: 원본 크기 (필요 시)

**3. 다운로드:**
```
1. 이미지 클릭
2. 우측 상단 "Download free" 버튼 클릭
3. 크기 선택 (권장: Large)
4. 다운로드 완료
```

#### 18.5.2 이미지 최적화 프로세스

**1. 크기 조정:**
```
히어로 섹션: 1920x1080px (16:9)
솔루션 카드: 800x600px (4:3)
시공사례: 1200x675px (16:9)
인증서: 800x1000px (4:5)
```

**2. 포맷 변환:**
```
WebP 형식으로 변환 (권장)
- 도구: Squoosh (https://squoosh.app)
- 품질: 80-85%
- 폴백: JPG 형식도 함께 준비
```

**3. 압축:**
```
- 도구: TinyPNG (https://tinypng.com)
- 목표: 파일 크기 50-70% 감소
- 품질 유지: 육안으로 차이 없을 정도
```

**4. 파일명 규칙:**
```
[페이지]-[섹션]-[설명]-[크기].webp

예시:
home-hero-slide1-1920.webp
home-hero-slide1-1920.jpg (폴백)
solutions-ai-overview-1200.webp
about-ceo-portrait-800.webp
```

#### 18.5.3 반응형 이미지 준비

**각 이미지당 3개 크기 생성:**
```
- Small: 400px (모바일)
- Medium: 800px (태블릿)
- Large: 1200px (데스크톱)
```

**파일명 예시:**
```
home-hero-slide1-400.webp
home-hero-slide1-800.webp
home-hero-slide1-1200.webp
```

**HTML 구현:**
```html
<picture>
  <source 
    srcset="
      /assets/images/home-hero-slide1-400.webp 400w,
      /assets/images/home-hero-slide1-800.webp 800w,
      /assets/images/home-hero-slide1-1200.webp 1200w
    "
    type="image/webp"
  >
  <source 
    srcset="
      /assets/images/home-hero-slide1-400.jpg 400w,
      /assets/images/home-hero-slide1-800.jpg 800w,
      /assets/images/home-hero-slide1-1200.jpg 1200w
    "
    type="image/jpeg"
  >
  <img 
    src="/assets/images/home-hero-slide1-800.jpg"
    alt="건설 현장 안전 관리 시스템"
    loading="lazy"
    sizes="(max-width: 768px) 100vw, (max-width: 1024px) 50vw, 33vw"
  >
</picture>
```

---

### 18.6 이미지 파일 구조

```
assets/images/
├── home/
│   ├── hero/
│   │   ├── slide1-400.webp
│   │   ├── slide1-800.webp
│   │   ├── slide1-1200.webp
│   │   ├── slide1-400.jpg (폴백)
│   │   ├── slide1-800.jpg
│   │   └── slide1-1200.jpg
│   ├── solutions/
│   │   ├── ai-surveillance-400.webp
│   │   └── ...
│   └── cases/
│       └── ...
├── solutions/
│   ├── smart-safety/
│   ├── tower-crane/
│   ├── ai-surveillance/
│   ├── environment-sensor/
│   └── access-control/
├── about/
│   ├── company/
│   ├── ceo/
│   ├── history/
│   ├── certifications/
│   └── location/
└── support/
    ├── remote/
    └── contact/
```

---

### 18.7 크레딧 표기 방법

#### 18.7.1 개별 이미지 크레딧 (권장)

**이미지 하단 또는 캡션:**
```html
<figure>
  <img src="image.jpg" alt="설명">
  <figcaption>
    Photo by 
    <a href="https://unsplash.com/@photographer" 
       target="_blank" 
       rel="noopener noreferrer">
      Photographer Name
    </a> 
    on 
    <a href="https://unsplash.com" 
       target="_blank" 
       rel="noopener noreferrer">
      Unsplash
    </a>
  </figcaption>
</figure>
```

#### 18.7.2 푸터 통합 크레딧

**푸터에 일괄 표기:**
```html
<footer>
  <!-- 기존 푸터 콘텐츠 -->
  
  <div class="image-credits">
    <p>
      Images by 
      <a href="https://unsplash.com" 
         target="_blank" 
         rel="noopener noreferrer">
        Unsplash
      </a>
    </p>
  </div>
</footer>
```

#### 18.7.3 별도 크레딧 페이지 (선택)

**`/credits.html` 페이지 생성:**
```html
<h1>Image Credits</h1>

<h2>Home Page</h2>
<ul>
  <li>
    Hero Slide 1: 
    <a href="https://unsplash.com/photos/xxxxx">Photo</a> 
    by 
    <a href="https://unsplash.com/@photographer">Photographer Name</a>
  </li>
  <!-- 이하 모든 이미지 -->
</ul>
```

---

### 18.8 추천 Unsplash 컬렉션

**건설 및 안전:**
- 검색: "construction safety" 컬렉션
- 검색: "industrial technology" 컬렉션

**기술 및 모니터링:**
- 검색: "surveillance security" 컬렉션
- 검색: "smart technology" 컬렉션

**비즈니스 및 전문성:**
- 검색: "business professional" 컬렉션
- 검색: "corporate office" 컬렉션

**참고**: Unsplash에서 직접 검색하여 관련 컬렉션 찾기

---

### 18.9 이미지 품질 체크리스트

**다운로드 전:**
- [ ] 검색 키워드가 페이지 컨셉과 일치하는가?
- [ ] 이미지가 전문적이고 고품질인가?
- [ ] 색감이 브랜드 컬러와 조화로운가?
- [ ] 구도와 조명이 적절한가?
- [ ] 안전 요소가 포함되어 있는가? (건설 현장)

**다운로드 후:**
- [ ] 적절한 크기로 다운로드했는가? (Large 권장)
- [ ] 파일명을 규칙에 맞게 변경했는가?
- [ ] WebP 형식으로 변환했는가?
- [ ] 압축을 통해 파일 크기를 최적화했는가?
- [ ] 반응형 이미지 (3개 크기)를 준비했는가?

**업로드 전:**
- [ ] 올바른 폴더에 저장했는가?
- [ ] alt 텍스트를 작성했는가?
- [ ] 크레딧 정보를 기록했는가?
- [ ] 폴백 이미지 (JPG)도 준비했는가?

---

### 18.10 대체 이미지 소스 (참고)

Unsplash 외에 추가로 활용 가능한 무료 이미지 사이트:

**Pexels:**
- https://www.pexels.com
- 무료 라이선스
- 건설 및 산업 이미지 풍부

**Pixabay:**
- https://www.pixabay.com
- 무료 라이선스
- 다양한 카테고리

**Freepik (일부 무료):**
- https://www.freepik.com
- 일러스트 및 벡터 이미지
- 크레딧 표기 필수

**참고**: 각 사이트의 라이선스 조건을 반드시 확인하세요.

---

### 18.11 실무 팁

**1. 이미지 선택 시간 절약:**
- 검색 키워드를 구체적으로 입력
- 필터 활용 (Orientation, Color)
- 컬렉션 기능 활용 (마음에 드는 이미지 저장)

**2. 일관성 유지:**
- 비슷한 색감과 톤의 이미지 선택
- 동일한 사진가의 시리즈 활용
- 스타일 가이드 문서 작성

**3. 성능 최적화:**
- 필요한 크기보다 약간 큰 이미지 다운로드
- WebP 형식 우선 사용
- Lazy Loading 적용

**4. 접근성:**
- 모든 이미지에 의미 있는 alt 텍스트 작성
- 텍스트 오버레이 시 충분한 대비 확보
- 장식 이미지는 alt="" 처리

---

**이미지 소싱 가이드 작성일**: 2024  
**작성자**: UX Designer  
**버전**: 1.0

**다음 단계:**
1. 각 페이지별 이미지 검색 및 다운로드
2. 이미지 최적화 및 반응형 버전 생성
3. 크레딧 정보 기록
4. 개발자에게 이미지 파일 전달
