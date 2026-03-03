# 프론트엔드 개발자를 위한 요구사항 문서

## 문서 개요

**프로젝트명**: 홈페이지 리뉴얼 프로젝트  
**대상**: 프론트엔드 개발자  
**목적**: B2B 공사/현장 솔루션 회사의 정적 웹사이트 개발 가이드  
**작성일**: 2024  
**버전**: 1.0

---

## 1. 프로젝트 개요

### 1.1 기술 스택
- **마크업**: HTML5 (시맨틱 태그)
- **스타일**: CSS3 (Flexbox, Grid, CSS Variables)
- **스크립트**: JavaScript (ES6+), jQuery 3.x
- **라이브러리**:
  - Swiper.js (슬라이더/캐러셀)
  - AOS (Animate On Scroll)
  - Lightbox2 또는 GLightbox (이미지 갤러리)
  - jQuery Validation (폼 검증)

### 1.2 프로젝트 제약사항
- **정적 웹사이트**: 데이터베이스 없음
- **제외 기능**: 로그인, 회원가입, 게시판, 실시간 채팅
- **포함 기능**: 문의 폼, 검색, 다운로드, 지도 연동
- **데이터 관리**: JSON 파일 활용 (제품 정보, 실적 등)

### 1.3 브라우저 지원
- **데스크톱**:
  - Chrome (최신 버전 및 -1)
  - Firefox (최신 버전 및 -1)
  - Safari (최신 버전 및 -1)
  - Edge (최신 버전 및 -1)
- **모바일**:
  - iOS Safari (최신 2개 버전)
  - Chrome Mobile (최신 버전)
  - Samsung Internet (최신 버전)

---

## 2. 프로젝트 구조

### 2.1 디렉토리 구조
```
project-root/
├── index.html
├── about/
│   ├── index.html
│   ├── history.html
│   ├── vision.html
│   └── certifications.html
├── products/
│   ├── index.html
│   ├── category-a.html
│   ├── category-b.html
│   └── detail.html (템플릿)
├── portfolio/
│   └── index.html
├── support/
│   ├── faq.html
│   └── downloads.html
├── contact/
│   └── index.html
├── assets/
│   ├── css/
│   │   ├── reset.css
│   │   ├── variables.css
│   │   ├── common.css
│   │   ├── components.css
│   │   ├── layout.css
│   │   └── pages/
│   │       ├── home.css
│   │       ├── products.css
│   │       └── ...
│   ├── js/
│   │   ├── vendor/
│   │   │   ├── jquery-3.7.1.min.js
│   │   │   ├── swiper-bundle.min.js
│   │   │   └── ...
│   │   ├── common.js
│   │   ├── components/
│   │   │   ├── header.js
│   │   │   ├── search.js
│   │   │   └── ...
│   │   └── pages/
│   │       ├── home.js
│   │       └── ...
│   ├── images/
│   │   ├── common/
│   │   ├── products/
│   │   ├── portfolio/
│   │   └── ...
│   ├── fonts/
│   └── data/
│       ├── products.json
│       ├── portfolio.json
│       └── faq.json
├── favicon.ico
├── robots.txt
├── sitemap.xml
└── README.md
```


### 2.2 네이밍 컨벤션

#### HTML 파일
- 소문자 사용
- 하이픈으로 단어 구분
- 예: `index.html`, `product-detail.html`, `contact-us.html`

#### CSS 클래스 (BEM 방식)
```css
/* Block */
.header {}
.product-card {}

/* Element */
.header__logo {}
.header__nav {}
.product-card__image {}
.product-card__title {}

/* Modifier */
.header--sticky {}
.product-card--featured {}
.button--primary {}
.button--secondary {}
```

#### JavaScript 변수/함수
```javascript
// camelCase
const headerElement = document.querySelector('.header');
const isMenuOpen = false;

function toggleMenu() {}
function initSlider() {}
function validateForm() {}
```

#### 이미지 파일
- 소문자 사용
- 하이픈으로 단어 구분
- 의미 있는 이름
- 예: `hero-banner.jpg`, `product-01.png`, `logo-white.svg`

---

## 3. HTML 개발 가이드

### 3.1 시맨틱 HTML 구조
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="페이지 설명 (160자 이내)">
    <meta name="keywords" content="키워드1, 키워드2, 키워드3">
    
    <!-- Open Graph -->
    <meta property="og:title" content="페이지 제목">
    <meta property="og:description" content="페이지 설명">
    <meta property="og:image" content="대표 이미지 URL">
    <meta property="og:url" content="페이지 URL">
    
    <title>페이지 제목 - 사이트명</title>
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    
    <!-- CSS -->
    <link rel="stylesheet" href="/assets/css/reset.css">
    <link rel="stylesheet" href="/assets/css/variables.css">
    <link rel="stylesheet" href="/assets/css/common.css">
    <link rel="stylesheet" href="/assets/css/pages/home.css">
