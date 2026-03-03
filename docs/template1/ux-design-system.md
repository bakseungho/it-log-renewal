# UX 디자인 시스템

## 1. 디자인 시스템 개요

### 1.1 목적
이 디자인 시스템은 공사/현장 솔루션 회사 홈페이지의 일관된 사용자 경험을 제공하기 위한 재사용 가능한 컴포넌트, 스타일, 가이드라인을 정의합니다.

### 1.2 원칙
- **일관성 (Consistency)**: 모든 페이지에서 동일한 패턴 사용
- **재사용성 (Reusability)**: 컴포넌트 기반 설계
- **확장성 (Scalability)**: 향후 추가 기능 고려
- **접근성 (Accessibility)**: WCAG 2.1 AA 준수
- **성능 (Performance)**: 최적화된 구현

### 1.3 사용 방법
- 디자이너: Figma 컴포넌트 라이브러리 활용
- 개발자: CSS 변수 및 컴포넌트 클래스 사용
- 콘텐츠 관리자: 스타일 가이드 참조

## 2. 색상 시스템 (Color System)

### 2.1 Primary Colors

#### Industrial Blue (메인 컬러)
```css
--color-primary-900: #0D2847;  /* 가장 어두운 */
--color-primary-800: #153A6B;
--color-primary-700: #1A4D8F;  /* 기본 Primary */
--color-primary-600: #2563B3;
--color-primary-500: #3B82F6;
--color-primary-400: #60A5FA;
--color-primary-300: #93C5FD;
--color-primary-200: #BFDBFE;
--color-primary-100: #DBEAFE;  /* 가장 밝은 */
```

**사용 예시:**
- 700: 헤더, 주요 버튼, 링크
- 600: 버튼 호버
- 500: 아이콘, 강조 요소
- 100-200: 배경, 하이라이트

#### Steel Gray (보조 컬러)
```css
--color-secondary-900: #1F2937;
--color-secondary-800: #374151;
--color-secondary-700: #4B5563;
--color-secondary-600: #5A6C7D;  /* 기본 Secondary */
--color-secondary-500: #6B7280;
--color-secondary-400: #9CA3AF;
--color-secondary-300: #D1D5DB;
--color-secondary-200: #E5E7EB;
--color-secondary-100: #F3F4F6;
```

**사용 예시:**
- 600-700: 보조 텍스트, 아이콘
- 400-500: 비활성 상태
- 200-300: 테두리, 구분선
- 100: 배경

#### Safety Orange (강조 컬러)
```css
--color-accent-900: #7C2D12;
--color-accent-800: #9A3412;
--color-accent-700: #C2410C;
--color-accent-600: #EA580C;
--color-accent-500: #FF6B35;  /* 기본 Accent */
--color-accent-400: #FF8A5B;
--color-accent-300: #FFB088;
--color-accent-200: #FFD4B5;
--color-accent-100: #FFE8D9;
```

**사용 예시:**
- 500: CTA 버튼, 중요 알림
- 400: 호버 상태
- 100-200: 배경, 하이라이트

### 2.2 Neutral Colors

```css
/* Grayscale */
--color-white: #FFFFFF;
--color-gray-50: #F8F9FA;
--color-gray-100: #F1F3F5;
--color-gray-200: #E9ECEF;
--color-gray-300: #DEE2E6;
--color-gray-400: #CED4DA;
--color-gray-500: #ADB5BD;
--color-gray-600: #6C757D;
--color-gray-700: #495057;
--color-gray-800: #343A40;
--color-gray-900: #212529;
--color-black: #000000;
```

**사용 예시:**
- white: 카드, 모달 배경
- gray-50/100: 페이지 배경
- gray-200/300: 테두리, 구분선
- gray-600: 보조 텍스트
- gray-900: 주요 텍스트

### 2.3 Semantic Colors

```css
/* Success */
--color-success-700: #15803D;
--color-success-600: #16A34A;
--color-success-500: #22C55E;
--color-success-100: #DCFCE7;

/* Warning */
--color-warning-700: #A16207;
--color-warning-600: #CA8A04;
--color-warning-500: #EAB308;
--color-warning-100: #FEF9C3;

/* Error */
--color-error-700: #B91C1C;
--color-error-600: #DC2626;
--color-error-500: #EF4444;
--color-error-100: #FEE2E2;

/* Info */
--color-info-700: #0369A1;
--color-info-600: #0284C7;
--color-info-500: #06B6D4;
--color-info-100: #CFFAFE;
```

**사용 예시:**
- Success: 성공 메시지, 완료 상태
- Warning: 경고 메시지, 주의 필요
- Error: 오류 메시지, 필수 입력
- Info: 정보 메시지, 도움말

### 2.4 색상 사용 규칙

#### 텍스트 색상
```css
--text-primary: var(--color-gray-900);      /* 주요 텍스트 */
--text-secondary: var(--color-gray-600);    /* 보조 텍스트 */
--text-tertiary: var(--color-gray-500);     /* 3차 텍스트 */
--text-disabled: var(--color-gray-400);     /* 비활성 텍스트 */
--text-inverse: var(--color-white);         /* 어두운 배경 위 */
--text-link: var(--color-primary-700);      /* 링크 */
--text-link-hover: var(--color-primary-600);/* 링크 호버 */
```

#### 배경 색상
```css
--bg-primary: var(--color-white);           /* 주요 배경 */
--bg-secondary: var(--color-gray-50);       /* 보조 배경 */
--bg-tertiary: var(--color-gray-100);       /* 3차 배경 */
--bg-overlay: rgba(0, 0, 0, 0.5);          /* 오버레이 */
--bg-hover: var(--color-gray-100);          /* 호버 배경 */
```

#### 테두리 색상
```css
--border-default: var(--color-gray-300);    /* 기본 테두리 */
--border-light: var(--color-gray-200);      /* 밝은 테두리 */
--border-dark: var(--color-gray-400);       /* 어두운 테두리 */
--border-focus: var(--color-primary-500);   /* 포커스 테두리 */
```

