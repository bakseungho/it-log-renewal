# 개발 가이드

## 개발 환경 설정

### 1. 필수 도구

- **코드 에디터**: VS Code 권장
- **웹 브라우저**: Chrome (개발자 도구 포함)
- **로컬 서버**: Python, Node.js, 또는 VS Code Live Server 확장

### 2. VS Code 권장 확장

```
- Live Server: 로컬 개발 서버
- HTML CSS Support: HTML/CSS 자동완성
- IntelliSense for CSS: CSS 클래스명 자동완성
- ESLint: JavaScript 린팅
- Prettier: 코드 포맷팅
- Path Intellisense: 파일 경로 자동완성
```

### 3. jQuery 설치

1. [jQuery 공식 사이트](https://jquery.com/download/)에서 다운로드
2. `jquery-3.x.x.min.js` 파일을 `assets/js/vendor/` 폴더에 저장
3. 파일명을 `jquery.min.js`로 변경

## 개발 워크플로우

### 1. 새 페이지 추가

```bash
# 1. pages 폴더에 HTML 파일 생성
pages/about.html

# 2. 필요시 페이지 전용 CSS 생성
assets/css/pages/about.css

# 3. HTML에서 CSS 링크 추가
<link rel="stylesheet" href="/assets/css/pages/about.css">
```

### 2. 새 컴포넌트 추가

```javascript
// components.js에 추가
const NewComponent = {
  init() {
    // 초기화 로직
  },
  
  bindEvents() {
    // 이벤트 바인딩
  }
};

// main.js에서 초기화
NewComponent.init();
```

### 3. CSS 변수 사용

```css
/* variables.css에 변수 정의 */
:root {
  --color-custom: #123456;
}

/* 다른 CSS 파일에서 사용 */
.element {
  color: var(--color-custom);
}
```

## 코딩 스타일 가이드

### HTML

```html
<!-- 좋은 예 -->
<section class="section section--about">
  <div class="container">
    <h2 class="section__title">제목</h2>
    <p class="section__description">설명</p>
  </div>
</section>

<!-- 나쁜 예 -->
<div class="about">
  <div>
    <h2>제목</h2>
    <p>설명</p>
  </div>
</div>
```

### CSS (BEM)

```css
/* 좋은 예 */
.card {}
.card__header {}
.card__body {}
.card--featured {}

/* 나쁜 예 */
.card .header {}
.cardBody {}
.featured-card {}
```

### JavaScript

```javascript
// 좋은 예
const getUserData = () => {
  const data = fetchData();
  return data;
};

// 나쁜 예
function get_user_data() {
  var data = fetchData();
  return data;
}
```

## 디버깅 팁

### 1. Chrome DevTools 활용

```javascript
// 콘솔 로그
console.log('변수:', variable);
console.table(arrayData);
console.error('에러:', error);

// 디버거 중단점
debugger;

// 성능 측정
console.time('작업');
// ... 코드 실행
console.timeEnd('작업');
```

### 2. jQuery 디버깅

```javascript
// 요소 존재 확인
if ($('.element').length) {
  console.log('요소가 존재합니다');
}

// 이벤트 리스너 확인
$._data($('.element')[0], 'events');

// 체이닝 중간 확인
$('.element')
  .addClass('active')
  .each(function() {
    console.log(this);
  })
  .fadeIn();
```

### 3. 반응형 디버깅

```javascript
// 현재 브레이크포인트 확인
$(window).on('resize', function() {
  console.log('Width:', $(window).width());
});

// 미디어 쿼리 매칭 확인
if (window.matchMedia('(min-width: 768px)').matches) {
  console.log('태블릿 이상');
}
```

## 성능 최적화

### 1. 이미지 최적화

```bash
# 이미지 압축 도구
- TinyPNG: https://tinypng.com/
- Squoosh: https://squoosh.app/
- ImageOptim (Mac): https://imageoptim.com/

# WebP 변환
- Convertio: https://convertio.co/kr/jpg-webp/
```

### 2. CSS 최적화

```bash
# CSS 압축
- cssnano
- clean-css

# 사용하지 않는 CSS 제거
- PurgeCSS
- UnCSS
```

### 3. JavaScript 최적화

```bash
# JS 압축
- UglifyJS
- Terser

# 번들링
- Webpack
- Rollup
```

## 테스트

### 1. 수동 테스트 체크리스트

```
□ 모든 링크 클릭 테스트
□ 폼 제출 테스트 (정상/에러 케이스)
□ 모바일 메뉴 열기/닫기
□ 스크롤 동작 확인
□ 이미지 로딩 확인
□ 다양한 화면 크기에서 테스트
```

### 2. 브라우저 테스트

```
□ Chrome
□ Firefox
□ Safari
□ Edge
□ 모바일 브라우저 (iOS Safari, Chrome Mobile)
```

### 3. 성능 테스트

```bash
# Lighthouse 실행
1. Chrome DevTools 열기 (F12)
2. Lighthouse 탭 선택
3. "Generate report" 클릭
4. 점수 확인 (목표: 90점 이상)
```

### 4. 접근성 테스트

```bash
# WAVE 도구
1. https://wave.webaim.org/ 방문
2. URL 입력 또는 브라우저 확장 설치
3. 에러 및 경고 확인

# 키보드 테스트
1. Tab 키로 모든 요소 접근 가능한지 확인
2. Enter/Space로 버튼 활성화 확인
3. Esc로 모달/메뉴 닫기 확인
```

## 배포

### 1. 배포 전 준비

```bash
# 1. 파일 압축
- CSS 파일 minify
- JavaScript 파일 minify
- 이미지 최적화

# 2. 메타 정보 업데이트
- 페이지 제목 및 설명
- OG 이미지
- Canonical URL

# 3. 사이트맵 업데이트
- sitemap.xml에 모든 페이지 추가
- 날짜 업데이트

# 4. 최종 테스트
- 모든 기능 테스트
- 성능 테스트
- 접근성 테스트
```

### 2. 배포 방법

```bash
# GitHub Pages
1. GitHub 저장소 생성
2. Settings > Pages에서 활성화
3. 브랜치 선택 (main 또는 gh-pages)

# Netlify
1. https://www.netlify.com/ 가입
2. "New site from Git" 클릭
3. 저장소 연결 또는 폴더 드래그

# Vercel
1. https://vercel.com/ 가입
2. "New Project" 클릭
3. 저장소 연결 또는 폴더 업로드
```

### 3. 배포 후 확인

```
□ 모든 페이지 정상 작동
□ 이미지 및 리소스 로딩
□ 링크 작동 확인
□ 폼 제출 테스트
□ Google Search Console 등록
□ Google Analytics 작동 확인
```

## 문제 해결

### 일반적인 문제

#### 1. jQuery가 작동하지 않음

```javascript
// 해결: jQuery 로드 확인
if (typeof jQuery === 'undefined') {
  console.error('jQuery가 로드되지 않았습니다');
}

// 해결: DOM 로드 후 실행
$(document).ready(function() {
  // 코드
});
```

#### 2. CSS가 적용되지 않음

```html
<!-- 해결: 경로 확인 -->
<link rel="stylesheet" href="/assets/css/common.css">

<!-- 해결: 캐시 삭제 -->
<link rel="stylesheet" href="/assets/css/common.css?v=1.0.1">
```

#### 3. 이미지가 표시되지 않음

```html
<!-- 해결: 경로 확인 (절대 경로 사용) -->
<img src="/assets/images/logo.png" alt="로고">

<!-- 해결: 파일 존재 확인 -->
```

#### 4. 모바일에서 레이아웃 깨짐

```html
<!-- 해결: viewport 메타 태그 확인 -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## 유용한 리소스

### 학습 자료
- [MDN Web Docs](https://developer.mozilla.org/)
- [jQuery API Documentation](https://api.jquery.com/)
- [CSS-Tricks](https://css-tricks.com/)
- [Web.dev](https://web.dev/)

### 도구
- [Can I Use](https://caniuse.com/) - 브라우저 호환성
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) - 성능 측정
- [WAVE](https://wave.webaim.org/) - 접근성 검사
- [PageSpeed Insights](https://pagespeed.web.dev/) - 성능 분석

### 디자인 리소스
- [Unsplash](https://unsplash.com/) - 무료 이미지
- [Pexels](https://www.pexels.com/) - 무료 이미지/비디오
- [Font Awesome](https://fontawesome.com/) - 아이콘
- [Google Fonts](https://fonts.google.com/) - 웹폰트

## 지원

문제가 발생하거나 질문이 있으면:
- 이메일: dev@example.com
- 이슈 트래커: GitHub Issues
