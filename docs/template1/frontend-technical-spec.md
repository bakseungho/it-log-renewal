# 프론트엔드 기술 명세서

## 1. 프로젝트 개요

### 1.1 기술 스택
- **HTML5**: 시맨틱 마크업
- **CSS3**: 반응형 디자인, Flexbox, Grid
- **JavaScript (ES6+)**: 모던 자바스크립트 문법
- **jQuery 3.x**: DOM 조작 및 이벤트 핸들링
- **정적 웹사이트**: 프레임워크 없이 순수 HTML/CSS/JS 구현

### 1.2 브라우저 지원
- Chrome (최신 버전)
- Firefox (최신 버전)
- Safari (최신 버전)
- Edge (최신 버전)
- 모바일: iOS Safari 13+, Chrome Mobile

### 1.3 성능 목표
- Lighthouse 점수: 90점 이상
- First Contentful Paint (FCP): 1.8초 이내
- Largest Contentful Paint (LCP): 2.5초 이내
- Cumulative Layout Shift (CLS): 0.1 이하
- Time to Interactive (TTI): 3.8초 이내

## 2. 프로젝트 구조

### 2.1 디렉토리 구조
```
project-root/
├── index.html              # 메인 페이지
├── assets/
│   ├── css/
│   │   ├── reset.css      # CSS 리셋
│   │   ├── variables.css  # CSS 변수
│   │   ├── common.css     # 공통 스타일
│   │   ├── components.css # 컴포넌트 스타일
│   │   └── pages/         # 페이지별 스타일
│   ├── js/
│   │   ├── vendor/        # 외부 라이브러리
│   │   │   └── jquery.min.js
│   │   ├── utils.js       # 유틸리티 함수
│   │   ├── components.js  # 컴포넌트 로직
│   │   └── main.js        # 메인 스크립트
│   ├── images/            # 이미지 파일
│   │   ├── logo/
│   │   ├── icons/
│   │   └── content/
│   └── fonts/             # 웹폰트
└── pages/                 # 서브 페이지들
```


### 2.2 파일 명명 규칙
- HTML: 소문자, 하이픈 구분 (about-us.html)
- CSS: 소문자, 하이픈 구분 (main-header.css)
- JS: 카멜케이스 (mainNavigation.js)
- 이미지: 소문자, 하이픈 구분, 의미있는 이름 (hero-banner-01.jpg)

## 3. HTML 구조

### 3.1 기본 템플릿
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="페이지 설명 (160자 이내)">
    <meta name="keywords" content="키워드1, 키워드2">
    
    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="페이지 제목">
    <meta property="og:description" content="페이지 설명">
    <meta property="og:image" content="대표 이미지 URL">
    <meta property="og:url" content="페이지 URL">
    
    <title>페이지 제목 - 사이트명</title>
    
    <!-- Favicon -->
    <link rel="icon" type="image/png" href="/assets/images/favicon.png">
    
    <!-- CSS -->
    <link rel="stylesheet" href="/assets/css/reset.css">
    <link rel="stylesheet" href="/assets/css/variables.css">
    <link rel="stylesheet" href="/assets/css/common.css">
    <link rel="stylesheet" href="/assets/css/components.css">
</head>
<body>
    <!-- Skip Navigation -->
    <a href="#main-content" class="skip-link">본문으로 바로가기</a>
    
    <!-- Header -->
    <header class="header" role="banner">
        <!-- 헤더 내용 -->
    </header>
    
    <!-- Main Navigation -->
    <nav class="main-nav" role="navigation" aria-label="주 메뉴">
        <!-- 네비게이션 내용 -->
    </nav>
    
    <!-- Main Content -->
    <main id="main-content" role="main">
        <!-- 페이지 콘텐츠 -->
    </main>
    
    <!-- Footer -->
    <footer class="footer" role="contentinfo">
        <!-- 푸터 내용 -->
    </footer>
    
    <!-- Scripts -->
    <script src="/assets/js/vendor/jquery.min.js"></script>
    <script src="/assets/js/utils.js"></script>
    <script src="/assets/js/components.js"></script>
    <script src="/assets/js/main.js"></script>
</body>
</html>
```

### 3.2 시맨틱 마크업 원칙
- 적절한 HTML5 시맨틱 태그 사용 (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- 제목 태그 계층 구조 준수 (h1 → h2 → h3)
- 리스트는 `<ul>`, `<ol>`, `<dl>` 사용
- 버튼은 `<button>`, 링크는 `<a>` 태그 사용
- 폼 요소는 `<label>`과 연결

### 3.3 접근성 속성
```html
<!-- ARIA 레이블 -->
<button aria-label="메뉴 열기" aria-expanded="false">
    <span class="icon-menu"></span>