### 2.5 접근성 대비율

```
텍스트 대비 (WCAG AA 기준):
✓ gray-900 on white: 16.1:1 (AAA)
✓ gray-600 on white: 5.7:1 (AA)
✓ white on primary-700: 8.2:1 (AAA)
✓ white on accent-500: 4.5:1 (AA)

버튼 대비:
✓ Primary 버튼: 8.2:1 (AAA)
✓ Accent 버튼: 4.5:1 (AA)
✓ Secondary 버튼: 7.5:1 (AAA)
```


## 3. 타이포그래피 시스템 (Typography)

### 3.1 폰트 패밀리

```css
/* 한글 + 영문 */
--font-primary: 'Pretendard', -apple-system, BlinkMacSystemFont, 
                'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, 
                sans-serif;

/* 영문/숫자 강조 */
--font-secondary: 'Inter', 'Pretendard', sans-serif;

/* 헤드라인 강조 (선택) */
--font-display: 'Montserrat', 'Pretendard', sans-serif;

/* 코드/기술 문서 */
--font-mono: 'JetBrains Mono', 'Consolas', 'Monaco', monospace;
```

### 3.2 폰트 크기 스케일

```css
/* Type Scale (1.250 - Major Third) */
--text-xs: 0.75rem;      /* 12px */
--text-sm: 0.875rem;     /* 14px */
--text-base: 1rem;       /* 16px - 기본 */
--text-lg: 1.125rem;     /* 18px */
--text-xl: 1.25rem;      /* 20px */
--text-2xl: 1.5rem;      /* 24px */
--text-3xl: 1.875rem;    /* 30px */
--text-4xl: 2rem;        /* 32px */
--text-5xl: 2.5rem;      /* 40px */
--text-6xl: 3rem;        /* 48px */
--text-7xl: 3.5rem;      /* 56px */
--text-8xl: 4rem;        /* 64px */
```

### 3.3 폰트 굵기

```css
--font-thin: 100;
--font-extralight: 200;
--font-light: 300;
--font-regular: 400;     /* 기본 본문 */
--font-medium: 500;      /* 강조 텍스트 */
--font-semibold: 600;    /* 소제목 */
--font-bold: 700;        /* 제목 */
--font-extrabold: 800;   /* 특별 강조 */
--font-black: 900;
```

### 3.4 행간 (Line Height)

```css
--leading-none: 1;
--leading-tight: 1.25;   /* 큰 제목 */
--leading-snug: 1.375;   /* 제목 */
--leading-normal: 1.5;   /* 소제목 */
--leading-relaxed: 1.625;/* 본문 */
--leading-loose: 1.75;   /* 긴 본문 */
```

### 3.5 자간 (Letter Spacing)

```css
--tracking-tighter: -0.05em;
--tracking-tight: -0.025em;  /* 한글 제목 */
--tracking-normal: 0;        /* 기본 */
--tracking-wide: 0.025em;
--tracking-wider: 0.05em;
--tracking-widest: 0.1em;
```

### 3.6 타이포그래피 스타일 정의

#### 헤딩 (Headings)

```css
/* H1 - Hero Title */
.text-h1 {
  font-family: var(--font-primary);
  font-size: var(--text-6xl);      /* 48px */
  font-weight: var(--font-bold);   /* 700 */
  line-height: var(--leading-tight);/* 1.25 */
  letter-spacing: var(--tracking-tight);
  color: var(--text-primary);
}

/* H2 - Section Title */
.text-h2 {
  font-family: var(--font-primary);
  font-size: var(--text-5xl);      /* 40px */
  font-weight: var(--font-bold);   /* 700 */
  line-height: var(--leading-snug); /* 1.375 */
  letter-spacing: var(--tracking-tight);
  color: var(--text-primary);
}

/* H3 - Subsection Title */
.text-h3 {
  font-family: var(--font-primary);
  font-size: var(--text-4xl);      /* 32px */
  font-weight: var(--font-semibold);/* 600 */
  line-height: var(--leading-snug); /* 1.375 */
  letter-spacing: var(--tracking-tight);
  color: var(--text-primary);
}

/* H4 - Card Title */
.text-h4 {
  font-family: var(--font-primary);
  font-size: var(--text-2xl);      /* 24px */
  font-weight: var(--font-semibold);/* 600 */
  line-height: var(--leading-normal);/* 1.5 */
  color: var(--text-primary);
}

/* H5 - Small Title */
.text-h5 {
  font-family: var(--font-primary);
  font-size: var(--text-xl);       /* 20px */
  font-weight: var(--font-medium);  /* 500 */
  line-height: var(--leading-normal);/* 1.5 */
  color: var(--text-primary);
}

/* H6 - Tiny Title */
.text-h6 {
  font-family: var(--font-primary);
  font-size: var(--text-lg);       /* 18px */
  font-weight: var(--font-medium);  /* 500 */
  line-height: var(--leading-normal);/* 1.5 */
  color: var(--text-primary);
}
```

#### 본문 (Body)

```css
/* Body Large */
.text-body-lg {
  font-family: var(--font-primary);
  font-size: var(--text-lg);       /* 18px */
  font-weight: var(--font-regular); /* 400 */
  line-height: var(--leading-relaxed);/* 1.625 */
  color: var(--text-primary);
}

/* Body Default */
.text-body {
  font-family: var(--font-primary);
  font-size: var(--text-base);     /* 16px */
  font-weight: var(--font-regular); /* 400 */
  line-height: var(--leading-relaxed);/* 1.625 */
  color: var(--text-primary);
}

/* Body Small */
.text-body-sm {
  font-family: var(--font-primary);
  font-size: var(--text-sm);       /* 14px */
  font-weight: var(--font-regular); /* 400 */
  line-height: var(--leading-relaxed);/* 1.625 */
  color: var(--text-secondary);
}

/* Caption */
.text-caption {
  font-family: var(--font-primary);
  font-size: var(--text-xs);       /* 12px */
  font-weight: var(--font-regular); /* 400 */
  line-height: var(--leading-normal);/* 1.5 */
  color: var(--text-tertiary);
}
```

