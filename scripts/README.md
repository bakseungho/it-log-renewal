# Scripts Directory

이 디렉토리는 프로젝트 개발 및 유지보수를 위한 Python 스크립트들을 관리합니다.

## 디렉토리 구조

```
scripts/
├── README.md           # 이 파일
├── completed/          # 최근 완료된 스크립트 (재사용 가능)
└── archived/           # 과거에 사용된 스크립트 (참고용)
```

## 폴더 설명

### `completed/`
최근에 실행 완료된 스크립트들이 저장됩니다.
- 재사용 가능성이 있는 스크립트
- 최근 작업 내역 추적용
- 필요시 다시 실행하거나 수정하여 사용 가능

**현재 파일:**
- `update_footer_structure.py` - 푸터 구조를 모든 페이지에 일괄 적용

### `archived/`
과거에 사용되었던 스크립트들이 보관됩니다.
- 일회성으로 실행된 스크립트
- 참고용으로 보관
- 필요시 복사하여 수정 후 재사용 가능

**보관된 스크립트 목록:**
- `add_projects_menu_to_all.py` - GNB에 시공사례 메뉴 추가
- `add_smart_safety_to_gnb.py` - GNB에 스마트 안전 메뉴 추가
- `apply_component_images.py` - 컴포넌트 이미지 적용
- `apply_no_image.py` - no_image 플레이스홀더 적용
- `fix_solution_css.py` - 솔루션 페이지 CSS 수정
- `fix_solution_features_layout.py` - 솔루션 페이지 주요 기능 레이아웃 수정
- `fix_solution_pages.py` - 솔루션 페이지 일괄 수정
- `fix_timeline_markers.py` - 타임라인 마커 수정
- `remove_diagram_caption.py` - 다이어그램 캡션 제거
- `update_all_gnb_menus.py` - 모든 GNB 메뉴 업데이트
- `update_all_templates_gnb.py` - 모든 템플릿 GNB 업데이트
- `update_contact_to_mailto.py` - 문의하기 링크를 mailto로 변경
- `update_cta_sections.py` - CTA 섹션 업데이트
- `update_customer_support_link.py` - 고객지원 링크 수정
- `update_footer_layout.py` - 푸터 레이아웃 업데이트
- `update_gnb_links.py` - GNB 링크 업데이트
- `update_history_months.py` - 연혁 페이지 월 정보 업데이트
- `update_logo_favicon.py` - 로고 및 파비콘 업데이트
- `update_onestop_links.py` - 원스탑 솔루션 링크 업데이트
- `update_subpage_headers.py` - 서브페이지 헤더 업데이트
- `update_template2_template3.py` - template2를 template3로 업데이트

## 사용 방법

### 스크립트 실행
```bash
# 루트 디렉토리에서 실행
python scripts/completed/script_name.py

# 또는 scripts 디렉토리에서 실행
cd scripts/completed
python script_name.py
```

### 새 스크립트 추가
1. 루트 디렉토리에서 스크립트 작성 및 테스트
2. 실행 완료 후 `scripts/completed/`로 이동
3. 더 이상 사용하지 않을 경우 `scripts/archived/`로 이동

### 정리 규칙
- **completed**: 최근 1-2주 내 사용된 스크립트 보관
- **archived**: 오래된 스크립트 또는 일회성 스크립트 보관
- 주기적으로 completed 폴더를 정리하여 archived로 이동

## 주의사항

⚠️ 스크립트 실행 전 반드시:
1. 백업 생성
2. 스크립트 내용 확인
3. 테스트 환경에서 먼저 실행
4. Git으로 변경사항 추적

## 템플릿별 스크립트 위치

일부 템플릿 전용 스크립트는 해당 템플릿 디렉토리에 위치합니다:
- `web/template1/*.py` - template1 전용 스크립트
- `web/template2/*.py` - template2 전용 스크립트
- `web/template3/*.py` - template3 전용 스크립트