</button>

<!-- 폼 접근성 -->
<label for="email">이메일</label>
<input type="email" id="email" name="email" required aria-required="true">

<!-- 이미지 대체 텍스트 -->
<img src="logo.png" alt="회사 로고">

<!-- 랜드마크 역할 -->
<nav role="navigation" aria-label="주 메뉴">
<main role="main">
<aside role="complementary">
```

## 4. CSS 아키텍처

### 4.1 CSS 방법론: BEM (Block Element Modifier)
```css
/* Block */
.card {}

/* Element */
.card__header {}
.card__body {}
.card__footer {}

/* Modifier */
.card--featured {}
.card--large {}
```

### 4.2 CSS 변수 (variables.css)
```css
:root {
    /* Colors */
    --color-primary: #[메인컬러];
    --color-secondary: #[보조컬러];
    --color-accent: #[강조컬러];
    --color-text-primary: #333333;
    --color-text-secondary: #666666;
    --color-background: #FFFFFF;
    --color-background-alt: #F5F5F5;
    --color-border: #DDDDDD;
    
    /* Typography */
    --font-family-primary: 'Noto Sans KR', sans-serif;
    --font-size-base: 16px;
    --font-size-small: 14px;
    --font-size-large: 18px;
    --font-size-h1: 48px;
    --font-size-h2: 36px;
    --font-size-h3: 28px;
    --font-size-h4: 24px;
    --line-height-base: 1.6;
    --line-height-heading: 1.3;
    
    /* Spacing */
    --spacing-xs: 8px;
    --spacing-sm: 16px;
    --spacing-md: 24px;
    --spacing-lg: 32px;
    --spacing-xl: 48px;
    --spacing-xxl: 80px;
    
    /* Layout */
    --container-max-width: 1200px;
    --border-radius: 4px;
    --border-radius-large: 8px;
    
    /* Transitions */
    --transition-fast: 0.2s ease;
    --transition-base: 0.3s ease;
    --transition-slow: 0.5s ease;
    
    /* Shadows */
    --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.1);
    --shadow-md: 0 4px 8px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 8px 16px rgba(0, 0, 0, 0.15);
}
```

### 4.3 반응형 디자인 (모바일 퍼스트)
```css
/* 기본 스타일 (모바일) */
.container {
    padding: 0 16px;
}

/* 태블릿 */
@media (min-width: 768px) {
    .container {
        padding: 0 24px;
    }
}

/* 데스크톱 */
@media (min-width: 1024px) {
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 40px;
    }
}

/* 대형 데스크톱 */
@media (min-width: 1441px) {
    .container {
        max-width: 1400px;
    }
}
```

### 4.4 공통 컴포넌트 스타일
```css
/* 버튼 */
.btn {
    display: inline-block;
    padding: 12px 24px;
    font-size: var(--font-size-base);
    font-weight: 500;
    text-align: center;
    text-decoration: none;
    border: none;
    border-radius: var(--border-radius);
    cursor: pointer;
    transition: all var(--transition-base);
}

.btn--primary {
    background-color: var(--color-primary);
    color: #FFFFFF;
}

.btn--primary:hover {
    opacity: 0.9;
    transform: translateY(-2px);
}

/* 카드 */
.card {
    background: #FFFFFF;
    border-radius: var(--border-radius-large);
    box-shadow: var(--shadow-md);
    padding: var(--spacing-lg);
    transition: box-shadow var(--transition-base);
}

.card:hover {
    box-shadow: var(--shadow-lg);
}

/* 입력 필드 */
.input {
    width: 100%;
    height: 48px;
    padding: 0 16px;
    font-size: var(--font-size-base);
    border: 1px solid var(--color-border);
    border-radius: var(--border-radius);
    transition: border-color var(--transition-fast);
}

.input:focus {
    outline: none;
    border-color: var(--color-primary);
    box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.1);
}
```

## 5. JavaScript 구조

### 5.1 코딩 컨벤션
- ES6+ 문법 사용 (const, let, arrow function, template literals)
- 엄격 모드 사용 (`'use strict';`)
- 세미콜론 사용
- 들여쓰기: 2 spaces
- 변수명: camelCase
- 상수명: UPPER_SNAKE_CASE
- 함수명: 동사로 시작 (getData, handleClick)

### 5.2 유틸리티 함수 (utils.js)
```javascript
'use strict';

