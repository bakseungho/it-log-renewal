# Web Template

아이티로그 웹사이트 템플릿입니다.

## 템플릿 구조

### Light Mode
라이트 모드 테마의 웹사이트 템플릿
- 밝은 배경, 어두운 텍스트
- 깔끔하고 모던한 디자인
- 접근성 최적화 (WCAG AA)
- GSAP 애니메이션
- Swiper 슬라이더

**디렉토리**: `web/light/`

## 페이지 구조

```
light/
├── index.html              # 메인 페이지
├── pages/                  # 서브페이지 폴더
│   ├── about/              # 회사소개
│   │   ├── company.html
│   │   ├── ceo-message.html
│   │   ├── history.html
│   │   ├── safety-policy.html
│   │   ├── certifications.html
│   │   └── location.html
│   ├── solutions/          # 제품 솔루션
│   │   ├── one-stop-solution.html
│   │   ├── ai-surveillance.html
│   │   ├── smart-safety.html
│   │   ├── tower-crane.html
│   │   ├── access-control.html
│   │   └── environment-sensor.html
│   ├── projects/           # 시공사례
│   │   └── index.html
│   └── support/            # 고객지원
│       ├── remote-support.html
│       └── contact.html
├── css/                    # 스타일시트
├── js/                     # JavaScript
├── images/                 # 이미지
├── privacy.html            # 개인정보처리방침
├── terms.html              # 이용약관
└── 404.html                # 404 페이지
```

## 사용 방법

### 개발 환경
1. `web/light/` 디렉토리로 이동
2. 로컬 서버 실행:
   ```bash
   python -m http.server 8000
   ```
3. `http://localhost:8000` 접속

## 커스터마이징

### 컬러 변경
`web/light/css/variables.css` 파일에서 컬러 변수 수정

### 레이아웃 변경
- `css/common.css`: 공통 레이아웃
- `css/components.css`: 컴포넌트 스타일
- `css/pages/`: 페이지별 스타일

## 기술 스택

- HTML5
- CSS3 (CSS Variables, Grid, Flexbox)
- JavaScript (ES6+)
- GSAP (애니메이션)
- Swiper.js (슬라이더)
- Pretendard 폰트

## 브라우저 지원

- Chrome (최신 버전)
- Firefox (최신 버전)
- Safari (최신 버전)
- Edge (최신 버전)
- 모바일 브라우저

## 라이선스

© 2024 ITLOG. All rights reserved.