</head>
<body>
    <!-- Skip Navigation -->
    <a href="#main-content" class="skip-link">본문으로 바로가기</a>
    
    <!-- Header -->
    <header class="header">
        <div class="container">
            <h1 class="header__logo">
                <a href="/">
                    <img src="/assets/images/logo.svg" alt="회사명">
                </a>
            </h1>
            <nav class="header__nav" aria-label="주 메뉴">
                <!-- Navigation -->
            </nav>
        </div>
    </header>
    
    <!-- Main Content -->
    <main id="main-content">
        <section class="hero">
            <!-- Hero Section -->
        </section>
        
        <section class="products">
            <!-- Products Section -->
        </section>
    </main>
    
    <!-- Footer -->
    <footer class="footer">
        <!-- Footer Content -->
    </footer>
    
    <!-- Scripts -->
    <script src="/assets/js/vendor/jquery-3.7.1.min.js"></script>
    <script src="/assets/js/common.js"></script>
    <script src="/assets/js/pages/home.js"></script>
</body>
</html>
```

### 3.2 접근성 필수 요소
```html
<!-- 이미지 대체 텍스트 -->
<img src="product.jpg" alt="제품명 - 간단한 설명">

<!-- 장식용 이미지 -->
<img src="decoration.jpg" alt="" role="presentation">

<!-- 폼 레이블 -->
<label for="name">이름</label>
<input type="text" id="name" name="name" required>

<!-- 버튼 -->
<button type="button" aria-label="메뉴 열기">
    <span class="icon-menu"></span>
</button>

<!-- 링크 -->
<a href="/products" aria-label="제품 페이지로 이동">
    제품 보기
</a>

<!-- ARIA 속성 -->
<nav aria-label="주 메뉴">
<button aria-expanded="false" aria-controls="submenu">
<div role="alert" aria-live="polite">
```


---

## 4. CSS 개발 가이드

### 4.1 CSS 변수 (variables.css)
```css
:root {
  /* Colors */
  --color-primary: #[메인 컬러];
  --color-secondary: #[보조 컬러];
  --color-accent: #[강조 컬러];
  
  --color-text-primary: #212529;
  --color-text-secondary: #6C757D;
  --color-text-light: #FFFFFF;
  
  --color-bg-primary: #FFFFFF;
  --color-bg-secondary: #F8F9FA;
  --color-bg-dark: #212529;
  
  --color-border: #DEE2E6;
  --color-success: #28A745;
  --color-error: #DC3545;
  --color-warning: #FFC107;
  
  /* Typography */
  --font-family-base: 'Noto Sans KR', 'Apple SD Gothic Neo', sans-serif;
  --font-family-en: 'Roboto', -apple-system, sans-serif;
  
  --font-size-xs: 0.75rem;    /* 12px */
  --font-size-sm: 0.875rem;   /* 14px */
  --font-size-base: 1rem;     /* 16px */
  --font-size-lg: 1.125rem;   /* 18px */
  --font-size-xl: 1.25rem;    /* 20px */
  --font-size-2xl: 1.5rem;    /* 24px */
  --font-size-3xl: 1.875rem;  /* 30px */
  --font-size-4xl: 2.25rem;   /* 36px */
  --font-size-5xl: 3rem;      /* 48px */
  
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;
  
  --line-height-tight: 1.25;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.75;
  
  /* Spacing */
  --spacing-xs: 0.5rem;   /* 8px */
  --spacing-sm: 1rem;     /* 16px */
  --spacing-md: 1.5rem;   /* 24px */
  --spacing-lg: 2rem;     /* 32px */
  --spacing-xl: 3rem;     /* 48px */
  --spacing-2xl: 4rem;    /* 64px */
  --spacing-3xl: 5rem;    /* 80px */
  
  /* Layout */
  --container-max-width: 1200px;
  --container-padding: 1rem;
  
  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 2px 8px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 4px 16px rgba(0, 0, 0, 0.15);
  
  /* Transitions */
  --transition-fast: 150ms ease-in-out;
  --transition-base: 300ms ease-in-out;
  --transition-slow: 500ms ease-in-out;
  
  /* Z-index */
  --z-dropdown: 1000;
  --z-sticky: 1020;
  --z-fixed: 1030;
  --z-modal-backdrop: 1040;
  --z-modal: 1050;
  --z-popover: 1060;
  --z-tooltip: 1070;
}
```

### 4.2 반응형 미디어 쿼리
```css
/* Mobile First Approach */

/* Base styles (Mobile: 320px+) */
.container {
  width: 100%;
  padding: 0 var(--container-padding);
}

/* Tablet: 768px+ */
@media (min-width: 768px) {
  .container {
    padding: 0 2rem;
  }
}

/* Desktop: 1024px+ */
@media (min-width: 1024px) {
  .container {
    max-width: var(--container-max-width);
    margin: 0 auto;
  }
}

/* Large Desktop: 1440px+ */
@media (min-width: 1440px) {
  .container {
    max-width: 1400px;
  }
}
```

### 4.3 공통 컴포넌트 스타일

#### 버튼
```css
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem 2rem;
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  text-decoration: none;
  border: none;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all var(--transition-base);
}

.button--primary {
  background-color: var(--color-primary);
  color: var(--color-text-light);
}

