# Images Directory

## 이미지 가이드

### 필요한 이미지 목록

#### 로고
- `logo-white.png` - 화이트 로고 (헤더, 푸터용)
- `favicon.png` - 파비콘 (32x32px)

#### 히어로 섹션 (hero/)
- `hero-1.jpg` - 브랜드 가치 배경 (1920x1080px)
- `hero-2.jpg` - AI 영상 관제 배경 (1920x1080px)
- `hero-3.jpg` - 환경센서 배경 (1920x1080px)
- `hero-4.jpg` - 고객지원 배경 (1920x1080px)

#### 고객사 로고 (clients/)
- `client-1.png` - 삼성물산 (200x80px)
- `client-2.png` - 현대건설 (200x80px)
- `client-3.png` - GS건설 (200x80px)
- `client-4.png` - 대림산업 (200x80px)
- `client-5.png` - 포스코건설 (200x80px)
- `client-6.png` - LH공사 (200x80px)
- `client-7.png` - SH공사 (200x80px)
- `client-8.png` - 롯데건설 (200x80px)
- `client-9.png` - 대우건설 (200x80px)
- `client-10.png` - SK건설 (200x80px)

#### 프로젝트 (projects/)
- `project-1.jpg` - 재개발 프로젝트 (800x600px)
- `project-2.jpg` - 건설 현장 (800x600px)
- `project-3.jpg` - 시티 프로젝트 (800x600px)

#### 솔루션 (solutions/)
- `smart-safety.jpg` - 스마트 현장안전 (1920x1080px)
- `tower-crane.jpg` - 타워크레인 (1920x1080px)
- `ai-surveillance.jpg` - AI 영상 관제 (1920x1080px)
- `environment-sensor.jpg` - 환경센서 (1920x1080px)
- `access-control.jpg` - 출입통제 (1920x1080px)
- `diagram-smart-safety.png` - 시스템 구성도 (1200x800px)
- `diagram-tower-crane.png` - 시스템 구성도 (1200x800px)
- `diagram-ai-surveillance.png` - 시스템 구성도 (1200x800px)
- `diagram-environment-sensor.png` - 시스템 구성도 (1200x800px)
- `diagram-access-control.png` - 시스템 구성도 (1200x800px)

#### 회사소개 (about/)
- `company-header.jpg` - 회사소개 헤더 (1920x1080px)
- `ceo-photo.jpg` - CEO 사진 (400x500px)
- `ceo-signature.png` - CEO 서명 (200x80px)
- `location-map.jpg` - 오시는 길 (1200x800px)
- `cert-1.jpg` - 인증서 1 (600x800px)
- `cert-2.jpg` - 인증서 2 (600x800px)
- `cert-3.jpg` - 인증서 3 (600x800px)
- `cert-4.jpg` - 특허 1 (600x800px)
- `cert-5.jpg` - 특허 2 (600x800px)

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

## 다크 모드 이미지 가이드

### 배경 이미지
- 어두운 톤 선호
- 오버레이 적용 (rgba(10, 10, 10, 0.7))
- 텍스트 가독성 확보

### 로고
- 화이트 버전 사용
- 투명 배경 PNG
- 최소 크기: 200x60px

### 고객사 로고
- 그레이스케일 처리
- 또는 화이트 버전
- 호버 시 컬러 복원

## Placeholder 이미지

개발 중에는 다음 서비스를 사용할 수 있습니다:

- **Unsplash**: https://source.unsplash.com/1920x1080/?construction
- **Placeholder**: https://via.placeholder.com/1920x1080/0a0a0a/ffffff?text=Hero+Image
- **Lorem Picsum**: https://picsum.photos/1920/1080

## 이미지 체크리스트

배포 전 확인사항:
- [ ] 모든 이미지 WebP 변환
- [ ] 이미지 압축 (80-85% 품질)
- [ ] alt 속성 추가
- [ ] 반응형 이미지 설정
- [ ] 레이지 로딩 적용
- [ ] 다크 모드 적합성 확인
- [ ] 파일명 소문자 + 하이픈
- [ ] 불필요한 메타데이터 제거
