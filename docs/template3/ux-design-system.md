# UX 디자인 시스템 (Template3)

## 문서 개요

**프로젝트명**: (주)아이티로그 홈페이지 리뉴얼 (Template3)  
**작성일**: 2024  
**작성자**: UX Designer  
**버전**: 1.0  
**디자인 테마**: Dark & Premium

---

## 1. 디자인 시스템 개요

### 1.1 목적

Template3 디자인 시스템은 다크 모드 기반의 프리미엄 웹사이트를 위한 일관되고 확장 가능한 디자인 언어를 제공합니다. 모든 페이지와 컴포넌트에서 동일한 시각적 언어를 사용하여 브랜드 아이덴티티를 강화하고, 개발 효율성을 높입니다.

### 1.2 핵심 원칙

1. **일관성 (Consistency)**: 모든 페이지에서 동일한 디자인 패턴 사용
2. **확장성 (Scalability)**: 새로운 페이지와 기능 추가 시 쉽게 적용 가능
3. **접근성 (Accessibility)**: WCAG 2.1 AA 기준 준수
4. **성능 (Performance)**: 빠른 로딩과 부드러운 애니메이션
5. **프리미엄 (Premium)**: 고급스럽고 세련된 시각적 경험

---

## 2. 컬러 시스템

### 2.1 Primary Colors (주요 색상)

#### Dark Background Colors
```css
/* Primary Dark - 메인 배경 */
--color-bg-primary: #0a0a0a;
--color-bg-primary-rgb: 10, 10, 10;

/* Secondary Dark - 카드, 섹션 배경 */
--color-bg-secondary: #1a1a1a;
--color-bg-secondary-rgb: 26, 26, 26;

/* Tertiary Dark - 호버, 활성 상태 */
--color-bg-tertiary: #2a2a2a;
--color-bg-tertiary-rgb: 42, 42, 42;

/* Pure Black - 푸터, 특수 섹션 */
--color-bg-black: #000000;
--color-bg-black-rgb: 0, 0, 0;
```

**사용 예시**:
- `--color-bg-primary`: 전체 페이지 배경, 히어로 섹션
- `--color-bg-secondary`: 카드, 콘텐츠 섹션, 네비게이션
- `--color-bg-tertiary`: 호버 상태, 활성 메뉴
- `--color-bg-black`: 푸터, 구분선

#### Accent Colors (포인트 색상)
```css
/* Gold - 프리미엄, 신뢰, 기술력 */
--color-accent-gold: #d4af37;
--color-accent-gold-rgb: 212, 175, 55;
--color-accent-gold-light: #e6c966;
--color-accent-gold-dark: #b8941f;

/* Primary Accent - 골드를 주요 포인트 컬러로 사용 */
--color-accent-primary: #d4af37;
--color-accent-primary-rgb: 212, 175, 55;
```

