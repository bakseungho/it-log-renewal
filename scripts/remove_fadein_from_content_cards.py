#!/usr/bin/env python3
"""
모든 서브페이지의 content-card에서 fade-in 클래스를 제거합니다.
GSAP initSubpageScrollAnimations()에서 .content-card를 직접 처리하므로
CSS .fade-in.will-animate와 충돌하는 문제를 해결합니다.
"""
import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    # "content-card fade-in" -> "content-card"
    content = content.replace('content-card fade-in', 'content-card')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count = original.count('content-card fade-in')
        print(f"  Updated: {filepath} ({count} replacements)")
        return count
    return 0

total = 0
for root, dirs, files in os.walk('web'):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            total += process_file(filepath)

print(f"\nDone. Total replacements: {total}")
