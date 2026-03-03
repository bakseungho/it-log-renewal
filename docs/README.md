# 프로젝트 문서

이 폴더는 프로젝트 관련 문서를 포함합니다.

## 폴더 구조

```
docs/
├── README.md           # 이 파일
└── template1/          # Template1 (아이티로그 홈페이지) 관련 문서
    ├── 기획 문서 (PM)
    ├── 디자인 문서 (UX)
    ├── 개발 문서 (Frontend)
    ├── 테스트 문서
    └── 완료 보고서
```

## Template1 문서 목록

### 📋 기획 문서 (PM)
- `pm-project-brief.md` - 프로젝트 브리프
- `pm-brief-for-web-planner.md` - 웹 기획자용 브리프
- `pm-brief-for-ux-designer.md` - UX 디자이너용 브리프
- `pm-brief-for-frontend-dev.md` - 프론트엔드 개발자용 브리프
- `pm-requirements-for-ux.md` - UX 요구사항
- `pm-requirements-for-frontend.md` - 프론트엔드 요구사항
- `pm-task-assignment.md` - 작업 할당
- `website-renewal-direction.md` - 웹사이트 리뉴얼 방향
- `website-renewal-guidelines.md` - 웹사이트 리뉴얼 가이드라인

### 🎨 디자인 문서 (UX)
- `ux-design-concept.md` - 디자인 컨셉
- `ux-design-system.md` - 디자인 시스템
- `ux-design-handoff.md` - 디자인 핸드오프
- `ux-design-final-summary.md` - 디자인 최종 요약
- `ux-information-architecture.md` - 정보 구조
- `ux-wireframes.md` - 와이어프레임
- `ux-wireframes-updated.md` - 와이어프레임 (업데이트)
- `ux-final-summary.md` - UX 최종 요약

### 🌐 웹 기획 문서
- `web-planning-sitemap.md` - 사이트맵
- `web-planning-content-strategy.md` - 콘텐츠 전략
- `web-planning-functional-spec.md` - 기능 명세
- `web-planning-user-flow.md` - 사용자 플로우
- `web-planning-summary.md` - 웹 기획 요약

### 💻 개발 문서 (Frontend)
- `frontend-technical-spec.md` - 기술 명세서
- `DEVELOPMENT.md` - 개발 가이드
- `IMAGE-GUIDE.md` - 이미지 가이드
- `PLACEHOLDER-IMAGES.md` - 플레이스홀더 이미지 가이드
- `VISUAL-CHECK-GUIDE.md` - 시각적 검증 가이드

### 🧪 테스트 문서
- `TESTING-CHECKLIST.md` - 테스트 체크리스트
- `TEST-RESULTS.md` - 테스트 결과
- `WEEK-3-4-TEST-SUMMARY.md` - Week 3-4 테스트 요약
- `WEEK-7-8-TEST-REPORT.md` - Week 7-8 테스트 보고서

### 📊 완료 보고서
- `WEEK-3-4-COMPLETION-REPORT.md` - Week 3-4 완료 보고서
- `WEEK-3-4-SUMMARY.md` - Week 3-4 요약
- `WEEK-5-6-COMPLETION-REPORT.md` - Week 5-6 완료 보고서
- `WEEK-5-6-SOLUTIONS-COMPLETION.md` - Week 5-6 솔루션 완료
- `WEEK-7-8-PLAN.md` - Week 7-8 계획
- `WEEK-7-8-COMPLETION-REPORT.md` - Week 7-8 완료 보고서
- `FINAL-SUMMARY.md` - 최종 요약

### 📚 프로젝트 관리
- `PROJECT-SUMMARY.md` - 프로젝트 요약
- `DOCUMENT-SUMMARY.md` - 문서 요약
- `DOCUMENT-ORGANIZATION.md` - 문서 구성
- `CONTEXT-TRANSFER-SUMMARY.md` - 컨텍스트 전환 요약
- `QUICK-REFERENCE.md` - 빠른 참조
- `hopage_renewal_content.md` - 홈페이지 리뉴얼 콘텐츠

## 문서 읽는 순서

### 1. 프로젝트 이해하기
1. `PROJECT-SUMMARY.md` - 프로젝트 전체 개요
2. `pm-project-brief.md` - 프로젝트 브리프
3. `QUICK-REFERENCE.md` - 빠른 참조

### 2. 기획 이해하기
1. `web-planning-sitemap.md` - 사이트 구조
2. `web-planning-content-strategy.md` - 콘텐츠 전략
3. `web-planning-functional-spec.md` - 기능 명세

### 3. 디자인 이해하기
1. `ux-design-system.md` - 디자인 시스템
2. `ux-design-handoff.md` - 디자인 핸드오프
3. `ux-wireframes.md` - 와이어프레임

#### 3.1. 디자인 규칙
1. 메인페이지와 서브페이지의 header와 footer는 공통 UI 활용
2. 테마 컬러는 다양한 컬러 활용을 지양, 하나의 포인트 컬러를 기준으로 테마 적용

### 4. 개발하기
1. `frontend-technical-spec.md` - 기술 명세
2. `DEVELOPMENT.md` - 개발 가이드
3. `IMAGE-GUIDE.md` - 이미지 가이드

#### 4.1. 개발 규칙
1. 외부 라이브러리 활용은 CDN 방식 활용
2. 애니메이션 관련 라이브러리는 GSAP로만 활용
3. 이미지 들어가야 하는 공간은 더미 링크로만 적용 ( 이미지만 넣으면 되는 구조로 )
  3.1. 이미지를 적용할 수 있으면 적극 활용

### 5. 테스트하기
1. `TESTING-CHECKLIST.md` - 테스트 체크리스트
2. `TEST-RESULTS.md` - 테스트 결과

### 6. 완료 확인하기
1. `FINAL-SUMMARY.md` - 최종 요약
2. `WEEK-7-8-COMPLETION-REPORT.md` - 최종 완료 보고서

## 문서 작성 규칙

### 파일명 규칙
- 소문자 사용: `project-summary.md`
- 대문자 사용 (중요 문서): `README.md`, `FINAL-SUMMARY.md`
- 하이픈 구분: `web-planning-sitemap.md`
- Week 표기: `WEEK-3-4-COMPLETION-REPORT.md`

### 문서 구조
```markdown
# 문서 제목

## 개요
- 작성일
- 작성자
- 버전

## 내용
...

## 관련 문서
- 링크1
- 링크2
```

## 템플릿 구조

```
docs/
├── README.md
├── template1/    # 아이티로그 홈페이지 (전통적 & 안정적)
├── template2/    # 아이티로그 홈페이지 (트렌디 & 심플)
└── template3/    # 아이티로그 홈페이지 (다크 & 프리미엄)
```

각 템플릿 폴더는 독립적인 문서 세트를 포함합니다.

### Template 비교

| 구분 | Template1 | Template2 | Template3 |
|------|-----------|-----------|-----------|
| **테마** | 전통적 & 안정적 | 트렌디 & 심플 | 다크 & 프리미엄 |
| **컬러** | 따뜻한 톤 (오렌지, 레드) | 차가운 톤 (블루, 시안) | 다크 + 골드/시안 |
| **분위기** | 신뢰감, 안정감 | 혁신적, 스마트 | 고급스러움, 전문성 |
| **타겟** | 보수적 고객 | 젊은 의사결정자 | 프리미엄 고객 |
| **참고** | 일반 기업 사이트 | 최신 트렌드 | https://www.dwce.co.kr/ |

---

**참고**: 모든 문서는 한국어로 작성되어 있습니다.
