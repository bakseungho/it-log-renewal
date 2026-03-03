/**
 * (주)아이티로그 홈페이지 리뉴얼 - Main Script
 * 메인 초기화 및 전역 이벤트 핸들러
 */
'use strict';

// ========== DOM Content Loaded ==========
document.addEventListener('DOMContentLoaded', function() {
  
  // Initialize all components
  initializeComponents();
  
  // Initialize lazy loading
  Utils.lazyLoadImages();
  
  // Initialize smooth scroll
  initializeSmoothScroll();
  
  // Initialize external links
  initializeExternalLinks();
  
  // Initialize animations
  initializeAnimations();
  
  console.log('ITLOG Website initialized');
});

// ========== Initialize Components ==========
function initializeComponents() {
  MobileMenu.init();
  ScrollHeader.init();
  BackToTop.init();
  SmoothScrollLinks.init();
  FormValidation.init();
  Tabs.init();
  Accordion.init();
  Modal.init();
}

// ========== Smooth Scroll ==========
function initializeSmoothScroll() {
  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      
      // Skip if href is just # or #!
      if (href === '#' || href === '#!') return;
      
      e.preventDefault();
      
      const target = document.querySelector(href);
      if (!target) return;
      
      const headerHeight = document.querySelector('.header')?.offsetHeight || 0;
      const targetPosition = target.offsetTop - headerHeight;
      
      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    });
  });
}

// ========== External Links ==========
function initializeExternalLinks() {
  // Open external links in new tab
  const hostname = window.location.hostname;
  
  document.querySelectorAll('a[href^="http"]').forEach(link => {
    const linkHostname = new URL(link.href).hostname;
    
    if (linkHostname !== hostname) {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer');
    }
  });
}

// ========== Scroll Animations ==========
function initializeAnimations() {
  // Intersection Observer for scroll animations
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  // Observe all sections
  document.querySelectorAll('.section').forEach(section => {
    observer.observe(section);
  });
  
  // Observe solution cards
  document.querySelectorAll('.solution-card').forEach(card => {
    observer.observe(card);
  });
  
  // Observe project cards
  document.querySelectorAll('.project-card').forEach(card => {
    observer.observe(card);
  });
}

// ========== Window Load ==========
window.addEventListener('load', function() {
  // Remove loading class if exists
  document.body.classList.remove('loading');
  
  // Initialize any components that need full page load
  console.log('Page fully loaded');
});

// ========== Window Resize ==========
let resizeTimer;
window.addEventListener('resize', function() {
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(function() {
    // Handle resize events
    console.log('Window resized');
  }, 250);
});

// ========== Service Worker Registration (Optional) ==========
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    // Uncomment to enable service worker
    // navigator.serviceWorker.register('/sw.js')
    //   .then(registration => console.log('SW registered:', registration))
    //   .catch(error => console.log('SW registration failed:', error));
  });
}

// ========== Error Handling ==========
window.addEventListener('error', function(e) {
  console.error('Global error:', e.error);
  // Add error reporting service here if needed
});

// ========== Unhandled Promise Rejection ==========
window.addEventListener('unhandledrejection', function(e) {
  console.error('Unhandled promise rejection:', e.reason);
  // Add error reporting service here if needed
});
