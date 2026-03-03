# UI 컴포넌트 가이드 (Template2)

## 문서 개요

**프로젝트명**: (주)아이티로그 홈페이지 리뉴얼 (Template2)  
**작성일**: 2024  
**작성자**: UX Designer  
**버전**: 1.0  
**디자인 테마**: Trendy & Simple

---

## 1. 컴포넌트 라이브러리 개요

### 1.1 목적

재사용 가능한 UI 컴포넌트를 정의하여:
- 일관된 사용자 경험 제공
- 개발 효율성 향상
- 유지보수 용이성 확보
- 디자인 품질 보장

### 1.2 컴포넌트 분류

**기본 컴포넌트 (Atoms)**
- 버튼, 입력 필드, 링크, 아이콘, 라벨

**조합 컴포넌트 (Molecules)**
- 카드, 폼 그룹, 네비게이션 아이템

**복합 컴포넌트 (Organisms)**
- 헤더, 푸터, 히어로 섹션, 폼

---

## 2. 버튼 컴포넌트

### 2.1 Primary Button (주 버튼)

**용도**: 주요 행동 유도 (문의하기, 제출하기 등)

**스타일**:
```
배경: Electric Blue (#0066FF)
텍스트: White (#FFFFFF)
패딩: 14px 32px
테두리 반경: 8px
폰트 크기: 16px
폰트 웨이트: 600 (SemiBold)
```

**상태**:
- **기본**: 배경 #0066FF
- **호버**: 배경 #0052CC, 상승 2px, 그림자 추가
- **액티브**: 배경 #0052CC, 눌림 효과
- **비활성**: 배경 #E2E8F0, 텍스트 #64748B, 커서 not-allowed

**HTML 예시**:
```html
<button class="btn btn-primary">문의하기</button>
```

### 2.2 Secondary Button (보조 버튼)

**용도**: 보조 행동 (둘러보기, 취소 등)

**스타일**:
```
배경: Transparent
텍스트: Electric Blue (#0066FF)
테두리: 2px solid #0066FF
패딩: 14px 32px
테두리 반경: 8px
```

**상태**:
- **기본**: 투명 배경, 블루 테두리
- **호버**: 배경 #0066FF, 텍스트 White, 상승 2px
- **액티브**: 배경 #0052CC, 텍스트 White

**HTML 예시**:
```html
<button class="btn btn-secondary">솔루션 둘러보기</button>
```

### 2.3 버튼 크기 변형

**Large (큰 버튼)**
```
패딩: 16px 40px
폰트 크기: 18px
용도: 히어로 섹션 CTA
```

**Medium (기본)**
```
패딩: 14px 32px
폰트 크기: 16px
용도: 일반 CTA
```

**Small (작은 버튼)**
```
패딩: 10px 24px
폰트 크기: 14px
용도: 카드 내부, 보조 액션
```

---

## 3. 카드 컴포넌트

### 3.1 Solution Card (솔루션 카드)

**용도**: 메인 페이지 솔루션 섹션

**구조**:
```
┌──────────────────┐
│                  │
│     [ICON]       │
│                  │
│   솔루션 제목    │
│                  │
│   간단한 설명    │
│   (2-3줄)        │
│                  │
│   [자세히 보기→] │
│                  │
└──────────────────┘
```

**스타일**:
```
배경: White (#FFFFFF)
테두리 반경: 16px
패딩: 32px
그림자: 0 4px 12px rgba(0,0,0,0.08)
```

**상태**:
- **기본**: 기본 그림자
- **호버**: 상승 8px, 그림자 증가 (0 12px 24px rgba(0,0,0,0.12))

**HTML 예시**:
```html
<div class="card solution-card">
  <div class="card-icon">
    <img src="icon.svg" alt="아이콘">
  </div>
  <h3 class="card-title">지능형 영상 관제</h3>
  <p class="card-description">AI 기반 실시간 위험 감지 및 통합 대응</p>
  <a href="#" class="card-link">자세히 보기 →</a>
</div>
```

### 3.2 Project Card (시공사례 카드)

**용도**: 시공사례 섹션

**구조**:
```
┌──────────────────┐
│                  │
│    [IMAGE]       │
│                  │
├──────────────────┤
│ 프로젝트명       │
│ 발주처           │
│ 적용 솔루션      │
└──────────────────┘
```

**스타일**:
```
배경: White
테두리 반경: 12px
오버플로: hidden
그림자: 0 2px 8px rgba(0,0,0,0.06)
```

**상태**:
- **호버**: 이미지 확대 (scale: 1.05), 그림자 증가

