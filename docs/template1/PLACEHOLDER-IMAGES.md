# 플레이스홀더 이미지 가이드

## 개요
실제 이미지를 다운로드하기 전까지 사용할 임시 플레이스홀더 이미지 정보입니다.

## 온라인 플레이스홀더 서비스 사용

### 1. Hero 슬라이더 이미지 (1920x1080)
```
https://via.placeholder.com/1920x1080/2563EB/FFFFFF?text=Slide+1
https://via.placeholder.com/1920x1080/1E40AF/FFFFFF?text=Slide+2
https://via.placeholder.com/1920x1080/3B82F6/FFFFFF?text=Slide+3
https://via.placeholder.com/1920x1080/60A5FA/FFFFFF?text=Slide+4
```

### 2. 고객사 로고 (150x75)
```
https://via.placeholder.com/150x75/CCCCCC/666666?text=Client+1
https://via.placeholder.com/150x75/CCCCCC/666666?text=Client+2
https://via.placeholder.com/150x75/CCCCCC/666666?text=Client+3
https://via.placeholder.com/150x75/CCCCCC/666666?text=Client+4
https://via.placeholder.com/150x75/CCCCCC/666666?text=Client+5
https://via.placeholder.com/150x75/CCCCCC/666666?text=Client+6
https://via.placeholder.com/150x75/CCCCCC/666666?text=Client+7
https://via.placeholder.com/150x75/CCCCCC/666666?text=Client+8
```

### 3. 시공사례 이미지 (800x600)
```
https://via.placeholder.com/800x600/2563EB/FFFFFF?text=Project+1
https://via.placeholder.com/800x600/1E40AF/FFFFFF?text=Project+2
https://via.placeholder.com/800x600/3B82F6/FFFFFF?text=Project+3
```

## 실제 이미지로 교체하기

### 단계별 가이드
1. IMAGE-GUIDE.md 참고하여 Unsplash에서 이미지 다운로드
2. 파일명을 규칙에 맞게 변경
3. 이미지 최적화 (TinyPNG 등 사용)
4. 해당 폴더에 저장
5. index.html의 이미지 경로 확인

### 우선순위
1. **높음:** Hero 슬라이더 이미지 (첫 화면)
2. **중간:** 시공사례 이미지
3. **낮음:** 고객사 로고 (실제 로고 필요)

## 참고사항
- 플레이스홀더 이미지는 개발/테스트 용도로만 사용
- 실제 배포 전 반드시 실제 이미지로 교체 필요
- 로고는 실제 회사 로고 파일 필요