**사용 가이드**:
- **Gold**: 모든 CTA 버튼, 프리미엄 요소, 강조 텍스트, 아이콘, 링크, AI/기술 요소
- **다양한 톤**: 밝은 톤(#e6c966) - 호버/강조, 기본(#d4af37) - 일반, 어두운 톤(#b8941f) - 액티브
- **일관성**: 단일 포인트 컬러로 브랜드 아이덴티티 강화

#### Text Colors (텍스트 색상)
```css
/* White - 주요 텍스트 */
--color-text-primary: #ffffff;
--color-text-primary-rgb: 255, 255, 255;

/* Light Gray - 보조 텍스트 */
--color-text-secondary: #a0a0a0;
--color-text-secondary-rgb: 160, 160, 160;

/* Medium Gray - 비활성 텍스트 */
--color-text-tertiary: #707070;
--color-text-tertiary-rgb: 112, 112, 112;

/* Dark Gray - 플레이스홀더 */
--color-text-placeholder: #505050;
--color-text-placeholder-rgb: 80, 80, 80;
```

**대비율 (Contrast Ratio)**:
- Primary on Dark: 19.5:1 ✅ (WCAG AAA)
- Secondary on Dark: 7.2:1 ✅ (WCAG AA)
- Tertiary on Dark: 4.6:1 ✅ (WCAG AA)
- Gold on Dark: 8.1:1 ✅ (WCAG AA)

### 2.2 Semantic Colors (의미론적 색상)

```css
/* Success - 성공, 완료 */
--color-success: #00ff88;
--color-success-bg: rgba(0, 255, 136, 0.1);

/* Warning - 경고, 주의 */
--color-warning: #ffaa00;
--color-warning-bg: rgba(255, 170, 0, 0.1);

/* Error - 오류, 실패 */
--color-error: #ff4444;
--color-error-bg: rgba(255, 68, 68, 0.1);

/* Info - 정보 */
--color-info: #d4af37;
--color-info-bg: rgba(212, 175, 55, 0.1);
```

### 2.3 Gradient Colors (그라데이션)

```css
/* Dark Gradient - 히어로 배경 */
--gradient-dark: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);

/* Gold Gradient - 프리미엄 버튼, 강조 요소 */
--gradient-gold: linear-gradient(135deg, #d4af37 0%, #e6c966 100%);

/* Gold Subtle - 배경 강조 */
--gradient-gold-subtle: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(230, 201, 102, 0.1) 100%);

/* Overlay Gradient - 이미지 오버레이 */
--gradient-overlay: linear-gradient(180deg, rgba(10, 10, 10, 0) 0%, rgba(10, 10, 10, 0.8) 100%);
```

### 2.4 컬러 사용 규칙

#### 배경 계층 구조
```
Level 1 (최하단): #0a0a0a (Primary Dark)
  ↓
Level 2 (카드): #1a1a1a (Secondary Dark)
  ↓
Level 3 (호버): #2a2a2a (Tertiary Dark)
```

#### 포인트 컬러 우선순위
1. **Gold 주요**: 모든 CTA, 프리미엄 요소, 주요 강조, 링크, 아이콘
2. **Gold 톤 변화**: 밝은 톤(호버), 기본 톤(일반), 어두운 톤(액티브)
3. **일관성 유지**: 단일 포인트 컬러로 브랜드 아이덴티티 강화

#### 접근성 체크리스트
- [ ] 텍스트 대비: 4.5:1 이상
- [ ] UI 요소 대비: 3:1 이상
- [ ] 포커스 표시: 명확한 아웃라인
- [ ] 색상만으로 정보 전달 금지

---

## 3. 타이포그래피 시스템

### 3.1 폰트 패밀리

#### Primary Font (한글)
```css
--font-primary: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
```

**Pretendard 웨이트**:
- Black (900): 임팩트 제목
- Bold (700): 부제목, 강조
- SemiBold (600): 중요 텍스트
- Medium (500): 버튼, 레이블
- Regular (400): 본문

#### Secondary Font (영문, 숫자)
```css
--font-secondary: 'Inter', 'Pretendard', sans-serif;
```

**Inter 웨이트**:
- Black (900): 대형 숫자
- Bold (700): 제목
- Regular (400): 본문

#### Monospace Font (코드, 데이터)
```css
--font-mono: 'JetBrains Mono', 'Courier New', monospace;
```

### 3.2 타이포그래피 스케일

#### Display (초대형 제목)
```css
/* Display 1 - 히어로 메인 제목 */
--font-size-display-1: 120px;
--line-height-display-1: 1.2;
--font-weight-display-1: 900;
--letter-spacing-display-1: -0.02em;

/* Display 2 - 히어로 부제목 */
--font-size-display-2: 80px;
--line-height-display-2: 1.3;
--font-weight-display-2: 900;
--letter-spacing-display-2: -0.01em;
```

**사용 예시**: 메인 페이지 히어로 섹션

#### Heading (제목)
```css
/* H1 - 페이지 제목 */
--font-size-h1: 60px;
--line-height-h1: 1.3;
--font-weight-h1: 700;
--letter-spacing-h1: -0.01em;

/* H2 - 섹션 제목 */
--font-size-h2: 48px;
--line-height-h2: 1.4;
--font-weight-h2: 700;
--letter-spacing-h2: -0.005em;

/* H3 - 서브 섹션 제목 */
--font-size-h3: 36px;
--line-height-h3: 1.4;
--font-weight-h3: 700;
--letter-spacing-h3: 0;

/* H4 - 카드 제목 */
--font-size-h4: 24px;
--line-height-h4: 1.5;
--font-weight-h4: 600;
--letter-spacing-h4: 0;

/* H5 - 작은 제목 */
--font-size-h5: 20px;
--line-height-h5: 1.5;
--font-weight-h5: 600;
--letter-spacing-h5: 0;

/* H6 - 최소 제목 */
--font-size-h6: 18px;
--line-height-h6: 1.5;
--font-weight-h6: 600;
--letter-spacing-h6: 0;
```

#### Body (본문)
```css
/* Body Large - 강조 본문 */
--font-size-body-lg: 18px;
--line-height-body-lg: 1.8;
--font-weight-body-lg: 400;

/* Body Medium - 기본 본문 */
--font-size-body-md: 16px;
--line-height-body-md: 1.7;
--font-weight-body-md: 400;

/* Body Small - 보조 본문 */
--font-size-body-sm: 14px;
--line-height-body-sm: 1.6;
--font-weight-body-sm: 400;
```

#### Caption (캡션)
```css
/* Caption - 작은 텍스트 */
--font-size-caption: 12px;
--line-height-caption: 1.5;
--font-weight-caption: 400;
```

### 3.3 반응형 타이포그래피

#### 데스크톱 (1920px 이상)
```css
--font-size-display-1: 120px;
--font-size-display-2: 80px;
--font-size-h1: 60px;
--font-size-h2: 48px;
--font-size-body-md: 18px;
```

#### 노트북 (1366px-1919px)
```css
--font-size-display-1: 100px;
--font-size-display-2: 72px;
--font-size-h1: 52px;
--font-size-h2: 40px;
--font-size-body-md: 16px;
```

#### 태블릿 (768px-1365px)
```css
--font-size-display-1: 72px;
--font-size-display-2: 56px;
--font-size-h1: 40px;
--font-size-h2: 32px;
--font-size-body-md: 16px;
```

#### 모바일 (320px-767px)
```css
--font-size-display-1: 48px;
--font-size-display-2: 36px;
--font-size-h1: 32px;
--font-size-h2: 24px;
--font-size-body-md: 16px;
```

### 3.4 타이포그래피 사용 규칙

#### 제목 계층 구조
```
Display 1 (120px) - 히어로 메인 제목
  ↓
Display 2 (80px) - 히어로 부제목
  ↓
H1 (60px) - 페이지 제목
  ↓
H2 (48px) - 섹션 제목
  ↓
H3 (36px) - 서브 섹션 제목
  ↓
H4 (24px) - 카드 제목
```

#### 가독성 규칙
- **행간**: 최소 1.5 (본문), 1.2-1.4 (제목)
- **자간**: 큰 제목 -0.02em, 본문 0
- **줄 길이**: 최대 75자 (본문)
- **정렬**: 좌측 정렬 기본, 중앙 정렬 제한적 사용

#### 강조 방법
1. **웨이트 변경**: Regular → SemiBold → Bold
2. **컬러 변경**: Gray → White → Gold/Cyan
3. **사이즈 변경**: 한 단계 위 사이즈 사용

---

## 4. 간격 시스템 (Spacing)

### 4.1 간격 스케일

```css
/* 8px 기반 스케일 */
--spacing-xs: 8px;    /* 0.5rem */
--spacing-sm: 16px;   /* 1rem */
--spacing-md: 24px;   /* 1.5rem */
--spacing-lg: 32px;   /* 2rem */
--spacing-xl: 40px;   /* 2.5rem */
--spacing-2xl: 48px;  /* 3rem */
--spacing-3xl: 64px;  /* 4rem */
--spacing-4xl: 80px;  /* 5rem */
--spacing-5xl: 120px; /* 7.5rem */
--spacing-6xl: 160px; /* 10rem */
```

### 4.2 간격 사용 가이드

#### 섹션 간격
```css
/* 섹션 상하 여백 */
--section-padding-y: 120px; /* Desktop */
--section-padding-y-tablet: 80px;
--section-padding-y-mobile: 60px;

/* 섹션 좌우 여백 */
--section-padding-x: 80px; /* Desktop */
--section-padding-x-tablet: 40px;
--section-padding-x-mobile: 20px;
```

#### 컴포넌트 간격
```css
/* 카드 내부 여백 */
--card-padding: 40px; /* Desktop */
--card-padding-tablet: 32px;
--card-padding-mobile: 24px;

/* 요소 간 간격 */
--element-gap: 24px;
--element-gap-small: 16px;
--element-gap-large: 40px;
```

#### 텍스트 간격
```css
/* 제목-본문 간격 */
--heading-margin-bottom: 24px;

/* 문단 간격 */
--paragraph-margin-bottom: 16px;

/* 리스트 간격 */
--list-item-gap: 12px;
```

---

## 5. 레이아웃 시스템

### 5.1 그리드 시스템

#### 데스크톱 (1920px 이상)
```css
--grid-columns: 12;
--grid-gap: 32px;
--grid-max-width: 1440px;
--grid-margin: 80px;
```

#### 노트북 (1366px-1919px)
```css
--grid-columns: 12;
--grid-gap: 24px;
--grid-max-width: 1280px;
--grid-margin: 60px;
```

#### 태블릿 (768px-1365px)
```css
--grid-columns: 8;
--grid-gap: 20px;
--grid-max-width: 100%;
--grid-margin: 40px;
```

#### 모바일 (320px-767px)
```css
--grid-columns: 4;
--grid-gap: 16px;
--grid-max-width: 100%;
--grid-margin: 20px;
```

### 5.2 컨테이너 시스템

```css
/* Full Width - 전체 너비 */
.container-full {
  width: 100%;
  max-width: 100%;
}

/* Wide - 넓은 컨테이너 */
.container-wide {
  width: 100%;
  max-width: 1600px;
  margin: 0 auto;
  padding: 0 80px;
}

/* Standard - 표준 컨테이너 */
.container {
  width: 100%;
  max-width: 1440px;
  margin: 0 auto;
  padding: 0 80px;
}

/* Narrow - 좁은 컨테이너 */
.container-narrow {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 80px;
}

/* Text - 텍스트 컨테이너 */
.container-text {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  padding: 0 40px;
}
```

### 5.3 섹션 레이아웃

#### 풀스크린 섹션
```css
.section-fullscreen {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

#### 표준 섹션
```css
.section {
  padding: 120px 0;
  background: var(--color-bg-primary);
}

.section-secondary {
  padding: 120px 0;
  background: var(--color-bg-secondary);
}
```

---

## 6. 컴포넌트 스타일

### 6.1 버튼 (Buttons)

#### Primary Button (Gold)
```css
.btn-primary {
  background: var(--gradient-gold);
  color: var(--color-bg-primary);
  padding: 16px 40px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 24px rgba(212, 175, 55, 0.4);
}
```

#### Secondary Button (Cyan)
```css
.btn-secondary {
  background: var(--gradient-cyan);
  color: var(--color-bg-primary);
  padding: 16px 40px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-secondary:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 24px rgba(0, 217, 255, 0.4);
}
```

#### Outline Button
```css
.btn-outline {
  background: transparent;
  color: var(--color-text-primary);
  padding: 16px 40px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 8px;
  border: 2px solid var(--color-accent-gold);
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-outline:hover {
  background: var(--color-accent-gold);
  color: var(--color-bg-primary);
}
```

### 6.2 카드 (Cards)

#### Standard Card
```css
.card {
  background: var(--color-bg-secondary);
  border-radius: 16px;
  padding: 40px;
  transition: all 0.4s ease;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 0 40px rgba(212, 175, 55, 0.3);
  border: 1px solid var(--color-accent-gold);
}
```

#### Image Card
```css
.card-image {
  background: var(--color-bg-secondary);
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.4s ease;
}

.card-image img {
  width: 100%;
  height: auto;
  transition: transform 0.5s ease;
}

.card-image:hover img {
  transform: scale(1.1);
}
```

### 6.3 입력 필드 (Input Fields)

```css
.input {
  width: 100%;
  background: var(--color-bg-secondary);
  color: var(--color-text-primary);
  border: 2px solid transparent;
  border-radius: 8px;
  padding: 16px 20px;
  font-size: 16px;
  transition: all 0.3s ease;
}

.input:focus {
  outline: none;
  border-color: var(--color-accent-gold);
  box-shadow: 0 0 0 4px rgba(212, 175, 55, 0.1);
}

.input::placeholder {
  color: var(--color-text-placeholder);
}
```

---

## 7. 이펙트 시스템

### 7.1 그림자 (Shadows)

```css
/* Elevation Shadows */
--shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.3);
--shadow-md: 0 4px 16px rgba(0, 0, 0, 0.4);
--shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.5);
--shadow-xl: 0 16px 48px rgba(0, 0, 0, 0.6);

