# 디자인 시스템 (Template2)

## 문서 개요

**프로젝트명**: (주)아이티로그 홈페이지 리뉴얼 (Template2)  
**작성일**: 2024  
**작성자**: UX Designer  
**버전**: 1.0  
**디자인 테마**: Trendy & Simple

---

## 1. 디자인 시스템 개요

### 1.1 목적

일관되고 확장 가능한 디자인 언어를 구축하여:
- 모든 페이지에서 통일된 사용자 경험 제공
- 개발 효율성 향상
- 유지보수 용이성 확보
- 브랜드 아이덴티티 강화

### 1.2 원칙

**단순성 (Simplicity)**
- 최소한의 요소로 최대 효과
- 명확한 시각적 계층

**일관성 (Consistency)**
- 재사용 가능한 컴포넌트
- 통일된 패턴

**확장성 (Scalability)**
- 새로운 페이지 추가 용이
- 유연한 그리드 시스템

---

## 2. 컬러 시스템

### 2.1 컬러 팔레트

#### Primary Color (주 색상)
```
Electric Blue (일렉트릭 블루)
- Hex: #0066FF
- RGB: rgb(0, 102, 255)
- 용도: 주요 CTA 버튼, 링크, 강조 요소
- 특징: 기술적이고 신뢰감 있는 블루
```

#### Secondary Color (보조 색상)
```
Cyan Accent (시안 액센트)
- Hex: #00D9FF
- RGB: rgb(0, 217, 255)
- 용도: 그라데이션, 아이콘, 호버 효과
- 특징: 밝고 현대적인 시안
```

#### Neutral Colors (중립 색상)
```
Dark Navy (다크 네이비)
- Hex: #0A1929
- RGB: rgb(10, 25, 41)
- 용도: 헤더, 푸터, 제목

Charcoal (차콜)
- Hex: #1E293B
- RGB: rgb(30, 41, 59)
- 용도: 본문 텍스트, 서브 제목

Medium Gray (미디엄 그레이)
- Hex: #64748B
- RGB: rgb(100, 116, 139)
- 용도: 보조 텍스트, 아이콘

Light Gray (라이트 그레이)
- Hex: #E2E8F0
- RGB: rgb(226, 232, 240)
- 용도: 배경, 구분선, 카드 배경

Off White (오프 화이트)
- Hex: #F8FAFC
- RGB: rgb(248, 250, 252)
- 용도: 페이지 배경, 섹션 배경

Pure White (순백)
- Hex: #FFFFFF
- RGB: rgb(255, 255, 255)
- 용도: 카드, 모달, 주요 배경
```

#### System Colors (시스템 색상)
```
Success (성공)
- Hex: #10B981
- RGB: rgb(16, 185, 129)
- 용도: 성공 메시지, 완료 상태

Warning (경고)
- Hex: #F59E0B
- RGB: rgb(245, 158, 11)
- 용도: 경고 메시지, 주의 사항

Error (오류)
- Hex: #EF4444
- RGB: rgb(239, 68, 68)
- 용도: 오류 메시지, 필수 입력
```

### 2.2 컬러 사용 규칙

**단일 포인트 컬러 원칙**
- 주 색상(Electric Blue)을 중심으로 디자인
- 보조 색상(Cyan)은 그라데이션 및 강조에만 사용
- 다양한 색상 남발 지양

**색상 대비**
- 텍스트와 배경: 최소 4.5:1 (WCAG AA)
- 큰 텍스트 (18pt+): 최소 3:1
- 링크: 주변 텍스트와 명확히 구분

**그라데이션**
```css
/* Primary Gradient */
background: linear-gradient(135deg, #0066FF 0%, #00D9FF 100%);

/* Subtle Gradient (배경용) */
background: linear-gradient(180deg, #F8FAFC 0%, #FFFFFF 100%);

/* Dark Gradient (헤더/푸터) */
background: linear-gradient(135deg, #0A1929 0%, #1E293B 100%);
```