const Utils = {
  // 디바운스
  debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  },

  // 스로틀
  throttle(func, limit) {
    let inThrottle;
    return function(...args) {
      if (!inThrottle) {
        func.apply(this, args);
        inThrottle = true;
        setTimeout(() => inThrottle = false, limit);
      }
    };
  },

  // 스무스 스크롤
  smoothScroll(target, duration = 800) {
    const targetElement = document.querySelector(target);
    if (!targetElement) return;
    
    const targetPosition = targetElement.offsetTop;
    const startPosition = window.pageYOffset;
    const distance = targetPosition - startPosition;
    let startTime = null;

    function animation(currentTime) {
      if (startTime === null) startTime = currentTime;
      const timeElapsed = currentTime - startTime;
      const run = ease(timeElapsed, startPosition, distance, duration);
      window.scrollTo(0, run);
      if (timeElapsed < duration) requestAnimationFrame(animation);
    }

    function ease(t, b, c, d) {
      t /= d / 2;
      if (t < 1) return c / 2 * t * t + b;
      t--;
      return -c / 2 * (t * (t - 2) - 1) + b;
    }

    requestAnimationFrame(animation);
  },

  // 이미지 Lazy Loading
  lazyLoadImages() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
          observer.unobserve(img);
        }
      });
    });

    images.forEach(img => imageObserver.observe(img));
  }
};
```

### 5.3 컴포넌트 로직 (components.js)
```javascript
'use strict';

// 모바일 메뉴
const MobileMenu = {
  init() {
    this.menuButton = $('.js-menu-toggle');
    this.menu = $('.js-mobile-menu');
    this.bindEvents();
  },

  bindEvents() {
    this.menuButton.on('click', () => this.toggle());
    $(document).on('click', (e) => this.handleOutsideClick(e));
  },

  toggle() {
    const isExpanded = this.menuButton.attr('aria-expanded') === 'true';
    this.menuButton.attr('aria-expanded', !isExpanded);
    this.menu.toggleClass('is-open');
    $('body').toggleClass('menu-open');
  },

  handleOutsideClick(e) {
    if (!$(e.target).closest('.js-mobile-menu, .js-menu-toggle').length) {
      this.close();
    }
  },

  close() {
    this.menuButton.attr('aria-expanded', 'false');
    this.menu.removeClass('is-open');
    $('body').removeClass('menu-open');
  }
};
```

// 스크롤 헤더
const ScrollHeader = {
  init() {
    this.header = $('.header');
    this.lastScroll = 0;
    this.bindEvents();
  },

  bindEvents() {
    $(window).on('scroll', Utils.throttle(() => this.handleScroll(), 100));
  },

  handleScroll() {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
      this.header.addClass('header--scrolled');
    } else {
      this.header.removeClass('header--scrolled');
    }

    if (currentScroll > this.lastScroll && currentScroll > 300) {
      this.header.addClass('header--hidden');
    } else {
      this.header.removeClass('header--hidden');
    }

    this.lastScroll = currentScroll;
  }
};

// 탭 컴포넌트
const Tabs = {
  init() {
    this.bindEvents();
  },

  bindEvents() {
    $('.js-tab-button').on('click', (e) => this.handleTabClick(e));
    $('.js-tab-button').on('keydown', (e) => this.handleKeyboard(e));
  },

  handleTabClick(e) {
    e.preventDefault();
    const $button = $(e.currentTarget);
    const targetId = $button.attr('aria-controls');
    
    // 모든 탭 비활성화
    $button.closest('.tabs').find('.js-tab-button')
      .attr('aria-selected', 'false')
      .removeClass('is-active');
    
    $button.closest('.tabs').find('.js-tab-panel')
      .attr('hidden', 'true')
      .removeClass('is-active');
    
    // 선택된 탭 활성화
    $button.attr('aria-selected', 'true').addClass('is-active');
    $(`#${targetId}`).removeAttr('hidden').addClass('is-active');
  },

  handleKeyboard(e) {
    const $current = $(e.currentTarget);
    const $tabs = $current.closest('.tabs').find('.js-tab-button');
    const currentIndex = $tabs.index($current);
    
    let $next;
    
    switch(e.key) {
      case 'ArrowLeft':
        e.preventDefault();
        $next = currentIndex > 0 ? $tabs.eq(currentIndex - 1) : $tabs.last();
        break;
      case 'ArrowRight':
        e.preventDefault();
        $next = currentIndex < $tabs.length - 1 ? $tabs.eq(currentIndex + 1) : $tabs.first();
        break;
      case 'Home':
        e.preventDefault();
        $next = $tabs.first();
        break;
      case 'End':
        e.preventDefault();
        $next = $tabs.last();
        break;
    }
    
    if ($next) {
      $next.focus().trigger('click');
    }
  }
};
```

### 5.4 메인 스크립트 (main.js)
```javascript
'use strict';