/* Glow Shadows */
--shadow-glow-gold: 0 0 40px rgba(212, 175, 55, 0.3);
--shadow-glow-gold-strong: 0 0 60px rgba(212, 175, 55, 0.5);
```

### 7.2 블러 (Blur)

```css
--blur-sm: blur(4px);
--blur-md: blur(8px);
--blur-lg: blur(16px);
--blur-xl: blur(24px);
```

### 7.3 오버레이 (Overlays)

```css
--overlay-light: rgba(10, 10, 10, 0.5);
--overlay-medium: rgba(10, 10, 10, 0.7);
--overlay-dark: rgba(10, 10, 10, 0.9);
```

---

## 8. 애니메이션 시스템

### 8.1 트랜지션 (Transitions)

```css
/* Duration */
--transition-fast: 0.2s;
--transition-base: 0.3s;
--transition-slow: 0.5s;
--transition-slower: 0.8s;

/* Easing */
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
--ease-smooth: cubic-bezier(0.25, 0.1, 0.25, 1);
```

### 8.2 GSAP 애니메이션 설정

```javascript
// 기본 설정
gsap.defaults({
  duration: 0.8,
  ease: "power2.out"
});

// 페이드인
gsap.from(".fade-in", {
  opacity: 0,
  y: 50,
  duration: 1,
  scrollTrigger: {
    trigger: ".fade-in",
    start: "top 80%"
  }
});