### 2.3 CSS Variables

```css
:root {
  /* Primary Colors */
  --color-primary: #0066FF;
  --color-primary-hover: #0052CC;
  --color-primary-light: #3385FF;
  --color-secondary: #00D9FF;
  
  /* Neutral Colors */
  --color-dark: #0A1929;
  --color-charcoal: #1E293B;
  --color-gray: #64748B;
  --color-light-gray: #E2E8F0;
  --color-off-white: #F8FAFC;
  --color-white: #FFFFFF;
  
  /* System Colors */
  --color-success: #10B981;
  --color-warning: #F59E0B;
  --color-error: #EF4444;
  
  /* Gradients */
  --gradient-primary: linear-gradient(135deg, #0066FF 0%, #00D9FF 100%);
  --gradient-subtle: linear-gradient(180deg, #F8FAFC 0%, #FFFFFF 100%);
  --gradient-dark: linear-gradient(135deg, #0A1929 0%, #1E293B 100%);
}
```

---

## 3. 타이포그래피

### 3.1 폰트 패밀리

#### 한글 폰트
```
Pretendard (프리텐다드)
- 타입: 가변 폰트 (Variable Font)
- 웨이트: 400 (Regular), 600 (SemiBold), 700 (Bold)
- 특징: 모던하고 깔끔한 고딕체
- 라이선스: SIL Open Font License
- CDN: https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css
```

#### 영문/숫자 폰트
```
Inter
- 타입: 가변 폰트
- 웨이트: 400, 600, 700
- 특징: 기하학적 산세리프, 가독성 우수
- 라이선스: SIL Open Font License
- CDN: Google Fonts
```

#### 폴백 폰트
```css
font-family: 'Pretendard Variable', 'Pretendard', -apple-system, BlinkMacSystemFont, 
             'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', sans-serif;
```

### 3.2 타이포그래피 스케일

#### 데스크톱 (1024px+)
```
H1 (Hero Title)
- 크기: 64px / 4rem
- 웨이트: 700 (Bold)
- 행간: 1.1 (70.4px)
- 자간: -0.02em
- 용도: 히어로 섹션 메인 타이틀

H2 (Section Title)
- 크기: 48px / 3rem
- 웨이트: 700 (Bold)
- 행간: 1.2 (57.6px)
- 자간: -0.01em
- 용도: 섹션 제목

H3 (Subsection Title)
- 크기: 32px / 2rem
- 웨이트: 600 (SemiBold)
- 행간: 1.3 (41.6px)
- 자간: 0
- 용도: 서브섹션 제목, 카드 제목

H4 (Card Title)
- 크기: 24px / 1.5rem
- 웨이트: 600 (SemiBold)
- 행간: 1.4 (33.6px)
- 자간: 0
- 용도: 카드 제목, 작은 섹션 제목

Body Large
- 크기: 20px / 1.25rem
- 웨이트: 400 (Regular)
- 행간: 1.6 (32px)
- 용도: 리드 텍스트, 중요 본문

Body Regular
- 크기: 16px / 1rem
- 웨이트: 400 (Regular)
- 행간: 1.6 (25.6px)
- 용도: 일반 본문

Body Small
- 크기: 14px / 0.875rem
- 웨이트: 400 (Regular)
- 행간: 1.5 (21px)
- 용도: 보조 텍스트, 캡션

Caption
- 크기: 12px / 0.75rem
- 웨이트: 400 (Regular)
- 행간: 1.4 (16.8px)
- 용도: 라벨, 작은 설명
```

#### 모바일 (320-767px)
```
H1: 40px / 2.5rem (행간: 1.2)
H2: 32px / 2rem (행간: 1.3)
H3: 24px / 1.5rem (행간: 1.4)
H4: 20px / 1.25rem (행간: 1.4)
Body Large: 18px / 1.125rem (행간: 1.6)
Body Regular: 16px / 1rem (행간: 1.6)
Body Small: 14px / 0.875rem (행간: 1.5)
Caption: 12px / 0.75rem (행간: 1.4)
```