.button--primary:hover {
  opacity: 0.9;
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.button--secondary {
  background-color: transparent;
  color: var(--color-primary);
  border: 2px solid var(--color-primary);
}

.button--secondary:hover {
  background-color: var(--color-primary);
  color: var(--color-text-light);
}

.button--large {
  padding: 1rem 2.5rem;
  font-size: var(--font-size-lg);
}

.button--full {
  width: 100%;
}
```

#### 카드
```css
.card {
  background-color: var(--color-bg-primary);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
  overflow: hidden;
  transition: all var(--transition-base);
}

.card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-4px);
}

.card__image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.card__content {
  padding: var(--spacing-md);
}

.card__title {
  font-size: var(--font-size-xl);
  font-weight: var(--font-weight-bold);
  margin-bottom: var(--spacing-sm);
}

.card__description {
  color: var(--color-text-secondary);
  line-height: var(--line-height-relaxed);
}
```


---

## 5. JavaScript 개발 가이드

### 5.1 공통 스크립트 (common.js)
```javascript
// Strict Mode
'use strict';

// Global App Object
const App = {
  init() {
    this.initHeader();
    this.initMobileMenu();
    this.initSmoothScroll();
    this.initBackToTop();
  },

  // Sticky Header
  initHeader() {
    const header = document.querySelector('.header');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
      const currentScroll = window.pageYOffset;

      if (currentScroll > 100) {
        header.classList.add('header--sticky');
      } else {
        header.classList.remove('header--sticky');
      }

      lastScroll = currentScroll;
    });
  },

  // Mobile Menu Toggle
  initMobileMenu() {
    const menuToggle = document.querySelector('.menu-toggle');
    const mobileMenu = document.querySelector('.mobile-menu');
    const body = document.body;

    if (!menuToggle || !mobileMenu) return;

    menuToggle.addEventListener('click', () => {
      const isOpen = mobileMenu.classList.toggle('is-open');
      menuToggle.setAttribute('aria-expanded', isOpen);
      body.classList.toggle('menu-open');
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!mobileMenu.contains(e.target) && !menuToggle.contains(e.target)) {
        mobileMenu.classList.remove('is-open');
        menuToggle.setAttribute('aria-expanded', 'false');
        body.classList.remove('menu-open');
      }
    });
  },

  // Smooth Scroll
  initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#') return;

        e.preventDefault();
        const target = document.querySelector(href);
        
        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      });
    });
  },

  // Back to Top Button
  initBackToTop() {
    const backToTop = document.querySelector('.back-to-top');
    if (!backToTop) return;

    window.addEventListener('scroll', () => {
      if (window.pageYOffset > 300) {
        backToTop.classList.add('is-visible');
      } else {
        backToTop.classList.remove('is-visible');
      }
    });

    backToTop.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }
};