#### 특수 스타일

```css
/* Lead Text (인트로 텍스트) */
.text-lead {
  font-family: var(--font-primary);
  font-size: var(--text-xl);       /* 20px */
  font-weight: var(--font-regular); /* 400 */
  line-height: var(--leading-loose);/* 1.75 */
  color: var(--text-secondary);
}

/* Overline (상단 레이블) */
.text-overline {
  font-family: var(--font-primary);
  font-size: var(--text-xs);       /* 12px */
  font-weight: var(--font-semibold);/* 600 */
  line-height: var(--leading-normal);/* 1.5 */
  letter-spacing: var(--tracking-wider);
  text-transform: uppercase;
  color: var(--text-tertiary);
}

/* Button Text */
.text-button {
  font-family: var(--font-primary);
  font-size: var(--text-base);     /* 16px */
  font-weight: var(--font-medium);  /* 500 */
  line-height: var(--leading-normal);/* 1.5 */
  letter-spacing: var(--tracking-wide);
}

/* Link */
.text-link {
  font-family: var(--font-primary);
  font-size: inherit;
  font-weight: var(--font-medium);  /* 500 */
  color: var(--text-link);
  text-decoration: none;
  transition: color 0.2s ease;
}

.text-link:hover {
  color: var(--text-link-hover);
  text-decoration: underline;
}
```

### 3.7 반응형 타이포그래피

```css
/* 모바일 (< 768px) */
@media (max-width: 767px) {
  .text-h1 { font-size: var(--text-5xl); }  /* 40px */
  .text-h2 { font-size: var(--text-4xl); }  /* 32px */
  .text-h3 { font-size: var(--text-2xl); }  /* 24px */
  .text-h4 { font-size: var(--text-xl); }   /* 20px */
  .text-h5 { font-size: var(--text-lg); }   /* 18px */
  .text-h6 { font-size: var(--text-base); } /* 16px */
}

/* 태블릿 (768px - 1023px) */
@media (min-width: 768px) and (max-width: 1023px) {
  .text-h1 { font-size: var(--text-6xl); }  /* 48px */
  .text-h2 { font-size: var(--text-4xl); }  /* 32px */
  .text-h3 { font-size: var(--text-3xl); }  /* 30px */
}
```


## 4. 간격 시스템 (Spacing)

### 4.1 스페이싱 스케일

```css
/* 8px 기반 스케이싱 시스템 */
--space-0: 0;
--space-1: 0.25rem;   /* 4px */
--space-2: 0.5rem;    /* 8px */
--space-3: 0.75rem;   /* 12px */
--space-4: 1rem;      /* 16px */
--space-5: 1.25rem;   /* 20px */
--space-6: 1.5rem;    /* 24px */
--space-8: 2rem;      /* 32px */
--space-10: 2.5rem;   /* 40px */
--space-12: 3rem;     /* 48px */
--space-16: 4rem;     /* 64px */
--space-20: 5rem;     /* 80px */
--space-24: 6rem;     /* 96px */
--space-32: 8rem;     /* 128px */
```

### 4.2 사용 가이드

```css
/* 섹션 간격 */
--section-spacing-sm: var(--space-12);   /* 48px - 모바일 */
--section-spacing-md: var(--space-16);   /* 64px - 태블릿 */
--section-spacing-lg: var(--space-20);   /* 80px - 데스크톱 */

/* 컴포넌트 간격 */
--component-spacing-sm: var(--space-6);  /* 24px - 모바일 */
--component-spacing-md: var(--space-8);  /* 32px - 태블릿 */
--component-spacing-lg: var(--space-10); /* 40px - 데스크톱 */

/* 요소 간격 */
--element-spacing-xs: var(--space-2);    /* 8px */
--element-spacing-sm: var(--space-3);    /* 12px */
--element-spacing-md: var(--space-4);    /* 16px */
--element-spacing-lg: var(--space-6);    /* 24px */
```

### 4.3 컨테이너 패딩

```css
/* 페이지 컨테이너 */
--container-padding-mobile: var(--space-4);    /* 16px */
--container-padding-tablet: var(--space-6);    /* 24px */
--container-padding-desktop: var(--space-8);   /* 32px */

/* 카드/컴포넌트 패딩 */
--card-padding-sm: var(--space-4);   /* 16px */
--card-padding-md: var(--space-6);   /* 24px */
--card-padding-lg: var(--space-8);   /* 32px */
```

## 5. 레이아웃 시스템 (Layout)

### 5.1 그리드 시스템

```css
/* 컨테이너 최대 너비 */
--container-sm: 640px;
--container-md: 768px;
--container-lg: 1024px;
--container-xl: 1280px;
--container-2xl: 1440px;

/* 그리드 설정 */
--grid-columns-mobile: 4;
--grid-columns-tablet: 8;
--grid-columns-desktop: 12;

/* 거터 (컬럼 간격) */
--grid-gutter-mobile: var(--space-4);    /* 16px */
--grid-gutter-tablet: var(--space-6);    /* 24px */
--grid-gutter-desktop: var(--space-6);   /* 24px */
```

### 5.2 브레이크포인트

```css
/* 미디어 쿼리 브레이크포인트 */
--breakpoint-sm: 640px;
--breakpoint-md: 768px;
--breakpoint-lg: 1024px;
--breakpoint-xl: 1280px;
--breakpoint-2xl: 1440px;
```

```css
/* 사용 예시 */
@media (min-width: 768px) {
  /* 태블릿 이상 */
}

@media (min-width: 1024px) {
  /* 데스크톱 이상 */
}
```

### 5.3 Z-Index 레이어

```css
--z-base: 0;
--z-dropdown: 1000;
--z-sticky: 1020;
--z-fixed: 1030;
--z-modal-backdrop: 1040;
--z-modal: 1050;
--z-popover: 1060;
--z-tooltip: 1070;
```

## 6. 그림자 시스템 (Shadows)

### 6.1 그림자 스케일

