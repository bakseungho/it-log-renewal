# 이미지 가이드

## 개요
이 문서는 아이티로그 웹사이트에 필요한 이미지 다운로드 및 최적화 가이드입니다.

## 이미지 디렉토리 구조

```
assets/images/
├── hero/           # Hero 슬라이더 이미지 (4개)
├── clients/        # 고객사 로고 (8개)
├── projects/       # 시공사례 이미지 (3개)
└── logo/          # 로고 파일 (2개)
```

---

## 1. Hero 슬라이더 이미지 (4개)

### 필요한 이미지
| 파일명 | 설명 | 권장 크기 | Unsplash 검색 키워드 |
|--------|------|-----------|---------------------|
| slide-1.jpg | 건설 현장 안전 | 1920x1080px | "construction site safety" |
| slide-2.jpg | CCTV 관제실 | 1920x1080px | "security control room" |
| slide-3.jpg | 스마트 기술 | 1920x1080px | "smart building technology" |
| slide-4.jpg | 엔지니어 지원 | 1920x1080px | "engineer construction site" |

### Unsplash 다운로드 방법
1. [Unsplash](https://unsplash.com/) 접속
2. 검색창에 키워드 입력 (영문)
3. 적합한 이미지 선택
4. "Download free" 버튼 클릭
5. 파일명을 위 표의 파일명으로 변경
6. `assets/images/hero/` 폴더에 저장

### 추천 이미지 URL
```
slide-1.jpg: https://unsplash.com/s/photos/construction-site-safety
slide-2.jpg: https://unsplash.com/s/photos/security-control-room
slide-3.jpg: https://unsplash.com/s/photos/smart-building-technology
slide-4.jpg: https://unsplash.com/s/photos/engineer-construction-site
```

---

## 2. 고객사 로고 (8개)

### 필요한 이미지
| 파일명 | 설명 | 권장 크기 |
|--------|------|-----------|
| client-1.png | 고객사 로고 1 | 150x75px |
| client-2.png | 고객사 로고 2 | 150x75px |
| client-3.png | 고객사 로고 3 | 150x75px |
| client-4.png | 고객사 로고 4 | 150x75px |
| client-5.png | 고객사 로고 5 | 150x75px |
| client-6.png | 고객사 로고 6 | 150x75px |
| client-7.png | 고객사 로고 7 | 150x75px |
| client-8.png | 고객사 로고 8 | 150x75px |

### 임시 플레이스홀더 생성 방법
실제 고객사 로고를 받기 전까지 플레이스홀더 이미지를 사용할 수 있습니다.

**온라인 도구 사용:**
- [Placeholder.com](https://placeholder.com/): `https://via.placeholder.com/150x75/CCCCCC/666666?text=Client+1`
- [Lorem Picsum](https://picsum.photos/): `https://picsum.photos/150/75`

**저장 위치:** `assets/images/clients/`

---

## 3. 시공사례 이미지 (3개)

### 필요한 이미지
| 파일명 | 설명 | 권장 크기 | Unsplash 검색 키워드 |
|--------|------|-----------|---------------------|
| project-1.jpg | AI 영상 관제 프로젝트 | 800x600px | "surveillance control room" |
| project-2.jpg | 환경센서 프로젝트 | 800x600px | "environmental monitoring" |
| project-3.jpg | 출입통제 프로젝트 | 800x600px | "access control system" |

### Unsplash 다운로드 방법
1. [Unsplash](https://unsplash.com/) 접속
2. 검색창에 키워드 입력
3. 적합한 이미지 선택
4. "Download free" 버튼 클릭
5. 파일명을 위 표의 파일명으로 변경
6. `assets/images/projects/` 폴더에 저장

### 추천 이미지 URL
```
project-1.jpg: https://unsplash.com/s/photos/surveillance-control-room
project-2.jpg: https://unsplash.com/s/photos/environmental-monitoring
project-3.jpg: https://unsplash.com/s/photos/access-control-system
```

---

## 4. 로고 파일 (2개)

### 필요한 파일
| 파일명 | 설명 | 형식 | 용도 |
|--------|------|------|------|
| logo.svg | 일반 로고 | SVG | 헤더 (밝은 배경) |
| logo-white.svg | 흰색 로고 | SVG | 푸터 (어두운 배경) |

### 로고 제작 가이드
- **형식:** SVG (벡터 형식 권장)
- **크기:** 가변 (SVG는 크기 조절 가능)
- **색상:**
  - logo.svg: 브랜드 컬러 (#1E40AF 또는 #2563EB)
  - logo-white.svg: 흰색 (#FFFFFF)
- **저장 위치:** `assets/images/logo/`

### 임시 로고 생성
실제 로고가 없는 경우, 텍스트 기반 SVG 로고를 임시로 사용할 수 있습니다.

---

## 이미지 최적화 가이드

### 1. 파일 크기 최적화
이미지 파일 크기를 줄여 웹 성능을 향상시킵니다.

**추천 도구:**
- [TinyPNG](https://tinypng.com/) - PNG/JPG 압축
- [Squoosh](https://squoosh.app/) - 다양한 형식 지원
- [ImageOptim](https://imageoptim.com/) - Mac 전용

**목표 파일 크기:**
- Hero 이미지: 200KB 이하
- 프로젝트 이미지: 100KB 이하
- 로고: 20KB 이하

### 2. 반응형 이미지
다양한 화면 크기에 대응하기 위해 여러 크기의 이미지를 준비합니다.

**Hero 이미지 예시:**
```
slide-1.jpg       (1920x1080px) - 데스크톱
slide-1-md.jpg    (1280x720px)  - 태블릿
slide-1-sm.jpg    (768x432px)   - 모바일
```

### 3. WebP 형식 변환
최신 브라우저를 위해 WebP 형식도 함께 제공합니다.

**변환 도구:**
- [Squoosh](https://squoosh.app/)
- [CloudConvert](https://cloudconvert.com/)

**예시:**
```
slide-1.jpg
slide-1.webp
```

### 4. Lazy Loading
이미지 지연 로딩을 위해 `loading="lazy"` 속성을 사용합니다.

```html
<img src="/assets/images/projects/project-1.jpg" 
     alt="프로젝트 1" 
     loading="lazy">
```

---

## 이미지 파일명 규칙

### 기본 규칙
- 소문자 사용
- 단어 구분은 하이픈(-) 사용
- 공백 사용 금지
- 특수문자 사용 금지

### 예시
✅ 좋은 예:
```
slide-1.jpg
project-ai-surveillance.jpg
client-logo-samsung.png
```

❌ 나쁜 예:
```
Slide 1.jpg
프로젝트_1.jpg
client logo (1).png
```

---

## 이미지 Alt 텍스트 가이드

### 기본 원칙
- 이미지 내용을 명확하게 설명
- 30-125자 권장
- 키워드 자연스럽게 포함
- 장식용 이미지는 빈 alt 사용 (`alt=""`)

### 예시
```html
<!-- 좋은 예 -->
<img src="slide-1.jpg" alt="안전모를 착용한 작업자들이 건설 현장에서 안전 점검을 하는 모습">

<!-- 나쁜 예 -->
<img src="slide-1.jpg" alt="이미지">
<img src="slide-1.jpg" alt="건설 현장 안전 솔루션 스마트 시스템 AI 관제">
```

---

## 체크리스트

### 다운로드 전
- [ ] 필요한 이미지 목록 확인
- [ ] Unsplash 검색 키워드 준비
- [ ] 저장 폴더 구조 확인

### 다운로드 후
- [ ] 파일명 규칙에 맞게 변경
- [ ] 올바른 폴더에 저장
- [ ] 이미지 크기 확인 (권장 크기)
- [ ] 파일 크기 최적화 (압축)

### 웹사이트 적용 전
- [ ] 모든 이미지 경로 확인
- [ ] Alt 텍스트 작성
- [ ] Lazy loading 속성 추가
- [ ] 반응형 테스트 (모바일/태블릿/데스크톱)

---

## 참고 자료

### 무료 이미지 사이트
- [Unsplash](https://unsplash.com/) - 고품질 무료 이미지
- [Pexels](https://www.pexels.com/) - 무료 스톡 사진
- [Pixabay](https://pixabay.com/) - 무료 이미지 및 비디오

### 이미지 최적화 도구
- [TinyPNG](https://tinypng.com/) - PNG/JPG 압축
- [Squoosh](https://squoosh.app/) - 이미지 압축 및 변환
- [ImageOptim](https://imageoptim.com/) - Mac 전용 최적화

### 플레이스홀더 생성
- [Placeholder.com](https://placeholder.com/)
- [Lorem Picsum](https://picsum.photos/)
- [DummyImage](https://dummyimage.com/)

---

## 문의
이미지 관련 문의사항은 프로젝트 관리자에게 연락해주세요.

**작성일:** 2024-01-XX  
**최종 수정일:** 2024-01-XX