// Initialize on DOM Ready
document.addEventListener('DOMContentLoaded', () => {
  App.init();
});
```

### 5.2 검색 기능 (search.js)
```javascript
const Search = {
  data: [],
  
  async init() {
    await this.loadData();
    this.bindEvents();
  },

  async loadData() {
    try {
      // 제품 데이터 로드
      const productsResponse = await fetch('/assets/data/products.json');
      const products = await productsResponse.json();
      
      // 검색 인덱스 생성
      this.data = products.map(product => ({
        title: product.name,
        description: product.description,
        url: `/products/${product.slug}.html`,
        type: 'product'
      }));
    } catch (error) {
      console.error('검색 데이터 로드 실패:', error);
    }
  },

  bindEvents() {
    const searchInput = document.querySelector('.search-input');
    const searchResults = document.querySelector('.search-results');

    if (!searchInput) return;

    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.trim().toLowerCase();
      
      if (query.length < 2) {
        searchResults.innerHTML = '';
        searchResults.classList.remove('is-visible');
        return;
      }

      const results = this.search(query);
      this.displayResults(results);
    });
  },

  search(query) {
    return this.data.filter(item => {
      return item.title.toLowerCase().includes(query) ||
             item.description.toLowerCase().includes(query);
    }).slice(0, 5); // 최대 5개 결과
  },

  displayResults(results) {
    const searchResults = document.querySelector('.search-results');
    
    if (results.length === 0) {
      searchResults.innerHTML = '<p class="no-results">검색 결과가 없습니다.</p>';
    } else {
      searchResults.innerHTML = results.map(item => `
        <a href="${item.url}" class="search-result-item">
          <strong>${item.title}</strong>
          <p>${item.description}</p>
        </a>
      `).join('');
    }
    
    searchResults.classList.add('is-visible');
  }
};

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  Search.init();
});
```

### 5.3 문의 폼 검증 (contact-form.js)
```javascript
const ContactForm = {
  init() {
    this.form = document.querySelector('.contact-form');
    if (!this.form) return;

    this.bindEvents();
  },

  bindEvents() {
    this.form.addEventListener('submit', (e) => {
      e.preventDefault();
      
      if (this.validate()) {
        this.submit();
      }
    });

    // 실시간 검증
    this.form.querySelectorAll('input, textarea').forEach(field => {
      field.addEventListener('blur', () => {
        this.validateField(field);
      });
    });
  },

  validate() {
    let isValid = true;
    const fields = this.form.querySelectorAll('[required]');

    fields.forEach(field => {
      if (!this.validateField(field)) {
        isValid = false;
      }
    });

    return isValid;
  },

  validateField(field) {
    const value = field.value.trim();
    const type = field.type;
    let isValid = true;
    let errorMessage = '';

    // 필수 입력 검증
    if (field.hasAttribute('required') && !value) {
      isValid = false;
      errorMessage = '필수 입력 항목입니다.';
    }

    // 이메일 검증
    if (type === 'email' && value) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(value)) {
        isValid = false;
        errorMessage = '올바른 이메일 형식이 아닙니다.';
      }
    }

    // 전화번호 검증
    if (type === 'tel' && value) {
      const phoneRegex = /^[0-9-+()]{10,}$/;
      if (!phoneRegex.test(value)) {
        isValid = false;
        errorMessage = '올바른 전화번호 형식이 아닙니다.';
      }
    }

    this.showError(field, isValid, errorMessage);
    return isValid;
  },

  showError(field, isValid, message) {
    const formGroup = field.closest('.form-group');
    const errorElement = formGroup.querySelector('.error-message');

    if (isValid) {
      formGroup.classList.remove('has-error');
      if (errorElement) errorElement.textContent = '';
    } else {
      formGroup.classList.add('has-error');
      if (errorElement) errorElement.textContent = message;
    }
  },

  async submit() {
    const formData = new FormData(this.form);
    const submitButton = this.form.querySelector('[type="submit"]');
    
    // 버튼 비활성화
    submitButton.disabled = true;
    submitButton.textContent = '전송 중...';

    try {
      // 이메일 전송 서비스 연동 (예: FormSpree, EmailJS)
      const response = await fetch('YOUR_FORM_ENDPOINT', {
        method: 'POST',
        body: formData,
        headers: {
          'Accept': 'application/json'
        }
      });

      if (response.ok) {
        this.showSuccess();
        this.form.reset();
      } else {
        throw new Error('전송 실패');
      }
    } catch (error) {
      this.showError(null, false, '문의 전송에 실패했습니다. 다시 시도해주세요.');
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = '문의하기';
    }
  },

  showSuccess() {
    const successMessage = document.createElement('div');
    successMessage.className = 'alert alert--success';
    successMessage.textContent = '문의가 성공적으로 전송되었습니다. 빠른 시일 내에 연락드리겠습니다.';
    
    this.form.insertAdjacentElement('beforebegin', successMessage);
    
    setTimeout(() => {
      successMessage.remove();
    }, 5000);
  }
};

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  ContactForm.init();
});
```


### 5.4 슬라이더 구현 (Swiper.js)
```javascript
// 메인 히어로 슬라이더
const heroSlider = new Swiper('.hero-slider', {
  loop: true,
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  effect: 'fade',
  fadeEffect: {
    crossFade: true
  },
  a11y: {
    prevSlideMessage: '이전 슬라이드',
    nextSlideMessage: '다음 슬라이드',
  }
});

// 제품 슬라이더
const productSlider = new Swiper('.product-slider', {
  slidesPerView: 1,
  spaceBetween: 16,
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  breakpoints: {
    768: {
      slidesPerView: 2,
      spaceBetween: 24,
    },
    1024: {
      slidesPerView: 3,
      spaceBetween: 32,
    },
  }
});
```

### 5.5 이미지 갤러리 (GLightbox)
```javascript
const lightbox = GLightbox({
  selector: '.gallery-item',
  touchNavigation: true,
  loop: true,
  autoplayVideos: true,
  closeButton: true,
  closeOnOutsideClick: true,
  keyboardNavigation: true,
  draggable: true,
  dragToleranceX: 100,
  dragToleranceY: 100,
});
```

### 5.6 애니메이션 (AOS)
```javascript
// AOS 초기화
AOS.init({
  duration: 800,
  easing: 'ease-in-out',
  once: true,
  offset: 100,
  disable: 'mobile' // 모바일에서는 비활성화 (성능)
});

// HTML에서 사용
// <div data-aos="fade-up" data-aos-delay="100">
```

---

## 6. 데이터 관리 (JSON)

### 6.1 제품 데이터 (products.json)
```json
[
  {
    "id": 1,
    "slug": "product-a",
    "name": "제품명 A",
    "category": "카테고리 A",
    "description": "제품 설명",
    "features": [
      "특징 1",
      "특징 2",
      "특징 3"
    ],
    "specifications": {
      "크기": "1000 x 500 x 300mm",
      "무게": "50kg",
      "재질": "스테인리스 스틸"
    },
    "images": [
      "/assets/images/products/product-a-01.jpg",
      "/assets/images/products/product-a-02.jpg"
    ],
    "thumbnail": "/assets/images/products/product-a-thumb.jpg",
    "brochure": "/assets/downloads/product-a-brochure.pdf"
  }
]
```

### 6.2 시공 실적 데이터 (portfolio.json)
```json
[
  {
    "id": 1,
    "title": "프로젝트명",
    "client": "발주처",
    "category": "건축/토목/플랜트",
    "location": "서울시 강남구",
    "period": "2023.01 - 2023.06",
    "scale": "1,000㎡",
    "description": "프로젝트 설명",
    "images": [
      "/assets/images/portfolio/project-01-01.jpg",
      "/assets/images/portfolio/project-01-02.jpg"
    ],
    "thumbnail": "/assets/images/portfolio/project-01-thumb.jpg",
    "featured": true
  }
]
```

### 6.3 FAQ 데이터 (faq.json)
```json
[
  {
    "id": 1,
    "category": "제품",
    "question": "질문 내용",
    "answer": "답변 내용"
  }
]
```

### 6.4 데이터 로드 및 렌더링
```javascript
async function loadProducts() {
  try {
    const response = await fetch('/assets/data/products.json');
    const products = await response.json();
    renderProducts(products);
  } catch (error) {
    console.error('제품 데이터 로드 실패:', error);
  }
}

