# 프로젝트 문서

이 폴더에는 홈페이지 리뉴얼 프로젝트의 핵심 문서들이 포함되어 있습니다.

## 📁 폴더 구조

```
docs/
├── README.md                      # 이 파일
├── renewal_content.md             # 리뉴얼 콘텐츠 전체 내용 (핵심 문서)
├── renewal_project_summary.md     # 프로젝트 요약
├── implementation_progress.md     # Template3 구현 진행 상황
├── template1/                     # Template1 관련 문서
├── template2/                     # Template2 관련 문서
├── template3/                     # Template3 관련 문서
└── archive/                       # 보관된 기획 문서들
    ├── template3_planning/        # Template3 기획 단계 문서
    └── task_instructions/         # 작업 지침서
```

## 📄 핵심 문서

### 1. renewal_content.md
- **목적**: 홈페이지 리뉴얼의 전체 콘텐츠 구조 및 내용
- **내용**: 사이트맵, 페이지별 콘텐츠, 히어로 섹션, 회사 연혁, 솔루션 상세 등
- **사용**: 모든 템플릿 구현 시 참조하는 마스터 문서

### 2. implementation_progress.md
- **목적**: Template3 구현 진행 상황 추적
- **내용**: Phase별 완료 현황, 생성/업데이트된 파일 목록, 다음 단계 권장사항
- **사용**: 현재 작업 상태 확인 및 남은 작업 파악

### 3. renewal_project_summary.md
- **목적**: 프로젝트 전체 요약
- **내용**: 프로젝트 개요, 목표, 범위
- **사용**: 프로젝트 이해 및 방향성 확인

## 📂 템플릿별 문서

각 템플릿 폴더(template1, template2, template3)에는 다음 문서들이 포함되어 있습니다:
- `README.md`: 템플릿 개요
- `PM-DOCS.md`: PM 관점의 문서
- `UX-DOCS.md`: UX 디자인 문서
- `WEB-PLANNING-DOCS.md`: 웹 기획 문서
- `FRONTEND-DOCS.md`: 프론트엔드 개발 문서 (template1만)

## 📦 Archive 폴더

더 이상 활발히 사용되지 않지만 참고용으로 보관된 문서들입니다.

### archive/template3_planning/
Template3 초기 기획 단계에서 생성된 문서들:
- `ia_user_flow_template3.md`: 사용자 플로우
- `sitemap_visual_template3.md`: 시각적 사이트맵
- `ux_improvement_proposal_template3.md`: UX 개선 제안
- `ux_interaction_improvements_template3.md`: 인터랙션 개선
- `ux_layout_proposals_template3.md`: 레이아웃 제안
- `ux_quick_summary_template3.md`: UX 빠른 요약
- `ia_implementation_summary.md`: IA 구현 요약

### archive/task_instructions/
각 역할별 작업 지침서:
- `task_instructions_frontend_dev.md`: 프론트엔드 개발자용
- `task_instructions_ux_designer.md`: UX 디자이너용
- `task_instructions_web_planner.md`: 웹 기획자용

## 🔍 문서 사용 가이드

### 새로운 페이지 구현 시
1. `renewal_content.md`에서 해당 페이지의 콘텐츠 확인
2. 템플릿별 문서에서 디자인 가이드 확인
3. `implementation_progress.md`에 진행 상황 업데이트

### 프로젝트 이해가 필요할 때
1. `renewal_project_summary.md`로 전체 개요 파악
2. `renewal_content.md`로 상세 콘텐츠 확인
3. 필요시 archive 폴더의 기획 문서 참조

### 작업 현황 확인 시
1. `implementation_progress.md`에서 현재 진행 상황 확인
2. 완료된 작업과 남은 작업 파악
3. 다음 단계 권장사항 검토

## 📝 문서 업데이트 규칙

- **renewal_content.md**: 콘텐츠 변경 시에만 수정
- **implementation_progress.md**: 작업 완료 시마다 업데이트
- **템플릿별 문서**: 해당 템플릿 작업 시 필요에 따라 업데이트
- **Archive 문서**: 수정하지 않음 (읽기 전용)
