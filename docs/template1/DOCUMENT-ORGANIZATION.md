# 문서 정리 및 통합 권장사항

## 📊 현재 문서 현황 분석

### 총 문서 수: 17개

#### 분류별 현황
- **PM 관리 문서**: 6개
- **콘텐츠/기획**: 2개  
- **UX 디자인**: 4개
- **개발 문서**: 2개
- **프로젝트 전반**: 3개

---

## 🔍 문서 중복 및 통합 분석

### 1. 중복 문서 식별

#### ⚠️ 높은 중복도 (통합 권장)

**그룹 A: 요구사항 문서 vs 작업 지시서**

| 기존 문서 (참고용) | 신규 문서 (실행용) | 중복도 | 권장 조치 |
|-------------------|-------------------|--------|-----------|
| `pm-requirements-for-ux.md` | `pm-brief-for-ux-designer.md` | 70% | **통합** |
| `pm-requirements-for-frontend.md` | `pm-brief-for-frontend-dev.md` | 70% | **통합** |

**분석**:
- 작업 지시서가 요구사항 문서의 내용을 포함하면서 더 구체적
- 두 문서를 동시에 참조하면 혼란 발생 가능
- 작업 지시서가 최신 버전이며 실제 작업에 사용

**권장 조치**:
```
옵션 1 (권장): 작업 지시서로 통합
- pm-brief-for-ux-designer.md (유지)
- pm-brief-for-frontend-dev.md (유지)
- pm-requirements-for-ux.md (삭제 또는 아카이브)
- pm-requirements-for-frontend.md (삭제 또는 아카이브)

옵션 2: 역할 분리
- 작업 지시서: 실행 중심 (What, When, How)
- 요구사항 문서: 상세 참고 (Why, Details)
- 단, 내용 중복 최소화 필요
```

---

**그룹 B: 프로젝트 개요 문서**

| 문서 | 주요 내용 | 대상 | 중복도 |
|------|-----------|------|--------|
| `pm-project-brief.md` | 프로젝트 전체 개요, 목표, 일정 | 전체 팀 | - |
| `PROJECT-SUMMARY.md` | 기술 스택, 구조, 특징 | 개발자 중심 | 30% |
| `DEVELOPMENT.md` | 개발 환경, 가이드 | 개발자 | 20% |

**분석**:
- 각 문서가 다른 관점에서 작성됨
- 일부 기술 스택 정보 중복
- 대상 독자가 명확히 구분됨

**권장 조치**:
```
현재 구조 유지 (통합 불필요)
- pm-project-brief.md: 비즈니스/프로젝트 관점
- PROJECT-SUMMARY.md: 기술 개요
- DEVELOPMENT.md: 개발 실무 가이드

단, 기술 스택 정보는 한 곳에서 관리하고 참조
```

---

### 2. 문서 역할 재정의

#### 📋 명확한 역할 구분

| 문서 유형 | 목적 | 특징 | 예시 |
|-----------|------|------|------|
| **브리프** | 프로젝트 전체 개요 | 비즈니스 목표, 배경 | `pm-project-brief.md` |
| **작업 지시서** | 역할별 실행 가이드 | 구체적 작업, 산출물, 일정 | `pm-brief-for-*.md` |
| **요구사항** | 상세 스펙 및 기준 | 기술적 세부사항 | `pm-requirements-for-*.md` |
| **가이드라인** | 표준 및 규칙 | 디자인/코딩 표준 | `website-renewal-guidelines.md` |
| **산출물** | 작업 결과물 | 실제 설계/디자인 | `ux-*.md` |

---

## 📁 권장 문서 구조

### 옵션 1: 최소 구조 (권장)

