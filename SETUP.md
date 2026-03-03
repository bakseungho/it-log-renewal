# 프로젝트 설정 가이드

이 문서는 프로젝트를 처음 시작하는 개발자를 위한 빠른 설정 가이드입니다.

## 빠른 시작 (5분)

### 1단계: jQuery 다운로드

jQuery는 프로젝트에 포함되어 있지 않으므로 직접 다운로드해야 합니다.

```bash
# 방법 1: 수동 다운로드
1. https://jquery.com/download/ 방문
2. "Download the compressed, production jQuery 3.x.x" 클릭
3. 다운로드한 파일을 assets/js/vendor/jquery.min.js로 저장

# 방법 2: CDN 사용 (index.html 수정)
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
```

### 2단계: 로컬 서버 실행

정적 파일을 제공하기 위해 로컬 서버가 필요합니다.

```bash
# web/template1 폴더로 이동
cd web/template1

# 방법 1: Python (Python이 설치되어 있는 경우)
python -m http.server 8000
# 브라우저에서 http://localhost:8000 열기

# 방법 2: Node.js http-server
npx http-server
# 브라우저에서 http://localhost:8080 열기

# 방법 3: VS Code Live Server 확장
1. VS Code에서 "Live Server" 확장 설치
2. web/template1/index.html 파일에서 우클릭
3. "Open with Live Server" 선택
```

### 3단계: 브라우저에서 확인

로컬 서버 주소로 접속하여 웹사이트가 정상적으로 표시되는지 확인합니다.

```
✓ 헤더와 네비게이션이 표시됨
✓ 히어로 섹션이 표시됨
✓ 모바일 메뉴 버튼이 작동함
✓ 스무스 스크롤이 작동함
```

## 상세 설정

### 개발 환경 구성

#### VS Code 설정

1. **권장 확장 설치**
   ```
   - Live Server
   - HTML CSS Support
   - IntelliSense for CSS
   - Prettier - Code formatter
   - Path Intellisense
   ```

2. **설정 파일 (.vscode/settings.json)**
   ```json
   {
     "editor.formatOnSave": true,
     "editor.defaultFormatter": "esbenp.prettier-vscode",
     "files.associations": {
       "*.css": "css",
       "*.js": "javascript"
     }
   }
   ```

#### Git 설정

```bash
# 저장소 초기화
git init

# 첫 커밋
git add .
git commit -m "Initial commit: Project setup"

# 원격 저장소 연결 (선택사항)
git remote add origin https://github.com/username/repository.git
git push -u origin main
```

### 콘텐츠 커스터마이징

#### 1. 브랜드 컬러 변경

`web/template1/assets/css/variables.css` 파일을 열고 컬러 변수를 수정합니다:

```css
:root {
  --color-primary: #2563eb;        /* 메인 컬러 */
  --color-primary-dark: #1e40af;   /* 어두운 메인 컬러 */
  --color-primary-light: #3b82f6;  /* 밝은 메인 컬러 */
}
```

#### 2. 로고 및 이미지 추가

```bash
# 로고 파일 추가
web/template1/assets/images/logo/logo.svg
web/template1/assets/images/logo/logo-white.svg

# 파비콘 추가
web/template1/assets/images/favicon.png

# 콘텐츠 이미지 추가
web/template1/assets/images/content/portfolio-1.jpg
web/template1/assets/images/content/portfolio-2.jpg
web/template1/assets/images/content/portfolio-3.jpg

# 아이콘 추가
web/template1/assets/images/icons/service-1.svg
web/template1/assets/images/icons/service-2.svg
web/template1/assets/images/icons/service-3.svg
```

#### 3. 메타 정보 업데이트

`web/template1/index.html` 파일의 메타 태그를 수정합니다:

```html
<title>실제 사이트 제목 - 회사명</title>
<meta name="description" content="실제 사이트 설명 (160자 이내)">
<meta property="og:title" content="실제 사이트 제목">
<meta property="og:description" content="실제 사이트 설명">
<meta property="og:image" content="실제 이미지 URL">
<meta property="og:url" content="실제 사이트 URL">
```

#### 4. 사이트맵 업데이트

`web/template1/sitemap.xml` 파일을 수정합니다:

```xml
<url>
  <loc>https://실제도메인.com/</loc>
  <lastmod>2024-01-01</lastmod>
  <changefreq>daily</changefreq>
  <priority>1.0</priority>
</url>
```

### 추가 페이지 생성

새 페이지를 추가하려면:

```bash
# 1. pages 폴더에 HTML 파일 생성
web/template1/pages/about.html

# 2. index.html을 템플릿으로 복사
cp web/template1/index.html web/template1/pages/about.html

# 3. 페이지 내용 수정
# 4. 네비게이션 링크 업데이트
```

## 문제 해결

### jQuery가 로드되지 않음

**증상**: 콘솔에 "$ is not defined" 에러

**해결**:
1. `web/template1/assets/js/vendor/jquery.min.js` 파일이 존재하는지 확인
2. index.html에서 jQuery 스크립트 태그가 다른 스크립트보다 먼저 로드되는지 확인

### 이미지가 표시되지 않음

**증상**: 이미지 위치에 깨진 이미지 아이콘

**해결**:
1. 이미지 파일 경로 확인 (절대 경로 사용: `/assets/images/...`)
2. 이미지 파일이 실제로 존재하는지 확인
3. 파일명 대소문자 확인 (Linux/Mac은 대소문자 구분)

### CSS가 적용되지 않음

**증상**: 스타일이 없는 기본 HTML만 표시

**해결**:
1. CSS 파일 경로 확인
2. 브라우저 캐시 삭제 (Ctrl+Shift+R 또는 Cmd+Shift+R)
3. 개발자 도구 Network 탭에서 CSS 파일 로드 확인

### 모바일 메뉴가 작동하지 않음

**증상**: 메뉴 버튼 클릭 시 반응 없음

**해결**:
1. jQuery가 정상적으로 로드되었는지 확인
2. 콘솔에 JavaScript 에러가 있는지 확인
3. `js-menu-toggle` 클래스가 버튼에 있는지 확인

## 다음 단계

설정이 완료되면:

1. [개발 가이드](docs/DEVELOPMENT.md) 읽기
2. [기술 명세서](docs/frontend-technical-spec.md) 검토
3. 실제 콘텐츠로 교체 시작
4. 디자인 커스터마이징
5. 추가 페이지 개발

## 도움이 필요하신가요?

- 📧 이메일: dev@example.com
- 📚 문서: [README.md](README.md)
- 🔧 개발 가이드: [DEVELOPMENT.md](docs/DEVELOPMENT.md)
- 📋 기술 명세: [frontend-technical-spec.md](docs/frontend-technical-spec.md)
