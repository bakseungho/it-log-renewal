# Light Mode Template

라이트 모드 테마의 웹사이트 템플릿입니다.

## 특징

- 밝은 배경과 어두운 텍스트
- 깔끔하고 모던한 디자인
- 접근성 최적화 (WCAG 2.1 AA 준수)
- 반응형 레이아웃
- GSAP 애니메이션
- Swiper 슬라이더

## 컬러 시스템

- **배경**: #ffffff (순백색)
- **텍스트**: 다크 계열 (#1a1a1a, #505050, #767676)
- **Primary**: #0066FF (WCAG AA 준수, 대비율 5.1:1)
- **Accent Secondary**: #00A8E8

## 디렉토리 구조

```
light/
├── index.html              # 메인 페이지
├── pages/                  # 서브페이지 폴더
│   ├── about/              # 회사소개
│   ├── solutions/          # 제품 솔루션
│   ├── projects/           # 시공사례
│   └── support/            # 고객지원
├── css/                    # 스타일시트
│   ├── reset.css
│   ├── variables.css       # 라이트 모드 변수
│   ├── common.css
│   ├── components.css
│   ├── header.css
│   ├── footer.css
│   └── pages/
├── js/                     # JavaScript
│   ├── main.js
│   ├── components.js
│   └── utils.js
└── images/                 # 이미지 리소스
```

## 주요 기능

### 히어로 슬라이더
- Swiper.js 기반 슬라이더
- 자동 재생/정지 토글 버튼
- 프로그레스 바 애니메이션
- 페이드 전환 효과

### 스크롤 애니메이션
- GSAP ScrollTrigger
- Fade-in, Scale-in 효과
- 카운터 애니메이션

### 반응형 디자인
- 모바일 최적화
- 태블릿 레이아웃
- 데스크톱 레이아웃

## 개발 가이드

자세한 개발 가이드는 `DEVELOPMENT-GUIDE.md`를 참조하세요.

## 접근성

- WCAG 2.1 AA 레벨 준수
- 키보드 네비게이션 지원
- 스크린 리더 호환
- ARIA 레이블 적용