function renderProducts(products) {
  const container = document.querySelector('.product-list');
  
  const html = products.map(product => `
    <div class="product-card">
      <a href="/products/${product.slug}.html">
        <img src="${product.thumbnail}" alt="${product.name}" class="product-card__image">
        <div class="product-card__content">
          <h3 class="product-card__title">${product.name}</h3>
          <p class="product-card__description">${product.description}</p>
        </div>
      </a>
    </div>
  `).join('');
  
  container.innerHTML = html;
}

// 페이지 로드 시 실행
document.addEventListener('DOMContentLoaded', loadProducts);
```

---

## 7. 성능 최적화

### 7.1 이미지 최적화
```html
<!-- Lazy Loading -->
<img src="placeholder.jpg" 
     data-src="actual-image.jpg" 
     alt="설명"
     loading="lazy"
     class="lazy">

<!-- Responsive Images -->
<img srcset="image-320w.jpg 320w,
             image-640w.jpg 640w,
             image-1024w.jpg 1024w"
     sizes="(max-width: 768px) 100vw,
            (max-width: 1024px) 50vw,
            33vw"
     src="image-640w.jpg"
     alt="설명">

<!-- WebP with Fallback -->
<picture>
  <source srcset="image.webp" type="image/webp">
  <source srcset="image.jpg" type="image/jpeg">
  <img src="image.jpg" alt="설명">
</picture>
```

### 7.2 Lazy Loading 구현
```javascript
// Intersection Observer를 사용한 Lazy Loading
const lazyImages = document.querySelectorAll('img.lazy');

const imageObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.classList.remove('lazy');
      observer.unobserve(img);
    }
  });
});

lazyImages.forEach(img => imageObserver.observe(img));
```

### 7.3 코드 번들링 및 압축
```javascript
// 프로덕션 빌드 시
// - CSS/JS 파일 압축 (minify)
// - 불필요한 코드 제거 (tree shaking)
// - 파일 병합 (concatenation)

// 권장 도구:
// - CSS: cssnano, clean-css
// - JavaScript: Terser, UglifyJS
// - 이미지: ImageOptim, TinyPNG
```

### 7.4 캐싱 전략
```html
<!-- CSS/JS 파일에 버전 쿼리 추가 -->
<link rel="stylesheet" href="/assets/css/common.css?v=1.0.0">
<script src="/assets/js/common.js?v=1.0.0"></script>
```


---

## 8. SEO 최적화

### 8.1 메타 태그 템플릿
```html
<!-- 기본 메타 태그 -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="페이지 설명 (150-160자)">
<meta name="keywords" content="키워드1, 키워드2, 키워드3">
<meta name="author" content="회사명">

<!-- Open Graph (소셜 미디어) -->
<meta property="og:type" content="website">
<meta property="og:title" content="페이지 제목">
<meta property="og:description" content="페이지 설명">
<meta property="og:image" content="https://example.com/og-image.jpg">
<meta property="og:url" content="https://example.com/page">
<meta property="og:site_name" content="사이트명">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="페이지 제목">
<meta name="twitter:description" content="페이지 설명">
<meta name="twitter:image" content="https://example.com/twitter-image.jpg">

<!-- Canonical URL -->
<link rel="canonical" href="https://example.com/page">
```

### 8.2 구조화된 데이터 (Schema.org)
```html
<!-- 조직 정보 -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "회사명",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "description": "회사 설명",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "주소",
    "addressLocality": "서울",
    "addressRegion": "강남구",
    "postalCode": "12345",
    "addressCountry": "KR"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+82-2-1234-5678",
    "contactType": "customer service",
    "email": "info@example.com"
  },
  "sameAs": [
    "https://www.facebook.com/company",
    "https://www.linkedin.com/company"
  ]
}
</script>

<!-- 제품 정보 -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "제품명",
  "description": "제품 설명",
  "image": "https://example.com/product-image.jpg",
  "brand": {
    "@type": "Brand",
    "name": "브랜드명"
  },
  "offers": {
    "@type": "Offer",
    "availability": "https://schema.org/InStock",
    "price": "0",
    "priceCurrency": "KRW"
  }
}
</script>