$(document).ready(function() {
  // 컴포넌트 초기화
  MobileMenu.init();
  ScrollHeader.init();
  Tabs.init();
  
  // Lazy Loading 초기화
  Utils.lazyLoadImages();
  
  // 스무스 스크롤
  $('a[href^="#"]').on('click', function(e) {
    e.preventDefault();
    const target = $(this).attr('href');
    if (target !== '#') {
      Utils.smoothScroll(target);
    }
  });
  
  // 폼 검증
  $('form').on('submit', function(e) {
    e.preventDefault();
    // 폼 검증 로직
  });
  
  // 외부 링크 새 창 열기
  $('a[href^="http"]').not('[href*="' + window.location.hostname + '"]')
    .attr('target', '_blank')
    .attr('rel', 'noopener noreferrer');
});
```

## 6. 성능 최적화

### 6.1 이미지 최적화
```html
<!-- Lazy Loading -->
<img data-src="image.jpg" alt="설명" class="lazy">

<!-- Responsive Images -->
<img 
  srcset="image-320w.jpg 320w,
          image-640w.jpg 640w,
          image-1024w.jpg 1024w"
  sizes="(max-width: 768px) 100vw, 50vw"
  src="image-640w.jpg"
  alt="설명">

<!-- WebP 지원 -->
<picture>
  <source srcset="image.webp" type="image/webp">
  <source srcset="image.jpg" type="image/jpeg">
  <img src="image.jpg" alt="설명">
</picture>
```

### 6.2 CSS 최적화
- Critical CSS 인라인 삽입
- 사용하지 않는 CSS 제거
- CSS 파일 압축 (minify)
- 미디어 쿼리 최적화

### 6.3 JavaScript 최적화
- 스크립트 defer 또는 async 로딩
- 코드 압축 (minify)
- 이벤트 위임 사용
- 디바운스/스로틀 적용

### 6.4 로딩 전략
```html
<!-- Critical CSS -->
<style>
  /* 초기 렌더링에 필요한 최소 CSS */
</style>

<!-- Non-critical CSS -->
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="styles.css"></noscript>

<!-- JavaScript -->
<script src="main.js" defer></script>

<!-- 폰트 최적화 -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>
```

## 7. 접근성 구현

### 7.1 키보드 네비게이션
- Tab 키로 모든 인터랙티브 요소 접근 가능
- Enter/Space로 버튼 활성화
- Esc로 모달/메뉴 닫기
- 화살표 키로 탭/슬라이더 이동

### 7.2 스크린 리더 지원
```html
<!-- 숨김 텍스트 -->
<span class="sr-only">스크린 리더 전용 텍스트</span>

<!-- ARIA 레이블 -->
<button aria-label="검색">
  <svg aria-hidden="true">...</svg>
</button>

<!-- 라이브 리전 -->
<div role="alert" aria-live="polite">
  알림 메시지
</div>
```

### 7.3 색상 대비
- 텍스트와 배경 대비 비율 4.5:1 이상
- 큰 텍스트(18pt 이상) 3:1 이상
- 색상만으로 정보 전달하지 않기

### 7.4 포커스 표시
```css
/* 포커스 스타일 */
:focus {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/* 마우스 클릭 시 포커스 제거 (키보드 사용자는 유지) */
:focus:not(:focus-visible) {
  outline: none;
}

:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

## 8. SEO 최적화

### 8.1 메타 태그
```html
<!-- 기본 메타 태그 -->
<title>페이지 제목 - 사이트명 (60자 이내)</title>
<meta name="description" content="페이지 설명 (160자 이내)">
<meta name="keywords" content="키워드1, 키워드2, 키워드3">

<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:title" content="페이지 제목">
<meta property="og:description" content="페이지 설명">
<meta property="og:image" content="https://example.com/image.jpg">
<meta property="og:url" content="https://example.com/page">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="페이지 제목">
<meta name="twitter:description" content="페이지 설명">
<meta name="twitter:image" content="https://example.com/image.jpg">

<!-- Canonical URL -->
<link rel="canonical" href="https://example.com/page">
```

### 8.2 구조화된 데이터
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "회사명",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+82-2-1234-5678",
    "contactType": "customer service"
  }
}
</script>
```

### 8.3 사이트맵 및 robots.txt
```xml
<!-- sitemap.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2024-01-01</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

```
# robots.txt
User-agent: *
Allow: /
Sitemap: https://example.com/sitemap.xml
```

## 9. 테스트 체크리스트

