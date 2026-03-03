# 반응형 디자인 가이드 (Template2)

## 문서 개요

**프로젝트명**: (주)아이티로그 홈페이지 리뉴얼 (Template2)  
**작성일**: 2024  
**작성자**: UX Designer  
**버전**: 1.0  
**디자인 테마**: Trendy & Simple

---

## 1. 반응형 전략

### 1.1 모바일 퍼스트 접근

**원칙**:
- 모바일 화면을 기준으로 디자인 시작
- 점진적 향상 (Progressive Enhancement)
- 필수 콘텐츠 우선 배치
- 터치 친화적 인터페이스

**이유**:
- 모바일 트래픽 55% 이상 예상
- 현장 담당자의 모바일 사용 빈번
- 성능 최적화 용이

### 1.2 브레이크포인트

```css
/* Mobile First */
/* 기본: 320px - 767px (모바일) */

/* Tablet */
@media (min-width: 768px) {
  /* 768px - 1023px */
}

/* Desktop */
@media (min-width: 1024px) {
  /* 1024px 이상 */
}

/* Large Desktop (선택) */
@media (min-width: 1440px) {
  /* 1440px 이상 */
}
```

### 1.3 디바이스 타겟

**모바일 (320-767px)**
- iPhone SE (375px)
- iPhone 12/13/14 (390px)
- Samsung Galaxy (360px, 412px)

**태블릿 (768-1023px)**
- iPad (768px, 820px)
- iPad Pro (1024px)

**데스크톱 (1024px+)**
- 일반 노트북 (1366px, 1440px)
- 데스크톱 (1920px)

---

## 2. 레이아웃 변화

### 2.1 그리드 시스템

#### 모바일 (320-767px)
```
컬럼: 4 컬럼
간격: 16px
패딩: 16px (좌우)
최대 너비: 100%
```

**일반적 레이아웃**:
- 1열 스택 레이아웃
- 카드: 1열
- 이미지: 전체 너비

#### 태블릿 (768-1023px)
```
컬럼: 8 컬럼
간격: 20px
패딩: 24px (좌우)
최대 너비: 100%
```

**일반적 레이아웃**:
- 2열 그리드
- 카드: 2열
- 이미지: 2열 또는 전체 너비

#### 데스크톱 (1024px+)
```
컬럼: 12 컬럼
간격: 24px
패딩: 32px (좌우)
최대 너비: 1200px
```

**일반적 레이아웃**:
- 3-4열 그리드
- 카드: 3-4열
- 이미지: 다양한 배치

### 2.2 컨테이너 변화

```css
.container {
  width: 100%;
  margin: 0 auto;
  padding: 0 16px; /* 모바일 */
}

@media (min-width: 768px) {
  .container {
    padding: 0 24px; /* 태블릿 */
  }
}

@media (min-width: 1024px) {
  .container {
    max-width: 1200px;
    padding: 0 32px; /* 데스크톱 */
  }
}
```

---

## 3. 타이포그래피 변화

### 3.1 폰트 크기 스케일

| 요소 | 모바일 | 태블릿 | 데스크톱 |
|------|--------|--------|----------|
| H1 (Hero) | 40px | 52px | 64px |
| H2 (Section) | 32px | 40px | 48px |
| H3 (Subsection) | 24px | 28px | 32px |
| H4 (Card) | 20px | 22px | 24px |
| Body Large | 18px | 19px | 20px |
| Body Regular | 16px | 16px | 16px |
| Body Small | 14px | 14px | 14px |
| Caption | 12px | 12px | 12px |

### 3.2 행간 조정

```css
/* 모바일: 더 넓은 행간 (가독성) */
body {
  line-height: 1.6;
}

h1, h2, h3 {
  line-height: 1.2;
}

/* 데스크톱: 약간 좁은 행간 */
@media (min-width: 1024px) {
  body {
    line-height: 1.6;
  }
  
  h1 {
    line-height: 1.1;
  }
}
```

---

## 4. 스페이싱 변화

### 4.1 섹션 패딩

```css
/* 모바일 */
.section {
  padding: 48px 0;
}

/* 태블릿 */
@media (min-width: 768px) {
  .section {
    padding: 64px 0;
  }
}

/* 데스크톱 */
@media (min-width: 1024px) {
  .section {
    padding: 80px 0;
  }
}
```

### 4.2 요소 간 간격

| 간격 | 모바일 | 데스크톱 |
|------|--------|----------|
| 섹션 간 | 48px | 80px |
| 카드 간 | 16px | 24px |
| 요소 간 | 16px | 24px |
| 텍스트 간 | 12px | 16px |

