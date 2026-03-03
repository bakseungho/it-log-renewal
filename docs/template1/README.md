# 홈페이지 리뉴얼 프로젝트 문서 가이드

> (주)아이티로그 홈페이지 리뉴얼 프로젝트의 모든 문서를 체계적으로 정리한 가이드입니다.

## 📋 문서 개요

이 프로젝트는 건설 현장 솔루션 전문 기업인 (주)아이티로그의 홈페이지 리뉴얼을 위한 문서들로 구성되어 있습니다. 
정적 웹사이트(HTML/CSS/JavaScript) 기반으로 개발되며, 8주간의 일정으로 진행됩니다.

---

## 🗂️ 문서 구조

### 1️⃣ 프로젝트 관리 문서 (PM)

#### 📌 핵심 문서
| 문서명 | 파일 | 용도 | 대상 |
|--------|------|------|------|
| **프로젝트 브리프** | `pm-project-brief.md` | 프로젝트 전체 개요 및 목표 | 전체 팀 |
| **작업 배분 및 일정** | `pm-task-assignment.md` | 팀별 작업 배분 및 8주 일정 | 전체 팀 |
| **프로젝트 요약** | `PROJECT-SUMMARY.md` | 기술 스택 및 구조 요약 | 전체 팀 |

#### 📋 역할별 작업 지시서
| 문서명 | 파일 | 대상 | 작업 기간 |
|--------|------|------|-----------|
| **웹 기획자 작업 지시서** | `pm-brief-for-web-planner.md` | 웹 기획자 | Week 1-2 |
| **UX 디자이너 작업 지시서** | `pm-brief-for-ux-designer.md` | UX 디자이너 | Week 3-4 |
| **프론트엔드 개발자 작업 지시서** | `pm-brief-for-frontend-dev.md` | 프론트엔드 개발자 | Week 5-8 |

#### 📖 역할별 요구사항 문서 (기존 참고용)
| 문서명 | 파일 | 비고 |
|--------|------|------|
| UX 디자이너 요구사항 | `pm-requirements-for-ux.md` | 상세 요구사항 참고 |
| 프론트엔드 개발자 요구사항 | `pm-requirements-for-frontend.md` | 상세 요구사항 참고 |

---

### 2️⃣ 콘텐츠 및 기획 문서

| 문서명 | 파일 | 용도 | 작성자 |
|--------|------|------|--------|
| **홈페이지 리뉴얼 콘텐츠** | `hopage_renewal_content.md` | 전체 페이지 콘텐츠 요구사항 | PM |
| **웹사이트 리뉴얼 가이드라인** | `website-renewal-guidelines.md` | 디자인/콘텐츠/기술 가이드라인 | PM |

---

### 3️⃣ UX 디자인 산출물

| 문서명 | 파일 | 내용 | 작성 시기 |
|--------|------|------|-----------|
| **UX 디자인 컨셉** | `ux-design-concept.md` | 디자인 철학 및 방향성 | Week 3 |
| **정보 구조** | `ux-information-architecture.md` | 사이트맵 및 IA | Week 3 |
| **와이어프레임** | `ux-wireframes.md` | 주요 페이지 와이어프레임 | Week 3 |
| **디자인 시스템** | `ux-design-system.md` | 컬러, 타이포그래피, 컴포넌트 | Week 4 |

---

### 4️⃣ 개발 문서

| 문서명 | 파일 | 용도 | 대상 |
|--------|------|------|------|
| **프론트엔드 기술 명세** | `frontend-technical-spec.md` | 기술 스택 및 구조 상세 | 프론트엔드 개발자 |
| **개발 가이드** | `DEVELOPMENT.md` | 개발 환경 설정 및 가이드 | 프론트엔드 개발자 |

---

## 🎯 역할별 필독 문서

### 👨‍💼 PM (Product Manager)
1. `pm-project-brief.md` - 프로젝트 전체 개요
2. `pm-task-assignment.md` - 작업 배분 및 일정 관리
3. `hopage_renewal_content.md` - 콘텐츠 요구사항

### 📝 웹 기획자 (Week 1-2)
**필수 문서**
1. `pm-brief-for-web-planner.md` ⭐ **작업 지시서**
2. `hopage_renewal_content.md` - 콘텐츠 요구사항
3. `pm-project-brief.md` - 프로젝트 배경 이해

**참고 문서**
- `website-renewal-guidelines.md` - 가이드라인

**산출물**
- 사이트맵 및 IA
- 콘텐츠 전략
- 기능 명세서

### 🎨 UX 디자이너 (Week 3-4)
**필수 문서**
1. `pm-brief-for-ux-designer.md` ⭐ **작업 지시서**
2. `hopage_renewal_content.md` - 콘텐츠 요구사항
3. 웹 기획자 산출물 (Week 2 말 인계)