<!-- Breadcrumb -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "홈",
      "item": "https://example.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "제품",
      "item": "https://example.com/products"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "제품명",
      "item": "https://example.com/products/product-a"
    }
  ]
}
</script>
```

### 8.3 robots.txt
```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /assets/data/

Sitemap: https://example.com/sitemap.xml
```

### 8.4 sitemap.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2024-01-01</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://example.com/about/</loc>
    <lastmod>2024-01-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <!-- 추가 페이지 -->
</urlset>
```

---

## 9. 외부 서비스 연동

### 9.1 문의 폼 이메일 전송
**옵션 1: FormSpree**
```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
  <input type="text" name="name" required>
  <input type="email" name="email" required>
  <textarea name="message" required></textarea>
  <button type="submit">전송</button>
</form>
```

**옵션 2: EmailJS**
```javascript
emailjs.init("YOUR_PUBLIC_KEY");

emailjs.send("YOUR_SERVICE_ID", "YOUR_TEMPLATE_ID", {
  from_name: formData.name,
  from_email: formData.email,
  message: formData.message
}).then(
  function(response) {
    console.log("SUCCESS", response);
  },
  function(error) {
    console.log("FAILED", error);
  }
);
```

### 9.2 지도 연동
**Google Maps**
```html
<iframe 
  src="https://www.google.com/maps/embed?pb=YOUR_EMBED_CODE"
  width="100%" 
  height="400" 
  style="border:0;" 
  allowfullscreen="" 
  loading="lazy">
</iframe>
```

**Kakao Map**
```html
<div id="map" style="width:100%;height:400px;"></div>

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=YOUR_APP_KEY"></script>
<script>
var container = document.getElementById('map');
var options = {
  center: new kakao.maps.LatLng(37.5665, 126.9780),
  level: 3
};
var map = new kakao.maps.Map(container, options);

var markerPosition = new kakao.maps.LatLng(37.5665, 126.9780);
var marker = new kakao.maps.Marker({
  position: markerPosition
});
marker.setMap(map);
</script>
```

### 9.3 Google Analytics
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

---

## 10. 테스트 가이드

### 10.1 기능 테스트 체크리스트
- [ ] 모든 링크 작동 확인
- [ ] 네비게이션 메뉴 (데스크톱/모바일)
- [ ] 검색 기능
- [ ] 문의 폼 제출 및 검증
- [ ] 슬라이더/캐러셀 동작
- [ ] 이미지 갤러리 라이트박스
- [ ] 다운로드 링크
- [ ] 지도 표시 및 인터랙션
- [ ] Back to Top 버튼

### 10.2 반응형 테스트
**테스트 디바이스**
- iPhone SE (375px)
- iPhone 12/13 (390px)
- Samsung Galaxy S21 (360px)
- iPad (768px)
- iPad Pro (1024px)
- Desktop (1920px)

**테스트 항목**
- [ ] 레이아웃 깨짐 없음
- [ ] 이미지 비율 유지
- [ ] 텍스트 가독성
- [ ] 터치 영역 크기 (최소 44x44px)
- [ ] 가로/세로 모드 전환

### 10.3 브라우저 호환성 테스트
- [ ] Chrome (최신)
- [ ] Firefox (최신)
- [ ] Safari (최신)
- [ ] Edge (최신)
- [ ] iOS Safari
- [ ] Chrome Mobile

### 10.4 성능 테스트
**Lighthouse 점수 목표**
- Performance: 90점 이상
- Accessibility: 90점 이상
- Best Practices: 90점 이상
- SEO: 90점 이상

**Core Web Vitals**
- LCP (Largest Contentful Paint): 2.5초 이하
- FID (First Input Delay): 100ms 이하
- CLS (Cumulative Layout Shift): 0.1 이하

**테스트 도구**
- Google Lighthouse
- PageSpeed Insights
- WebPageTest
- GTmetrix

### 10.5 접근성 테스트
- [ ] WAVE 도구 검사 (에러 0개)
- [ ] 키보드 네비게이션 (Tab, Enter, Esc)
- [ ] 스크린 리더 테스트 (NVDA, VoiceOver)
- [ ] 색상 대비 검사 (4.5:1 이상)
- [ ] 포커스 인디케이터 표시
- [ ] 대체 텍스트 확인


---

## 11. 배포 가이드

### 11.1 배포 전 체크리스트
- [ ] 모든 기능 테스트 완료
- [ ] 반응형 테스트 완료
- [ ] 브라우저 호환성 테스트 완료
- [ ] 성능 최적화 완료 (Lighthouse 90점 이상)
- [ ] 접근성 테스트 통과
- [ ] 이미지 최적화 완료 (WebP, 압축)
- [ ] CSS/JS 파일 압축 (minify)
- [ ] 메타 태그 설정 완료
- [ ] robots.txt 설정
- [ ] sitemap.xml 생성
- [ ] Google Analytics 설정
- [ ] 404 페이지 제작
- [ ] favicon 설정
- [ ] 소셜 미디어 OG 이미지 준비

### 11.2 파일 최적화
```bash
# 이미지 압축
# - WebP 변환
# - 품질 80-85%
# - 적절한 크기로 리사이즈

# CSS 압축
# cssnano 또는 clean-css 사용

# JavaScript 압축
# Terser 또는 UglifyJS 사용

# HTML 압축 (선택 사항)
# html-minifier 사용
```

