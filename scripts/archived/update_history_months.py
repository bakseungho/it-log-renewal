#!/usr/bin/env python3
"""
연혁 페이지의 월(月) 부분을 "01" 포맷으로 변경하는 스크립트
"""

import re

def update_history_months(file_path):
    """연혁 항목의 월 부분을 "01" 포맷으로 변경 (대시 제거)"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 패턴: <li><strong class="timeline-month">02 -</strong> 내용
    # -> <li><strong class="timeline-month">02</strong> 내용
    pattern = r'<strong class="timeline-month">(\d{2}) -</strong>\s*'
    replacement = r'<strong class="timeline-month">\1</strong> '
    
    content = re.sub(pattern, replacement, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated: {file_path}")

if __name__ == '__main__':
    history_file = 'web/template3/about/history.html'
    update_history_months(history_file)
    print("\n완료: 연혁 페이지의 대시(-)가 제거되었습니다.")
