# Template2 개발 가이드

## 완성된 파일 목록

### ✅ 완료된 파일

#### CSS (7개)
- `css/reset.css` - CSS 리셋
- `css/variables.css` - CSS 변수 (색상, 폰트, 간격 등)
- `css/common.css` - 공통 스타일
- `css/components.css` - 재사용 컴포넌트
- `css/header.css` - 헤더 및 네비게이션
- `css/footer.css` - 푸터
- `css/pages/home.css` - 메인 페이지 스타일
- `css/pages/subpage.css` - 서브 페이지 공통 스타일
- `css/pages/solutions.css` - 솔루션 페이지 스타일

#### JavaScript (3개)
- `js/utils.js` - 유틸리티 함수
- `js/components.js` - UI 컴포넌트 (Header, Slider, Animation 등)
- `js/main.js` - 메인 초기화 및 라이브러리 설정

#### HTML (1개 완성)
- `index.html` - 메인 페이지 (완전 구현)

#### 문서
- `README.md` - 프로젝트 개요 및 사용 가이드
- `DEVELOPMENT-GUIDE.md` - 이 파일

## 나머지 페이지 개발 방법

### 1. 서브 페이지 템플릿 구조

모든 서브 페이지는 다음 구조를 따릅니다:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <!-- 메타 태그 -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="[페이지 설명]">
  <title>[페이지 제목] - 아이티로그</title>
  
  <!-- CSS -->
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/common.css">
  <link rel="stylesheet" href="../css/components.css">
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/footer.css">
  <link rel="stylesheet" href="../css/pages/subpage.css">
  <!-- 필요시 추가 CSS -->
</head>
<body>
  <!-- Header (index.html에서 복사) -->
  
  <!-- Page Header -->
  <div class="page-header">
    <div class="container">
      <nav class="breadcrumb">
        <div class="breadcrumb-item"><a href="../index.html">홈</a></div>
        <span class="breadcrumb-separator">></span>
        <div class="breadcrumb-item"><a href="#">[1Depth]</a></div>
        <span class="breadcrumb-separator">></span>
        <div class="breadcrumb-item active">[2Depth]</div>
      </nav>
      
      <h1 class="page-title">[페이지 제목]</h1>
      <p class="page-description">[페이지 설명]</p>
    </div>
  </div>
  
  <!-- Main Content -->
  <main>
    <section class="content-section">
      <div class="container">
        <!-- 페이지 콘텐츠 -->
      </div>
    </section>
  </main>
  
  <!-- Footer (index.html에서 복사) -->
  
  <!-- Scripts -->
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>
  <script src="../js/utils.js"></script>
  <script src="../js/components.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
```

### 2. 페이지별 개발 가이드

#### 회사소개 페이지 (5개)

**about/company.html - 회사소개**
```html
<section class="content-section">
  <div class="container">
    <div class="content-wrapper">
      <div class="content-block fade-in-up">
        <h2 class="content-block-title">기업정보</h2>
        <p class="content-block-text">
          (주)아이티로그는 20년간 건설 현장 안전 솔루션 분야에서...
        </p>
      </div>
      
      <div class="content-block fade-in-up">
        <h2 class="content-block-title">기업 이념</h2>
        <ul class="content-block-list">
          <li>안전 제일: 모든 작업자가 안전하게 귀가하는 현장</li>
          <li>기술 혁신: 최신 기술로 현장 안전 수준 향상</li>
          <li>고객 신뢰: 고객과 함께 성장하는 파트너</li>
        </ul>
      </div>
      
      <!-- 고객사 로고 그리드 -->
      <div class="clients-grid fade-in-up">
        <!-- 고객사 로고 -->
      </div>
    </div>
  </div>
</section>
```

**about/history.html - 회사연혁**
```html
<section class="content-section">
  <div class="container">
    <div class="timeline">
      <div class="timeline-item fade-in-up">
        <div class="timeline-dot"></div>
        <div class="timeline-content">
          <div class="timeline-year">2025</div>
          <p>스마트 통합 안전 플랫폼 출시</p>
        </div>
      </div>
      <!-- 더 많은 연혁 항목 -->
    </div>
  </div>