```css
/* Elevation Shadows */
--shadow-xs: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 
             0 1px 2px -1px rgba(0, 0, 0, 0.1);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 
             0 2px 4px -2px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 
             0 4px 6px -4px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 
             0 8px 10px -6px rgba(0, 0, 0, 0.1);
--shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);

/* Inner Shadow */
--shadow-inner: inset 0 2px 4px 0 rgba(0, 0, 0, 0.05);

/* No Shadow */
--shadow-none: none;
```

### 6.2 사용 가이드

```
shadow-xs: 입력 필드, 작은 카드
shadow-sm: 버튼, 작은 컴포넌트
shadow-md: 카드, 드롭다운
shadow-lg: 모달, 팝업
shadow-xl: 대형 모달, 중요 요소
shadow-2xl: 히어로 이미지, 특별 강조
```

## 7. 테두리 시스템 (Borders)

### 7.1 테두리 두께

```css
--border-0: 0;
--border-1: 1px;
--border-2: 2px;
--border-4: 4px;
--border-8: 8px;
```

### 7.2 테두리 반경 (Border Radius)

```css
--radius-none: 0;
--radius-sm: 0.25rem;    /* 4px */
--radius-md: 0.375rem;   /* 6px */
--radius-lg: 0.5rem;     /* 8px */
--radius-xl: 0.75rem;    /* 12px */
--radius-2xl: 1rem;      /* 16px */
--radius-3xl: 1.5rem;    /* 24px */
--radius-full: 9999px;   /* 완전한 원형 */
```

### 7.3 사용 가이드

```
radius-sm: 버튼, 뱃지, 태그
radius-md: 입력 필드
radius-lg: 카드, 이미지
radius-xl: 대형 카드, 섹션
radius-2xl: 모달, 특별 컴포넌트
radius-full: 아바타, 원형 버튼
```

## 8. 애니메이션 시스템 (Animation)

### 8.1 트랜지션 지속 시간

```css
--duration-fast: 150ms;
--duration-base: 200ms;
--duration-medium: 300ms;
--duration-slow: 500ms;
```

### 8.2 이징 함수

```css
--ease-linear: linear;
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
--ease-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);
```

### 8.3 공통 트랜지션

```css
--transition-colors: color var(--duration-base) var(--ease-out),
                     background-color var(--duration-base) var(--ease-out),
                     border-color var(--duration-base) var(--ease-out);

--transition-transform: transform var(--duration-base) var(--ease-out);

--transition-opacity: opacity var(--duration-base) var(--ease-out);

--transition-all: all var(--duration-base) var(--ease-out);
```

### 8.4 애니메이션 예시

```css
/* Fade In */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Slide Up */
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Scale In */
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* Shimmer (로딩) */
@keyframes shimmer {
  0% { background-position: -1000px 0; }
  100% { background-position: 1000px 0; }
}
```


## 9. 컴포넌트 라이브러리

### 9.1 버튼 (Buttons)

#### Primary Button
```css
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-3) var(--space-6);  /* 12px 24px */
  font-family: var(--font-primary);
  font-size: var(--text-base);
  font-weight: var(--font-medium);
  line-height: var(--leading-normal);
  color: var(--color-white);
  background-color: var(--color-primary-700);
  border: var(--border-1) solid transparent;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
  cursor: pointer;
  transition: var(--transition-all);
  min-height: 48px;
}

.btn-primary:hover {
  background-color: var(--color-primary-600);
  box-shadow: var(--shadow-md);
  transform: translateY(-1px);
}

.btn-primary:active {
  transform: translateY(0);
  box-shadow: var(--shadow-sm);
}

.btn-primary:disabled {
  background-color: var(--color-gray-300);
  color: var(--color-gray-500);
  cursor: not-allowed;
  box-shadow: none;
}
```

#### Secondary Button
```css
.btn-secondary {
  /* 기본 스타일 동일 */
  color: var(--color-primary-700);
  background-color: transparent;
  border: var(--border-2) solid var(--color-primary-700);
  box-shadow: none;
}

.btn-secondary:hover {
  background-color: var(--color-primary-50);
  border-color: var(--color-primary-600);
}
```

#### Accent Button
```css
.btn-accent {
  /* 기본 스타일 동일 */
  background-color: var(--color-accent-500);
}

.btn-accent:hover {
  background-color: var(--color-accent-400);
}
```

#### Ghost Button
```css
.btn-ghost {
  /* 기본 스타일 동일 */
  color: var(--color-gray-700);
  background-color: transparent;
  border: none;
  box-shadow: none;
}

.btn-ghost:hover {
  background-color: var(--color-gray-100);
}
```

#### 버튼 크기 변형
```css
/* Large */
.btn-lg {
  padding: var(--space-4) var(--space-8);  /* 16px 32px */
  font-size: var(--text-lg);
  min-height: 56px;
}

/* Small */
.btn-sm {
  padding: var(--space-2) var(--space-4);  /* 8px 16px */
  font-size: var(--text-sm);
  min-height: 40px;
}

/* Full Width */
.btn-block {
  width: 100%;
}

/* Icon Button */
.btn-icon {
  padding: var(--space-3);
  min-width: 48px;
  min-height: 48px;
}
```

### 9.2 입력 필드 (Input Fields)

#### Text Input
```css
.input {
  width: 100%;
  padding: var(--space-3) var(--space-4);  /* 12px 16px */
  font-family: var(--font-primary);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  color: var(--text-primary);
  background-color: var(--color-white);
  border: var(--border-1) solid var(--border-default);
  border-radius: var(--radius-md);
  transition: var(--transition-all);
  min-height: 48px;
}

.input:hover {
  border-color: var(--border-dark);
}

.input:focus {
  outline: none;
  border-color: var(--color-primary-500);
  box-shadow: 0 0 0 3px rgba(26, 77, 143, 0.1);
}

.input:disabled {
  background-color: var(--color-gray-100);
  color: var(--text-disabled);
  cursor: not-allowed;
}

.input.error {
  border-color: var(--color-error-500);
}

.input.error:focus {
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1);
}
```