```
docs/
├── README.md                          ⭐ 문서 인덱스 (신규)
│
├── 01-project-management/             📂 프로젝트 관리
│   ├── pm-project-brief.md           (프로젝트 브리프)
│   ├── pm-task-assignment.md         (작업 배분 및 일정)
│   └── hopage_renewal_content.md     (콘텐츠 요구사항)
│
├── 02-planning/                       📂 기획
│   ├── pm-brief-for-web-planner.md   (웹 기획자 작업 지시서)
│   └── [웹 기획자 산출물]
│
├── 03-ux-design/                      📂 UX 디자인
│   ├── pm-brief-for-ux-designer.md   (UX 디자이너 작업 지시서)
│   ├── ux-design-concept.md          (디자인 컨셉)
│   ├── ux-information-architecture.md (정보 구조)
│   ├── ux-wireframes.md              (와이어프레임)
│   └── ux-design-system.md           (디자인 시스템)
│
├── 04-development/                    📂 개발
│   ├── pm-brief-for-frontend-dev.md  (프론트엔드 작업 지시서)
│   ├── frontend-technical-spec.md    (기술 명세)
│   └── DEVELOPMENT.md                (개발 가이드)
│
├── 05-guidelines/                     📂 가이드라인
│   └── website-renewal-guidelines.md (전체 가이드라인)
│
├── 06-archive/                        📂 아카이브 (선택)
│   ├── pm-requirements-for-ux.md     (구 UX 요구사항)
│   └── pm-requirements-for-frontend.md (구 개발 요구사항)
│
└── PROJECT-SUMMARY.md                 (프로젝트 요약)
```

### 옵션 2: 현재 구조 유지 + 정리

```
docs/
├── README.md                          ⭐ 문서 인덱스 (신규)
├── DOCUMENT-ORGANIZATION.md           ⭐ 정리 가이드 (신규)
│
├── [PM 문서들]                        (현재 위치 유지)
├── [UX 문서들]                        (현재 위치 유지)
├── [개발 문서들]                      (현재 위치 유지)
│
└── archive/                           📂 아카이브
    ├── pm-requirements-for-ux.md
    └── pm-requirements-for-frontend.md
```

---

## 🎯 구체적 정리 방안

### 단계 1: 즉시 실행 (필수)

#### 1.1 문서 인덱스 생성 ✅
- [x] `docs/README.md` 생성 완료
- 모든 문서의 역할과 관계 명시
- 역할별 필독 문서 가이드

#### 1.2 중복 문서 처리 (선택)

**방안 A: 아카이브 (권장)**
```bash
# archive 폴더 생성
mkdir docs/archive

# 구 요구사항 문서 이동
mv docs/pm-requirements-for-ux.md docs/archive/
mv docs/pm-requirements-for-frontend.md docs/archive/

# README에 아카이브 설명 추가
```

**방안 B: 삭제**
```bash
# 백업 후 삭제
rm docs/pm-requirements-for-ux.md
rm docs/pm-requirements-for-frontend.md
```

**방안 C: 통합**
- 작업 지시서에 요구사항 문서 내용 병합
- 중복 제거 및 최신화
- 구 문서 삭제

---

### 단계 2: 문서 명명 규칙 통일 (선택)

#### 현재 명명 방식
- `pm-*`: PM 관련 문서
- `ux-*`: UX 디자인 산출물
- `frontend-*`: 개발 문서
- 대문자: 프로젝트 전반 문서

#### 권장 명명 규칙
```
[역할]-[유형]-[내용].md

예시:
- pm-brief-project.md (프로젝트 브리프)
- pm-brief-web-planner.md (웹 기획자 작업 지시서)
- ux-deliverable-wireframes.md (와이어프레임)
- dev-spec-frontend.md (프론트엔드 기술 명세)
```

---

### 단계 3: 문서 내용 최적화 (선택)

#### 3.1 작업 지시서 강화
각 작업 지시서에 다음 섹션 추가:
- [ ] 빠른 시작 가이드 (Quick Start)
- [ ] 체크리스트 (Checklist)
- [ ] FAQ (자주 묻는 질문)
- [ ] 트러블슈팅 (Troubleshooting)

#### 3.2 크로스 레퍼런스 추가
문서 간 연결 강화:
```markdown
## 관련 문서
- 이전 단계: [웹 기획자 산출물](../02-planning/)
- 참고 문서: [디자인 가이드라인](../05-guidelines/website-renewal-guidelines.md)
- 다음 단계: [프론트엔드 개발](../04-development/)
```