### 9.1 기능 테스트
- [ ] 모든 링크 작동 확인
- [ ] 폼 제출 및 검증
- [ ] 모바일 메뉴 동작
- [ ] 탭/아코디언 인터랙션
- [ ] 이미지 Lazy Loading
- [ ] 스무스 스크롤

### 9.2 반응형 테스트
- [ ] 모바일 (320px - 767px)
- [ ] 태블릿 (768px - 1023px)
- [ ] 데스크톱 (1024px+)
- [ ] 가로/세로 모드
- [ ] 터치 인터랙션

### 9.3 브라우저 호환성 테스트
- [ ] Chrome (최신)
- [ ] Firefox (최신)
- [ ] Safari (최신)
- [ ] Edge (최신)
- [ ] iOS Safari
- [ ] Chrome Mobile

### 9.4 성능 테스트
- [ ] Lighthouse 점수 90+ (모든 카테고리)
- [ ] PageSpeed Insights 통과
- [ ] Core Web Vitals 기준 충족
- [ ] 이미지 최적화 확인
- [ ] 네트워크 요청 최소화

### 9.5 접근성 테스트
- [ ] WAVE 도구 검사 (에러 0개)
- [ ] 키보드만으로 전체 네비게이션
- [ ] 스크린 리더 테스트 (NVDA/JAWS)
- [ ] 색상 대비 검사 (4.5:1 이상)
- [ ] 포커스 표시 확인
- [ ] ARIA 속성 검증

### 9.6 SEO 테스트
- [ ] 메타 태그 완성도
- [ ] 구조화된 데이터 검증
- [ ] sitemap.xml 생성
- [ ] robots.txt 설정
- [ ] 404 페이지 설정
- [ ] 페이지 로딩 속도

## 10. 배포 준비

### 10.1 파일 최적화
```bash
# CSS 압축
# 원본: styles.css → 압축: styles.min.css

# JavaScript 압축
# 원본: main.js → 압축: main.min.js

# 이미지 최적화
# JPG/PNG → WebP 변환
# 압축률 80-85% 적용
```

### 10.2 배포 전 체크리스트
- [ ] 모든 파일 압축 (CSS, JS)
- [ ] 이미지 최적화 완료
- [ ] 메타 태그 설정 완료
- [ ] Favicon 설정
- [ ] 404 페이지 생성
- [ ] sitemap.xml 생성
- [ ] robots.txt 설정
- [ ] Google Analytics 설치
- [ ] 성능 테스트 통과
- [ ] 접근성 테스트 통과
- [ ] 크로스 브라우저 테스트 완료
- [ ] 모바일 테스트 완료

### 10.3 모니터링 설정
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## 11. 유지보수 가이드

### 11.1 코드 주석 규칙
```javascript
/**
 * 함수 설명
 * @param {string} param1 - 파라미터 설명
 * @param {number} param2 - 파라미터 설명
 * @returns {boolean} 반환값 설명
 */
function exampleFunction(param1, param2) {
  // 구현
}
```

### 11.2 버전 관리
- Git을 사용한 버전 관리
- 의미있는 커밋 메시지 작성
- 브랜치 전략: main (배포), develop (개발)

### 11.3 문서화
- README.md: 프로젝트 개요 및 설치 방법
- CHANGELOG.md: 버전별 변경사항
- 주요 기능별 사용 가이드

## 12. 참고 자료

### 12.1 개발 도구
- VS Code: 코드 에디터
- Chrome DevTools: 디버깅 및 성능 분석
- Lighthouse: 성능/접근성 측정
- WAVE: 접근성 검사
- PageSpeed Insights: 성능 분석

### 12.2 학습 자료
- MDN Web Docs: https://developer.mozilla.org/
- Web.dev: https://web.dev/
- WCAG 가이드라인: https://www.w3.org/WAI/WCAG21/quickref/
- jQuery 문서: https://api.jquery.com/

### 12.3 유용한 라이브러리
- jQuery 3.x: DOM 조작
- Intersection Observer API: Lazy Loading
- Web Animations API: 애니메이션

---

## 다음 단계

1. **UX 설계 완료 대기**: PM 및 UX 디자이너의 설계 문서 완성
2. **프로젝트 구조 생성**: 폴더 및 기본 파일 셋업
3. **HTML 마크업**: 주요 페이지 구조 작성
4. **CSS 스타일링**: 디자인 시스템 구축
5. **JavaScript 구현**: 인터랙션 및 기능 개발
6. **테스트 및 최적화**: 성능, 접근성, 호환성 검증
7. **배포 준비**: 파일 최적화 및 최종 점검

현재 기술 명세서 작성이 완료되었습니다. UX 설계 문서가 완성되면 실제 코드 구현을 시작하겠습니다.
