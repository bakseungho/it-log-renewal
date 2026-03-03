# UI 컴포넌트 (Template3)

## 문서 개요

**프로젝트명**: (주)아이티로그 홈페이지 리뉴얼 (Template3)  
**작성일**: 2024  
**작성자**: UX Designer  
**버전**: 1.0  
**디자인 테마**: Dark & Premium

---

## 1. 컴포넌트 라이브러리 개요

### 1.1 목적

Template3의 모든 페이지에서 재사용 가능한 UI 컴포넌트를 정의하고, 다크 모드 프리미엄 디자인의 일관성을 유지합니다.

### 1.2 컴포넌트 분류

**기본 컴포넌트**:
- 버튼 (Buttons)
- 입력 필드 (Input Fields)
- 카드 (Cards)
- 배지 (Badges)

**네비게이션 컴포넌트**:
- 글로벌 네비게이션 (GNB)
- 브레드크럼 (Breadcrumb)
- 페이지네이션 (Pagination)

**콘텐츠 컴포넌트**:
- 히어로 섹션 (Hero Section)
- 섹션 헤더 (Section Header)
- 아이콘 박스 (Icon Box)
- 이미지 갤러리 (Image Gallery)

**폼 컴포넌트**:
- 텍스트 입력 (Text Input)
- 선택 박스 (Select Box)
- 체크박스 (Checkbox)
- 라디오 버튼 (Radio Button)

---

## 2. 버튼 컴포넌트

### 2.1 Primary Button (Gold)

**비주얼**:
```
┌─────────────────────┐
│   솔루션 보기 →     │
└─────────────────────┘
```

**스타일**:
```css
.btn-primary {
  background: linear-gradient(135deg, #d4af37 0%, #e6c966 100%);
  color: #0a0a0a;
  padding: 16px 40px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px rgba(212, 175, 55, 0.2);
}

.btn-primary:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 24px rgba(212, 175, 55, 0.4);
}

.btn-primary:active {
  transform: scale(0.95);
}
```

**사용 예시**:
- 주요 CTA (문의하기, 솔루션 보기)
- 폼 제출 버튼
- 히어로 섹션 메인 액션

### 2.2 Secondary Button (Cyan)

**비주얼**:
```
┌─────────────────────┐
│   자세히 보기 →     │
└─────────────────────┘
```

**스타일**:
```css
.btn-secondary {
  background: linear-gradient(135deg, #00d9ff 0%, #00b8d9 100%);
  color: #0a0a0a;
  padding: 16px 40px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px rgba(0, 217, 255, 0.2);
}

.btn-secondary:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 24px rgba(0, 217, 255, 0.4);
}
```

**사용 예시**:
- 보조 CTA
- AI/기술 관련 액션
- 링크 버튼

### 2.3 Outline Button

**비주얼**:
```
┌─────────────────────┐
│   더 알아보기       │
└─────────────────────┘
```

**스타일**:
```css
.btn-outline {
  background: transparent;
  color: #ffffff;
  padding: 16px 40px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 8px;
  border: 2px solid #d4af37;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-outline:hover {
  background: #d4af37;
  color: #0a0a0a;
  transform: translateY(-2px);
}
```

**사용 예시**:
- 보조 액션
- 카드 내부 버튼
- 덜 중요한 링크

### 2.4 Text Button

**비주얼**:
```
자세히 보기 →
```

**스타일**:
```css
.btn-text {
  background: none;
  color: #d4af37;
  padding: 8px 0;
  font-size: 16px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  position: relative;
  transition: all 0.3s ease;
}

.btn-text::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: #d4af37;
  transition: width 0.3s ease;
}

.btn-text:hover::after {
  width: 100%;
}
```

**사용 예시**:
- 카드 하단 링크
- 인라인 텍스트 링크
- 더보기 버튼

### 2.5 버튼 사이즈

```css
/* Large */
.btn-lg {
  padding: 20px 48px;
  font-size: 18px;
}

/* Medium (기본) */
.btn-md {
  padding: 16px 40px;
  font-size: 16px;
}

/* Small */
.btn-sm {
  padding: 12px 32px;
  font-size: 14px;
}
```

---

## 3. 카드 컴포넌트

