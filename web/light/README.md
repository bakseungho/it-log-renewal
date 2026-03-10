# Light Mode Template

라이트 모드 테마의 웹사이트 템플릿입니다.

## 특징

- 밝은 배경과 어두운 텍스트
- 깔끔하고 모던한 디자인
- 접근성 최적화 (WCAG 2.1 AA 준수)
- 반응형 레이아웃

## 컬러 시스템

- **배경**: 밝은 색상 계열 (#ffffff, #f8f9fa, #f1f3f5)
- **텍스트**: 어두운 색상 계열 (#1a1a1a, #4a4a4a, #6b6b6b)
- **Primary**: #0066FF (라이트 배경 최적화)
- **Accent**: 포인트 컬러

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
└── images/                 # 이미지 리소스
```

## 개발 가이드

자세한 개발 가이드는 `DEVELOPMENT-GUIDE.md`를 참조하세요.

## 접근성

- WCAG 2.1 AA 레벨 준수
- 텍스트 대비율 4.5:1 이상
- 키보드 네비게이션 지원
- 스크린 리더 호환

## 테마 전환

다크 모드가 필요한 경우 `../dark/`를 사용하세요.
