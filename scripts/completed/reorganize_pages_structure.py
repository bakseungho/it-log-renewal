#!/usr/bin/env python3
"""
Reorganize pages structure: Move subpage folders into pages/ directory
and update all paths accordingly
"""

import os
import re
import shutil
from pathlib import Path

def create_pages_structure(template_dir):
    """Create pages directory and move subpage folders"""
    template_path = Path(template_dir)
    pages_dir = template_path / 'pages'
    
    # Create pages directory
    pages_dir.mkdir(exist_ok=True)
    
    # Folders to move into pages/
    subpage_folders = ['about', 'solutions', 'support', 'projects']
    
    for folder in subpage_folders:
        src = template_path / folder
        dst = pages_dir / folder
        
        if src.exists() and src.is_dir():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.move(str(src), str(dst))
            print(f"✓ Moved {folder}/ to pages/{folder}/")
    
    return pages_dir

def update_html_paths(file_path, depth_from_root):
    """Update paths in HTML file based on new structure"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Determine path prefix based on depth
        if depth_from_root == 0:  # Root level (index.html)
            # No changes needed for root index.html
            return False
        elif depth_from_root == 1:  # pages/about/, pages/solutions/, etc.
            # Update relative paths
            # CSS: css/ -> ../../css/
            content = re.sub(r'href="(\.\./)?css/', r'href="../../css/', content)
            # JS: js/ -> ../../js/
            content = re.sub(r'src="(\.\./)?js/', r'src="../../js/', content)
            # Images: images/ -> ../../images/
            content = re.sub(r'(src|href)="(\.\./)?images/', r'\1="../../images/', content)
            
            # Update navigation links
            # about/ -> ../about/
            content = re.sub(r'href="about/', r'href="../about/', content)
            # solutions/ -> ../solutions/
            content = re.sub(r'href="solutions/', r'href="../solutions/', content)
            # support/ -> ../support/
            content = re.sub(r'href="support/', r'href="../support/', content)
            # projects/ -> ../projects/
            content = re.sub(r'href="projects/', r'href="../projects/', content)
            
            # Update root links (index.html, terms.html, privacy.html)
            content = re.sub(r'href="index\.html"', r'href="../../index.html"', content)
            content = re.sub(r'href="terms\.html"', r'href="../../terms.html"', content)
            content = re.sub(r'href="privacy\.html"', r'href="../../privacy.html"', content)
            
            # Update mailto links (keep as is)
            # Already correct
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"✗ Error updating {file_path}: {e}")
        return False

def update_root_html_files(template_dir):
    """Update root level HTML files (index.html, terms.html, privacy.html)"""
    template_path = Path(template_dir)
    root_files = ['index.html', 'terms.html', 'privacy.html', '404.html']
    
    updated_count = 0
    for filename in root_files:
        file_path = template_path / filename
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Update navigation links to pages/
                content = re.sub(r'href="about/', r'href="pages/about/', content)
                content = re.sub(r'href="solutions/', r'href="pages/solutions/', content)
                content = re.sub(r'href="support/', r'href="pages/support/', content)
                content = re.sub(r'href="projects/', r'href="pages/projects/', content)
                
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"✓ Updated {filename}")
                    updated_count += 1
                    
            except Exception as e:
                print(f"✗ Error updating {filename}: {e}")
    
    return updated_count

def process_template(template_name):
    """Process a single template directory"""
    template_dir = f'web/{template_name}'
    
    if not os.path.exists(template_dir):
        print(f"✗ Template directory not found: {template_dir}")
        return
    
    print(f"\n{'='*60}")
    print(f"Processing {template_name.upper()} template")
    print(f"{'='*60}\n")
    
    # Step 1: Create pages structure and move folders
    print("Step 1: Reorganizing folder structure...")
    pages_dir = create_pages_structure(template_dir)
    
    # Step 2: Update root HTML files
    print("\nStep 2: Updating root HTML files...")
    root_updated = update_root_html_files(template_dir)
    print(f"Updated {root_updated} root HTML files")
    
    # Step 3: Update all HTML files in pages/
    print("\nStep 3: Updating HTML files in pages/...")
    updated_count = 0
    
    for subdir in ['about', 'solutions', 'support', 'projects']:
        subdir_path = pages_dir / subdir
        if subdir_path.exists():
            for html_file in subdir_path.glob('*.html'):
                if update_html_paths(html_file, depth_from_root=1):
                    updated_count += 1
                    print(f"✓ Updated {html_file.relative_to(template_dir)}")
    
    print(f"\nTotal updated: {updated_count} subpage HTML files")

def main():
    """Main function"""
    print("Reorganizing pages structure for light and dark templates\n")
    
    # Process both templates
    for template in ['light', 'dark']:
        process_template(template)
    
    print(f"\n{'='*60}")
    print("Reorganization complete!")
    print(f"{'='*60}")
    print("\nNew structure:")
    print("web/light/")
    print("  ├── pages/")
    print("  │   ├── about/")
    print("  │   ├── solutions/")
    print("  │   ├── support/")
    print("  │   └── projects/")
    print("  ├── css/")
    print("  ├── js/")
    print("  ├── images/")
    print("  └── index.html")

if __name__ == '__main__':
    main()
