# Critical 이슈 수정 가이드

## 📋 개요

배포 전 필수로 수정해야 할 4개의 Critical 이슈에 대한 상세 수정 가이드입니다.

---

## 🔴 Issue #1: Template1 브레드크럼 HTML 구조 통일

### 문제 설명
- **현재 상태**: 솔루션 페이지는 `<nav>`, 회사소개/고객지원 페이지는 `<section>` 사용
- **영향도**: SEO 및 접근성
- **수정 대상**: 8개 파일

### 수정 전 (잘못된 구조)
```html
<section class="breadcrumb">
    <div class="container">
        <nav aria-label="breadcrumb">
            <ol class="breadcrumb__list">
                <li class="breadcrumb__item"><a href="/">홈</a></li>
                <li class="breadcrumb__item"><a href="#">카테고리</a></li>
                <li class="breadcrumb__item" aria-current="page">현재 페이지</li>
            </ol>
        </nav>
    </div>
</section>
```

### 수정 후 (올바른 구조)
```html
<nav class="breadcrumb" aria-label="breadcrumb">
    <div class="breadcrumb__container">
        <ol class="breadcrumb__list">
            <li class="breadcrumb__item"><a href="../index.html">홈</a></li>
            <li class="breadcrumb__item"><a href="#">카테고리</a></li>
            <li class="breadcrumb__item" aria-current="page">현재 페이지</li>
        </ol>
    </div>
</nav>
```

### 수정 대상 파일 목록

#### 1. web/template1/about/company.html
**위치**: 215-227줄 (대략)
**수정 내용**:
- `<section class="breadcrumb">` → `<nav class="breadcrumb" aria-label="breadcrumb">`
- `<div class="container">` → `<div class="breadcrumb__container">`
- 내부 `<nav aria-label="breadcrumb">` 제거
- `</section>` → `</nav>`

#### 2. web/template1/about/ceo-message.html
**위치**: 215-227줄 (대략)
**수정 내용**: company.html과 동일

#### 3. web/template1/about/history.html
**위치**: 219-231줄 (대략)
**수정 내용**: company.html과 동일

#### 4. web/template1/about/certifications.html
**위치**: 218-230줄 (대략)
**수정 내용**: company.html과 동일

#### 5. web/template1/about/location.html
**위치**: 216-228줄 (대략)
**수정 내용**: company.html과 동일

#### 6. web/template1/support/contact.html
**위치**: 216-228줄 (대략)
**수정 내용**: company.html과 동일

#### 7. web/template1/support/remote-support.html
**위치**: 216-228줄 (대략)
**수정 내용**: company.html과 동일

### CSS 확인
`web/template1/assets/css/pages/subpage.css`에 다음 스타일이 있는지 확인:

```css
.breadcrumb {
  padding: var(--space-4) 0;
  background-color: var(--color-gray-50);
  border-bottom: var(--border-1) solid var(--border-light);
}

.breadcrumb__container {
  max-width: var(--container-max-width);
  margin: 0 auto;
  padding: 0 var(--space-4);
}

.breadcrumb__list {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  flex-wrap: wrap;
}
```

---

## 🔴 Issue #2: Template2 브레드크럼 구분자 통일

### 문제 설명
- **현재 상태**: 솔루션/회사소개는 `>`, 고객지원은 `/` 사용
- **영향도**: UX 일관성
- **수정 대상**: 2개 파일

### 수정 전 (잘못된 구분자)
```html
<nav class="breadcrumb fade-in-up">
  <div class="breadcrumb-item">
    <a href="../index.html">홈</a>
  </div>
  <span class="breadcrumb-separator">/</span>  <!-- 잘못됨 -->
  <div class="breadcrumb-item">
    <span>고객지원</span>
  </div>
  <span class="breadcrumb-separator">/</span>  <!-- 잘못됨 -->
  <div class="breadcrumb-item active">
    <span>문의하기</span>
  </div>
</nav>
```