#### Textarea
```css
.textarea {
  /* input 스타일 상속 */
  min-height: 120px;
  resize: vertical;
}
```

#### Select
```css
.select {
  /* input 스타일 상속 */
  appearance: none;
  background-image: url("data:image/svg+xml,..."); /* 드롭다운 아이콘 */
  background-repeat: no-repeat;
  background-position: right var(--space-4) center;
  padding-right: var(--space-10);
}
```

#### Label
```css
.label {
  display: block;
  margin-bottom: var(--space-2);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  color: var(--text-primary);
}

.label-required::after {
  content: " *";
  color: var(--color-error-500);
}
```

#### Helper Text
```css
.helper-text {
  display: block;
  margin-top: var(--space-2);
  font-size: var(--text-sm);
  color: var(--text-secondary);
}

.error-text {
  color: var(--color-error-600);
}
```

### 9.3 카드 (Cards)

#### Basic Card
```css
.card {
  background-color: var(--color-white);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  overflow: hidden;
  transition: var(--transition-all);
}

.card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-4px);
}

.card-header {
  padding: var(--space-6);
  border-bottom: var(--border-1) solid var(--border-light);
}

.card-body {
  padding: var(--space-6);
}

.card-footer {
  padding: var(--space-6);
  border-top: var(--border-1) solid var(--border-light);
  background-color: var(--color-gray-50);
}
```

#### Product Card
```css
.product-card {
  /* card 스타일 상속 */
}

.product-card-image {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
}

.product-card-badge {
  position: absolute;
  top: var(--space-4);
  left: var(--space-4);
  padding: var(--space-2) var(--space-3);
  font-size: var(--text-xs);
  font-weight: var(--font-semibold);
  color: var(--color-white);
  background-color: var(--color-primary-700);
  border-radius: var(--radius-sm);
}

.product-card-content {
  padding: var(--space-6);
}

.product-card-title {
  font-size: var(--text-xl);
  font-weight: var(--font-semibold);
  color: var(--text-primary);
  margin-bottom: var(--space-2);
}

.product-card-description {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  margin-bottom: var(--space-4);
}
```

### 9.4 뱃지 (Badges)

```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: var(--space-1) var(--space-3);
  font-size: var(--text-xs);
  font-weight: var(--font-semibold);
  line-height: var(--leading-normal);
  border-radius: var(--radius-full);
}

.badge-primary {
  color: var(--color-primary-700);
  background-color: var(--color-primary-100);
}

.badge-success {
  color: var(--color-success-700);
  background-color: var(--color-success-100);
}

.badge-warning {
  color: var(--color-warning-700);
  background-color: var(--color-warning-100);
}

.badge-error {
  color: var(--color-error-700);
  background-color: var(--color-error-100);
}

.badge-gray {
  color: var(--color-gray-700);
  background-color: var(--color-gray-100);
}
```

### 9.5 알림 (Alerts)

```css
.alert {
  display: flex;
  align-items: flex-start;
  padding: var(--space-4);
  border-radius: var(--radius-lg);
  border-left: var(--border-4) solid;
}

.alert-icon {
  flex-shrink: 0;
  width: 24px;
  height: 24px;
  margin-right: var(--space-3);
}

.alert-content {
  flex: 1;
}

.alert-title {
  font-weight: var(--font-semibold);
  margin-bottom: var(--space-1);
}

.alert-description {
  font-size: var(--text-sm);
}

/* 타입별 스타일 */
.alert-success {
  background-color: var(--color-success-100);
  border-color: var(--color-success-600);
  color: var(--color-success-700);
}

.alert-warning {
  background-color: var(--color-warning-100);
  border-color: var(--color-warning-600);
  color: var(--color-warning-700);
}

.alert-error {
  background-color: var(--color-error-100);
  border-color: var(--color-error-600);
  color: var(--color-error-700);
}

.alert-info {
  background-color: var(--color-info-100);
  border-color: var(--color-info-600);
  color: var(--color-info-700);
}
```

### 9.6 모달 (Modal)

```css
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: var(--bg-overlay);
  z-index: var(--z-modal-backdrop);
  animation: fadeIn var(--duration-medium) var(--ease-out);
}

.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 90%;
  max-width: 600px;
  max-height: 90vh;
  background-color: var(--color-white);
  border-radius: var(--radius-2xl);
  box-shadow: var(--shadow-2xl);
  z-index: var(--z-modal);
  overflow: hidden;
  animation: scaleIn var(--duration-medium) var(--ease-out);
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-6);
  border-bottom: var(--border-1) solid var(--border-light);
}

.modal-title {
  font-size: var(--text-2xl);
  font-weight: var(--font-semibold);
  color: var(--text-primary);
}

.modal-close {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  background: none;
  cursor: pointer;
  color: var(--text-secondary);
  transition: var(--transition-colors);
}

.modal-close:hover {
  color: var(--text-primary);
}

.modal-body {
  padding: var(--space-6);
  overflow-y: auto;
  max-height: calc(90vh - 140px);
}

.modal-footer {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: var(--space-3);
  padding: var(--space-6);
  border-top: var(--border-1) solid var(--border-light);
}
```


### 9.7 네비게이션 (Navigation)

#### Header
```css
.header {
  position: sticky;
  top: 0;
  width: 100%;
  background-color: var(--color-white);
  border-bottom: var(--border-1) solid var(--border-light);
  box-shadow: var(--shadow-sm);
  z-index: var(--z-sticky);
}

.header-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: var(--container-2xl);
  margin: 0 auto;
  padding: var(--space-4) var(--container-padding-desktop);
}

.header-logo {
  height: 40px;
}

.header-nav {
  display: flex;
  align-items: center;
  gap: var(--space-8);
}

.header-nav-item {
  position: relative;
  font-size: var(--text-base);
  font-weight: var(--font-medium);
  color: var(--text-primary);
  text-decoration: none;
  transition: var(--transition-colors);
}

.header-nav-item:hover {
  color: var(--color-primary-700);
}

.header-nav-item::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 0;
  width: 0;
  height: 2px;
  background-color: var(--color-primary-700);
  transition: width var(--duration-base) var(--ease-out);
}

.header-nav-item:hover::after,
.header-nav-item.active::after {
  width: 100%;
}
```