#### 3.3 버전 관리 추가
각 문서에 버전 정보 명시:
```markdown
---
**문서 버전**: 2.0
**최종 수정일**: 2024-01-15
**작성자**: PM
**변경 이력**:
- v2.0 (2024-01-15): 작업 지시서로 전환
- v1.0 (2024-01-01): 초기 작성
---
```

---

## 📊 문서 매트릭스

### 역할별 문서 사용 매트릭스

| 문서 | PM | 웹기획 | UX | 개발 | 우선순위 |
|------|:--:|:------:|:--:|:----:|:--------:|
| pm-project-brief.md | ⭐ | ⭐ | ⭐ | ⭐ | 필수 |
| pm-task-assignment.md | ⭐ | ⭐ | ⭐ | ⭐ | 필수 |
| hopage_renewal_content.md | ⭐ | ⭐ | ⭐ | ⭐ | 필수 |
| pm-brief-for-web-planner.md | ○ | ⭐ | ○ | - | 필수 |
| pm-brief-for-ux-designer.md | ○ | ○ | ⭐ | - | 필수 |
| pm-brief-for-frontend-dev.md | ○ | - | ○ | ⭐ | 필수 |
| website-renewal-guidelines.md | ○ | ○ | ○ | ○ | 참고 |
| ux-design-concept.md | ○ | ○ | ⭐ | ○ | 참고 |
| frontend-technical-spec.md | ○ | - | ○ | ⭐ | 필수 |
| DEVELOPMENT.md | - | - | - | ⭐ | 필수 |
| PROJECT-SUMMARY.md | ○ | ○ | ○ | ⭐ | 참고 |
| pm-requirements-for-ux.md | - | - | △ | - | 아카이브 |
| pm-requirements-for-frontend.md | - | - | - | △ | 아카이브 |

**범례**:
- ⭐ 필수 문서
- ○ 참고 문서
- △ 선택적 참고
- \- 불필요

---

## ✅ 실행 체크리스트

### 즉시 실행 (완료)
- [x] `docs/README.md` 생성 - 문서 인덱스
- [x] `docs/DOCUMENT-ORGANIZATION.md` 생성 - 정리 가이드

### 권장 실행 (선택)
- [ ] 중복 문서 아카이브 또는 삭제
  - [ ] `pm-requirements-for-ux.md`
  - [ ] `pm-requirements-for-frontend.md`
- [ ] 폴더 구조 재구성 (옵션 1 또는 2 선택)
- [ ] 문서 명명 규칙 통일
- [ ] 각 문서에 버전 정보 추가
- [ ] 크로스 레퍼런스 추가

### 장기 개선 (선택)
- [ ] 작업 지시서에 FAQ 섹션 추가
- [ ] 트러블슈팅 가이드 작성
- [ ] 문서 템플릿 생성
- [ ] 자동화된 문서 검증 도구 도입

---

## 💡 권장 사항 요약

### 최소 조치 (현재 완료)
1. ✅ `docs/README.md` - 문서 인덱스 생성
2. ✅ `docs/DOCUMENT-ORGANIZATION.md` - 정리 가이드 생성

### 추가 권장 조치
1. **중복 문서 처리**
   - `pm-requirements-for-ux.md` → 아카이브 또는 삭제
   - `pm-requirements-for-frontend.md` → 아카이브 또는 삭제

2. **문서 우선순위 명확화**
   - 작업 지시서 (`pm-brief-for-*.md`)를 메인 문서로 사용
   - 요구사항 문서는 참고용으로만 활용

3. **팀원 교육**
   - `docs/README.md`를 프로젝트 킥오프 시 공유
   - 각 역할별 필독 문서 안내

---

## 📞 문의

문서 정리 관련 질문이나 제안사항이 있으시면 PM에게 연락해 주세요.

---

**작성일**: 2024  
**작성자**: PM  
**버전**: 1.0