**참고 문서**
- `pm-requirements-for-ux.md` - 상세 요구사항
- `website-renewal-guidelines.md` - 디자인 가이드라인
- `ux-design-concept.md` - 디자인 컨셉 참고

**산출물**
- `ux-information-architecture.md` - 정보 구조
- `ux-wireframes.md` - 와이어프레임
- `ux-design-system.md` - 디자인 시스템

### 💻 프론트엔드 개발자 (Week 5-8)
**필수 문서**
1. `pm-brief-for-frontend-dev.md` ⭐ **작업 지시서**
2. `frontend-technical-spec.md` - 기술 명세
3. `DEVELOPMENT.md` - 개발 가이드
4. UX 디자이너 산출물 (Week 4 말 인계)

**참고 문서**
- `pm-requirements-for-frontend.md` - 상세 요구사항
- `PROJECT-SUMMARY.md` - 프로젝트 구조
- `website-renewal-guidelines.md` - 기술 가이드라인

**산출물**
- HTML/CSS/JavaScript 소스 코드
- 배포된 웹사이트

---

## 📅 프로젝트 타임라인

```
Week 1-2: 기획 (웹 기획자)
  └─ 산출물: 사이트맵, IA, 콘텐츠 전략, 기능 명세

Week 3-4: UX 설계 (UX 디자이너)
  └─ 산출물: 와이어프레임, 프로토타입, 디자인 시스템

Week 5-6: HTML/CSS 개발 (프론트엔드 개발자)
  └─ 산출물: 정적 웹사이트 마크업

Week 7: JavaScript 개발 (프론트엔드 개발자)
  └─ 산출물: 완성된 웹사이트

Week 8: 테스트 및 배포 (전체 팀)
  └─ 산출물: 최종 배포
```

---

## 🔄 문서 간 관계도

```
pm-project-brief.md (프로젝트 개요)
    ↓
pm-task-assignment.md (작업 배분)
    ↓
┌───────────────┬───────────────┬───────────────┐
│               │               │               │
Week 1-2        Week 3-4        Week 5-8
웹 기획자        UX 디자이너      프론트엔드 개발자
│               │               │
pm-brief-for-   pm-brief-for-   pm-brief-for-
web-planner     ux-designer     frontend-dev
│               │               │
↓               ↓               ↓
사이트맵/IA      와이어프레임     HTML/CSS/JS
콘텐츠 전략      디자인 시스템    배포
기능 명세
```

---

## 📚 문서 활용 가이드

### 프로젝트 시작 시
1. **전체 팀**: `pm-project-brief.md` 읽고 프로젝트 이해
2. **전체 팀**: `pm-task-assignment.md`로 역할 및 일정 확인
3. **각 역할**: 해당 작업 지시서 (`pm-brief-for-*.md`) 정독

### 작업 진행 시
1. **작업 지시서** 기반으로 작업 수행
2. **참고 문서**에서 상세 정보 확인
3. **이전 단계 산출물** 인계받아 작업 연계

### 문서 업데이트 시
- 주요 변경사항은 해당 문서에 버전 기록
- PM에게 변경 사항 보고
- 관련 팀원에게 업데이트 공유

---

## ⚠️ 중요 사항

### 문서 우선순위
1. **작업 지시서** (`pm-brief-for-*.md`) - 각 역할의 핵심 문서
2. **콘텐츠 요구사항** (`hopage_renewal_content.md`) - 모든 팀 필수
3. **프로젝트 브리프** (`pm-project-brief.md`) - 전체 맥락 이해

### 문서 중복 관리
- **작업 지시서**가 최신 버전이며 우선 적용
- **요구사항 문서**는 상세 참고용
- 충돌 시 PM에게 문의

### 산출물 제출
- 각 역할별 작업 지시서에 명시된 형식으로 제출
- 제출 기한 엄수
- `docs/` 폴더에 산출물 저장

---

## 📞 문의 및 지원

### 문서 관련 문의
- **PM**: 프로젝트 전반, 일정, 의사결정
- **웹 기획자**: 정보 구조, 콘텐츠 전략
- **UX 디자이너**: 디자인, 사용자 경험
- **프론트엔드 개발자**: 기술 구현, 개발

### 커뮤니케이션 채널
- **정기 미팅**: 매주 월요일 오전 10시
- **Slack**: #homepage-renewal
- **긴급 이슈**: PM에게 직접 연락

---

## 📝 문서 버전 관리

| 버전 | 날짜 | 변경 내용 | 작성자 |
|------|------|-----------|--------|
| 1.0 | 2024 | 초기 문서 구조 정리 | PM |

---

**이 문서는 프로젝트 진행 상황에 따라 지속적으로 업데이트됩니다.**