</section>
```

**about/location.html - 오시는 길**
```html
<section class="content-section">
  <div class="container">
    <div class="content-wrapper">
      <!-- 카카오맵 -->
      <div id="kakao-map" style="width:100%;height:400px;"></div>
      
      <div class="info-box">
        <h3 class="info-box-title">주소</h3>
        <p class="info-box-text">서울특별시 강남구 테헤란로 123</p>
      </div>
      
      <div class="info-box">
        <h3 class="info-box-title">대중교통</h3>
        <p class="info-box-text">지하철 2호선 강남역 3번 출구</p>
      </div>
    </div>
  </div>
</section>

<script src="//dapi.kakao.com/v2/maps/sdk.js?appkey=YOUR_APP_KEY"></script>
```

#### 솔루션 페이지 (6개)

**solutions/smart-safety.html - 스마트 현장안전 시스템**
```html
<section class="content-section">
  <div class="container">
    <div class="content-wrapper">
      <div class="content-block fade-in-up">
        <h2 class="content-block-title">시스템 개요</h2>
        <p class="content-block-text">
          스마트 현장안전 시스템은 건설 현장의 안전교육과 방문자 관리를 통합한 솔루션입니다...
        </p>
      </div>
      
      <div class="content-block fade-in-up">
        <h2 class="content-block-title">주요 특징</h2>
        <ul class="content-block-list">
          <li>디지털 안전교육 시스템으로 교육 이력 자동 관리</li>
          <li>방문자 실시간 추적 및 출입 기록 관리</li>
          <li>안전 규정 미준수 시 즉각 알림</li>
        </ul>
      </div>
      
      <!-- 시스템 구성도 -->
      <div class="system-diagram fade-in-up">
        <img src="../assets/images/diagrams/smart-safety-diagram.jpg" 
             alt="시스템 구성도" 
             class="system-diagram-image"
             data-lightbox>
        <p class="system-diagram-caption">클릭하여 확대</p>
      </div>
    </div>
  </div>
</section>

<!-- 하위 시스템 섹션 -->
<section class="subsystems-section">
  <div class="container">
    <h2 class="section-title">하위 시스템</h2>
    
    <div class="subsystem-item fade-in-up">
      <div class="subsystem-header">
        <div class="subsystem-icon">
          <svg><!-- 아이콘 --></svg>
        </div>
        <h3 class="subsystem-title">스마트 안전교육 시스템</h3>
      </div>
      <p class="subsystem-description">온라인/오프라인 통합 교육 플랫폼...</p>
      <div class="subsystem-features">
        <div class="subsystem-feature">교육 이수 현황 실시간 모니터링</div>
        <div class="subsystem-feature">맞춤형 교육 콘텐츠 제공</div>
      </div>
    </div>
  </div>
</section>

<!-- 시공사례 섹션 -->
<section class="projects-section">
  <div class="container">
    <h2 class="section-title">주요 시공 사례</h2>
    <div class="projects-grid">
      <!-- 프로젝트 카드 (index.html 참고) -->
    </div>
  </div>
</section>
```

#### 고객지원 페이지 (2개)

**support/contact.html - 문의하기**
```html
<section class="content-section">
  <div class="container">
    <div class="content-wrapper">
      <form id="contact-form" class="fade-in-up" action="https://formsubmit.co/your@email.com" method="POST">
        <div class="form-group">
          <label for="name" class="form-label">이름 <span class="required">*</span></label>
          <input type="text" id="name" name="name" class="input" required>
        </div>
        
        <div class="form-group">
          <label for="company" class="form-label">회사명 <span class="required">*</span></label>
          <input type="text" id="company" name="company" class="input" required>
        </div>
        
        <div class="form-group">
          <label for="phone" class="form-label">연락처 <span class="required">*</span></label>
          <input type="tel" id="phone" name="phone" class="input" required>
        </div>
        
        <div class="form-group">
          <label for="email" class="form-label">이메일 <span class="required">*</span></label>
          <input type="email" id="email" name="email" class="input" required>
        </div>
        
        <div class="form-group">
          <label for="subject" class="form-label">문의 제목 <span class="required">*</span></label>
          <input type="text" id="subject" name="subject" class="input" required>
        </div>
        
        <div class="form-group">
          <label for="message" class="form-label">문의 내용 <span class="required">*</span></label>
          <textarea id="message" name="message" class="textarea" rows="6" required></textarea>
        </div>
        
        <div class="form-group">
          <div class="checkbox-wrapper">
            <input type="checkbox" id="privacy" name="privacy" class="checkbox" required>
            <label for="privacy" class="checkbox-label">
              개인정보 수집 및 이용에 동의합니다 (필수)
            </label>
          </div>
        </div>
        
        <button type="submit" class="btn btn-primary btn-lg">문의하기</button>
      </form>
    </div>
  </div>