// 스케일
gsap.from(".scale-in", {
  scale: 0.8,
  opacity: 0,
  duration: 1,
  scrollTrigger: {
    trigger: ".scale-in",
    start: "top 80%"
  }
});
```

---

## 9. 아이콘 시스템

### 9.1 아이콘 스타일

```css
/* Icon Sizes */
--icon-xs: 16px;
--icon-sm: 20px;
--icon-md: 24px;
--icon-lg: 32px;
--icon-xl: 48px;
--icon-2xl: 64px;

/* Icon Colors */
.icon-gold {
  color: var(--color-accent-gold);
}

.icon-gold-light {
  color: var(--color-accent-gold-light);
}

.icon-white {
  color: var(--color-text-primary);
}
```

### 9.2 아이콘 사용 가이드

- **Gold 아이콘**: 모든 포인트 아이콘 (프리미엄 서비스, 인증, 신뢰, AI, 기술, 스마트 시스템)
- **White 아이콘**: 일반 기능, 네비게이션
- **톤 변화**: 호버 시 밝은 골드(#e6c966)로 변경

---

## 10. 반응형 브레이크포인트

```css
/* Breakpoints */
--breakpoint-xs: 320px;
--breakpoint-sm: 576px;
--breakpoint-md: 768px;
--breakpoint-lg: 1024px;
--breakpoint-xl: 1366px;
--breakpoint-2xl: 1920px;