### 수정 후 (올바른 구분자)
```html
<nav class="breadcrumb fade-in-up">
  <div class="breadcrumb-item">
    <a href="../index.html">홈</a>
  </div>
  <span class="breadcrumb-separator">></span>  <!-- 수정됨 -->
  <div class="breadcrumb-item">
    <span>고객지원</span>
  </div>
  <span class="breadcrumb-separator">></span>  <!-- 수정됨 -->
  <div class="breadcrumb-item active">
    <span>문의하기</span>
  </div>
</nav>
```

### 수정 대상 파일 목록

#### 1. web/template2/support/contact.html
**위치**: 191-203줄 (대략)
**수정 내용**:
- 모든 `<span class="breadcrumb-separator">/</span>`를
- `<span class="breadcrumb-separator">></span>`로 변경

#### 2. web/template2/support/remote-support.html
**위치**: 191-203줄 (대략)
**수정 내용**: contact.html과 동일

### 검증 방법
수정 후 다음 페이지들의 브레드크럼 구분자가 모두 `>`인지 확인:
- ✅ solutions/smart-safety.html
- ✅ solutions/tower-crane.html
- ✅ solutions/ai-surveillance.html
- ✅ solutions/environment-sensor.html
- ✅ solutions/access-control.html
- ✅ about/company.html
- ✅ about/ceo-message.html
- ✅ about/history.html
- ✅ about/certifications.html
- ✅ about/location.html
- 🔧 support/contact.html (수정 필요)
- 🔧 support/remote-support.html (수정 필요)

---

## 🔴 Issue #3: Template1 헤더 로고 링크 경로 통일

### 문제 설명
- **현재 상태**: 페이지마다 다른 경로 사용
- **영향도**: 네비게이션 오류 가능
- **수정 대상**: 다수 파일

### 수정 원칙
```
루트 페이지 (index.html, 404.html, terms.html, privacy.html):
  href="index.html"

하위 페이지 (about/*, solutions/*, support/*):
  href="../index.html"
```

### 수정 대상 파일 목록

#### 루트 페이지 (수정 불필요 - 이미 올바름)
- ✅ web/template1/index.html: `href="index.html"` (올바름)
- ✅ web/template1/404.html: 확인 필요
- ✅ web/template1/terms.html: `href="/"` → `href="index.html"` (수정 필요)
- ✅ web/template1/privacy.html: `href="/"` → `href="index.html"` (수정 필요)

#### 회사소개 페이지
- 🔧 web/template1/about/company.html: `href="/"` → `href="../index.html"`
- 🔧 web/template1/about/ceo-message.html: `href="/"` → `href="../index.html"`
- ✅ web/template1/about/history.html: `href="../index.html"` (올바름)
- 🔧 web/template1/about/certifications.html: `href="/"` → `href="../index.html"`
- 🔧 web/template1/about/location.html: `href="/"` → `href="../index.html"`

#### 솔루션 페이지
- 🔧 web/template1/solutions/smart-safety.html: `href="/"` → `href="../index.html"`
- 🔧 web/template1/solutions/tower-crane.html: `href="/"` → `href="../index.html"`
- 🔧 web/template1/solutions/ai-surveillance.html: `href="/"` → `href="../index.html"`
- 🔧 web/template1/solutions/environment-sensor.html: `href="/"` → `href="../index.html"`
- 🔧 web/template1/solutions/access-control.html: `href="/"` → `href="../index.html"`

#### 고객지원 페이지
- 🔧 web/template1/support/contact.html: `href="/"` → `href="../index.html"`
- 🔧 web/template1/support/remote-support.html: `href="/"` → `href="../index.html"`

### 수정 예시

#### 수정 전
```html
<h1 class="header__logo">
    <a href="/">
        <img src="../assets/images/logo/logo.svg" alt="(주)아이티로그">
    </a>
</h1>
```

#### 수정 후
```html
<h1 class="header__logo">
    <a href="../index.html">
        <img src="../assets/images/logo/logo.svg" alt="(주)아이티로그">
    </a>
</h1>
```

