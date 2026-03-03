# 홈페이지 리뉴얼 가이드라인

## 1. 디자인 가이드라인

### 1.1 브랜드 아이덴티티

#### 컬러 팔레트
```
Primary Color: #[메인 컬러]
Secondary Color: #[보조 컬러]
Accent Color: #[강조 컬러]
Background: #FFFFFF / #F5F5F5
Text Primary: #333333
Text Secondary: #666666
```

#### 타이포그래피
- **제목 폰트**: [폰트명] - 굵기 700, 크기 32-48px
- **본문 폰트**: [폰트명] - 굵기 400, 크기 16-18px
- **행간**: 1.6-1.8
- **자간**: -0.02em (한글), 0 (영문)

#### 로고 사용
- 최소 크기: 120px (가로)
- 여백: 로고 높이의 50% 이상
- 배경: 흰색 또는 브랜드 컬러 위에만 사용

### 1.2 레이아웃 원칙

#### 그리드 시스템
- **데스크톱**: 12 컬럼, 최대 너비 1200px
- **태블릿**: 8 컬럼, 최대 너비 768px
- **모바일**: 4 컬럼, 최대 너비 375px
- **거터**: 24px (데스크톱), 16px (모바일)

#### 여백 규칙
```
Section Spacing: 80px (데스크톱), 48px (모바일)
Component Spacing: 40px (데스크톱), 24px (모바일)
Element Spacing: 16px, 24px, 32px
```

#### 반응형 브레이크포인트
```css
Mobile: 320px - 767px
Tablet: 768px - 1023px
Desktop: 1024px - 1440px
Large Desktop: 1441px+
```

### 1.3 UI 컴포넌트

#### 버튼
- **Primary Button**: 배경 Primary Color, 텍스트 흰색, 높이 48px
- **Secondary Button**: 테두리 Primary Color, 텍스트 Primary Color
- **Hover State**: 투명도 90% 또는 색상 10% 어둡게
- **Border Radius**: 4px (기본), 24px (라운드)

#### 입력 필드
- 높이: 48px
- 테두리: 1px solid #DDDDDD
- Focus: 테두리 Primary Color, 그림자 추가
- 에러: 테두리 빨간색, 에러 메시지 표시

#### 카드
- 배경: 흰색
- 그림자: 0 2px 8px rgba(0,0,0,0.1)
- Border Radius: 8px
- Padding: 24px

## 2. 콘텐츠 가이드라인

### 2.1 작성 원칙
- **명확성**: 간결하고 이해하기 쉬운 문장
- **일관성**: 통일된 톤앤매너 유지
- **사용자 중심**: 사용자 관점에서 작성
- **행동 유도**: 명확한 CTA (Call-to-Action)

### 2.2 텍스트 규칙
- 제목: 핵심 키워드 포함, 50자 이내
- 본문: 단락당 3-4문장, 150자 이내
- 리스트: 항목당 한 줄, 최대 7개 항목
- CTA: 동사로 시작, 명확한 행동 지시

### 2.3 이미지 가이드
- **형식**: WebP (대체: JPG, PNG)
- **해상도**: 2x 레티나 지원
- **최적화**: 압축률 80-85%
- **대체 텍스트**: 모든 이미지에 alt 속성 필수
- **비율**: 16:9 (히어로), 4:3 (썸네일), 1:1 (프로필)

### 2.4 비디오 가이드
- 자동재생: 음소거 상태에서만
- 컨트롤: 항상 제공
- 자막: 선택 가능하도록 제공
- 형식: MP4 (H.264 코덱)

## 3. 기술 가이드라인

### 3.1 코드 표준

#### HTML
```html
<!-- 시맨틱 태그 사용 -->
<header>, <nav>, <main>, <article>, <section>, <aside>, <footer>

<!-- 접근성 속성 -->
<button aria-label="메뉴 열기">
<img alt="회사 로고" src="logo.png">
```

#### CSS
```css
/* BEM 네이밍 컨벤션 */
.block {}
.block__element {}
.block--modifier {}

/* CSS 변수 활용 */
:root {
  --color-primary: #000000;
  --spacing-unit: 8px;
}
```

#### JavaScript
```javascript
// ES6+ 문법 사용
// 모듈화된 구조
// 주석으로 의도 명확히 표현
```

### 3.2 성능 최적화