### 3.3 CSS Variables

```css
:root {
  /* Font Families */
  --font-primary: 'Pretendard Variable', 'Pretendard', -apple-system, sans-serif;
  
  /* Font Sizes - Desktop */
  --font-size-h1: 4rem;      /* 64px */
  --font-size-h2: 3rem;      /* 48px */
  --font-size-h3: 2rem;      /* 32px */
  --font-size-h4: 1.5rem;    /* 24px */
  --font-size-body-lg: 1.25rem;  /* 20px */
  --font-size-body: 1rem;    /* 16px */
  --font-size-body-sm: 0.875rem; /* 14px */
  --font-size-caption: 0.75rem;  /* 12px */
  
  /* Font Weights */
  --font-weight-regular: 400;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  
  /* Line Heights */
  --line-height-tight: 1.1;
  --line-height-normal: 1.3;
  --line-height-relaxed: 1.6;
}

/* Mobile Overrides */
@media (max-width: 767px) {
  :root {
    --font-size-h1: 2.5rem;   /* 40px */
    --font-size-h2: 2rem;     /* 32px */
    --font-size-h3: 1.5rem;   /* 24px */
    --font-size-h4: 1.25rem;  /* 20px */
    --font-size-body-lg: 1.125rem; /* 18px */
  }
}
```

---

## 4. 스페이싱 시스템

### 4.1 기본 단위

**8px 기반 시스템**
```
모든 여백과 패딩은 8의 배수 사용
- 4px: 매우 작은 간격
- 8px: 작은 간격
- 16px: 기본 간격
- 24px: 중간 간격
- 32px: 큰 간격
- 48px: 매우 큰 간격
- 64px: 섹션 간격
- 80px: 대형 섹션 간격
- 120px: 특대 섹션 간격
```

### 4.2 CSS Variables

```css
:root {
  /* Spacing Scale */
  --space-xs: 0.25rem;   /* 4px */
  --space-sm: 0.5rem;    /* 8px */
  --space-md: 1rem;      /* 16px */
  --space-lg: 1.5rem;    /* 24px */
  --space-xl: 2rem;      /* 32px */
  --space-2xl: 3rem;     /* 48px */
  --space-3xl: 4rem;     /* 64px */
  --space-4xl: 5rem;     /* 80px */
  --space-5xl: 7.5rem;   /* 120px */
  
  /* Section Spacing */
  --section-padding-desktop: 5rem;  /* 80px */
  --section-padding-mobile: 3rem;   /* 48px */
  
  /* Container Padding */
  --container-padding-desktop: 2rem; /* 32px */
  --container-padding-mobile: 1rem;  /* 16px */
}
```

### 4.3 사용 예시

```css
/* 섹션 간 여백 */
section {
  padding: var(--section-padding-desktop) 0;
}

/* 카드 내부 패딩 */
.card {
  padding: var(--space-xl);
}

/* 요소 간 간격 */
.element + .element {
  margin-top: var(--space-lg);
}
```

---

## 5. 그리드 시스템

### 5.1 컨테이너

```css
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--container-padding-desktop);
}

@media (max-width: 767px) {
  .container {
    padding: 0 var(--container-padding-mobile);
  }
}
```

### 5.2 그리드 레이아웃

#### 데스크톱 (1024px+)
```
12 컬럼 그리드
- 컬럼 간격 (Gap): 24px
- 최대 너비: 1200px
```

#### 태블릿 (768-1023px)
```
8 컬럼 그리드
- 컬럼 간격: 20px
```

#### 모바일 (320-767px)
```
4 컬럼 그리드
- 컬럼 간격: 16px
```

### 5.3 CSS Grid 예시

