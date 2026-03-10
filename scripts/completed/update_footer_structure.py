#!/usr/bin/env python3
"""
Update footer structure in all template3 HTML files to match the main page
"""

import os
import re
from pathlib import Path

def update_footer_in_file(filepath):
    """Update footer structure in a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if it's the main index.html (already updated)
        if filepath.endswith('web/template3/index.html'):
            print(f"Skipping main page: {filepath}")
            return False
        
        # Check if file has footer
        if '<footer class="footer">' not in content:
            print(f"No footer found in: {filepath}")
            return False
        
        # Pattern to match the old footer-info structure
        old_pattern = r'<div class="footer-info">.*?<img src="[^"]*" alt="아이티로그" class="footer-logo">.*?<p class="footer-company-name">\(주\)아이티로그</p>.*?<div class="footer-policy-links">.*?</div>.*?<div class="footer-details">.*?</div>.*?</div>'
        
        # New footer-info structure
        new_footer_info = '''<div class="footer-info">
          <img src="../images/common/footer_logo.png" alt="아이티로그" class="footer-logo">
          <div class="footer-info-wrapper">
            <div class="footer-policy-links">
              <a href="../terms.html" class="footer-policy-link">이용약관</a>
              <span class="footer-policy-separator">|</span>
              <a href="../privacy.html" class="footer-policy-link">개인정보처리방침</a>
            </div>
            <div class="footer-details">
              <p class="footer-company-name">(주)아이티로그</p>  
              <p><strong>주소:</strong> 서울특별시 구로구 디지털로33길 28 우림이비즈센터 1차 308호 (우:03877)</p>
              <p class="footer-contact-info">
                <span><strong>TEL:</strong> 02-859-2064</span><span>|</span>
                <span><strong>FAX:</strong> 02-859-2065</span><span>|</span>
                <span><strong>이메일:</strong> ok@it-log.co.kr</span></p>
              <p class="footer-copyright">Copyright © 2024 ITLOG. All rights reserved.</p>
            </div>
          </div>
        </div>'''
        
        # Try to find and replace the footer-info section
        # More flexible pattern that captures the entire footer-info div
        pattern = r'<div class="footer-info">.*?</div>\s*</div>\s*\s*<div class="footer-sitemap">'
        
        if re.search(pattern, content, re.DOTALL):
            new_content = re.sub(
                pattern,
                new_footer_info + '\n        \n        <div class="footer-sitemap">',
                content,
                flags=re.DOTALL
            )
            
            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Updated: {filepath}")
            return True
        else:
            print(f"✗ Pattern not found in: {filepath}")
            return False
            
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    """Main function to update all HTML files"""
    template3_dir = Path('web/template3')
    
    if not template3_dir.exists():
        print("Error: web/template3 directory not found")
        return
    
    # Find all HTML files in template3
    html_files = []
    
    # Add subdirectory HTML files
    for subdir in ['about', 'solutions', 'support', 'projects']:
        subdir_path = template3_dir / subdir
        if subdir_path.exists():
            html_files.extend(subdir_path.glob('*.html'))
    
    # Add root level HTML files (except index.html)
    for html_file in template3_dir.glob('*.html'):
        if html_file.name != 'index.html':
            html_files.append(html_file)
    
    print(f"Found {len(html_files)} HTML files to update\n")
    
    updated_count = 0
    for html_file in sorted(html_files):
        if update_footer_in_file(str(html_file)):
            updated_count += 1
    
    print(f"\n{'='*60}")
    print(f"Summary: Updated {updated_count} out of {len(html_files)} files")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
