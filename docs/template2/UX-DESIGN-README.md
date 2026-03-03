# Template2 UX 디자인 문서 총괄

## 프로젝트 개요

**프로젝트명**: (주)아이티로그 홈페이지 리뉴얼 (Template2)  
**디자인 테마**: Trendy & Simple (트렌디하고 심플한)  
**작성일**: 2024  
**작성자**: UX Designer

---

## 디자인 컨셉

### 핵심 키워드
- **Trendy (트렌디)**: 최신 웹 디자인 트렌드 반영
- **Simple (심플)**: 불필요한 요소 제거, 본질에 집중
- **Clean (깔끔)**: 여백을 활용한 시원한 레이아웃
- **Modern (현대적)**: 세련된 타이포그래피와 그래픽
- **Professional (전문적)**: B2B 신뢰감 유지

### 디자인 철학
"Smart Simplicity" - 건설 현장 안전 솔루션의 전문성을 유지하면서도, 현대적이고 깔끔한 미니멀리즘을 추구합니다.

---

## 디자인 시스템 요약

### 컬러 팔레트

**Primary Color (주 색상)**
- Electric Blue: #0066FF
- 용도: 주요 CTA 버튼, 링크, 강조 요소

**Secondary Color (보조 색상)**
- Cyan Accent: #00D9FF
- 용도: 그라데이션, 아이콘, 호버 효과

**Neutral Colors (중립 색상)**
- Dark Navy: #0A1929 (헤더, 푸터, 제목)
- Charcoal: #1E293B (본문 텍스트)
- Medium Gray: #64748B (보조 텍스트)
- Light Gray: #E2E8F0 (배경, 구분선)
- Off White: #F8FAFC (페이지 배경)
- Pure White: #FFFFFF (카드, 주요 배경)

### 타이포그래피

**폰트 패밀리**
- 한글: Pretendard (프리텐다드)
- 영문: Inter
- 스타일: 모던하고 깔끔한 산세리프

**폰트 크기 (데스크톱)**
- H1: 64px (Hero Title)
- H2: 48px (Section Title)
- H3: 32px (Subsection Title)
- H4: 24px (Card Title)
- Body: 16px (일반 본문)

### 스페이싱
- 기본 단위: 8px
- 섹션 간 여백: 80px (데스크톱), 48px (모바일)
- 카드 패딩: 32px

### 그리드 시스템
- 데스크톱: 12 컬럼 (최대 너비 1200px)
- 태블릿: 8 컬럼
- 모바일: 4 컬럼

---

## 주요 컴포넌트

### 버튼
- **Primary Button**: 배경 Electric Blue, 텍스트 White
- **Secondary Button**: 투명 배경, Electric Blue 테두리
- 크기: Large (16px 40px), Medium (14px 32px), Small (10px 24px)

### 카드
- 배경: White
- 테두리 반경: 16px
- 그림자: 0 4px 12px rgba(0,0,0,0.08)
- 호버: 상승 8px, 그림자 증가

### 입력 필드
- 패딩: 14px 16px
- 테두리: 2px solid #E2E8F0
- 포커스: Electric Blue 테두리 + 그림자

---

## 페이지 구조

### 메인 페이지
1. **히어로 섹션** (4개 슬라이드)
   - 슬라이드 1: 브랜드 가치 (슬로건)
   - 슬라이드 2: 핵심 기술 (AI/통합안전)
   - 슬라이드 3: 현장 맞춤 솔루션 (환경센서)
   - 슬라이드 4: 신뢰와 유지보수 (CS)

2. **주요 솔루션 섹션** (4개 카드)
   - 지능형 영상 관제
   - 스마트 환경센서
   - 스마트 출입통제
   - 스마트 현장안전

3. **숫자로 보는 신뢰 섹션**
   - 설치 횟수, 연구 기간, 고객사 수, 프로젝트 완료율

4. **고객사 섹션**
   - 주요 고객사 CI 로고 그리드

5. **시공사례 섹션**
   - 대표 프로젝트 3-4개

### 솔루션 페이지
1. 페이지 헤더 (제목 + 소개)
2. 시스템 개요
3. 시스템 구성도
4. 하위 시스템 (해당 시)
5. 시공사례

### 문의하기 페이지
1. 문의 폼 (이름, 회사명, 연락처, 이메일, 제목, 내용)
2. 개인정보 수집 동의
3. 연락처 정보

---

## 반응형 디자인

### 브레이크포인트
- **모바일**: 320px - 767px
- **태블릿**: 768px - 1023px
- **데스크톱**: 1024px 이상

### 모바일 퍼스트 접근
- 모바일 화면을 기준으로 디자인 시작
- 점진적 향상 (Progressive Enhancement)
- 터치 친화적 인터페이스 (최소 44x44px)

### 레이아웃 변화
- **모바일**: 1열 스택 레이아웃
- **태블릿**: 2열 그리드
- **데스크톱**: 3-4열 그리드

