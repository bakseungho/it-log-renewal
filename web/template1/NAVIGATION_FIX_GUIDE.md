# Navigation Links Fix Guide for Template1

## Problem
All HTML files in template1 are using absolute paths (starting with `/`) for internal navigation links. This causes 404 errors when clicking links because the files are not deployed at the root of a web server.

## Solution
Convert all absolute paths to relative paths based on each file's location in the folder structure.

## Files Fixed
✅ index.html - All links converted to relative paths
✅ about/history.html - All links converted to relative paths

## Files Remaining to Fix

### Root Level Files
- terms.html
- privacy.html
- 404.html

**Pattern for root level files:**
- Home link: `href="index.html"` (instead of `href="/"`)
- About links: `href="about/company.html"` (instead of `href="/about/company.html"`)
- Solutions links: `href="solutions/smart-safety.html"` (instead of `href="/solutions/smart-safety.html"`)
- Support links: `href="support/contact.html"` (instead of `href="/support/contact.html"`)

### About Folder Files
- about/company.html
- about/ceo-message.html
- about/certifications.html
- about/location.html

**Pattern for about/ folder files:**
- Home link: `href="../index.html"` (instead of `href="/"`)
- Same folder links: `href="company.html"` (instead of `href="/about/company.html"`)
- Solutions links: `href="../solutions/smart-safety.html"` (instead of `href="/solutions/smart-safety.html"`)
- Support links: `href="../support/contact.html"` (instead of `href="/support/contact.html"`)

### Solutions Folder Files
- solutions/smart-safety.html
- solutions/tower-crane.html
- solutions/ai-surveillance.html
- solutions/environment-sensor.html
- solutions/access-control.html

**Pattern for solutions/ folder files:**
- Home link: `href="../index.html"` (instead of `href="/"`)
- Same folder links: `href="smart-safety.html"` (instead of `href="/solutions/smart-safety.html"`)
- About links: `href="../about/company.html"` (instead of `href="/about/company.html"`)
- Support links: `href="../support/contact.html"` (instead of `href="/support/contact.html"`)

### Support Folder Files
- support/contact.html
- support/remote-support.html

**Pattern for support/ folder files:**
- Home link: `href="../index.html"` (instead of `href="/"`)
- Same folder links: `href="contact.html"` (instead of `href="/support/contact.html"`)
- About links: `href="../about/company.html"` (instead of `href="/about/company.html"`)
- Solutions links: `href="../solutions/smart-safety.html"` (instead of `href="/solutions/smart-safety.html"`)

## Link Types to Fix in Each File

1. **Header Logo Link** - Links to home page
2. **Desktop Navigation Menu** - All dropdown menu links
3. **Mobile Navigation Menu** - All mobile submenu links
4. **Header Actions** - "문의하기" button
5. **Breadcrumb Navigation** - All breadcrumb links
6. **Content Links** - All links in main content area (CTAs, buttons, etc.)
7. **Footer Logo Link** - Links to home page
8. **Footer Navigation Links** - All footer menu links

## Testing
After fixing all files, test by:
1. Opening index.html in a browser (file:// protocol)
2. Click through all navigation links
3. Verify all pages load correctly
4. Test mobile menu navigation
5. Test footer links
6. Test breadcrumb navigation

## Status
- ✅ index.html - Complete
- ✅ about/history.html - Complete
- ⏳ Remaining files - In progress
