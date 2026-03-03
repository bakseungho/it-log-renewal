# 반응형 가이드 (Template3)

## 문서 개요

**프로젝트명**: (주)아이티로그 홈페이지 리뉴얼 (Template3)  
**작성일**: 2024  
**작성자**: UX Designer  
**버전**: 1.0  
**디자인 테마**: Dark & Premium

---

## 1. 반응형 전략

### 1.1 모바일 퍼스트 접근

Template3는 모바일 퍼스트 전략을 기반으로 하되, 데스크톱에서 프리미엄 경험을 극대화하는 하이브리드 접근 방식을 사용합니다.

**전략**:
1. 모바일: 핵심 콘텐츠와 기능 우선
2. 태블릿: 레이아웃 확장 및 인터랙션 추가
3. 데스크톱: 풀스크린 몰입형 경험 + 고급 애니메이션

### 1.2 브레이크포인트

```css
/* Mobile First Breakpoints */
--breakpoint-xs: 320px;   /* 최소 모바일 */
--breakpoint-sm: 576px;   /* 큰 모바일 */
--breakpoint-md: 768px;   /* 태블릿 */
--breakpoint-lg: 1024px;  /* 작은 노트북 */
--breakpoint-xl: 1366px;  /* 노트북 */
--breakpoint-2xl: 1920px; /* 데스크톱 */
```

**미디어 쿼리**:
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

/* Large Desktop */
@media (min-width: 1920px) {
  /* 대형 데스크톱 스타일 */
}
```

---

## 2. 디바이스별 레이아웃

### 2.1 모바일 (320px - 767px)

#### 레이아웃 특징
- 1열 그리드
- 70vh 히어로 섹션
- 세로 스크롤 중심
- 터치 제스처 최적화
- 패럴랙스 비활성화

#### 타이포그래피
```css
/* Mobile Typography */
--font-size-display-1: 48px;
--font-size-display-2: 36px;
--font-size-h1: 32px;
--font-size-h2: 24px;
--font-size-h3: 20px;
--font-size-body-md: 16px;
```

#### 간격
```css
/* Mobile Spacing */
--section-padding-y: 60px;
--section-padding-x: 20px;
--card-padding: 24px;
--element-gap: 16px;
```

#### 네비게이션
```css
.gnb-mobile {
  height: 60px;
  padding: 0 20px;
}

.gnb-mobile-menu {
  position: fixed;
  top: 60px;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(10, 10, 10, 0.98);
  transform: translateX(100%);
  transition: transform 0.3s ease;
}

.gnb-mobile-menu.active {
  transform: translateX(0);
}
```

#### 버튼
```css
.btn-mobile {
  width: 100%;
  padding: 16px 24px;
  font-size: 16px;
}
```

#### 카드
```css
.card-mobile {
  margin-bottom: 20px;
  padding: 24px;
}
```

### 2.2 태블릿 (768px - 1023px)

#### 레이아웃 특징
- 2열 그리드
- 80vh 히어로 섹션
- 터치 + 마우스 하이브리드
- 제한적 패럴랙스

#### 타이포그래피
```css
/* Tablet Typography */
--font-size-display-1: 72px;
--font-size-display-2: 56px;
--font-size-h1: 40px;
--font-size-h2: 32px;
--font-size-h3: 24px;
--font-size-body-md: 16px;
```

#### 간격
```css
/* Tablet Spacing */
--section-padding-y: 80px;
--section-padding-x: 40px;
--card-padding: 32px;
--element-gap: 20px;
```

#### 그리드
```css
.grid-tablet {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}
```

### 2.3 노트북 (1024px - 1365px)

#### 레이아웃 특징
- 3-4열 그리드
- 100vh 히어로 섹션
- 마우스 인터랙션 중심
- 패럴랙스 활성화

#### 타이포그래피
```css
/* Laptop Typography */
--font-size-display-1: 100px;
--font-size-display-2: 72px;
--font-size-h1: 52px;
--font-size-h2: 40px;
--font-size-h3: 32px;
--font-size-body-md: 16px;
```

#### 간격
```css
/* Laptop Spacing */
--section-padding-y: 100px;
--section-padding-x: 60px;
--card-padding: 36px;
--element-gap: 24px;
```

#### 그리드
```css
.grid-laptop {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 28px;
}
```

### 2.4 데스크톱 (1366px 이상)

#### 레이아웃 특징
- 4열 그리드
- 100vh 풀스크린 섹션
- 고급 애니메이션
- 풀 패럴랙스 효과

#### 타이포그래피
```css
/* Desktop Typography */
--font-size-display-1: 120px;
--font-size-display-2: 80px;
--font-size-h1: 60px;
--font-size-h2: 48px;
--font-size-h3: 36px;
--font-size-body-md: 18px;
```

#### 간격
```css
/* Desktop Spacing */
--section-padding-y: 120px;
--section-padding-x: 80px;
--card-padding: 40px;
--element-gap: 32px;
```

#### 그리드
```css
.grid-desktop {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 32px;
}
```

---

## 3. 컴포넌트별 반응형

### 3.1 히어로 섹션

#### 모바일
```css
.hero-mobile {
  min-height: 70vh;
  padding: 60px 20px;
}

