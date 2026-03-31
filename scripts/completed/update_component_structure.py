#!/usr/bin/env python3
"""
솔루션 페이지의 구성품 섹션 HTML 구조를 수정하는 스크립트
img 태그를 figure 태그로 감싸기
"""

import os
import re

def update_component_structure(file_path):
    """파일의 구성품 섹션 HTML 구조 수정"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # component-item 내부의 img 태그를 figure로 감싸기
        # <div class="component-item">
        #   <img src="..." alt="..." class="component-image">
        #   <p class="component-name">...</p>
        # </div>
        # 를
        # <div class="component-item">
        #   <figure>
        #     <img src="..." alt="..." class="component-image">
        #   </figure>
        #   <p class="component-name">...</p>
        # </div>
        # 로 변경
        
        pattern = r'(<div class="component-item">)\s*(<img[^>]*class="component-image"[^>]*>)\s*(<p class="component-name">)'
        
        def replace_func(match):
            return f'{match.group(1)}\n            <figure>\n              {match.group(2)}\n            </figure>\n            {match.group(3)}'
        
        new_content = re.sub(pattern, replace_func, content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        else:
            return False
            
    except Exception as e:
        print(f"  ❌ 오류 발생: {file_path} - {str(e)}")
        return False

def main():
    """메인 함수"""
    # 다크 모드와 라이트 모드의 솔루션 페이지들
    solution_files = [
        'web/dark/pages/solutions/ai-surveillance.html',
        'web/dark/pages/solutions/smart-safety.html',
        'web/dark/pages/solutions/tower-crane.html',
        'web/dark/pages/solutions/access-control.html',
        'web/dark/pages/solutions/environment-sensor.html',
        'web/light/pages/solutions/ai-surveillance.html',
        'web/light/pages/solutions/smart-safety.html',
        'web/light/pages/solutions/tower-crane.html',
        'web/light/pages/solutions/access-control.html',
        'web/light/pages/solutions/environment-sensor.html',
    ]
    
    print(f"🔍 {len(solution_files)}개의 솔루션 페이지 처리\n")
    
    updated_count = 0
    for file_path in solution_files:
        if os.path.exists(file_path):
            print(f"📝 처리 중: {file_path}")
            if update_component_structure(file_path):
                updated_count += 1
                print(f"  ✅ 구조 수정 완료")
            else:
                print(f"  ⚠️  변경 사항 없음")
        else:
            print(f"  ⚠️  파일 없음: {file_path}")
        print()
    
    print(f"\n{'='*60}")
    print(f"✨ 완료: {updated_count}/{len(solution_files)}개 파일 업데이트")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
