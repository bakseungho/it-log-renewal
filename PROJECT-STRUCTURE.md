# 프로젝트 구조

## 최종 디렉터리 구조

```
renewal2/
├── .kiro/                          # Kiro 설정 파일
├── .vscode/                        # VS Code 설정
│
├── docs/                           # 프로젝트 문서
│   ├── README.md                   # 문서 가이드
│   └── template1/                  # Template1 관련 문서 (45개)
│       ├── 기획 문서 (PM)
│       │   ├── pm-project-brief.md
│       │   ├── pm-brief-for-*.md
│       │   ├── pm-requirements-*.md
│       │   └── website-renewal-*.md
│       │
│       ├── 디자인 문서 (UX)
│       │   ├── ux-design-*.md
│       │   ├── ux-wireframes*.md
│       │   └── ux-information-architecture.md
│       │
│       ├── 웹 기획 문서
│       │   ├── web-planning-sitemap.md
│       │   ├── web-planning-content-strategy.md
│       │   ├── web-planning-functional-spec.md
│       │   └── web-planning-user-flow.md
│       │
│       ├── 개발 문서 (Frontend)
│       │   ├── frontend-technical-spec.md
│       │   ├── DEVELOPMENT.md
│       │   ├── IMAGE-GUIDE.md
│       │   └── VISUAL-CHECK-GUIDE.md
│       │
│       ├── 테스트 문서
│       │   ├── TESTING-CHECKLIST.md
│       │   ├── TEST-RESULTS.md
│       │   └── WEEK-*-TEST-*.md
│       │
│       └── 완료 보고서
│           ├── WEEK-*-COMPLETION-REPORT.md
│           ├── FINAL-SUMMARY.md
│           └── PROJECT-SUMMARY.md
│
├── web/                            # 웹 템플릿
│   ├── README.md                   # 템플릿 가이드
│   └── template1/                  # 아이티로그 홈페이지
│       ├── index.html              # 메인 페이지
│       ├── 404.html                # 에러 페이지
│       ├── terms.html              # 이용약관
│       ├── privacy.html            # 개인정보처리방침
│       ├── robots.txt              # 검색엔진 크롤링 규칙
│       ├── sitemap.xml             # 사이트맵
│       │
│       ├── about/                  # 회사소개 (5개)
│       │   ├── company.html
│       │   ├── ceo-message.html
│       │   ├── history.html
│       │   ├── certifications.html
│       │   └── location.html
│       │
│       ├── solutions/              # 솔루션 (5개)
│       │   ├── smart-safety.html
│       │   ├── tower-crane.html
│       │   ├── ai-surveillance.html
│       │   ├── environment-sensor.html
│       │   └── access-control.html
│       │
│       ├── support/                # 고객지원 (2개)
│       │   ├── remote-support.html
│       │   └── contact.html
│       │
│       ├── pages/                  # 추가 페이지
│       │
│       └── assets/                 # 정적 리소스
│           ├── css/
│           │   ├── reset.css
│           │   ├── variables.css
│           │   ├── common.css
│           │   ├── components.css
│           │   ├── header.css
│           │   ├── footer.css
│           │   └── pages/
│           │       ├── home.css
│           │       ├── subpage.css
│           │       └── solutions.css
│           │
│           ├── js/
│           │   ├── utils.js
│           │   ├── components.js
│           │   ├── main.js
│           │   └── vendor/
│           │
│           ├── images/
│           │   ├── logo/
│           │   ├── hero/
│           │   ├── clients/
│           │   ├── projects/
│           │   └── placeholder/
│           │
│           └── fonts/
│
├── .gitignore                      # Git 제외 파일
├── README.md                       # 프로젝트 개요
├── SETUP.md                        # 설정 가이드
├── DEVELOPMENT-LOG.md              # 개발 로그
├── CHANGELOG.md                    # 변경 이력
└── PROJECT-STRUCTURE.md            # 이 파일
```

## 폴더별 설명

### 📁 .kiro/
Kiro IDE 설정 파일이 저장되는 폴더입니다.

### 📁 .vscode/
VS Code 에디터 설정 파일이 저장되는 폴더입니다.

### 📁 docs/
프로젝트 관련 모든 문서가 저장되는 폴더입니다.
- `README.md`: 문서 구조 및 읽는 순서 안내
- `template1/`: Template1 (아이티로그 홈페이지) 관련 45개 문서

### 📁 web/
웹사이트 템플릿이 저장되는 폴더입니다.
- `README.md`: 템플릿 설명 및 사용 방법
- `template1/`: 아이티로그 홈페이지 (15개 페이지 + assets)

## 파일 개수 요약

| 카테고리 | 개수 | 위치 |
|---------|------|------|
| 프로젝트 문서 | 45개 | `docs/template1/` |
| 웹 페이지 | 15개 | `web/template1/` |
| CSS 파일 | 10개 | `web/template1/assets/css/` |
| JS 파일 | 3개 | `web/template1/assets/js/` |
| 설정 파일 | 5개 | Root |

## 주요 파일 설명

### Root 레벨
- `README.md`: 프로젝트 전체 개요 및 빠른 시작 가이드
- `SETUP.md`: 개발 환경 설정 가이드
- `DEVELOPMENT-LOG.md`: 8주간의 개발 로그
- `CHANGELOG.md`: 버전별 변경 이력
- `PROJECT-STRUCTURE.md`: 프로젝트 구조 설명 (이 파일)

### docs/template1/
- `FINAL-SUMMARY.md`: 프로젝트 최종 요약
- `frontend-technical-spec.md`: 기술 명세서
- `ux-design-handoff.md`: 디자인 핸드오프 문서
- `TESTING-CHECKLIST.md`: 테스트 체크리스트

### web/template1/
- `index.html`: 메인 페이지
- `sitemap.xml`: 검색엔진용 사이트맵
- `robots.txt`: 크롤링 규칙

## 템플릿 확장 가능성

향후 새로운 템플릿 추가 시:

```
docs/
├── template1/    # 아이티로그 홈페이지 (현재)
├── template2/    # 향후 추가 템플릿
└── template3/    # 향후 추가 템플릿

web/
├── template1/    # 아이티로그 홈페이지 (현재)
├── template2/    # 향후 추가 템플릿
└── template3/    # 향후 추가 템플릿
```

각 템플릿은 독립적으로 관리되며, 자체 문서와 리소스를 포함합니다.

## 로컬 개발 환경

### 웹사이트 실행
```bash
cd web/template1
python -m http.server 8000
# http://localhost:8000
```

### 문서 확인
```bash
# docs/template1/ 폴더의 .md 파일들을 
# Markdown 뷰어로 확인
```

## 배포 구조

배포 시에는 `web/template1/` 폴더의 내용만 서버에 업로드합니다:

```
서버 (public_html 또는 www)/
├── index.html
├── 404.html
├── terms.html
├── privacy.html
├── robots.txt
├── sitemap.xml
├── about/
├── solutions/
├── support/
├── pages/
└── assets/
```

## 버전 관리

Git 저장소 구조:
```
.git/
├── .gitignore          # 제외 파일 목록
└── (Git 내부 파일)
```

제외되는 파일/폴더 (`.gitignore`):
- `node_modules/`
- `.DS_Store`
- `*.log`
- 기타 임시 파일

---

**작성일**: 2024  
**최종 업데이트**: 2024  
**버전**: 1.0
