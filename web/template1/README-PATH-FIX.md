# Template1 경로 수정 가이드

## 🚀 빠른 시작

Template1의 모든 네비게이션 경로를 자동으로 수정하려면:

```bash
cd web/template1
python3 batch_fix_all_paths.py
```

## 📝 수정 내용

이 스크립트는 다음을 자동으로 수정합니다:

### 1. 절대 경로 → 상대 경로
```html
<!-- 변경 전 -->
href="/about/company.html"
href="/solutions/smart-safety.html"
href="/support/contact.html"
href="/"

<!-- 변경 후 (서브페이지에서) -->
href="company.html"              (같은 폴더)
href="../solutions/smart-safety.html"  (다른 폴더)
href="../support/contact.html"   (다른 폴더)
href="../index.html"             (홈)
```

### 2. 수정 대상 파일

**About 폴더 (5개)**
- company.html
- ceo-message.html
- history.html
- certifications.html
- location.html

**Solutions 폴더 (5개)**
- smart-safety.html
- tower-crane.html
- ai-surveillance.html
- environment-sensor.html
- access-control.html

**Support 폴더 (2개)**
- contact.html
- remote-support.html

**메인 페이지 (4개)**
- index.html
- terms.html
- privacy.html
- 404.html

### 3. 수정 위치

각 파일에서 다음 섹션의 링크를 수정합니다:
- ✅ 헤더 로고
- ✅ Desktop 네비게이션 메뉴
- ✅ Mobile 네비게이션 메뉴
- ✅ Header Actions (문의하기 버튼)
- ✅ Breadcrumb
- ✅ 본문 내 CTA 링크
- ✅ 푸터 로고
- ✅ 푸터 링크

## 🔧 스크립트 설명

### batch_fix_all_paths.py (권장)
가장 최신 버전으로, 모든 경로를 한 번에 수정합니다.

**특징**:
- 폴더별 자동 인식
- 같은 폴더 내 링크는 파일명만 사용
- 다른 폴더 링크는 상대 경로 사용
- 안전한 정규식 패턴 사용

### fix_navigation_paths.py
네비게이션 메뉴 경로만 수정합니다.

### fix_navigation_links.py
기존 링크 수정 스크립트입니다.

## ✅ 실행 결과 예시

```
============================================================
Template1 경로 일괄 수정 시작
============================================================

[about] 폴더 처리 중...
  ✓ ceo-message.html
  ✓ certifications.html
  ✓ company.html
  ✓ history.html
  ✓ location.html

[solutions] 폴더 처리 중...
  ✓ access-control.html
  ✓ ai-surveillance.html
  ✓ environment-sensor.html
  ✓ smart-safety.html
  ✓ tower-crane.html

[support] 폴더 처리 중...
  ✓ contact.html
  ✓ remote-support.html

[메인 페이지] 처리 중...
  ✓ index.html

============================================================
작업 완료: 총 13개 파일 수정
============================================================
```

## 🧪 테스트 방법

수정 후 다음을 확인하세요:

1. **로고 링크**
   - 메인 페이지: 클릭 시 메인 페이지 유지
   - 서브페이지: 클릭 시 템플릿 메인으로 이동

2. **네비게이션 메뉴**
   - About 페이지에서 다른 About 페이지로 이동
   - About 페이지에서 Solutions 페이지로 이동
   - Solutions 페이지에서 Support 페이지로 이동

3. **모바일 메뉴**
   - 모바일 화면에서 메뉴 동작 확인

4. **푸터 링크**
   - 모든 푸터 링크 동작 확인

## ⚠️ 주의사항

1. **백업**
   - 스크립트 실행 전 파일 백업 권장
   - Git을 사용 중이라면 커밋 후 실행

2. **Python 버전**
   - Python 3.6 이상 필요
   - 확인: `python3 --version`

3. **파일 인코딩**
   - UTF-8 인코딩 사용
   - 한글 깨짐 방지

## 🔄 되돌리기

Git을 사용 중이라면:
```bash
git checkout .
```

백업 파일이 있다면:
```bash
cp backup/*.html .
```

## 📞 문제 해결

### 스크립트가 실행되지 않음
```bash
# Python 3 설치 확인
python3 --version

# 실행 권한 부여
chmod +x batch_fix_all_paths.py

# 직접 실행
python3 batch_fix_all_paths.py
```

### 일부 파일만 수정하고 싶음
스크립트를 수정하여 특정 폴더만 처리하도록 변경하거나, 수동으로 수정하세요.

### 수정 결과 확인
```bash
# 절대 경로가 남아있는지 확인
grep -r 'href="/' *.html
grep -r 'href="/' about/*.html
grep -r 'href="/' solutions/*.html
grep -r 'href="/' support/*.html
```

## 📚 추가 문서

- `../NAVIGATION-FIX-COMPLETE-GUIDE.md` - 전체 가이드
- `../NAVIGATION-PATH-FIX-SUMMARY.md` - 수정 요약
- `LINK_FIX_SUMMARY.md` - 이전 링크 수정 내역

---

**작성일**: 2024년  
**버전**: 1.0  
**상태**: 준비 완료
