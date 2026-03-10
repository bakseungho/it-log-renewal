# Web Templates

아이티로그 웹사이트 템플릿 모음입니다.

## 템플릿 구조

### Light Mode
라이트 모드 테마의 웹사이트 템플릿
- 밝은 배경, 어두운 텍스트
- 깔끔하고 모던한 디자인
- 접근성 최적화 (WCAG AA)

**디렉토리**: `web/light/`

### Dark Mode
다크 모드 테마의 웹사이트 템플릿
- 어두운 배경, 밝은 텍스트
- 프리미엄 다크 테마
- WCAG AAA 접근성 준수
- GSAP 애니메이션
- Swiper 슬라이더

**디렉토리**: `web/dark/`

## 공통 구조

모든 템플릿은 동일한 페이지 구조를 가집니다:

```
template/
├── index.html              # 메인 페이지
├── pages/                  # 서브페이지 폴더
│   ├── about/              # 회사소개
│   │   ├── company.html
│   │   ├── ceo-message.html
│   │   ├── history.html
│   │   ├── safety-policy.html
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
1. 원하는 템플릿 디렉토리로 이동
2. HTML 파일을 브라우저에서 직접 열기
3. 또는 로컬 서버 실행:
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Node.js (http-server)
   npx http-server
   ```

### 배포
1. 템플릿 디렉토리 전체를 웹 서버에 업로드
2. 이미지 경로 확인
3. 도메인 설정

## 템플릿 선택 가이드

### Light Mode 사용 시
- 밝고 깔끔한 이미지 선호
- 전통적인 기업 웹사이트 스타일
- 인쇄물과의 일관성 필요
- 낮 시간대 주 사용자

### Dark Mode 사용 시
- 모던하고 프리미엄한 이미지
- 기술 중심 기업 이미지
- 눈의 피로도 감소 필요
- 멀티미디어 콘텐츠 강조
- 밤 시간대 주 사용자

## 커스터마이징

### 컬러 변경
각 템플릿의 `css/variables.css` 파일에서 컬러 변수 수정

### 레이아웃 변경
- `css/common.css`: 공통 레이아웃
- `css/components.css`: 컴포넌트 스타일
- `css/pages/`: 페이지별 스타일

### 콘텐츠 수정
HTML 파일에서 직접 텍스트 및 이미지 경로 수정

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