```css
.grid {
  display: grid;
  gap: var(--space-lg);
}

/* 4열 그리드 (데스크톱) */
.grid-4 {
  grid-template-columns: repeat(4, 1fr);
}

/* 3열 그리드 (데스크톱) */
.grid-3 {
  grid-template-columns: repeat(3, 1fr);
}

/* 2열 그리드 (태블릿) */
@media (max-width: 1023px) {
  .grid-4,
  .grid-3 {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* 1열 그리드 (모바일) */
@media (max-width: 767px) {
  .grid-4,
  .grid-3 {
    grid-template-columns: 1fr;
  }
}
```

---

## 6. 컴포넌트

### 6.1 버튼

#### Primary Button
```css
.btn-primary {
  /* 스타일 */
  background: var(--color-primary);
  color: var(--color-white);
  padding: 14px 32px;
  border-radius: 8px;
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-semibold);
  border: none;
  cursor: pointer;
  
  /* 트랜지션 */
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background: var(--color-primary-hover);
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(0, 102, 255, 0.3);
}

.btn-primary:active {
  transform: translateY(0);
}
```

#### Secondary Button
```css
.btn-secondary {
  background: transparent;
  color: var(--color-primary);
  padding: 14px 32px;
  border-radius: 8px;
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-semibold);
  border: 2px solid var(--color-primary);
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-secondary:hover {
  background: var(--color-primary);
  color: var(--color-white);
  transform: translateY(-2px);
}
```

#### Button Sizes
```css
/* Large */
.btn-lg {
  padding: 16px 40px;
  font-size: 1.125rem; /* 18px */
}

/* Medium (기본) */
.btn-md {
  padding: 14px 32px;
  font-size: 1rem; /* 16px */
}

/* Small */
.btn-sm {
  padding: 10px 24px;
  font-size: 0.875rem; /* 14px */
}
```

### 6.2 카드

```css
.card {
  background: var(--color-white);
  border-radius: 16px;
  padding: var(--space-xl);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.4s ease;
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.12);
}

/* 카드 내부 요소 */
.card-icon {
  width: 64px;
  height: 64px;
  margin-bottom: var(--space-lg);
}

.card-title {
  font-size: var(--font-size-h4);
  font-weight: var(--font-weight-semibold);
  margin-bottom: var(--space-md);
  color: var(--color-dark);
}

.card-description {
  font-size: var(--font-size-body);
  color: var(--color-gray);
  line-height: var(--line-height-relaxed);
}
```

### 6.3 입력 필드

```css
.input {
  width: 100%;
  padding: 14px 16px;
  border: 2px solid var(--color-light-gray);
  border-radius: 8px;
  font-size: var(--font-size-body);
  font-family: var(--font-primary);
  transition: all 0.3s ease;
}

.input:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 4px rgba(0, 102, 255, 0.1);
}

.input::placeholder {
  color: var(--color-gray);
}

/* 에러 상태 */
.input.error {
  border-color: var(--color-error);
}

/* Textarea */
.textarea {
  min-height: 120px;
  resize: vertical;
}
```

### 6.4 링크

```css
.link {
  color: var(--color-primary);
  text-decoration: none;
  position: relative;
  transition: color 0.3s ease;
}

.link:hover {
  color: var(--color-primary-hover);
}

/* 밑줄 애니메이션 */
.link::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--color-primary);
  transition: width 0.3s ease;
}

.link:hover::after {
  width: 100%;
}
```

---

## 7. 아이콘 시스템

### 7.1 아이콘 스타일

**스타일**: Line (라인형)
- 2px 선 두께
- 둥근 모서리 (rounded)
- 미니멀하고 모던한 느낌

**라이브러리**: Feather Icons 또는 Heroicons
- CDN 또는 SVG 직접 사용
- 일관된 스타일 유지

### 7.2 아이콘 크기

