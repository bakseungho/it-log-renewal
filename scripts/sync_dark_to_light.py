#!/usr/bin/env python3
"""
다크 테마의 모든 수정사항을 라이트 모드에 동기화
HTML, JS, 이미지 파일을 복사하고 CSS는 제외 (라이트 모드 전용 CSS 유지)
"""

import shutil
from pathlib import Path

def sync_dark_to_light():
    dark_dir = Path('web/dark')
    light_dir = Path('web/light')
    
    if not dark_dir.exists():
        print(f"❌ 다크 폴더를 찾을 수 없습니다: {dark_dir}")
        return
    
    if not light_dir.exists():
        print(f"❌ 라이트 폴더를 찾을 수 없습니다: {light_dir}")
        return
    
    # 복사할 파일 확장자
    copy_extensions = {'.html', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.md'}
    
    # CSS 폴더는 제외 (라이트 모드 전용 CSS 유지)
    exclude_dirs = {'css'}
    
    copied_count = 0
    skipped_count = 0
    
    # 다크 폴더의 모든 파일 순회
    for dark_file in dark_dir.rglob('*'):
        if dark_file.is_file():
            # 상대 경로 계산
            rel_path = dark_file.relative_to(dark_dir)
            
            # CSS 폴더 제외
            if any(part in exclude_dirs for part in rel_path.parts):
                skipped_count += 1
                continue
            
            # 복사할 확장자인지 확인
            if dark_file.suffix.lower() in copy_extensions:
                light_file = light_dir / rel_path
                
                # 디렉토리 생성
                light_file.parent.mkdir(parents=True, exist_ok=True)
                
                # 파일 복사
                shutil.copy2(dark_file, light_file)
                copied_count += 1
                print(f"✅ 복사: {rel_path}")
            else:
                skipped_count += 1
    
    print(f"\n✨ 완료! {copied_count}개 파일 복사, {skipped_count}개 파일 제외")
    print("⚠️  CSS 파일은 복사되지 않았습니다. 라이트 모드 전용 CSS가 유지됩니다.")

if __name__ == '__main__':
    sync_dark_to_light()
