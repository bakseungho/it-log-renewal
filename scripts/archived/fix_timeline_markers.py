#!/usr/bin/env python3
import re

file_path = 'web/template3/about/history.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 2018부터 2010까지 수정
years = [2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010]
for year in years:
    old = f'        <!-- {year} -->\n        <div class="timeline-item fade-in">\n          <div class="timeline-marker"></div>'
    new = f'        <!-- {year} -->\n        <div class="timeline-item fade-in" id="year-{year}">\n          <div class="timeline-dot"></div>'
    content = content.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('✓ Updated all timeline items')
