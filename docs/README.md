# 프로젝트 문서

이 폴더에는 홈페이지 리뉴얼 프로젝트의 핵심 문서들이 포함되어 있습니다.

## ⚠️ 주의사항

### 다크/라이트 테마 작업 규칙
1. **기준 테마**: 모든 내용 업데이트는 **다크 테마 기준**으로 먼저 적용
2. **효율적 동기화**: 추가/수정된 부분만 라이트 테마에 적용 (전체 복제 금지)
3. **라이트 테마 적용 시 규칙**:
   - ✅ 내용 구성: 다크 테마와 동일하게 복제
   - ✅ 레이아웃/구조: 다크 테마와 동일하게 복제
   - ⚠️ 색상/스타일: 라이트 테마에 맞게 조정 (CSS 변수 활용)
   - ✅ 이미지 경로: 그대로 복제
   - ❌ 이미지 파일: 복제하지 않음 (공유 사용)

### CSS 동기화 규칙
- `variables.css`: 테마별로 독립 관리 (색상 변수가 다름)
- 나머지 CSS: 다크 테마 기준으로 작성 후 라이트 테마에 복사
- 하드코딩된 색상 사용 금지 (CSS 변수 사용 필수)

##   폴더 구조

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
- **내용**: 
  - 사이트맵 및 페이지 구조
  - 페이지별 상세 콘텐츠
  - 히어로 섹션 문구
  - 회사 연혁 및 정보
  - 솔루션 상세 설명
- **사용**: 모든 페이지 구현 시 참조하는 마스터 문서
- **업데이트**: 콘텐츠 변경 시에만 수정

### 2. implementation_progress.md
- **목적**: 구현 진행 상황 추적 및 관리
- **내용**: 
  - Phase별 완료 현황
  - 생성/업데이트된 파일 목록
  - 다음 단계 권장사항
  - 주요 변경 이력
- **사용**: 현재 작업 상태 확인 및 남은 작업 파악
- **업데이트**: 작업 완료 시마다 업데이트

### 3. renewal_project_summary.md
- **목적**: 프로젝트 전체 요약 및 개요
- **내용**: 
  - 프로젝트 배경 및 목표
  - 주요 개선 사항
  - 기술 스택
  - 프로젝트 범위
- **사용**: 프로젝트 이해 및 방향성 확인
- **업데이트**: 프로젝트 방향 변경 시

## 📂 템플릿 문서

### template1/ (현재 사용 중인 템플릿)
- `README.md`: 템플릿 개요 및 특징
- `PM-DOCS.md`: PM 관점의 요구사항 및 기획
- `UX-DOCS.md`: UX 디자인 가이드 및 인터랙션
- `WEB-PLANNING-DOCS.md`: 웹 기획 및 정보 구조

## 📦 Archive 폴더

더 이상 활발히 사용되지 않지만 참고용으로 보관된 문서들입니다.

### archive/template3_planning/
Template3 초기 기획 단계에서 생성된 문서들:
- `ia_user_flow_template3.md`: 사용자 플로우 설계
- `sitemap_visual_template3.md`: 시각적 사이트맵
- `ux_improvement_proposal_template3.md`: UX 개선 제안
- `ux_interaction_improvements_template3.md`: 인터랙션 개선 방안
- `ux_layout_proposals_template3.md`: 레이아웃 제안
- `ux_quick_summary_template3.md`: UX 빠른 요약
- `ia_implementation_summary.md`: IA 구현 요약

### archive/task_instructions/
각 역할별 작업 지침서:
- `task_instructions_frontend_dev.md`: 프론트엔드 개발자용 가이드
- `task_instructions_ux_designer.md`: UX 디자이너용 가이드
- `task_instructions_web_planner.md`: 웹 기획자용 가이드

## 🔍 문서 사용 가이드

### 새로운 페이지 구현 시
1. `renewal_content.md`에서 해당 페이지의 콘텐츠 확인
2. `template1/` 폴더의 디자인 가이드 확인
3. 다크 테마에서 먼저 구현
4. 라이트 테마에 동기화 (위의 규칙 준수)
5. `implementation_progress.md`에 진행 상황 업데이트

### 프로젝트 이해가 필요할 때
1. `renewal_project_summary.md`로 전체 개요 파악
2. `renewal_content.md`로 상세 콘텐츠 확인
3. `template1/` 문서로 디자인 가이드 확인
4. 필요시 `archive/` 폴더의 기획 문서 참조

### 작업 현황 확인 시
1. `implementation_progress.md`에서 현재 진행 상황 확인
2. 완료된 작업과 남은 작업 파악
3. 다음 단계 권장사항 검토

### 스타일 수정 시
1. 다크 테마 CSS 먼저 수정
2. CSS 변수 사용 (하드코딩 금지)
3. `scripts/sync_dark_to_light_styles.py` 실행하여 라이트 테마 동기화
4. 라이트 테마 색상 확인 및 조정 (`variables.css` 제외)

## 📝 문서 업데이트 규칙

| 문서 | 업데이트 시점 | 담당 |
|------|--------------|------|
| `renewal_content.md` | 콘텐츠 변경 시 | PM/기획자 |
| `implementation_progress.md` | 작업 완료 시마다 | 개발자 |
| `renewal_project_summary.md` | 프로젝트 방향 변경 시 | PM |
| `template1/` 문서 | 디자인 가이드 변경 시 | UX/기획자 |
| `archive/` 문서 | 수정하지 않음 (읽기 전용) | - |

## 🛠️ 유용한 스크립트

프로젝트 루트의 `scripts/` 폴더에 다음 스크립트들이 있습니다:

- `sync_dark_to_light_styles.py`: 다크→라이트 CSS/JS 동기화
- `remove_page_header_description.py`: 페이지 헤더 설명 일괄 제거
- `comment_components_section.py`: 구성품 섹션 주석처리
- `fix_smart_safety_duplicate.py`: 중복 콘텐츠 제거

## 📌 참고사항

- 모든 문서는 Markdown 형식으로 작성
- 이미지는 `web/dark/images/` 또는 `web/light/images/`에 저장
- CSS 변수는 `web/[theme]/css/variables.css`에 정의
- 공통 스타일은 다크 테마 기준으로 작성 후 동기화

# 주의사항
- 내용 업데이트 중심은 다크 테마 기준으로 적용
- 내용 업데이트나 추가된 경우 추가된 부분만 적용할 것 (추가된 경우가 아닌 모든 리소스들을 복제하는 비효율성 제거)
- 다크테마에서 라이트 테마로 옮길 시 주의 및 규칙
    1. 내용 구성 중심은 다크 테마 내 내용들을 똑같이 복제
    2. 새로 추가된 스타일이나 수정된 (레이아웃이나 컬러 등) 그대로 복제하나 컬러 톤은 라이트 테마에 맞추어서 적용
    3. 이미지 경로 그대로 복제하되 이미지 리소스(파일)은 복제를 하면 안됨