### 11.3 호스팅 옵션
**정적 호스팅 서비스**
- Netlify (권장)
- Vercel
- GitHub Pages
- AWS S3 + CloudFront
- Firebase Hosting

**전통적 호스팅**
- 웹 호스팅 서버 (Apache, Nginx)
- FTP 업로드

### 11.4 배포 후 모니터링
- Google Analytics 데이터 확인
- Google Search Console 등록 및 모니터링
- 에러 로그 확인
- 성능 지표 추적
- 사용자 피드백 수집

---

## 12. 유지보수 가이드

### 12.1 콘텐츠 업데이트 방법

#### 제품 추가
1. `/assets/data/products.json` 파일 수정
2. 제품 이미지 업로드 (`/assets/images/products/`)
3. 제품 상세 페이지 HTML 생성 (템플릿 복사)
4. 사이트맵 업데이트

#### 시공 실적 추가
1. `/assets/data/portfolio.json` 파일 수정
2. 프로젝트 이미지 업로드 (`/assets/images/portfolio/`)
3. 사이트맵 업데이트

#### FAQ 추가
1. `/assets/data/faq.json` 파일 수정
2. 페이지 새로고침으로 자동 반영

### 12.2 이미지 업로드 가이드
```
파일명: 소문자-하이픈-구분.jpg
크기: 최대 1920px (가로)
형식: WebP (권장), JPG, PNG
압축: 80-85% 품질
위치: /assets/images/[카테고리]/
```

### 12.3 정기 점검 항목
**월간**
- 링크 깨짐 확인
- 이미지 로딩 확인
- 폼 작동 확인
- 성능 점수 확인

**분기별**
- 콘텐츠 업데이트
- 라이브러리 버전 업데이트
- 보안 패치 적용
- 백업 확인

---

## 13. 코드 품질 가이드

### 13.1 코드 스타일
```javascript
// 들여쓰기: 2 spaces
// 세미콜론: 사용
// 따옴표: 작은따옴표 (')
// 변수명: camelCase
// 상수: UPPER_SNAKE_CASE

// Good
const userName = 'John';
const MAX_ITEMS = 10;

function getUserData() {
  return {
    name: userName,
    age: 30
  };
}

// Bad
var user_name = "John"
const max_items = 10

function get_user_data() 
{
  return {
    name: user_name,
    age: 30
  }
}
```

### 13.2 주석 작성
```javascript
/**
 * 사용자 데이터를 가져오는 함수
 * @param {number} userId - 사용자 ID
 * @returns {Promise<Object>} 사용자 정보 객체
 */
async function getUserData(userId) {
  // API 호출
  const response = await fetch(`/api/users/${userId}`);
  
  // 에러 처리
  if (!response.ok) {
    throw new Error('사용자 데이터를 가져올 수 없습니다.');
  }
  
  return response.json();
}
```

### 13.3 에러 처리
```javascript
// Try-Catch 사용
async function loadData() {
  try {
    const response = await fetch('/api/data');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('데이터 로드 실패:', error);
    // 사용자에게 에러 메시지 표시
    showErrorMessage('데이터를 불러올 수 없습니다.');
    return null;
  }
}

// 방어적 프로그래밍
function processData(data) {
  if (!data || !Array.isArray(data)) {
    console.warn('유효하지 않은 데이터:', data);
    return [];
  }
  
  return data.filter(item => item.isActive);
}
```

---

## 14. 개발 일정 및 마일스톤

### 14.1 개발 단계 (5주)

#### Week 6-7: 기반 구축
**Week 6**
- [ ] 개발 환경 설정
- [ ] 디렉토리 구조 생성
- [ ] CSS 변수 및 리셋 스타일
- [ ] 공통 컴포넌트 (버튼, 카드, 폼)
- [ ] 헤더 및 푸터 개발

**Week 7**
- [ ] 네비게이션 (데스크톱/모바일)
- [ ] 반응형 레이아웃 시스템
- [ ] 공통 JavaScript (common.js)
- [ ] 검색 기능 구현

#### Week 8-9: 페이지 개발
**Week 8**
- [ ] 메인 페이지 (히어로, 제품, 실적, CTA)
- [ ] 회사 소개 페이지
- [ ] 제품 목록 페이지
- [ ] JSON 데이터 연동

**Week 9**
- [ ] 제품 상세 페이지
- [ ] 시공 실적 페이지
- [ ] 기술 지원 페이지 (FAQ, 자료실)
- [ ] 문의하기 페이지

#### Week 10: 기능 및 최적화
- [ ] 슬라이더/캐러셀 구현
- [ ] 이미지 갤러리 라이트박스
- [ ] 문의 폼 검증 및 전송
- [ ] 지도 연동
- [ ] 애니메이션 (AOS)
- [ ] 이미지 레이지 로딩
- [ ] 성능 최적화
- [ ] 크로스 브라우저 테스트