</section>
```

**support/remote-support.html - 원격지원**
```html
<section class="content-section">
  <div class="container">
    <div class="content-wrapper">
      <div class="content-block fade-in-up">
        <h2 class="content-block-title">서비스 설명</h2>
        <p class="content-block-text">
          아이티로그의 원격지원 서비스는 현장에서 발생하는 문제를 신속하게 해결합니다...
        </p>
      </div>
      
      <div class="info-box fade-in-up">
        <h3 class="info-box-title">운영 시간</h3>
        <p class="info-box-text">평일 09:00 - 18:00<br>긴급 상황: 24시간 대응</p>
      </div>
      
      <div class="fade-in-up" style="text-align: center; margin-top: 3rem;">
        <a href="https://remote-support-url.com" 
           target="_blank" 
           rel="noopener noreferrer" 
           class="btn btn-primary btn-lg">
          원격지원 시작하기
        </a>
      </div>
    </div>
  </div>
</section>
```

### 3. 빠른 개발 팁

#### Header/Footer 복사
1. `index.html`에서 `<header>` 전체 복사
2. 새 페이지에 붙여넣기
3. 경로 수정: `href="/..."` → `href="../..."`

#### 이미지 경로
- 메인 페이지: `assets/images/...`
- 서브 페이지: `../assets/images/...`

#### CSS/JS 경로
- 메인 페이지: `css/...`, `js/...`
- 서브 페이지: `../css/...`, `../js/...`

### 4. 더미 이미지 사용

개발 중에는 다음 더미 이미지 서비스 사용:

```html
<!-- 히어로 이미지 (1920x1080) -->
<img src="https://via.placeholder.com/1920x1080/0066FF/FFFFFF?text=Hero+Image" alt="Hero">

<!-- 솔루션 아이콘 (64x64) -->
<img src="https://via.placeholder.com/64x64/0066FF/FFFFFF?text=Icon" alt="Icon">

<!-- 프로젝트 이미지 (800x600) -->
<img src="https://via.placeholder.com/800x600/E2E8F0/64748B?text=Project" alt="Project">

<!-- 고객사 로고 (200x100) -->
<img src="https://via.placeholder.com/200x100/FFFFFF/0066FF?text=Logo" alt="Logo">
```

### 5. 체크리스트

각 페이지 완성 후 확인:

- [ ] 메타 태그 (title, description) 작성
- [ ] 브레드크럼 경로 정확
- [ ] 모든 링크 작동 확인
- [ ] 이미지 경로 정확
- [ ] 반응형 테스트 (모바일/태블릿/데스크톱)
- [ ] 애니메이션 작동 확인
- [ ] 폼 유효성 검사 작동 (문의하기)
- [ ] 브라우저 호환성 테스트

## 다음 단계

1. **나머지 HTML 페이지 작성** (12개)
   - about/ (4개 남음)
   - solutions/ (6개)
   - support/ (1개 남음)

2. **실제 콘텐츠 입력**
   - 회사 정보
   - 솔루션 설명
   - 시공사례

3. **이미지 준비 및 교체**
   - 로고
   - 히어로 이미지
   - 솔루션 아이콘
   - 시공사례 사진
   - 고객사 로고

4. **기능 연동**
   - 문의 폼 메일 발송
   - 카카오맵 API
   - Google Analytics

5. **테스트 및 최적화**
   - 성능 테스트
   - 접근성 테스트
   - SEO 최적화

6. **배포**
   - 호스팅 선택
   - 도메인 연결
   - SSL 설정

## 참고 자료

- 디자인 문서: `docs/template2/`
- 메인 페이지 예시: `index.html`
- CSS 변수: `css/variables.css`
- 컴포넌트 예시: `css/components.css`

---

**작성일**: 2024  
**버전**: 1.0