---

## 5. 컴포넌트별 반응형

### 5.1 헤더 네비게이션

#### 데스크톱 (1024px+)
```
┌─────────────────────────────────────────────────────────────┐
│ [LOGO]    메뉴1 ▼  메뉴2 ▼  메뉴3 ▼  메뉴4 ▼  [문의하기]  │
└─────────────────────────────────────────────────────────────┘

높이: 80px
드롭다운: 호버 시 표시
```

#### 모바일 (320-767px)
```
┌──────────────────────────┐
│ ☰  [LOGO]  [문의하기]   │
└──────────────────────────┘

높이: 64px
햄버거 메뉴: 전체 화면 오버레이
```

**CSS 예시**:
```css
/* 모바일: 햄버거 메뉴 */
.nav-desktop {
  display: none;
}
.nav-mobile {
  display: flex;
}

/* 데스크톱: 일반 메뉴 */
@media (min-width: 1024px) {
  .nav-desktop {
    display: flex;
  }
  .nav-mobile {
    display: none;
  }
}
```

### 5.2 히어로 섹션

#### 데스크톱
```
높이: 100vh (전체 화면)
제목: 64px
설명: 20px
버튼: 2개 가로 배치
```

#### 모바일
```
높이: auto (최소 600px)
제목: 40px
설명: 18px
버튼: 2개 세로 스택
```

**CSS 예시**:
```css
.hero {
  min-height: 600px;
  padding: 80px 0;
}

@media (min-width: 1024px) {
  .hero {
    height: 100vh;
    min-height: 700px;
  }
}

.hero-buttons {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

@media (min-width: 768px) {
  .hero-buttons {
    flex-direction: row;
    gap: 24px;
  }
}
```

### 5.3 솔루션 카드 그리드

#### 모바일 (320-767px)
```
1열 레이아웃
카드 간격: 16px
```

#### 태블릿 (768-1023px)
```
2열 레이아웃
카드 간격: 20px
```

#### 데스크톱 (1024px+)
```
4열 레이아웃
카드 간격: 24px
```

**CSS 예시**:
```css
.solution-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

@media (min-width: 768px) {
  .solution-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }
}

@media (min-width: 1024px) {
  .solution-grid {
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
  }
}
```

### 5.4 시공사례 그리드

#### 모바일
```
1열 레이아웃
이미지: 전체 너비
```

#### 태블릿
```
2열 레이아웃
```

#### 데스크톱
```
3열 레이아웃
```

### 5.5 폼 레이아웃

#### 모바일
```
모든 필드: 전체 너비
1열 스택
```

#### 데스크톱
```
이름/회사명: 2열
연락처/이메일: 2열
제목/내용: 전체 너비
```

**CSS 예시**:
```css
.form-row {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

@media (min-width: 768px) {
  .form-row {
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
  }
}
```

---

## 6. 이미지 반응형

### 6.1 반응형 이미지

**HTML 예시**:
```html
<picture>
  <source media="(min-width: 1024px)" srcset="image-desktop.jpg">
  <source media="(min-width: 768px)" srcset="image-tablet.jpg">
  <img src="image-mobile.jpg" alt="설명">
</picture>
```

**또는 srcset 사용**:
```html
<img 
  src="image-800.jpg" 
  srcset="image-400.jpg 400w, 
          image-800.jpg 800w, 
          image-1200.jpg 1200w"
  sizes="(max-width: 767px) 100vw, 
         (max-width: 1023px) 50vw, 
         33vw"
  alt="설명"
>
```

### 6.2 배경 이미지

```css
.hero {
  background-image: url('hero-mobile.jpg');
  background-size: cover;
  background-position: center;
}

@media (min-width: 768px) {
  .hero {
    background-image: url('hero-tablet.jpg');
  }
}

@media (min-width: 1024px) {
  .hero {
    background-image: url('hero-desktop.jpg');
  }
}
```

---

## 7. 터치 최적화

### 7.1 터치 타겟 크기

**최소 크기**: 44x44px (Apple HIG, Material Design 권장)

```css
/* 모바일 버튼 */
.btn {
  min-height: 44px;
  padding: 14px 32px;
}

/* 모바일 링크 */
.nav-link {
  padding: 12px 16px;
  min-height: 44px;
  display: flex;
  align-items: center;
}
```

### 7.2 터치 제스처

**스와이프**:
- 히어로 슬라이더: 좌우 스와이프
- 이미지 갤러리: 좌우 스와이프

