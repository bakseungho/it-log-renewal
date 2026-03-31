# Template3 개발 가이드

## 목차
1. [시작하기](#시작하기)
2. [프로젝트 구조](#프로젝트-구조)
3. [CSS 아키텍처](#css-아키텍처)
4. [JavaScript 구조](#javascript-구조)
5. [컴포넌트 가이드](#컴포넌트-가이드)
6. [페이지 개발](#페이지-개발)
7. [애니메이션](#애니메이션)
8. [반응형 개발](#반응형-개발)
9. [성능 최적화](#성능-최적화)
10. [배포](#배포)

---

## 시작하기

### 필수 요구사항
- 웹 서버 (Live Server, XAMPP, MAMP 등)
- 모던 브라우저 (Chrome, Firefox, Safari, Edge)
- 코드 에디터 (VS Code 권장)

### 로컬 개발 환경 설정

1. **프로젝트 클론**
```bash
cd web/template3
```

2. **Live Server 실행**
- VS Code: Live Server 확장 설치 후 `index.html` 우클릭 → "Open with Live Server"
- 또는 Python: `python -m http.server 8000`

3. **브라우저에서 확인**
```
http://localhost:8000
```

---

## 프로젝트 구조

### 디렉토리 구조
```
web/template3/
├── index.html              # 메인 페이지
├── about/                  # 회사소개 페이지들
├── solutions/              # 솔루션 페이지들
├── support/                # 고객지원 페이지들
├── css/                    # 스타일시트
│   ├── reset.css          # CSS 리셋
│   ├── variables.css      # CSS 변수 (다크 테마)
│   ├── common.css         # 공통 스타일
│   ├── components.css     # 컴포넌트 스타일
│   ├── header.css         # 헤더 스타일
│   ├── footer.css         # 푸터 스타일
│   └── pages/             # 페이지별 스타일
├── js/                     # JavaScript
│   ├── utils.js           # 유틸리티 함수
│   ├── components.js      # 컴포넌트 로직
│   └── main.js            # GSAP 애니메이션
└── images/                 # 이미지 에셋
```

### 파일 명명 규칙
- HTML: `kebab-case.html` (예: `ceo-message.html`)
- CSS: `kebab-case.css` (예: `header.css`)
- JavaScript: `camelCase.js` (예: `main.js`)
- 이미지: `kebab-case.jpg/png` (예: `hero-1.jpg`)

---

## CSS 아키텍처

### CSS 로딩 순서
```html
<link rel="stylesheet" href="css/reset.css">
<link rel="stylesheet" href="css/variables.css">
<link rel="stylesheet" href="css/common.css">
<link rel="stylesheet" href="css/components.css">
<link rel="stylesheet" href="css/header.css">
<link rel="stylesheet" href="css/footer.css">
<link rel="stylesheet" href="css/pages/home.css">
```

### CSS 변수 사용

#### 컬러
```css
/* 다크 배경 */
background: var(--color-bg-primary);      /* #0a0a0a */
background: var(--color-bg-secondary);    /* #1a1a1a */

/* 포인트 컬러 */
color: var(--color-accent-gold);          /* #d4af37 */
color: var(--color-accent-cyan);          /* #00d9ff */

/* 텍스트 */
color: var(--color-text-primary);         /* #ffffff */
color: var(--color-text-secondary);       /* #a0a0a0 */
```

#### 타이포그래피
```css
font-size: var(--font-size-h1);          /* 60px */
font-size: var(--font-size-h2);          /* 48px */
font-weight: var(--font-weight-bold);    /* 700 */
```

#### 간격
```css
padding: var(--section-padding-y) 0;     /* 120px 0 */
gap: var(--element-gap);                  /* 24px */
```

### BEM 명명 규칙
```css
/* Block */
.card { }

/* Element */
.card-title { }
.card-description { }

/* Modifier */
.card--large { }
.card--featured { }
```

---

## JavaScript 구조

### 파일별 역할

#### utils.js
유틸리티 함수 모음
```javascript
// 이메일 검증
validateEmail(email)

// 전화번호 검증
validatePhone(phone)

// 메시지 표시
showMessage(message, type)

// 레이지 로딩
lazyLoadImages()
```

#### components.js
컴포넌트 클래스
```javascript
// 헤더 네비게이션
new HeaderNav()

// 폼 검증
new FormValidator('#contact-form')

// 라이트박스
new Lightbox()

// 스크롤 애니메이션
new ScrollAnimations()
```

#### main.js
GSAP 애니메이션
```javascript
// 히어로 슬라이더
initHeroSlider()

// 스크롤 애니메이션
initScrollAnimations()

// 카운터 애니메이션
initCounterAnimations()

// 패럴랙스
initParallax()
```

---

## 컴포넌트 가이드

### 버튼

#### Primary Button (Gold)
```html
<a href="#" class="btn btn-primary">솔루션 보기</a>
```

#### Secondary Button (Cyan)
```html
<a href="#" class="btn btn-secondary">자세히 보기</a>
```

#### Outline Button
```html
<a href="#" class="btn btn-outline">더 알아보기</a>
```

#### Text Button
```html
<a href="#" class="btn-text">자세히 보기 →</a>
```

### 카드

#### Solution Card
```html
<div class="card card-solution">
  <div class="icon">
    <!-- SVG 아이콘 -->
  </div>
  <h3 class="title">제목</h3>
  <p class="description">설명</p>
  <span class="btn-text">자세히 보기 →</span>
</div>
```

#### Project Card
```html
<div class="card-project">
  <img src="image.jpg" alt="프로젝트" class="image">
  <div class="content">
    <h3 class="title">프로젝트명</h3>
    <p class="meta">설명</p>
  </div>
</div>
```

#### Stat Card
```html
<div class="card-stat">
  <div class="number" data-count="1500">0+</div>
  <div class="label">설치 현장</div>
  <div class="description">전국 주요 건설 현장</div>
</div>
```

### 폼

#### Input Group
```html
<div class="input-group">
  <label class="input-label">
    이름 <span class="required">*</span>
  </label>
  <input type="text" class="input-text" placeholder="홍길동" required>
</div>
```

#### Textarea
```html
<div class="input-group">
  <label class="input-label">문의 내용 <span class="required">*</span></label>
  <textarea class="input-textarea" placeholder="문의 내용을 입력하세요" required></textarea>
</div>
```

#### Select
```html
<div class="input-group">
  <label class="input-label">관심 솔루션</label>
  <select class="input-select">
    <option value="">선택하세요</option>
    <option value="ai">AI 영상 관제</option>
    <option value="sensor">환경센서</option>
  </select>
</div>
```

---

## 페이지 개발

### 새 페이지 생성 템플릿

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="페이지 설명">
  <title>페이지 제목 | 아이티로그</title>
  
  <!-- Fonts -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
  
  <!-- Stylesheets -->
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/common.css">
  <link rel="stylesheet" href="../css/components.css">
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/footer.css">
  <link rel="stylesheet" href="../css/pages/subpage.css">
</head>
<body>
  <!-- Header (공통) -->
  
  <!-- Page Header -->
  <section class="page-header">
    <img src="../images/page-header.jpg" alt="" class="page-header-background">
    <div class="page-header-overlay"></div>
    <div class="page-header-content">
      <h1 class="page-header-title">페이지 제목</h1>
      <p class="page-header-description">페이지 설명</p>
    </div>
  </section>
  
  <!-- Content Section -->
  <section class="content-section">
    <div class="container">
      <div class="breadcrumb">
        <a href="../index.html" class="breadcrumb-item">Home</a>
        <span class="breadcrumb-separator">></span>
        <span class="breadcrumb-item active">페이지명</span>
      </div>
      
      <!-- 콘텐츠 -->
    </div>
  </section>
  
  <!-- Footer (공통) -->
  
  <!-- Scripts -->
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12/dist/ScrollTrigger.min.js"></script>
  <script src="../js/utils.js"></script>
  <script src="../js/components.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
```

---

## 애니메이션

### GSAP 기본 사용법

#### Fade In
```javascript
gsap.from('.element', {
  scrollTrigger: {
    trigger: '.element',
    start: 'top 80%',
  },
  opacity: 0,
  y: 50,
  duration: 0.8,
  ease: 'power2.out',
});
```

#### Scale In
```javascript
gsap.from('.element', {
  scrollTrigger: {
    trigger: '.element',
    start: 'top 80%',
  },
  opacity: 0,
  scale: 0.8,
  duration: 1,
  ease: 'power2.out',
});
```

#### Stagger Animation
```javascript
gsap.from('.cards', {
  scrollTrigger: {
    trigger: '.section',
    start: 'top 70%',
  },
  opacity: 0,
  y: 50,
  duration: 0.8,
  stagger: 0.1,
  ease: 'power2.out',
});
```

#### Counter Animation
```javascript
gsap.to('.counter', {
  scrollTrigger: {
    trigger: '.counter',
    start: 'top 80%',
    once: true,
  },
  textContent: 1500,
  duration: 2,
  ease: 'power1.out',
  snap: { textContent: 1 },
});
```

### CSS 애니메이션

#### Fade In (CSS)
```css
.fade-in {
  opacity: 0;
  transform: translateY(50px);
  transition: opacity 0.8s ease, transform 0.8s ease;
}

.fade-in.active {
  opacity: 1;
  transform: translateY(0);
}
```

#### Hover Effect
```css
.card {
  transition: all 0.4s ease;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 0 40px rgba(212, 175, 55, 0.3);
}
```

---

## 반응형 개발

### 브레이크포인트
```css
/* Mobile (기본) */
/* 320px - 767px */

/* Tablet */
@media (min-width: 768px) {
  /* 태블릿 스타일 */
}

/* Laptop */
@media (min-width: 1024px) {
  /* 노트북 스타일 */
}

/* Desktop */
@media (min-width: 1366px) {
  /* 데스크톱 스타일 */
}
```

### 반응형 이미지
```html
<picture>
  <source media="(min-width: 1366px)" srcset="image-desktop.webp">
  <source media="(min-width: 768px)" srcset="image-tablet.webp">
  <img src="image-mobile.webp" alt="설명">
</picture>
```

### 반응형 타이포그래피
CSS 변수가 자동으로 조정됩니다:
```css
/* Desktop */
--font-size-h1: 60px;

/* Tablet */
@media (max-width: 1023px) {
  --font-size-h1: 52px;
}

/* Mobile */
@media (max-width: 767px) {
  --font-size-h1: 32px;
}
```

---

## 성능 최적화

### 이미지 최적화

1. **WebP 포맷 사용**
```html
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="설명">
</picture>
```

2. **레이지 로딩**
```html
<img src="placeholder.jpg" data-src="actual-image.jpg" loading="lazy" alt="설명">
```

3. **반응형 이미지**
```html
<img srcset="image-320.jpg 320w,
             image-768.jpg 768w,
             image-1366.jpg 1366w"
     sizes="(max-width: 767px) 100vw,
            (max-width: 1023px) 50vw,
            33vw"
     src="image-768.jpg" alt="설명">
```

### CSS 최적화

1. **Critical CSS 인라인**
```html
<style>
  /* 중요한 스타일만 인라인 */
  body { background: #0a0a0a; }
</style>
```

2. **CSS 미니파이**
- 배포 전 CSS 파일 압축

### JavaScript 최적화

1. **Defer 로딩**
```html
<script src="js/main.js" defer></script>
```

2. **Debounce/Throttle 사용**
```javascript
window.addEventListener('scroll', throttle(() => {
  // 스크롤 이벤트 처리
}, 100));
```

---

## 배포

### 배포 전 체크리스트

- [ ] 모든 이미지 최적화 (WebP 변환, 압축)
- [ ] CSS/JS 미니파이
- [ ] 메타 태그 확인 (title, description, OG)
- [ ] 404 페이지 설정
- [ ] robots.txt 생성
- [ ] sitemap.xml 생성
- [ ] 브라우저 테스트 (Chrome, Firefox, Safari, Edge)
- [ ] 모바일 테스트 (iOS, Android)
- [ ] Lighthouse 점수 확인 (95점 이상)
- [ ] 접근성 테스트 (WCAG 2.1 AA)

### 배포 방법

1. **정적 호스팅 (Netlify, Vercel)**
```bash
# 프로젝트 루트에서
netlify deploy --prod
```

2. **FTP 업로드**
- FileZilla 등 FTP 클라이언트 사용
- 모든 파일 업로드

3. **GitHub Pages**
```bash
git add .
git commit -m "Deploy"
git push origin main
```

---

## 문제 해결

### 자주 발생하는 문제

#### 1. GSAP 애니메이션이 작동하지 않음
```javascript
// ScrollTrigger 등록 확인
gsap.registerPlugin(ScrollTrigger);
```

#### 2. 모바일 메뉴가 닫히지 않음
```javascript
// body overflow 확인
document.body.style.overflow = '';
```

#### 3. 이미지가 로드되지 않음
```html
<!-- 상대 경로 확인 -->
<img src="../images/logo.png" alt="로고">
```

#### 4. CSS 변수가 적용되지 않음
```css
/* :root에 정의되어 있는지 확인 */
:root {
  --color-accent-gold: #d4af37;
}
```

---

## 추가 리소스

### 공식 문서
- [GSAP Documentation](https://greensock.com/docs/)
- [Swiper.js Documentation](https://swiperjs.com/)
- [MDN Web Docs](https://developer.mozilla.org/)

### 디자인 참고
- [Awwwards](https://www.awwwards.com/)
- [CSS Design Awards](https://www.cssdesignawards.com/)

---

## 문의

개발 관련 문의사항은 아래로 연락주세요:
- **이메일**: dev@itlog.co.kr
- **전화**: 02-XXXX-XXXX