### 3.1 Solution Card (솔루션 카드)

**비주얼**:
```
┌──────────────────────┐
│                      │
│    [AI 아이콘]       │
│                      │
│  AI 영상 관제시스템  │
│                      │
│  실시간 위험 감지    │
│  및 즉각 대응        │
│                      │
│  자세히 보기 →       │
│                      │
└──────────────────────┘
```

**스타일**:
```css
.card-solution {
  background: #1a1a1a;
  border-radius: 16px;
  padding: 40px;
  transition: all 0.4s ease;
  border: 1px solid transparent;
}

.card-solution:hover {
  transform: scale(1.05);
  box-shadow: 0 0 40px rgba(212, 175, 55, 0.3);
  border-color: #d4af37;
}

.card-solution .icon {
  width: 64px;
  height: 64px;
  margin-bottom: 24px;
  color: #d4af37;
}

.card-solution .title {
  font-size: 24px;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 16px;
}

.card-solution .description {
  font-size: 16px;
  color: #a0a0a0;
  line-height: 1.7;
  margin-bottom: 24px;
}
```

### 3.2 Project Card (프로젝트 카드)

**비주얼**:
```
┌──────────────────────┐
│                      │
│   [프로젝트 이미지]  │
│                      │
├──────────────────────┤
│ ○○○ 재개발 프로젝트 │
│ AI 관제 + 환경센서   │
│ 1,000세대 이상       │
└──────────────────────┘
```

**스타일**:
```css
.card-project {
  background: #1a1a1a;
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.4s ease;
}

.card-project:hover {
  transform: translateY(-8px);
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.6);
}

.card-project .image {
  width: 100%;
  height: 240px;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.card-project:hover .image {
  transform: scale(1.1);
}

.card-project .content {
  padding: 24px;
}

.card-project .title {
  font-size: 20px;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 8px;
}

.card-project .meta {
  font-size: 14px;
  color: #a0a0a0;
  line-height: 1.6;
}
```

### 3.3 Stat Card (통계 카드)

**비주얼**:
```
┌──────────────────────┐
│                      │
│      1,500+          │
│                      │
│     설치 현장        │
│                      │
│  전국 주요 건설 현장 │
│                      │
└──────────────────────┘
```

**스타일**:
```css
.card-stat {
  text-align: center;
  padding: 40px 24px;
}

.card-stat .number {
  font-size: 72px;
  font-weight: 900;
  color: #d4af37;
  line-height: 1;
  margin-bottom: 16px;
}

.card-stat .label {
  font-size: 20px;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 8px;
}

.card-stat .description {
  font-size: 16px;
  color: #a0a0a0;
}
```

---

## 4. 입력 필드 컴포넌트

### 4.1 Text Input

**비주얼**:
```
이름 *
┌──────────────────────────────┐
│ 홍길동                       │
└──────────────────────────────┘
```

**스타일**:
```css
.input-group {
  margin-bottom: 24px;
}

.input-label {
  display: block;
  font-size: 16px;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 8px;
}

.input-label .required {
  color: #d4af37;
}

.input-text {
  width: 100%;
  background: #1a1a1a;
  color: #ffffff;
  border: 2px solid transparent;
  border-radius: 8px;
  padding: 16px 20px;
  font-size: 16px;
  transition: all 0.3s ease;
}

.input-text:focus {
  outline: none;
  border-color: #d4af37;
  box-shadow: 0 0 0 4px rgba(212, 175, 55, 0.1);
}

.input-text::placeholder {
  color: #505050;
}
```

### 4.2 Textarea

**스타일**:
```css
.input-textarea {
  width: 100%;
  background: #1a1a1a;
  color: #ffffff;
  border: 2px solid transparent;
  border-radius: 8px;
  padding: 16px 20px;
  font-size: 16px;
  min-height: 120px;
  resize: vertical;
  transition: all 0.3s ease;
}

.input-textarea:focus {
  outline: none;
  border-color: #d4af37;
  box-shadow: 0 0 0 4px rgba(212, 175, 55, 0.1);
}
```

### 4.3 Select Box

**비주얼**:
```
관심 솔루션
┌──────────────────────────────┐
│ 선택하세요              ▼    │
└──────────────────────────────┘
```

