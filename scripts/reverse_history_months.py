#!/usr/bin/env python3
"""
연혁 페이지의 월을 역순(12월→1월)으로 정렬하는 스크립트
"""

import re
from pathlib import Path

def reverse_months_in_timeline(html_content):
    """타임라인 아이템 내의 월을 역순으로 정렬"""
    
    # 각 timeline-item을 찾아서 처리
    def process_timeline_item(match):
        full_item = match.group(0)
        
        # timeline-list 내의 li 항목들을 추출
        li_pattern = r'<li><strong class="timeline-month">(\d{2})</strong>(.*?)</li>'
        li_items = re.findall(li_pattern, full_item, re.DOTALL)
        
        if not li_items:
            return full_item
        
        # 월 기준으로 역순 정렬 (12월 → 1월)
        sorted_items = sorted(li_items, key=lambda x: int(x[0]), reverse=True)
        
        # 정렬된 항목들로 재구성
        new_list = []
        for month, content in sorted_items:
            new_list.append(f'              <li><strong class="timeline-month">{month}</strong>{content}</li>')
        
        # 원본에서 ul 태그 사이의 내용을 교체
        ul_start = full_item.find('<ul class="timeline-list">')
        ul_end = full_item.find('</ul>') + 5
        
        before_ul = full_item[:ul_start]
        after_ul = full_item[ul_end:]
        
        new_ul = '<ul class="timeline-list">\n' + '\n'.join(new_list) + '\n            </ul>'
        
        return before_ul + new_ul + after_ul
    
    # 모든 timeline-item 처리
    pattern = r'<div class="timeline-item[^>]*>.*?</div>\s*</div>'
    result = re.sub(pattern, process_timeline_item, html_content, flags=re.DOTALL)
    
    return result

def main():
    history_file = Path('web/dark/pages/about/history.html')
    
    if not history_file.exists():
        print(f"❌ 파일을 찾을 수 없습니다: {history_file}")
        return
    
    print(f"📖 파일 읽기: {history_file}")
    content = history_file.read_text(encoding='utf-8')
    
    print("🔄 월 역순 정렬 중...")
    updated_content = reverse_months_in_timeline(content)
    
    print(f"💾 파일 저장: {history_file}")
    history_file.write_text(updated_content, encoding='utf-8')
    
    print("✅ 완료! 모든 연도의 월이 역순으로 정렬되었습니다.")

if __name__ == '__main__':
    main()