---

## 🔴 Issue #4: Template1 솔루션 페이지 로고 이미지 경로 수정

### 문제 설명
- **현재 상태**: 솔루션 페이지만 다른 이미지 경로 사용
- **영향도**: 이미지 로드 실패 가능
- **수정 대상**: 5개 파일

### 수정 전 (잘못된 경로)
```html
<div class="header__logo">
    <a href="/">
        <img src="../assets/images/logo.svg" alt="아이티로그 로고" width="180" height="40">
    </a>
</div>
```

### 수정 후 (올바른 경로)
```html
<h1 class="header__logo">
    <a href="../index.html">
        <img src="../assets/images/logo/logo.svg" alt="(주)아이티로그">
    </a>
</h1>
```

### 수정 사항
1. `<div class="header__logo">` → `<h1 class="header__logo">`
2. `href="/"` → `href="../index.html"`
3. `src="../assets/images/logo.svg"` → `src="../assets/images/logo/logo.svg"`
4. `alt="아이티로그 로고"` → `alt="(주)아이티로그"`
5. `width`, `height` 속성 제거 (CSS로 제어)
6. `</div>` → `</h1>`

### 수정 대상 파일 목록

#### 1. web/template1/solutions/smart-safety.html
**위치**: 40-44줄 (대략)

#### 2. web/template1/solutions/tower-crane.html
**위치**: 31-35줄 (대략)

#### 3. web/template1/solutions/ai-surveillance.html
**위치**: 31-35줄 (대략)

#### 4. web/template1/solutions/environment-sensor.html
**위치**: 31-35줄 (대략)

#### 5. web/template1/solutions/access-control.html
**위치**: 31-35줄 (대략)

### 검증 방법
수정 후 각 솔루션 페이지를 브라우저에서 열어 로고 이미지가 정상적으로 표시되는지 확인

---

## 🔧 수정 작업 순서

### Step 1: 백업 생성
```bash
# 전체 프로젝트 백업
cp -r web web_backup_$(date +%Y%m%d)
```

### Step 2: Issue #1 수정 (Template1 브레드크럼)
1. about/company.html 수정
2. about/ceo-message.html 수정
3. about/history.html 수정
4. about/certifications.html 수정
5. about/location.html 수정
6. support/contact.html 수정
7. support/remote-support.html 수정
8. 브라우저에서 각 페이지 확인

### Step 3: Issue #2 수정 (Template2 브레드크럼)
1. support/contact.html 수정
2. support/remote-support.html 수정
3. 브라우저에서 각 페이지 확인

### Step 4: Issue #3 수정 (Template1 로고 링크)
1. 루트 페이지 2개 수정
2. 회사소개 페이지 4개 수정
3. 솔루션 페이지 5개 수정
4. 고객지원 페이지 2개 수정
5. 각 페이지에서 로고 클릭 테스트

### Step 5: Issue #4 수정 (Template1 로고 이미지)
1. 솔루션 페이지 5개 수정
2. 각 페이지에서 로고 이미지 표시 확인
3. 로고 클릭 테스트

### Step 6: 전체 검증
1. 모든 페이지 브라우저에서 열기
2. 브레드크럼 구조 확인
3. 로고 링크 작동 확인
4. 로고 이미지 표시 확인
5. 모바일 뷰 확인

---

## ✅ 검증 체크리스트

### Template1 검증

#### 브레드크럼 구조
- [ ] about/company.html - `<nav class="breadcrumb">` 사용
- [ ] about/ceo-message.html - `<nav class="breadcrumb">` 사용
- [ ] about/history.html - `<nav class="breadcrumb">` 사용
- [ ] about/certifications.html - `<nav class="breadcrumb">` 사용
- [ ] about/location.html - `<nav class="breadcrumb">` 사용
- [ ] support/contact.html - `<nav class="breadcrumb">` 사용
- [ ] support/remote-support.html - `<nav class="breadcrumb">` 사용