#### Dropdown Menu
```css
.dropdown {
  position: relative;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  min-width: 200px;
  margin-top: var(--space-2);
  padding: var(--space-2);
  background-color: var(--color-white);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  opacity: 0;
  visibility: hidden;
  transform: translateY(-10px);
  transition: var(--transition-all);
  z-index: var(--z-dropdown);
}

.dropdown:hover .dropdown-menu {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.dropdown-item {
  display: block;
  padding: var(--space-3) var(--space-4);
  font-size: var(--text-sm);
  color: var(--text-primary);
  text-decoration: none;
  border-radius: var(--radius-md);
  transition: var(--transition-colors);
}

.dropdown-item:hover {
  background-color: var(--color-gray-100);
  color: var(--color-primary-700);
}
```

#### Breadcrumb
```css
.breadcrumb {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-4) 0;
  font-size: var(--text-sm);
}

.breadcrumb-item {
  display: flex;
  align-items: center;
  color: var(--text-secondary);
}

.breadcrumb-item a {
  color: var(--text-secondary);
  text-decoration: none;
  transition: var(--transition-colors);
}

.breadcrumb-item a:hover {
  color: var(--color-primary-700);
}

.breadcrumb-item.active {
  color: var(--text-primary);
  font-weight: var(--font-medium);
}

.breadcrumb-separator {
  margin: 0 var(--space-2);
  color: var(--text-tertiary);
}
```

### 9.8 탭 (Tabs)

```css
.tabs {
  border-bottom: var(--border-1) solid var(--border-light);
}

.tabs-list {
  display: flex;
  gap: var(--space-6);
}

.tabs-trigger {
  position: relative;
  padding: var(--space-4) var(--space-2);
  font-size: var(--text-base);
  font-weight: var(--font-medium);
  color: var(--text-secondary);
  background: none;
  border: none;
  cursor: pointer;
  transition: var(--transition-colors);
}

.tabs-trigger:hover {
  color: var(--text-primary);
}

.tabs-trigger.active {
  color: var(--color-primary-700);
}

.tabs-trigger.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 2px;
  background-color: var(--color-primary-700);
}

.tabs-content {
  padding: var(--space-6) 0;
}
```

### 9.9 아코디언 (Accordion)

```css
.accordion {
  border: var(--border-1) solid var(--border-light);
  border-radius: var(--radius-lg);
  overflow: hidden;
}

.accordion-item {
  border-bottom: var(--border-1) solid var(--border-light);
}

.accordion-item:last-child {
  border-bottom: none;
}

.accordion-trigger {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: var(--space-4) var(--space-6);
  font-size: var(--text-base);
  font-weight: var(--font-medium);
  color: var(--text-primary);
  background-color: var(--color-white);
  border: none;
  cursor: pointer;
  transition: var(--transition-colors);
}

.accordion-trigger:hover {
  background-color: var(--color-gray-50);
}

.accordion-icon {
  width: 20px;
  height: 20px;
  transition: transform var(--duration-base) var(--ease-out);
}

.accordion-trigger[aria-expanded="true"] .accordion-icon {
  transform: rotate(180deg);
}

.accordion-content {
  padding: 0 var(--space-6) var(--space-4);
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: var(--leading-relaxed);
}
```

### 9.10 페이지네이션 (Pagination)

```css
.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  margin: var(--space-8) 0;
}

.pagination-item {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 40px;
  height: 40px;
  padding: var(--space-2);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  color: var(--text-primary);
  background-color: var(--color-white);
  border: var(--border-1) solid var(--border-default);
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: var(--transition-all);
}

.pagination-item:hover {
  background-color: var(--color-gray-50);
  border-color: var(--color-primary-500);
}

.pagination-item.active {
  color: var(--color-white);
  background-color: var(--color-primary-700);
  border-color: var(--color-primary-700);
}

.pagination-item:disabled {
  color: var(--text-disabled);
  background-color: var(--color-gray-100);
  cursor: not-allowed;
}
```

### 9.11 로딩 (Loading)

#### Spinner
```css
.spinner {
  display: inline-block;
  width: 40px;
  height: 40px;
  border: 4px solid var(--color-gray-200);
  border-top-color: var(--color-primary-700);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.spinner-sm {
  width: 20px;
  height: 20px;
  border-width: 2px;
}

.spinner-lg {
  width: 60px;
  height: 60px;
  border-width: 6px;
}
```

#### Skeleton
```css
.skeleton {
  background: linear-gradient(
    90deg,
    var(--color-gray-200) 0%,
    var(--color-gray-300) 50%,
    var(--color-gray-200) 100%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s ease-in-out infinite;
  border-radius: var(--radius-md);
}

.skeleton-text {
  height: 1em;
  margin-bottom: var(--space-2);
}

.skeleton-title {
  height: 2em;
  width: 60%;
  margin-bottom: var(--space-4);
}

.skeleton-image {
  width: 100%;
  aspect-ratio: 16 / 9;
}
```

### 9.12 툴팁 (Tooltip)

```css
.tooltip-wrapper {
  position: relative;
  display: inline-block;
}

.tooltip {
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(-8px);
  padding: var(--space-2) var(--space-3);
  font-size: var(--text-xs);
  color: var(--color-white);
  background-color: var(--color-gray-900);
  border-radius: var(--radius-md);
  white-space: nowrap;
  opacity: 0;
  visibility: hidden;
  transition: var(--transition-all);
  z-index: var(--z-tooltip);
}

.tooltip::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 4px solid transparent;
  border-top-color: var(--color-gray-900);
}

.tooltip-wrapper:hover .tooltip {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(-4px);
}
```

## 10. 아이콘 시스템

### 10.1 아이콘 스타일

```css
.icon {
  display: inline-block;
  width: 24px;
  height: 24px;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  fill: none;
}

.icon-sm {
  width: 16px;
  height: 16px;
}

.icon-lg {
  width: 32px;
  height: 32px;
}

.icon-xl {
  width: 48px;
  height: 48px;
}
```

