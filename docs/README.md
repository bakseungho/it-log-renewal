# 프로젝트 문서

이 폴더에는 홈페이지 리뉴얼 프로젝트의 핵심 문서들이 포함되어 있습니다.

## ⚠️ 주의사항

### 작업 규칙
1. **기준 테마**: 라이트 테마 단일 운영 (`web/light/`)
2. **CSS 변수 사용 필수**: 하드코딩된 색상 사용 금지
3. **반응형 대응**: 모든 변경사항은 PC/태블릿/모바일 확인 필수

## 📁 폴더 구조

```
docs/
├── README.md                      # 이 파일 (프로젝트 문서 가이드)
├── renewal_content.md             # 리뉴얼 콘텐츠 전체 내용 (핵심 문서)
├── renewal_project_summary.md     # 프로젝트 요약
├── implementation_progress.md     # 구현 진행 상황 추적
├── template1/                     # Template1 관련 문서
│   ├── README.md
│   ├── PM-DOCS.md
│   ├── UX-DOCS.md
│   └── WEB-PLANNING-DOCS.md
└── archive/                       # 보관된 기획 문서들
    ├── README.md
    ├── template3_planning/        # Template3 기획 단계 문서
    └── task_instructions/         # 작업 지침서
```

## 📄 핵심 문서

### 1. renewal_content.md ⭐
- **목적**: 홈페이지 리뉴얼의 전체 콘텐츠 구조 및 내용
- **내용**: 사이트맵, 페이지별 상세 콘텐츠, 히어로 섹션 문구, 회사 연혁, 솔루션 상세 설명
- **사용**: 모든 페이지 구현 시 참조하는 마스터 문서

### 2. implementation_progress.md
- **목적**: 구현 진행 상황 추적 및 관리
- **내용**: Phase별 완료 현황, 파일 목록, 다음 단계 권장사항

### 3. renewal_project_summary.md
- **목적**: 프로젝트 전체 요약 및 개요
- **내용**: 프로젝트 배경, 목표, 주요 개선 사항, 기술 스택

## 📂 템플릿 문서

### template1/ (참고용)
- `README.md`: 템플릿 개요 및 특징
- `PM-DOCS.md`: PM 관점의 요구사항 및 기획
- `UX-DOCS.md`: UX 디자인 가이드 및 인터랙션
- `WEB-PLANNING-DOCS.md`: 웹 기획 및 정보 구조

## 📦 Archive 폴더

더 이상 활발히 사용되지 않지만 참고용으로 보관된 문서들입니다.

## 🔍 문서 사용 가이드

### 새로운 페이지 구현 시
1. `renewal_content.md`에서 해당 페이지의 콘텐츠 확인
2. `template1/` 폴더의 디자인 가이드 확인
3. `web/light/`에서 구현
4. `implementation_progress.md`에 진행 상황 업데이트

### 프로젝트 이해가 필요할 때
1. `renewal_project_summary.md`로 전체 개요 파악
2. `renewal_content.md`로 상세 콘텐츠 확인
3. 필요시 `archive/` 폴더의 기획 문서 참조

## 📝 문서 업데이트 규칙

| 문서 | 업데이트 시점 | 담당 |
|------|--------------|------|
| `renewal_content.md` | 콘텐츠 변경 시 | PM/기획자 |
| `implementation_progress.md` | 작업 완료 시마다 | 개발자 |
| `renewal_project_summary.md` | 프로젝트 방향 변경 시 | PM |
| `archive/` 문서 | 수정하지 않음 (읽기 전용) | - |

## 📌 참고사항
- 모든 문서는 Markdown 형식으로 작성
- 이미지는 `web/light/images/`에 저장
- CSS 변수는 `web/light/css/variables.css`에 정의

## 반응형 분기점
- 3분기점 (3분기점으로 진행)
  - PC, 노트북 (해상도 1025px ~)
  - 태블릿 세로 가로 (해상도 769px ~ 1024px)
  - 모바일 세로 (해상도 ~ 768px)

- 4분기점
  - PC, 노트북 (해상도 1024px ~)
  - 태블릿 세로 가로 (해상도 768px ~ 1023px)
  - 모바일 세로 (해상도 480px ~ 767px)
  - 모바일 가로 (해상도 ~ 479px)