**스타일**:
```css
.input-select {
  width: 100%;
  background: #1a1a1a;
  color: #ffffff;
  border: 2px solid transparent;
  border-radius: 8px;
  padding: 16px 20px;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  appearance: none;
  background-image: url("data:image/svg+xml,..."); /* 화살표 아이콘 */
  background-repeat: no-repeat;
  background-position: right 20px center;
}

.input-select:focus {
  outline: none;
  border-color: #d4af37;
  box-shadow: 0 0 0 4px rgba(212, 175, 55, 0.1);
}
```

### 4.4 Checkbox

**비주얼**:
```
☑ 개인정보 처리방침에 동의합니다
```

**스타일**:
```css
.input-checkbox {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.input-checkbox input[type="checkbox"] {
  width: 20px;
  height: 20px;
  margin-right: 12px;
  cursor: pointer;
  accent-color: #d4af37;
}

.input-checkbox label {
  font-size: 16px;
  color: #ffffff;
  cursor: pointer;
}
```

---

## 5. 네비게이션 컴포넌트

### 5.1 Global Navigation (GNB)

**데스크톱 비주얼**:
```
┌─────────────────────────────────────────────────────────────┐
│ [LOGO]  회사소개  현장안전  스마트관제  환경출입  고객지원    │
└─────────────────────────────────────────────────────────────┘
```

**스타일**:
```css
.gnb {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 80px;
  background: rgba(10, 10, 10, 0.8);
  backdrop-filter: blur(10px);
  z-index: 1000;
  transition: all 0.3s ease;
}

.gnb.scrolled {
  background: rgba(10, 10, 10, 0.95);
  box-shadow: 0 2px 16px rgba(0, 0, 0, 0.5);
}

.gnb-container {
  max-width: 1440px;
  margin: 0 auto;
  padding: 0 80px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.gnb-logo {
  height: 40px;
}

.gnb-menu {
  display: flex;
  gap: 48px;
}

.gnb-menu-item {
  font-size: 16px;
  font-weight: 600;
  color: #ffffff;
  text-decoration: none;
  position: relative;
  transition: color 0.3s ease;
}

.gnb-menu-item::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 0;
  width: 0;
  height: 2px;
  background: #d4af37;
  transition: width 0.3s ease;
}

.gnb-menu-item:hover {
  color: #d4af37;
}

.gnb-menu-item:hover::after {
  width: 100%;
}
```

### 5.2 Mobile Navigation

**모바일 비주얼**:
```
┌─────────────────────────────┐
│ [LOGO]          [☰]         │
└─────────────────────────────┘
```

**스타일**:
```css
.gnb-mobile-toggle {
  display: none;
  width: 32px;
  height: 32px;
  flex-direction: column;
  justify-content: space-around;
  cursor: pointer;
}

.gnb-mobile-toggle span {
  width: 100%;
  height: 3px;
  background: #ffffff;
  transition: all 0.3s ease;
}

.gnb-mobile-menu {
  position: fixed;
  top: 80px;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(10, 10, 10, 0.98);
  backdrop-filter: blur(20px);
  padding: 40px;
  transform: translateX(100%);
  transition: transform 0.3s ease;
}

.gnb-mobile-menu.active {
  transform: translateX(0);
}

.gnb-mobile-menu-item {
  display: block;
  font-size: 24px;
  font-weight: 700;
  color: #ffffff;
  padding: 20px 0;
  border-bottom: 1px solid #2a2a2a;
}
```

### 5.3 Breadcrumb

**비주얼**:
```
Home > 회사소개 > 회사연혁
```

**스타일**:
```css
.breadcrumb {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 14px;
  color: #a0a0a0;
}

.breadcrumb-item {
  color: #a0a0a0;
  text-decoration: none;
  transition: color 0.3s ease;
}

.breadcrumb-item:hover {
  color: #d4af37;
}

.breadcrumb-item.active {
  color: #ffffff;
}

.breadcrumb-separator {
  color: #505050;
}
```

---

## 6. 콘텐츠 컴포넌트

### 6.1 Hero Section

