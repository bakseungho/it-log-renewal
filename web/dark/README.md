# Dark Mode Template

다크 모드 테마의 웹사이트 템플릿입니다.

## 특징

- 어두운 배경과 밝은 텍스트
- 프리미엄 다크 테마 디자인
- 접근성 최적화 (WCAG 2.1 AAA 준수)
- 반응형 레이아웃
- GSAP 애니메이션
- Swiper 슬라이더

## 컬러 시스템

- **배경**: 다크 그라데이션 (#0a0a0a ~ #1a1a1a)
- **텍스트**: 밝은 색상 계열 (#ffffff, #e0e0e0, #b0b0b0)
- **Primary**: #4D9FFF (다크모드 최적화, 대비율 7.2:1)
- **Accent**: 시안 계열 (#00E5FF)

## 디렉토리 구조

```
dark/
├── index.html              # 메인 페이지
├── pages/                  # 서브페이지 폴더
│   ├── about/              # 회사소개
│   ├── solutions/          # 제품 솔루션
│   ├── projects/           # 시공사례
│   └── support/            # 고객지원
├── css/                    # 스타일시트
│   ├── reset.css
│   ├── variables.css       # 다크 모드 변수
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
- Parallax 효과

### 반응형 디자인
- 모바일 최적화
- 태블릿 레이아웃
- 데스크톱 레이아웃

## 개발 가이드

자세한 개발 가이드는 `DEVELOPMENT-GUIDE.md`를 참조하세요.

## 접근성

- WCAG 2.1 AAA 레벨 준수
- 다크모드 최적화 컬러 (대비율 7.2:1)
- 키보드 네비게이션 지원
- 스크린 리더 호환

## 테마 전환

라이트 모드가 필요한 경우 `../light/`를 사용하세요.