.hero-mobile .hero-title {
  font-size: 48px;
  line-height: 1.2;
}

.hero-mobile .hero-description {
  font-size: 16px;
  margin-bottom: 32px;
}

.hero-mobile .hero-actions {
  flex-direction: column;
  gap: 16px;
}

.hero-mobile .btn {
  width: 100%;
}
```

#### 태블릿
```css
.hero-tablet {
  min-height: 80vh;
  padding: 80px 40px;
}

.hero-tablet .hero-title {
  font-size: 72px;
}

.hero-tablet .hero-description {
  font-size: 18px;
}

.hero-tablet .hero-actions {
  flex-direction: row;
  gap: 20px;
}
```

#### 데스크톱
```css
.hero-desktop {
  min-height: 100vh;
  padding: 120px 80px;
}

.hero-desktop .hero-title {
  font-size: 120px;
}

.hero-desktop .hero-description {
  font-size: 20px;
}

.hero-desktop .hero-actions {
  gap: 24px;
}
```

### 3.2 솔루션 카드 그리드

#### 모바일
```css
.solution-grid-mobile {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
}
```

#### 태블릿
```css
.solution-grid-tablet {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}
```

#### 데스크톱
```css
.solution-grid-desktop {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 32px;
}
```

### 3.3 통계 섹션

#### 모바일
```css
.stats-mobile {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.stats-mobile .stat-number {
  font-size: 48px;
}

.stats-mobile .stat-label {
  font-size: 16px;
}
```

#### 태블릿
```css
.stats-tablet {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 32px;
}

.stats-tablet .stat-number {
  font-size: 60px;
}
```

#### 데스크톱
```css
.stats-desktop {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 48px;
}

.stats-desktop .stat-number {
  font-size: 72px;
}
```

### 3.4 폼 레이아웃

#### 모바일
```css
.form-mobile {
  padding: 24px;
}

.form-mobile .input-group {
  margin-bottom: 20px;
}

.form-mobile .btn-submit {
  width: 100%;
}
```

#### 데스크톱
```css
.form-desktop {
  max-width: 800px;
  margin: 0 auto;
  padding: 40px;
}

.form-desktop .form-row {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.form-desktop .btn-submit {
  width: auto;
  min-width: 200px;
}
```

---

## 4. 이미지 반응형

### 4.1 반응형 이미지

```html
<picture>
  <source media="(min-width: 1366px)" srcset="image-desktop.webp">
  <source media="(min-width: 768px)" srcset="image-tablet.webp">
  <img src="image-mobile.webp" alt="설명">
</picture>
```

### 4.2 이미지 사이즈 가이드

| 디바이스 | 히어로 배경 | 카드 이미지 | 아이콘 |
|---------|------------|------------|--------|
| 모바일   | 768x1024   | 400x300    | 32px   |
| 태블릿   | 1024x768   | 600x450    | 48px   |
| 데스크톱 | 1920x1080  | 800x600    | 64px   |

### 4.3 레이지 로딩

```html
<img src="placeholder.jpg" 
     data-src="actual-image.jpg" 
     loading="lazy" 
     alt="설명">
```

---

## 5. 터치 최적화

### 5.1 터치 타겟 사이즈

```css
/* 최소 터치 영역: 44x44px */
.touch-target {
  min-width: 44px;
  min-height: 44px;
  padding: 12px;
}
```

### 5.2 스와이프 제스처

```javascript
// 히어로 슬라이더 스와이프
let touchStartX = 0;
let touchEndX = 0;

element.addEventListener('touchstart', (e) => {
  touchStartX = e.changedTouches[0].screenX;
});

element.addEventListener('touchend', (e) => {
  touchEndX = e.changedTouches[0].screenX;
  handleSwipe();
});

function handleSwipe() {
  if (touchEndX < touchStartX) {
    // 왼쪽 스와이프 (다음)
    nextSlide();
  }
  if (touchEndX > touchStartX) {
    // 오른쪽 스와이프 (이전)
    prevSlide();
  }
}
```

### 5.3 호버 대체

```css
/* 모바일: 호버 대신 탭 */
@media (hover: none) {
  .card:active {
    transform: scale(1.05);
  }
}

/* 데스크톱: 호버 */
@media (hover: hover) {
  .card:hover {
    transform: scale(1.05);
  }
}
```

---

## 6. 성능 최적화

### 6.1 모바일 성능

```css
/* 모바일: 애니메이션 간소화 */
@media (max-width: 767px) {
  * {
    animation-duration: 0.3s !important;
  }
  
  .parallax {
    transform: none !important;
  }
}
```

### 6.2 이미지 최적화

```css
/* 모바일: 배경 이미지 제거 */
@media (max-width: 767px) {
  .hero-background {
    display: none;
  }
  
  .hero {
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
  }
}
```

### 6.3 폰트 로딩

```css
/* 폰트 디스플레이 최적화 */
@font-face {
  font-family: 'Pretendard';
  src: url('pretendard.woff2') format('woff2');
  font-display: swap;
}
```

---

## 7. 테스트 가이드

### 7.1 테스트 디바이스

**필수 테스트**:
- iPhone 12/13/14 (375x812)
- iPhone 12/13/14 Pro Max (428x926)
- iPad (768x1024)
- iPad Pro (1024x1366)
- MacBook Pro 13" (1440x900)
- Desktop 1920x1080

**브라우저**:
- Safari (iOS)
- Chrome (Android)
- Chrome (Desktop)
- Firefox (Desktop)
- Edge (Desktop)

### 7.2 체크리스트

#### 모바일
- [ ] 터치 타겟 44px 이상
- [ ] 스와이프 제스처 작동
- [ ] 세로 스크롤 부드러움
- [ ] 폼 입력 편리
- [ ] 로딩 속도 3초 이내

#### 태블릿
- [ ] 가로/세로 모드 정상
- [ ] 터치 + 마우스 하이브리드
- [ ] 레이아웃 균형
- [ ] 이미지 품질 유지

#### 데스크톱
- [ ] 풀스크린 레이아웃
- [ ] 호버 효과 정상
- [ ] 애니메이션 60fps
- [ ] 패럴랙스 부드러움

---

## 8. 반응형 유틸리티 클래스

### 8.1 표시/숨김

```css
/* 모바일만 표시 */
.show-mobile {
  display: block;
}

@media (min-width: 768px) {
  .show-mobile {
    display: none;
  }
}

/* 데스크톱만 표시 */
.show-desktop {
  display: none;
}

@media (min-width: 1024px) {
  .show-desktop {
    display: block;
  }
}

/* 태블릿만 표시 */
.show-tablet {
  display: none;
}

@media (min-width: 768px) and (max-width: 1023px) {
  .show-tablet {
    display: block;
  }
}
```

### 8.2 간격 유틸리티

```css
/* 반응형 마진 */
.mt-mobile { margin-top: 20px; }
.mt-tablet { margin-top: 40px; }
.mt-desktop { margin-top: 60px; }

@media (min-width: 768px) {
  .mt-mobile { margin-top: 40px; }
}

@media (min-width: 1024px) {
  .mt-mobile { margin-top: 60px; }
}
```

### 8.3 텍스트 정렬

```css
/* 모바일: 중앙 정렬 */
.text-center-mobile {
  text-align: center;
}

/* 데스크톱: 좌측 정렬 */
@media (min-width: 1024px) {
  .text-center-mobile {
    text-align: left;
  }
}
```

---

## 9. 접근성 고려사항

### 9.1 키보드 네비게이션

```css
/* 포커스 표시 */
*:focus {
  outline: 2px solid #d4af37;
  outline-offset: 2px;
}

/* 스킵 링크 */
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #d4af37;
  color: #0a0a0a;
  padding: 8px 16px;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
```

### 9.2 스크린 리더

```html
<!-- 숨김 텍스트 -->
<span class="sr-only">메뉴 열기</span>

<!-- ARIA 레이블 -->
<button aria-label="다음 슬라이드">→</button>
```

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

## 10. 반응형 디버깅

### 10.1 브레이크포인트 표시

```css
/* 개발 중 브레이크포인트 표시 */
body::before {
  content: 'Mobile';
  position: fixed;
  bottom: 10px;
  right: 10px;
  background: #d4af37;
  color: #0a0a0a;
  padding: 4px 8px;
  font-size: 12px;
  z-index: 9999;
}

@media (min-width: 768px) {
  body::before {
    content: 'Tablet';
  }
}

@media (min-width: 1024px) {
  body::before {
    content: 'Laptop';
  }
}

@media (min-width: 1366px) {
  body::before {
    content: 'Desktop';
  }
}
```

### 10.2 그리드 오버레이

```css
/* 개발 중 그리드 표시 */
.debug-grid {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 9998;
  background-image: repeating-linear-gradient(
    90deg,
    rgba(212, 175, 55, 0.1) 0px,
    rgba(212, 175, 55, 0.1) 1px,
    transparent 1px,
    transparent calc(100% / 12)
  );
}
```

---

**문서 버전**: 1.0  
**작성일**: 2024  
**작성자**: UX Designer  

**관련 문서**:
- ux-design-system.md
- ux-wireframes.md
- ux-ui-components.md