```css
.icon-sm { width: 16px; height: 16px; }
.icon-md { width: 24px; height: 24px; }
.icon-lg { width: 32px; height: 32px; }
.icon-xl { width: 48px; height: 48px; }
```

### 7.3 주요 아이콘

```
- 메뉴: menu (햄버거)
- 닫기: x
- 화살표: arrow-right, arrow-left, chevron-down
- 체크: check, check-circle
- 검색: search
- 위치: map-pin
- 전화: phone
- 이메일: mail
- 외부 링크: external-link
- 다운로드: download
```

---

## 8. 그림자 시스템

### 8.1 그림자 레벨

```css
:root {
  /* Elevation Shadows */
  --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.06);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.12);
  --shadow-xl: 0 16px 48px rgba(0, 0, 0, 0.16);
  
  /* Colored Shadows (Primary) */
  --shadow-primary: 0 8px 16px rgba(0, 102, 255, 0.3);
}
```

### 8.2 사용 예시

```css
/* 카드 기본 */
.card {
  box-shadow: var(--shadow-md);
}

/* 카드 호버 */
.card:hover {
  box-shadow: var(--shadow-lg);
}

/* 버튼 호버 */
.btn-primary:hover {
  box-shadow: var(--shadow-primary);
}

/* 모달 */
.modal {
  box-shadow: var(--shadow-xl);
}
```

---

## 9. 애니메이션

### 9.1 트랜지션 타이밍

```css
:root {
  /* Duration */
  --duration-fast: 0.2s;
  --duration-normal: 0.3s;
  --duration-slow: 0.4s;
  
  /* Easing */
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1);
  --ease-in: cubic-bezier(0.4, 0, 1, 1);
}
```

### 9.2 공통 애니메이션

```css
/* 페이드인 */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* 슬라이드업 */
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 스케일업 */
@keyframes scaleUp {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
```

### 9.3 사용 예시

```css
.fade-in {
  animation: fadeIn var(--duration-normal) var(--ease-out);
}

.slide-up {
  animation: slideUp var(--duration-slow) var(--ease-out);
}
```

---

## 10. 반응형 유틸리티

### 10.1 브레이크포인트

```css
:root {
  --breakpoint-mobile: 767px;
  --breakpoint-tablet: 1023px;
  --breakpoint-desktop: 1024px;
}
```

### 10.2 미디어 쿼리 믹스인 (참고용)

```css
/* Mobile First Approach */

/* Tablet and up */
@media (min-width: 768px) {
  /* 태블릿 이상 스타일 */
}

/* Desktop and up */
@media (min-width: 1024px) {
  /* 데스크톱 이상 스타일 */
}

/* Mobile only */
@media (max-width: 767px) {
  /* 모바일 전용 스타일 */
}
```

---

## 11. 접근성

### 11.1 포커스 스타일

```css
:focus {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

:focus:not(:focus-visible) {
  outline: none;
}

:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

### 11.2 스크린 리더 전용

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
```

---

## 12. 체크리스트

### 12.1 디자인 시스템 완성도
- [x] 컬러 시스템 정의
- [x] 타이포그래피 시스템 정의
- [x] 스페이싱 시스템 정의
- [x] 그리드 시스템 정의
- [x] 버튼 컴포넌트 정의
- [x] 카드 컴포넌트 정의
- [x] 입력 필드 컴포넌트 정의
- [x] 아이콘 시스템 정의
- [x] 그림자 시스템 정의
- [x] 애니메이션 정의
- [x] 반응형 유틸리티 정의
- [x] 접근성 고려사항 정의

---

**문서 버전**: 1.0  
**작성일**: 2024  
**작성자**: UX Designer  
**검토자**: PM, 프론트엔드 개발자  
**승인일**: [승인 후 기입]

**관련 문서**:
- 디자인 컨셉 (ux-design-concept.md)
- 와이어프레임 (ux-wireframes.md)
- UI 컴포넌트 가이드 (ux-ui-components.md)