### 10.2 추천 아이콘 세트

- **Heroicons**: https://heroicons.com/
- **Feather Icons**: https://feathericons.com/
- **Lucide**: https://lucide.dev/

### 10.3 주요 아이콘 목록

```
네비게이션:
- menu (햄버거 메뉴)
- x (닫기)
- chevron-down (드롭다운)
- chevron-right (다음)
- arrow-right (화살표)

액션:
- search (검색)
- phone (전화)
- mail (이메일)
- download (다운로드)
- upload (업로드)
- edit (수정)
- trash (삭제)

상태:
- check (완료)
- alert-circle (경고)
- info (정보)
- x-circle (오류)

소셜:
- facebook
- instagram
- youtube
- linkedin

기타:
- home (홈)
- user (사용자)
- calendar (날짜)
- clock (시간)
- map-pin (위치)
- file (파일)
```


## 11. 이미지 가이드라인

### 11.1 이미지 형식

```
WebP (우선):
- 최신 브라우저 지원
- 우수한 압축률
- 투명도 지원

JPEG (대체):
- 사진 이미지
- 압축률 80-85%
- Progressive JPEG 사용

PNG (대체):
- 투명도 필요 시
- 로고, 아이콘
- 8-bit PNG 권장

SVG:
- 로고, 아이콘
- 벡터 그래픽
- 인라인 또는 외부 파일
```

### 11.2 이미지 크기 및 비율

```css
/* 히어로 이미지 */
--image-hero-ratio: 16 / 9;
--image-hero-width: 1920px;
--image-hero-height: 1080px;

/* 제품 이미지 */
--image-product-ratio: 4 / 3;
--image-product-width: 800px;
--image-product-height: 600px;

/* 썸네일 */
--image-thumbnail-ratio: 1 / 1;
--image-thumbnail-width: 400px;
--image-thumbnail-height: 400px;

/* 카드 이미지 */
--image-card-ratio: 16 / 9;
--image-card-width: 600px;
--image-card-height: 338px;
```

### 11.3 반응형 이미지

```html
<!-- srcset 사용 -->
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

<!-- picture 태그 (WebP 지원) -->
<picture>
  <source srcset="image.webp" type="image/webp">
  <source srcset="image.jpg" type="image/jpeg">
  <img src="image.jpg" alt="제품 이미지" loading="lazy">
</picture>
```

### 11.4 이미지 최적화

```css
.image-container {
  position: relative;
  overflow: hidden;
  background-color: var(--color-gray-100);
}

.image-responsive {
  width: 100%;
  height: auto;
  display: block;
}

.image-cover {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.image-contain {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

/* Lazy Loading Placeholder */
.image-loading {
  background: linear-gradient(
    90deg,
    var(--color-gray-200) 0%,
    var(--color-gray-300) 50%,
    var(--color-gray-200) 100%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s ease-in-out infinite;
}
```

## 12. 접근성 가이드라인

### 12.1 색상 대비

```
WCAG 2.1 AA 기준:
- 일반 텍스트: 최소 4.5:1
- 큰 텍스트 (18px+ 또는 14px+ bold): 최소 3:1
- UI 컴포넌트: 최소 3:1

검증 도구:
- WebAIM Contrast Checker
- Chrome DevTools Lighthouse
```

### 12.2 키보드 네비게이션

```css
/* 포커스 스타일 */
*:focus {
  outline: 2px solid var(--color-primary-500);
  outline-offset: 2px;
}

/* 포커스 가시성 */
*:focus:not(:focus-visible) {
  outline: none;
}

*:focus-visible {
  outline: 2px solid var(--color-primary-500);
  outline-offset: 2px;
}

/* Skip Link */
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  padding: var(--space-2) var(--space-4);
  background-color: var(--color-primary-700);
  color: var(--color-white);
  text-decoration: none;
  z-index: var(--z-modal);
}

.skip-link:focus {
  top: 0;
}
```

### 12.3 ARIA 속성

```html
<!-- 랜드마크 -->
<header role="banner">
<nav role="navigation" aria-label="주 메뉴">
<main role="main" id="main-content">
<aside role="complementary">
<footer role="contentinfo">

<!-- 버튼 -->
<button aria-label="메뉴 열기" aria-expanded="false">
  <span aria-hidden="true">☰</span>
</button>

<!-- 폼 -->
<label for="email">이메일</label>
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

<!-- 탭 -->
<div role="tablist">
  <button role="tab" aria-selected="true" aria-controls="panel-1">
    탭 1
  </button>
</div>
<div role="tabpanel" id="panel-1">
  콘텐츠
</div>

<!-- 모달 -->
<div 
  role="dialog" 
  aria-modal="true" 
  aria-labelledby="modal-title"
  aria-describedby="modal-description"
>
  <h2 id="modal-title">제목</h2>
  <p id="modal-description">설명</p>
</div>
```

### 12.4 스크린 리더 지원

```html
<!-- 시각적으로 숨기기 (스크린 리더는 읽음) -->
<style>
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
</style>

<!-- 사용 예시 -->
<button>
  <span class="sr-only">검색</span>
  <svg aria-hidden="true">...</svg>
</button>

<!-- 장식 이미지 -->
<img src="decoration.jpg" alt="" role="presentation">

<!-- 의미 있는 이미지 -->
<img src="product.jpg" alt="스마트 안전 모니터링 시스템">
```

## 13. 반응형 디자인 패턴

### 13.1 컨테이너 쿼리 (선택)

```css
/* 컨테이너 정의 */
.container {
  container-type: inline-size;
  container-name: card;
}

/* 컨테이너 쿼리 */
@container card (min-width: 400px) {
  .card-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}
```

### 13.2 유틸리티 클래스