**스타일**:
```css
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -2;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(180deg, rgba(10, 10, 10, 0.5) 0%, rgba(10, 10, 10, 0.8) 100%);
  z-index: -1;
}

.hero-content {
  text-align: center;
  max-width: 1200px;
  padding: 0 40px;
}

.hero-subtitle {
  font-size: 18px;
  font-weight: 600;
  color: #a0a0a0;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 24px;
}

.hero-title {
  font-size: 100px;
  font-weight: 900;
  color: #ffffff;
  line-height: 1.2;
  margin-bottom: 32px;
}

.hero-title .highlight {
  color: #d4af37;
}

.hero-description {
  font-size: 20px;
  color: #a0a0a0;
  line-height: 1.8;
  margin-bottom: 48px;
}

.hero-actions {
  display: flex;
  gap: 24px;
  justify-content: center;
}
```

### 6.2 Section Header

**비주얼**:
```
        프리미엄 안전 솔루션
  건설 현장의 모든 안전을 책임지는 통합 솔루션
```

**스타일**:
```css
.section-header {
  text-align: center;
  margin-bottom: 80px;
}

.section-title {
  font-size: 48px;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 16px;
}

.section-description {
  font-size: 18px;
  color: #a0a0a0;
  line-height: 1.7;
}
```

### 6.3 Icon Box

**비주얼**:
```
┌──────────────────────┐
│                      │
│    [아이콘]          │
│                      │
│    제목              │
│                      │
│    설명 텍스트       │
│                      │
└──────────────────────┘
```

**스타일**:
```css
.icon-box {
  text-align: center;
  padding: 40px 24px;
}

.icon-box-icon {
  width: 64px;
  height: 64px;
  margin: 0 auto 24px;
  color: #d4af37;
}

.icon-box-title {
  font-size: 20px;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 12px;
}

.icon-box-description {
  font-size: 16px;
  color: #a0a0a0;
  line-height: 1.7;
}
```

---

## 7. 상태별 스타일

### 7.1 로딩 상태

```css
.loading {
  display: inline-block;
  width: 40px;
  height: 40px;
  border: 4px solid #1a1a1a;
  border-top-color: #d4af37;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

### 7.2 에러 상태

```css
.error-message {
  padding: 16px 20px;
  background: rgba(255, 68, 68, 0.1);
  border: 1px solid #ff4444;
  border-radius: 8px;
  color: #ff4444;
  font-size: 14px;
}
```

### 7.3 성공 상태

```css
.success-message {
  padding: 16px 20px;
  background: rgba(0, 255, 136, 0.1);
  border: 1px solid #00ff88;
  border-radius: 8px;
  color: #00ff88;
  font-size: 14px;
}
```

---

## 8. 애니메이션 컴포넌트

### 8.1 Fade In

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

### 8.2 Scale In

```css
.scale-in {
  opacity: 0;
  transform: scale(0.8);
  transition: opacity 0.8s ease, transform 0.8s ease;
}

.scale-in.active {
  opacity: 1;
  transform: scale(1);
}
```

### 8.3 Slide In

```css
.slide-in-left {
  opacity: 0;
  transform: translateX(-100px);
  transition: opacity 0.8s ease, transform 0.8s ease;
}

.slide-in-left.active {
  opacity: 1;
  transform: translateX(0);
}
```

---

## 9. 컴포넌트 사용 가이드

### 9.1 버튼 사용 우선순위

1. **Primary (Gold)**: 주요 CTA, 폼 제출
2. **Secondary (Cyan)**: 보조 CTA, 기술 관련
3. **Outline**: 덜 중요한 액션
4. **Text**: 인라인 링크, 더보기

### 9.2 카드 사용 가이드

- **Solution Card**: 솔루션 소개, 서비스 나열
- **Project Card**: 시공사례, 포트폴리오
- **Stat Card**: 통계, 실적 데이터

### 9.3 색상 사용 규칙

- **Gold**: 프리미엄, 신뢰, 주요 액션
- **Cyan**: 기술, AI, 보조 액션
- **White**: 주요 텍스트, 제목
- **Gray**: 보조 텍스트, 설명

---

**문서 버전**: 1.0  
**작성일**: 2024  
**작성자**: UX Designer  

**관련 문서**:
- ux-design-system.md
- ux-wireframes.md
- ux-responsive-guide.md
