# Images Directory

## 이미지 가이드

### 필요한 이미지 목록

#### 로고
- `header_logo.png` - 헤더 로고
- `footer_logo.png` - 푸터 로고
- `favicon.ico` - 파비콘

#### 히어로 섹션 (hero/)
- `img01.jpg` - 브랜드 가치 배경 (1920x1080px)
- `img02.jpg` - AI 영상 관제 배경 (1920x1080px)
- `img03.png` - 환경센서 배경 (1920x1080px)
- `img04.jpg` - 고객지원 배경 (1920x1080px)

#### 솔루션 (solutions/)
- 각 솔루션별 배경 이미지 및 구성품 이미지

#### 회사소개 (about/)
- 회사소개, CEO, 연혁, 안전보건 배경 이미지

#### 시공사례 (projects/)
- 프로젝트별 이미지

#### 고객지원 (support/)
- 원격지원 배경 이미지

## 이미지 최적화 가이드

### 포맷
- **사진**: WebP (fallback: JPG)
- **로고/아이콘**: PNG (투명 배경)
- **일러스트**: SVG (가능한 경우)

### 압축
- **품질**: 80-85%
- **도구**: TinyPNG, ImageOptim, Squoosh

### 반응형 이미지
```html
<picture>
  <source media="(min-width: 1366px)" srcset="image-desktop.webp">
  <source media="(min-width: 768px)" srcset="image-tablet.webp">
  <img src="image-mobile.webp" alt="설명">
</picture>
```

### 레이지 로딩
```html
<img src="placeholder.jpg" data-src="actual-image.jpg" loading="lazy" alt="설명">
```

## 이미지 체크리스트

배포 전 확인사항:
- [ ] 모든 이미지 WebP 변환
- [ ] 이미지 압축 (80-85% 품질)
- [ ] alt 속성 추가
- [ ] 반응형 이미지 설정
- [ ] 레이지 로딩 적용
- [ ] 파일명 소문자 + 하이픈
- [ ] 불필요한 메타데이터 제거