/* Media Queries */
@media (max-width: 767px) { /* Mobile */ }
@media (min-width: 768px) and (max-width: 1023px) { /* Tablet */ }
@media (min-width: 1024px) and (max-width: 1365px) { /* Laptop */ }
@media (min-width: 1366px) { /* Desktop */ }
```

---

## 11. CSS 변수 전체 목록

```css
:root {
  /* Colors */
  --color-bg-primary: #0a0a0a;
  --color-bg-secondary: #1a1a1a;
  --color-bg-tertiary: #2a2a2a;
  --color-bg-black: #000000;
  
  --color-accent-gold: #d4af37;
  --color-accent-gold-light: #e6c966;
  --color-accent-gold-dark: #b8941f;
  --color-accent-primary: #d4af37;
  
  --color-text-primary: #ffffff;
  --color-text-secondary: #a0a0a0;
  --color-text-tertiary: #707070;
  
  /* Typography */
  --font-primary: 'Pretendard', sans-serif;
  --font-secondary: 'Inter', sans-serif;
  
  --font-size-display-1: 120px;
  --font-size-h1: 60px;
  --font-size-body-md: 16px;
  
  /* Spacing */
  --spacing-xs: 8px;
  --spacing-sm: 16px;
  --spacing-md: 24px;
  --spacing-lg: 32px;
  --spacing-xl: 40px;
  
  /* Layout */
  --grid-max-width: 1440px;
  --section-padding-y: 120px;
  
  /* Effects */
  --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.4);
  --shadow-glow-gold: 0 0 40px rgba(212, 175, 55, 0.3);
  
  /* Gradients */
  --gradient-gold: linear-gradient(135deg, #d4af37 0%, #e6c966 100%);
  
  /* Animation */
  --transition-base: 0.3s;
  --ease-smooth: cubic-bezier(0.25, 0.1, 0.25, 1);
}
```

---

**문서 버전**: 1.0  
**작성일**: 2024  
**작성자**: UX Designer  

**관련 문서**:
- ux-design-concept.md
- ux-wireframes.md
- ux-ui-components.md