### 14.2 주요 마일스톤
- **M1 (Week 7 말)**: 공통 컴포넌트 및 레이아웃 완료
- **M2 (Week 9 말)**: 모든 페이지 개발 완료
- **M3 (Week 10 말)**: 기능 구현 및 최적화 완료

---

## 15. 협업 가이드

### 15.1 Git 워크플로우
```bash
# 브랜치 전략
main (프로덕션)
└── develop (개발)
    ├── feature/header
    ├── feature/product-page
    └── feature/contact-form

# 커밋 메시지 규칙
feat: 새로운 기능 추가
fix: 버그 수정
style: 코드 포맷팅 (기능 변경 없음)
refactor: 코드 리팩토링
docs: 문서 수정
test: 테스트 코드
chore: 빌드, 설정 파일 수정

# 예시
git commit -m "feat: 메인 페이지 히어로 섹션 추가"
git commit -m "fix: 모바일 메뉴 닫기 버튼 오류 수정"
```

### 15.2 코드 리뷰
- Pull Request 생성 시 상세한 설명 작성
- 변경 사항 스크린샷 첨부
- 테스트 완료 여부 명시
- 최소 1명 이상의 리뷰 필수

### 15.3 커뮤니케이션
- **일일 스탠드업**: 진행 상황, 이슈 공유
- **주간 리뷰**: 완료 항목, 다음 주 계획
- **이슈 트래킹**: GitHub Issues 또는 Jira 사용
- **긴급 이슈**: 즉시 PM에게 에스컬레이션

### 15.4 디자이너와 협업
- Figma 파일 접근 권한 확보
- 디자인 변경 사항 실시간 확인
- 구현 불가능한 디자인은 즉시 피드백
- 에셋 추출 요청 (SVG, PNG @2x)

---

## 16. 참고 자료

### 16.1 라이브러리 문서
- jQuery: https://api.jquery.com/
- Swiper.js: https://swiperjs.com/
- GLightbox: https://biati-digital.github.io/glightbox/
- AOS: https://michalsnik.github.io/aos/

### 16.2 학습 자료
- MDN Web Docs: https://developer.mozilla.org/
- Web.dev: https://web.dev/
- CSS-Tricks: https://css-tricks.com/
- Can I Use: https://caniuse.com/

### 16.3 도구
- VS Code (에디터)
- Chrome DevTools (디버깅)
- Lighthouse (성능 테스트)
- WAVE (접근성 테스트)
- Git (버전 관리)

---

## 17. 최종 체크리스트

### 17.1 개발 완료 체크리스트
- [ ] 모든 페이지 HTML 마크업 완료
- [ ] 반응형 CSS 스타일링 완료
- [ ] JavaScript 기능 구현 완료
- [ ] JSON 데이터 연동 완료
- [ ] 이미지 최적화 완료
- [ ] 코드 압축 (minify) 완료
- [ ] 메타 태그 설정 완료
- [ ] 구조화된 데이터 추가
- [ ] robots.txt, sitemap.xml 생성
- [ ] Google Analytics 설정

### 17.2 테스트 완료 체크리스트
- [ ] 기능 테스트 통과
- [ ] 반응형 테스트 통과
- [ ] 브라우저 호환성 테스트 통과
- [ ] Lighthouse 점수 90점 이상
- [ ] 접근성 테스트 통과 (WAVE)
- [ ] 키보드 네비게이션 테스트 통과
- [ ] 성능 테스트 통과 (Core Web Vitals)

### 17.3 배포 준비 체크리스트
- [ ] 프로덕션 빌드 생성
- [ ] 파일 최적화 완료
- [ ] 호스팅 환경 설정
- [ ] 도메인 연결
- [ ] SSL 인증서 설정
- [ ] 백업 계획 수립
- [ ] 모니터링 도구 설정

---

**문서 버전**: 1.0  
**작성일**: 2024  
**작성자**: PM  
**대상**: 프론트엔드 개발자  
**검토자**: 프로젝트 팀  

**문의사항**: PM에게 연락 바랍니다.

---

## 부록: 빠른 참조

### A. 주요 라이브러리 CDN
```html
<!-- jQuery -->
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>

<!-- Swiper -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

<!-- GLightbox -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glightbox/dist/css/glightbox.min.css">
<script src="https://cdn.jsdelivr.net/npm/glightbox/dist/js/glightbox.min.js"></script>

<!-- AOS -->
<link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css">
<script src="https://unpkg.com/aos@next/dist/aos.js"></script>
```

### B. 유용한 CSS 스니펫
```css
/* 텍스트 말줄임 */
.text-ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* 여러 줄 말줄임 */
.text-ellipsis-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* 이미지 비율 유지 */
.aspect-ratio-16-9 {
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

/* 중앙 정렬 */
.center {
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 스크린 리더 전용 텍스트 */
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

### C. 디버깅 팁
```javascript
// 콘솔 로그 그룹화
console.group('사용자 데이터');
console.log('이름:', userName);
console.log('이메일:', userEmail);
console.groupEnd();

// 성능 측정
console.time('데이터 로드');
await loadData();
console.timeEnd('데이터 로드');

// 조건부 로그
const DEBUG = true;
if (DEBUG) console.log('디버그 정보:', data);
```