#### 로고 링크 경로
- [ ] index.html - `href="index.html"`
- [ ] terms.html - `href="index.html"`
- [ ] privacy.html - `href="index.html"`
- [ ] about/* (5개) - `href="../index.html"`
- [ ] solutions/* (5개) - `href="../index.html"`
- [ ] support/* (2개) - `href="../index.html"`

#### 로고 이미지 경로
- [ ] solutions/* (5개) - `src="../assets/images/logo/logo.svg"`

### Template2 검증

#### 브레드크럼 구분자
- [ ] support/contact.html - `>` 구분자 사용
- [ ] support/remote-support.html - `>` 구분자 사용

---

## 🚀 수정 완료 후

### 1. HTML 진단 실행
```bash
# 수정한 파일들의 HTML 진단
```

### 2. 브라우저 테스트
- Chrome
- Firefox
- Safari
- Edge

### 3. 반응형 테스트
- 데스크톱 (1920px)
- 태블릿 (768px)
- 모바일 (375px)

### 4. 기능 테스트
- 모든 링크 클릭
- 브레드크럼 네비게이션
- 로고 클릭
- 모바일 메뉴

### 5. 최종 보고
- 수정 완료 보고서 작성
- 스크린샷 첨부
- 배포 승인 요청

---

## 📝 수정 완료 보고서 템플릿

```markdown
# Critical 이슈 수정 완료 보고

## 수정 일시
YYYY-MM-DD HH:MM

## 수정자
[이름]

## 수정 내용

### Issue #1: Template1 브레드크럼 HTML 구조 통일
- ✅ 8개 파일 수정 완료
- ✅ 브라우저 테스트 완료
- ✅ HTML 진단 통과

### Issue #2: Template2 브레드크럼 구분자 통일
- ✅ 2개 파일 수정 완료
- ✅ 브라우저 테스트 완료
- ✅ HTML 진단 통과

### Issue #3: Template1 헤더 로고 링크 경로 통일
- ✅ 13개 파일 수정 완료
- ✅ 링크 작동 테스트 완료

### Issue #4: Template1 솔루션 페이지 로고 이미지 경로 수정
- ✅ 5개 파일 수정 완료
- ✅ 이미지 표시 확인 완료

## 테스트 결과
- ✅ HTML 진단: 통과
- ✅ 브라우저 호환성: 통과
- ✅ 반응형 디자인: 정상
- ✅ 기능 테스트: 정상

## 배포 준비 상태
🟢 배포 가능

## 첨부 파일
- 수정 전후 스크린샷
- 테스트 결과 보고서
```

---

## 💡 추가 권장사항

### 자동화 스크립트 작성
반복적인 수정 작업을 자동화하는 스크립트를 작성하면 효율적입니다.

```bash
#!/bin/bash
# fix_breadcrumb.sh - 브레드크럼 구조 자동 수정 스크립트

# Template1 브레드크럼 수정
files=(
  "web/template1/about/company.html"
  "web/template1/about/ceo-message.html"
  "web/template1/about/history.html"
  "web/template1/about/certifications.html"
  "web/template1/about/location.html"
  "web/template1/support/contact.html"
  "web/template1/support/remote-support.html"
)

for file in "${files[@]}"; do
  echo "Processing $file..."
  # sed 명령어로 자동 수정
done

echo "Done!"
```

### Git 커밋 메시지 예시
```
fix: Critical 이슈 수정 - 브레드크럼 구조 및 로고 링크 통일

- Template1 브레드크럼 HTML 구조를 <nav>로 통일 (8개 파일)
- Template2 브레드크럼 구분자를 '>'로 통일 (2개 파일)
- Template1 헤더 로고 링크 경로 통일 (13개 파일)
- Template1 솔루션 페이지 로고 이미지 경로 수정 (5개 파일)

Closes #1, #2, #3, #4
```

---

**작성자**: PM (Product Manager)  
**작성일**: 2024년  
**버전**: 1.0