---

## 4. 입력 필드 컴포넌트

### 4.1 Text Input (텍스트 입력)

**스타일**:
```
너비: 100%
패딩: 14px 16px
테두리: 2px solid #E2E8F0
테두리 반경: 8px
폰트 크기: 16px
```

**상태**:
- **기본**: 회색 테두리
- **포커스**: 블루 테두리 (#0066FF), 블루 그림자
- **에러**: 빨간 테두리 (#EF4444)
- **비활성**: 회색 배경, 커서 not-allowed

**HTML 예시**:
```html
<div class="form-group">
  <label for="name">이름 *</label>
  <input type="text" id="name" class="input" placeholder="이름을 입력하세요" required>
</div>
```

### 4.2 Textarea (텍스트 영역)

**스타일**:
```
최소 높이: 120px
리사이즈: vertical (세로만)
기타: Text Input과 동일
```

### 4.3 Checkbox (체크박스)

**스타일**:
```
크기: 20x20px
테두리: 2px solid #E2E8F0
테두리 반경: 4px
체크 시: 배경 #0066FF, 체크 아이콘 White
```

**HTML 예시**:
```html
<label class="checkbox">
  <input type="checkbox" required>
  <span>개인정보 수집 및 이용에 동의합니다 (필수)</span>
</label>
```

---

## 5. 네비게이션 컴포넌트

### 5.1 Header Navigation (헤더 네비게이션)

**데스크톱 스타일**:
```
높이: 80px
배경: White (스크롤 시 그림자 추가)
패딩: 0 32px
```

**메뉴 아이템**:
```
폰트 크기: 16px
폰트 웨이트: 600
색상: #1E293B
간격: 32px
```

**드롭다운**:
```
배경: White
테두리 반경: 8px
그림자: 0 8px 24px rgba(0,0,0,0.12)
패딩: 16px 0
```

### 5.2 Mobile Menu (모바일 메뉴)

**햄버거 아이콘**:
```
크기: 24x24px
색상: #1E293B
```

**오버레이 메뉴**:
```
배경: White
너비: 100%
높이: 100vh
애니메이션: 우측에서 슬라이드인
```

### 5.3 Breadcrumb (브레드크럼)

**스타일**:
```
폰트 크기: 14px
색상: #64748B
구분자: > (회색)
현재 페이지: #1E293B, 굵게
```

**HTML 예시**:
```html
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li><a href="/">홈</a></li>
    <li><a href="/solutions">현장 안전 플랫폼</a></li>
    <li class="active">스마트 현장안전 시스템</li>
  </ol>
</nav>
```

---

## 6. 아이콘 컴포넌트

### 6.1 아이콘 스타일

**타입**: Line (라인형)
**선 두께**: 2px
**모서리**: Rounded (둥근)
**라이브러리**: Feather Icons 또는 Heroicons

### 6.2 아이콘 크기

```
Small: 16x16px (텍스트 옆)
Medium: 24x24px (버튼, 메뉴)
Large: 32x32px (카드 헤더)
XLarge: 48x48px (솔루션 카드)
```

### 6.3 주요 아이콘

```
메뉴: menu
닫기: x
화살표: arrow-right, chevron-down
체크: check, check-circle
위치: map-pin
전화: phone
이메일: mail
외부 링크: external-link
```

---

## 7. 타이포그래피 컴포넌트

### 7.1 제목 스타일

**H1 (Hero Title)**
```html
<h1 class="hero-title">건설은 안전하게! 안전은 스마트하게!</h1>
```
```css
.hero-title {
  font-size: 4rem;        /* 64px */
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -0.02em;
  color: var(--color-dark);
}
```

**H2 (Section Title)**
```html
<h2 class="section-title">아이티로그의 스마트 솔루션</h2>
```
```css
.section-title {
  font-size: 3rem;        /* 48px */
  font-weight: 700;
  line-height: 1.2;
  text-align: center;
  margin-bottom: 1rem;
}
```

### 7.2 본문 스타일

**Body Large (리드 텍스트)**
```html
<p class="lead">건설 현장의 안전과 효율을 높이는 4대 핵심 솔루션</p>
```
```css
.lead {
  font-size: 1.25rem;     /* 20px */
  line-height: 1.6;
  color: var(--color-gray);
  text-align: center;
}
```

**Body Regular (일반 본문)**
```html
<p>스마트 현장안전 시스템은 건설 현장의 안전교육과...</p>
```

---

## 8. 레이아웃 컴포넌트

### 8.1 Section (섹션)

**스타일**:
```
패딩: 80px 0 (데스크톱)
패딩: 48px 0 (모바일)
```

**변형**:
- **White Section**: 배경 White
- **Gray Section**: 배경 Off White (#F8FAFC)
- **Dark Section**: 배경 Dark Navy, 텍스트 White

**HTML 예시**:
```html
<section class="section section-gray">
  <div class="container">
    <h2 class="section-title">섹션 제목</h2>
    <!-- 콘텐츠 -->
  </div>
</section>
```

### 8.2 Container (컨테이너)

**스타일**:
```
최대 너비: 1200px
마진: 0 auto
패딩: 0 32px (데스크톱)
패딩: 0 16px (모바일)
```

---

## 9. 특수 컴포넌트

### 9.1 Number Counter (숫자 카운터)

**용도**: 숫자로 보는 신뢰 섹션

**구조**:
```
┌──────────┐
│          │
│  1,247+  │  ← 큰 숫자
│          │
│ 설치횟수 │  ← 작은 라벨
│          │
└──────────┘
```

**스타일**:
```
숫자:
  폰트 크기: 48px
  폰트 웨이트: 700
  색상: Electric Blue (#0066FF)

라벨:
  폰트 크기: 16px
  색상: #64748B
```

**애니메이션**: 스크롤 시 0부터 카운트업

### 9.2 Timeline (타임라인)

**용도**: 회사연혁 페이지

**구조** (데스크톱):
```
2025 ●────────────── 내용
              ●───── 내용 2024
2023 ●────────────── 내용
```

**스타일**:
```
선: 2px solid #E2E8F0
점: 12px 원, 배경 #0066FF
```

### 9.3 Image Gallery (이미지 갤러리)

**용도**: 시공사례

**기능**:
- 그리드 레이아웃
- 클릭 시 라이트박스 (확대 보기)
- 호버 시 오버레이 정보 표시

---

## 10. 상태 및 피드백

### 10.1 로딩 상태

**Spinner (스피너)**
```html
<div class="spinner"></div>
```
```css
.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #E2E8F0;
  border-top-color: #0066FF;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
```

### 10.2 알림 메시지

**Success (성공)**
```
배경: #10B981 (연한 녹색)
아이콘: check-circle
```

**Error (오류)**
```
배경: #EF4444 (연한 빨강)
아이콘: x-circle
```

**Warning (경고)**
```
배경: #F59E0B (연한 주황)
아이콘: alert-triangle
```

---

## 11. 애니메이션 가이드

### 11.1 호버 애니메이션

**카드 호버**
```css
.card {
  transition: all 0.4s ease;
}
.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 24px rgba(0,0,0,0.12);
}
```

**버튼 호버**
```css
.btn {
  transition: all 0.3s ease;
}
.btn:hover {
  transform: translateY(-2px);
}
```

### 11.2 스크롤 애니메이션

**페이드인 + 슬라이드업**
```css
.fade-in-up {
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.6s ease;
}
.fade-in-up.visible {
  opacity: 1;
  transform: translateY(0);
}
```

---

## 12. 반응형 규칙

### 12.1 브레이크포인트별 변화

**모바일 (320-767px)**
- 1열 레이아웃
- 폰트 크기 축소
- 패딩 축소
- 터치 타겟 최소 44px

**태블릿 (768-1023px)**
- 2열 레이아웃
- 중간 폰트 크기
- 적절한 패딩

**데스크톱 (1024px+)**
- 3-4열 레이아웃
- 큰 폰트 크기
- 넉넉한 패딩
- 호버 효과 활용

---

## 13. 접근성 가이드

### 13.1 키보드 네비게이션

- Tab 키로 포커스 이동
- Enter/Space로 버튼 활성화
- Esc로 모달/메뉴 닫기
- 명확한 포커스 표시

### 13.2 스크린 리더

- 시맨틱 HTML 사용
- 이미지 alt 텍스트 필수
- ARIA 레이블 적절히 사용
- 랜드마크 역할 정의

### 13.3 색상 대비

- 텍스트/배경: 최소 4.5:1
- 큰 텍스트: 최소 3:1
- 링크: 주변 텍스트와 구분

---

**문서 버전**: 1.0  
**작성일**: 2024  
**작성자**: UX Designer  
**검토자**: PM, 프론트엔드 개발자  
**승인일**: [승인 후 기입]

**관련 문서**:
- 디자인 컨셉 (ux-design-concept.md)
- 디자인 시스템 (ux-design-system.md)
- 와이어프레임 (ux-wireframes.md)
- 반응형 디자인 가이드 (ux-responsive-guide.md)