---

## 인터랙션 디자인

### 애니메이션
- **스크롤 애니메이션**: 페이드인 + 슬라이드업
- **호버 효과**: 카드 상승, 버튼 확대, 그림자 증가
- **트랜지션**: 0.3-0.4초, ease-out

### 마이크로 인터랙션
- 버튼 호버: 배경색 변화 + 약간 확대
- 카드 호버: 상승 + 그림자 증가
- 링크 호버: 밑줄 애니메이션

---

## 접근성

### WCAG 2.1 AA 준수
- 색상 대비: 최소 4.5:1
- 키보드 네비게이션 지원
- 스크린 리더 호환
- 명확한 포커스 표시

### 모바일 접근성
- 터치 타겟 최소 44x44px
- 스와이프 제스처 지원
- 반응형 타이포그래피

---

## Template1과의 차별화

| 요소 | Template1 | Template2 |
|------|-----------|-----------|
| **컬러** | 따뜻한 톤 (오렌지, 레드) | 차가운 톤 (블루, 시안) |
| **타이포** | 전통적 고딕 | 모던 기하학 산세리프 |
| **레이아웃** | 대칭적, 안정적 | 비대칭적, 역동적 |
| **여백** | 적당한 여백 | 넉넉한 여백 (미니멀) |
| **이미지** | 사실적 사진 | 일러스트 + 사진 혼합 |
| **애니메이션** | 기본적 | 다이나믹하고 세련됨 |
| **분위기** | 신뢰감, 안정감 | 혁신적, 스마트 |

---

## 산출물 목록

### 완성된 문서
1. **ux-design-concept.md** - 디자인 컨셉 및 무드보드
2. **ux-design-system.md** - 디자인 시스템 (컬러, 타이포, 스페이싱)
3. **ux-wireframes.md** - 와이어프레임 (메인 + 주요 페이지)
4. **ux-ui-components.md** - UI 컴포넌트 가이드
5. **ux-responsive-guide.md** - 반응형 디자인 가이드

### 다음 단계 (개발팀 인계)
- Figma 디자인 파일 제작 (선택)
- 이미지 에셋 준비
- 아이콘 세트 선정
- 프론트엔드 개발 시작

---

## 개발 가이드라인

### 기술 스택
- **HTML5**: 시맨틱 태그 사용
- **CSS3**: Flexbox, Grid, CSS Variables
- **JavaScript**: ES6+
- **라이브러리**: Swiper.js (슬라이더), GSAP (애니메이션)

### CSS Variables 활용
```css
:root {
  --color-primary: #0066FF;
  --color-secondary: #00D9FF;
  --font-size-h1: 4rem;
  --space-xl: 2rem;
}
```

### 반응형 구현
```css
/* Mobile First */
.container {
  padding: 0 16px;
}

@media (min-width: 768px) {
  .container {
    padding: 0 24px;
  }
}

@media (min-width: 1024px) {
  .container {
    max-width: 1200px;
    padding: 0 32px;
  }
}
```

---

## 성공 지표

### UX 지표
- 평균 작업 완료 시간: 3분 이내
- 문의 폼 완료율: 70% 이상
- 이탈률: 35% 이하
- 사용자 만족도: 4.5/5 이상

### 기술 지표
- 페이지 로딩 속도: 2.5초 이내
- Lighthouse 점수: 90점 이상
- 접근성 점수: 95점 이상
- WCAG 2.1 AA 준수

---

## 참고 자료

### 디자인 레퍼런스
- Apple 제품 페이지 (미니멀하고 임팩트 있는 레이아웃)
- Stripe (깔끔한 B2B 웹사이트)
- Linear (모던한 SaaS 디자인)

### 폰트 리소스
- Pretendard: https://github.com/orioncactus/pretendard
- Inter: https://fonts.google.com/specimen/Inter

### 아이콘 라이브러리
- Feather Icons: https://feathericons.com/
- Heroicons: https://heroicons.com/

### 컬러 도구
- Coolors: https://coolors.co/
- Adobe Color: https://color.adobe.com/

---

## 연락처

**UX Designer**
- 문의사항이나 추가 설명이 필요한 경우 PM을 통해 연락 주시기 바랍니다.

**검토 및 승인**
- PM: 전체 디자인 방향성 검토
- 프론트엔드 개발자: 기술적 구현 가능성 검토
- 마케팅팀: 브랜드 아이덴티티 일치성 검토

---

**문서 버전**: 1.0  
**최종 업데이트**: 2024  
**작성자**: UX Designer  
**상태**: 검토 대기

**관련 문서**:
- 프로젝트 브리프 (pm-project-brief.md)
- 요구사항 정의서 (pm-requirements.md)
- 사이트맵 (web-planning-sitemap.md)
- 콘텐츠 전략 (web-planning-content-strategy.md)
- 기능 명세서 (web-planning-functional-spec.md)