#### 이미지 최적화
- Lazy Loading 적용
- 적절한 크기로 제공 (srcset 활용)
- WebP 형식 우선 사용
- 압축 도구 활용

#### 코드 최적화
- CSS/JS 파일 번들링 및 압축
- 불필요한 코드 제거
- 비동기 로딩 활용
- 캐싱 전략 수립

#### 로딩 전략
```
Critical CSS: 인라인 삽입
Non-critical CSS: 비동기 로드
JavaScript: defer 또는 async 속성 사용
폰트: font-display: swap 사용
```

### 3.3 접근성 (WCAG 2.1 AA)

#### 필수 요구사항
- 키보드만으로 모든 기능 접근 가능
- 색상 대비 비율 4.5:1 이상
- 모든 이미지에 대체 텍스트
- 폼 요소에 레이블 연결
- 스크린 리더 호환성

#### ARIA 사용
```html
<nav aria-label="주 메뉴">
<button aria-expanded="false" aria-controls="menu">
<div role="alert" aria-live="polite">
```

### 3.4 SEO 최적화

#### 메타 태그
```html
<title>페이지 제목 - 사이트명 (60자 이내)</title>
<meta name="description" content="페이지 설명 (160자 이내)">
<meta property="og:title" content="소셜 미디어 제목">
<meta property="og:image" content="대표 이미지 URL">
```

#### 구조화된 데이터
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "회사명",
  "url": "https://example.com"
}
```

#### URL 구조
- 의미 있는 URL 사용
- 소문자 사용
- 하이픈으로 단어 구분
- 깊이 3단계 이내 권장

## 4. 테스트 가이드라인

### 4.1 브라우저 테스트
- Chrome (최신 버전)
- Firefox (최신 버전)
- Safari (최신 버전)
- Edge (최신 버전)
- 모바일 브라우저 (iOS Safari, Chrome Mobile)

### 4.2 디바이스 테스트
- iPhone (최신 2개 모델)
- Android (최신 2개 모델)
- iPad
- 데스크톱 (다양한 해상도)

### 4.3 성능 테스트
- Lighthouse 점수: 90점 이상
- Core Web Vitals 통과
- 페이지 로딩 속도: 3초 이내
- 이미지 최적화 확인

### 4.4 접근성 테스트
- WAVE 도구 검사
- 스크린 리더 테스트 (NVDA, JAWS)
- 키보드 네비게이션 테스트
- 색상 대비 검사

## 5. 배포 가이드라인

### 5.1 배포 전 체크리스트
- [ ] 모든 링크 작동 확인
- [ ] 이미지 최적화 완료
- [ ] 메타 태그 설정 완료
- [ ] 404 페이지 설정
- [ ] robots.txt 설정
- [ ] sitemap.xml 생성
- [ ] 분석 도구 설치 (Google Analytics 등)
- [ ] 성능 테스트 통과
- [ ] 접근성 테스트 통과
- [ ] 크로스 브라우저 테스트 완료

### 5.2 모니터링
- 에러 로그 모니터링
- 성능 지표 추적
- 사용자 행동 분석
- 전환율 측정
- 피드백 수집

### 5.3 유지보수
- 정기적인 콘텐츠 업데이트
- 보안 패치 적용
- 성능 최적화 지속
- 사용자 피드백 반영
- A/B 테스트 진행

## 6. 협업 가이드라인

### 6.1 커뮤니케이션
- 정기 미팅: 주 2회
- 진행 상황 공유: 일일 스탠드업
- 이슈 트래킹: [도구명] 사용
- 문서화: 모든 결정사항 기록

### 6.2 버전 관리
- Git 사용
- 브랜치 전략: Git Flow
- 커밋 메시지 규칙 준수
- 코드 리뷰 필수

### 6.3 디자인 파일 관리
- Figma/Sketch 사용
- 컴포넌트 라이브러리 구축
- 버전 관리 및 히스토리 유지
- 개발자와 실시간 공유

## 7. 참고 자료

### 도구 및 리소스
- 디자인: Figma, Adobe XD
- 프로토타이핑: Figma, InVision
- 성능 테스트: Lighthouse, WebPageTest
- 접근성 테스트: WAVE, axe DevTools
- SEO 분석: Google Search Console, Screaming Frog

### 학습 자료
- WCAG 가이드라인: https://www.w3.org/WAI/WCAG21/quickref/
- Web.dev: https://web.dev/
- MDN Web Docs: https://developer.mozilla.org/
