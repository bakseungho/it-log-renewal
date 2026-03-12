#!/usr/bin/env python3
"""
Sync CSS and layout changes from dark theme to light theme
Keep image paths unchanged
"""

import os
import shutil

def sync_css_files():
    """Sync CSS files from dark to light (excluding variables.css)"""
    css_files = [
        'common.css',
        'components.css',
        'header.css',
        'footer.css',
        'pages/home.css',
        'pages/subpage.css',
        'pages/solutions.css'
    ]
    
    synced = []
    
    for css_file in css_files:
        dark_path = f'web/dark/css/{css_file}'
        light_path = f'web/light/css/{css_file}'
        
        if os.path.exists(dark_path):
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(light_path), exist_ok=True)
            
            # Copy file
            shutil.copy2(dark_path, light_path)
            synced.append(css_file)
            print(f"Synced: {css_file}")
        else:
            print(f"Not found: {dark_path}")
    
    return synced

def sync_js_files():
    """Sync JavaScript files from dark to light"""
    js_files = [
        'main.js',
        'utils.js',
        'components.js'
    ]
    
    synced = []
    
    for js_file in js_files:
        dark_path = f'web/dark/js/{js_file}'
        light_path = f'web/light/js/{js_file}'
        
        if os.path.exists(dark_path):
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(light_path), exist_ok=True)
            
            # Copy file
            shutil.copy2(dark_path, light_path)
            synced.append(js_file)
            print(f"Synced: {js_file}")
        else:
            print(f"Not found: {dark_path}")
    
    return synced

def main():
    print("=== Syncing CSS files ===")
    css_synced = sync_css_files()
    
    print("\n=== Syncing JS files ===")
    js_synced = sync_js_files()
    
    print(f"\n=== Summary ===")
    print(f"CSS files synced: {len(css_synced)}")
    print(f"JS files synced: {len(js_synced)}")
    print(f"\nNote: Image paths in HTML files are NOT changed.")
    print(f"Note: variables.css is NOT synced (theme-specific colors).")

if __name__ == '__main__':
    main()