```css
/* Display */
.hidden { display: none; }
.block { display: block; }
.flex { display: flex; }
.grid { display: grid; }

/* 반응형 Display */
@media (max-width: 767px) {
  .hidden-mobile { display: none; }
}

@media (min-width: 768px) {
  .hidden-desktop { display: none; }
}

/* Flexbox */
.flex-row { flex-direction: row; }
.flex-col { flex-direction: column; }
.items-center { align-items: center; }
.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }
.gap-4 { gap: var(--space-4); }

/* Grid */
.grid-cols-1 { grid-template-columns: repeat(1, 1fr); }
.grid-cols-2 { grid-template-columns: repeat(2, 1fr); }
.grid-cols-3 { grid-template-columns: repeat(3, 1fr); }
.grid-cols-4 { grid-template-columns: repeat(4, 1fr); }

/* Spacing */
.m-0 { margin: 0; }
.m-4 { margin: var(--space-4); }
.mt-4 { margin-top: var(--space-4); }
.mb-4 { margin-bottom: var(--space-4); }
.p-4 { padding: var(--space-4); }
.pt-4 { padding-top: var(--space-4); }
.pb-4 { padding-bottom: var(--space-4); }

/* Text Alignment */
.text-left { text-align: left; }
.text-center { text-align: center; }
.text-right { text-align: right; }

/* Width */
.w-full { width: 100%; }
.w-auto { width: auto; }
.max-w-screen-sm { max-width: var(--container-sm); }
.max-w-screen-lg { max-width: var(--container-lg); }
```

## 14. 성능 최적화

### 14.1 CSS 최적화

```css
/* Critical CSS (인라인) */
/* 초기 렌더링에 필요한 최소 CSS */

/* Non-critical CSS (비동기 로드) */
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="styles.css"></noscript>
```

### 14.2 폰트 최적화

```css
/* 폰트 로딩 전략 */
@font-face {
  font-family: 'Pretendard';
  src: url('/fonts/Pretendard-Regular.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap; /* FOUT 방지 */
}

/* 폰트 프리로드 */
<link rel="preload" href="/fonts/Pretendard-Regular.woff2" as="font" type="font/woff2" crossorigin>
```

### 14.3 이미지 최적화

```html
<!-- Lazy Loading -->
<img src="image.jpg" loading="lazy" alt="설명">

<!-- Blur-up 기법 -->
<div class="image-wrapper">
  <img 
    src="image-placeholder.jpg" 
    data-src="image-full.jpg"
    class="blur-up"
    alt="설명"
  >
</div>

<style>
.blur-up {
  filter: blur(10px);
  transition: filter 0.3s;
}

.blur-up.loaded {
  filter: blur(0);
}
</style>
```

## 15. 다크모드 (선택사항)

### 15.1 다크모드 색상

```css
:root {
  --color-scheme: light;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-scheme: dark;
    
    /* 색상 재정의 */
    --text-primary: var(--color-gray-100);
    --text-secondary: var(--color-gray-400);
    --bg-primary: var(--color-gray-900);
    --bg-secondary: var(--color-gray-800);
    --border-default: var(--color-gray-700);
  }
}

/* 수동 토글 */
[data-theme="dark"] {
  --color-scheme: dark;
  /* 다크모드 색상 */
}
```

## 16. 브라우저 지원

### 16.1 지원 브라우저

```
Desktop:
- Chrome: 최신 2개 버전
- Firefox: 최신 2개 버전
- Safari: 최신 2개 버전
- Edge: 최신 2개 버전

Mobile:
- iOS Safari: 최신 2개 버전
- Chrome Mobile: 최신 2개 버전
- Samsung Internet: 최신 버전
```

### 16.2 폴리필 및 폴백

```html
<!-- CSS 변수 폴백 -->
<style>
.button {
  background-color: #1A4D8F; /* 폴백 */
  background-color: var(--color-primary-700);
}
</style>

<!-- 모던 기능 감지 -->
<script>
if (!('IntersectionObserver' in window)) {
  // 폴리필 로드
}
</script>
```

## 17. 개발 가이드

### 17.1 CSS 네이밍 컨벤션

```
BEM (Block Element Modifier):
.block {}
.block__element {}
.block--modifier {}

예시:
.card {}
.card__header {}
.card__body {}
.card--featured {}
```

### 17.2 파일 구조

```
styles/
├── base/
│   ├── reset.css
│   ├── typography.css
│   └── variables.css
├── components/
│   ├── button.css
│   ├── card.css
│   ├── modal.css
│   └── ...
├── layout/
│   ├── header.css
│   ├── footer.css
│   └── grid.css
├── pages/
│   ├── home.css
│   ├── product.css
│   └── ...
└── utilities/
    ├── spacing.css
    └── display.css
```

### 17.3 코드 품질

```
도구:
- Stylelint: CSS 린팅
- Prettier: 코드 포맷팅
- PostCSS: CSS 변환
- Autoprefixer: 벤더 프리픽스 자동 추가

검증:
- W3C CSS Validator
- Lighthouse 성능 점수
- WAVE 접근성 검사
```

## 18. 디자인 토큰 (Design Tokens)

### 18.1 JSON 형식

```json
{
  "color": {
    "primary": {
      "700": { "value": "#1A4D8F" }
    }
  },
  "spacing": {
    "4": { "value": "1rem" }
  },
  "typography": {
    "fontSize": {
      "base": { "value": "1rem" }
    }
  }
}
```

### 18.2 플랫폼별 변환

```
CSS Variables → Web
JSON → iOS/Android
Figma Tokens → Design
```

---

**문서 버전**: 1.0  
**작성일**: 2024  
**작성자**: UX Design Team  
**관련 문서**: ux-design-concept.md, ux-information-architecture.md, ux-wireframes.md

**사용 방법**:
1. 디자이너: Figma에서 컴포넌트 라이브러리 구축
2. 개발자: CSS 변수 및 클래스 구현
3. 프로젝트 관리자: 일관성 검증 및 품질 관리

**업데이트 정책**:
- 주요 변경: 버전 업데이트 (1.0 → 2.0)
- 마이너 변경: 패치 업데이트 (1.0 → 1.1)
- 모든 변경사항은 팀 리뷰 후 반영