**핀치 줌**:
- 이미지 확대 보기 (선택)

**탭**:
- 모든 인터랙티브 요소

### 7.3 호버 대체

```css
/* 데스크톱: 호버 효과 */
@media (hover: hover) {
  .card:hover {
    transform: translateY(-8px);
  }
}

/* 모바일: 호버 없음 */
@media (hover: none) {
  .card:active {
    transform: scale(0.98);
  }
}
```

---

## 8. 성능 최적화

### 8.1 이미지 최적화

**모바일**:
- 작은 이미지 크기 (최대 800px 너비)
- WebP 형식 우선
- 레이지 로딩

**데스크톱**:
- 큰 이미지 크기 (최대 1920px 너비)
- 고해상도 지원 (2x)

### 8.2 폰트 로딩

```css
/* 폰트 디스플레이 전략 */
@font-face {
  font-family: 'Pretendard';
  src: url('pretendard.woff2') format('woff2');
  font-display: swap; /* 폴백 폰트 먼저 표시 */
}
```

### 8.3 CSS 최적화

```css
/* 모바일 전용 스타일 분리 */
@media (max-width: 767px) {
  /* 모바일 전용 */
}

/* 데스크톱 전용 스타일 분리 */
@media (min-width: 1024px) {
  /* 데스크톱 전용 */
}
```

---

## 9. 테스트 가이드

### 9.1 테스트 디바이스

**필수 테스트**:
- iPhone 12/13/14 (390px)
- Samsung Galaxy S21 (360px)
- iPad (768px, 820px)
- MacBook (1440px)
- Desktop (1920px)

### 9.2 테스트 브라우저

**모바일**:
- iOS Safari
- Chrome (Android)
- Samsung Internet

**데스크톱**:
- Chrome
- Firefox
- Safari
- Edge

### 9.3 테스트 체크리스트

**레이아웃**:
- [ ] 모든 브레이크포인트에서 레이아웃 정상
- [ ] 가로/세로 모드 모두 정상
- [ ] 스크롤 정상 작동
- [ ] 오버플로 없음

**타이포그래피**:
- [ ] 모든 텍스트 가독성 확보
- [ ] 폰트 크기 적절
- [ ] 행간 적절

**인터랙션**:
- [ ] 모든 버튼 클릭 가능
- [ ] 터치 타겟 크기 충분
- [ ] 스와이프 제스처 작동
- [ ] 애니메이션 부드러움

**성능**:
- [ ] 페이지 로딩 속도 2.5초 이내
- [ ] 이미지 레이지 로딩 작동
- [ ] 스크롤 부드러움

---

## 10. 디버깅 팁

### 10.1 Chrome DevTools

**디바이스 모드**:
1. F12 또는 Cmd+Opt+I
2. 디바이스 툴바 토글 (Cmd+Shift+M)
3. 다양한 디바이스 선택

**반응형 뷰**:
- 너비 조절하며 브레이크포인트 확인
- 네트워크 속도 시뮬레이션

### 10.2 유용한 CSS

```css
/* 디버깅용 아웃라인 */
* {
  outline: 1px solid red;
}

/* 브레이크포인트 표시 */
body::before {
  content: 'Mobile';
  position: fixed;
  top: 0;
  left: 0;
  background: red;
  color: white;
  padding: 4px 8px;
  z-index: 9999;
}

@media (min-width: 768px) {
  body::before {
    content: 'Tablet';
    background: orange;
  }
}

@media (min-width: 1024px) {
  body::before {
    content: 'Desktop';
    background: green;
  }
}
```

---

## 11. 체크리스트

### 11.1 반응형 디자인 완성도

- [x] 브레이크포인트 정의
- [x] 모바일 퍼스트 전략 수립
- [x] 레이아웃 변화 정의
- [x] 타이포그래피 스케일 정의
- [x] 스페이싱 변화 정의
- [x] 컴포넌트별 반응형 정의
- [x] 이미지 반응형 전략
- [x] 터치 최적화 가이드
- [x] 성능 최적화 전략
- [x] 테스트 가이드 작성

---

**문서 버전**: 1.0  
**작성일**: 2024  
**작성자**: UX Designer  
**검토자**: PM, 프론트엔드 개발자  
**승인일**: [승인 후 기입]

**관련 문서**:
- 디자인 컨셉 (ux-design-concept.md)
- 디자인 시스템 (ux-design-system.md)
- UI 컴포넌트 가이드 (ux-ui-components.md)
- 와이어프레임 (ux-wireframes.md)
