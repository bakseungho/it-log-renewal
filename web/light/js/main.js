// Main JavaScript - Template3 with GSAP

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  // GSAP Configuration
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);
    
    // Mark elements for animation
    document.querySelectorAll('.fade-in, .scale-in').forEach(el => {
      el.classList.add('will-animate');
    });
  } else {
    // Fallback: ensure all elements are visible
    console.warn('GSAP not loaded, animations disabled');
    document.querySelectorAll('.fade-in, .scale-in').forEach(el => {
      el.style.opacity = '1';
      el.style.transform = 'none';
    });
  }
  
  initHeaderScroll();
  initHeroSlider();
  initScrollAnimations();
  initCounterAnimations();
  initParallax();
  initTopButton();
  
  // 페이지 로드 완료 시 fade-in
  document.body.classList.add('page-loaded');

  // 이용약관, 개인정보처리방침 페이지에서는 헤더 애니메이션 제거
  const pagePath = window.location.pathname;
  if (pagePath.includes('terms.html') || pagePath.includes('privacy.html')) {
    document.querySelectorAll('.page-header-breadcrumb, .page-header-title, .page-header-image').forEach(el => {
      el.style.opacity = '1';
      el.style.transform = 'none';
      el.style.animation = 'none';
    });
  }
});

// Header Scroll Effect
function initHeaderScroll() {
  const header = document.querySelector('.header');
  if (!header) return;
  
  // 메인 페이지인지 확인 (body에 home-page 클래스가 있는지 체크)
  const isHomePage = document.body.classList.contains('home-page');
  
  // 로고 SVG path 요소들 가져오기
  const logoSvg = header.querySelector('.header-logo-link svg');
  const logoPaths = logoSvg ? logoSvg.querySelectorAll('path') : [];
  
  // 로고 색상 변경 함수 (메인 페이지에서만 작동)
  function updateLogoColor(isScrolled) {
    if (!isHomePage || logoPaths.length === 0) return;
    
    logoPaths.forEach(path => {
      const currentFill = path.getAttribute('fill');
      // #EF3A3C는 그대로 유지, 나머지만 변경
      if (currentFill && currentFill !== '#EF3A3C' && currentFill !== 'none') {
        if (isScrolled) {
          // 스크롤 시: 원래 색상 (#6D6D6F)
          path.setAttribute('fill', '#6D6D6F');
        } else {
          // 최상단: 흰색
          path.setAttribute('fill', '#ffffff');
        }
      }
    });
  }
  
  // 초기 로고 색상 설정 (메인 페이지에서만)
  if (isHomePage) {
    // 페이지 로드 직후 초기 색상 설정
    setTimeout(() => {
      updateLogoColor(window.pageYOffset > 50);
    }, 0);
  }
  
  // 스크롤 이벤트
  window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 50) {
      header.classList.add('scrolled');
      updateLogoColor(true);
    } else {
      header.classList.remove('scrolled');
      updateLogoColor(false);
    }
  });
  
  // 마우스 호버 이벤트
  header.addEventListener('mouseenter', () => {
    if (window.pageYOffset <= 50) {
      header.classList.add('scrolled');
      updateLogoColor(true);
    }
  });
  
  header.addEventListener('mouseleave', () => {
    if (window.pageYOffset <= 50) {
      header.classList.remove('scrolled');
      updateLogoColor(false);
    }
  });
}

// Top Button
function initTopButton() {
  // Top 버튼 생성
  const topButton = document.createElement('button');
  topButton.className = 'top-button';
  topButton.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 19V5M5 12L12 5L19 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  topButton.setAttribute('aria-label', '맨 위로');
  document.body.appendChild(topButton);
  
  // 스크롤 이벤트
  window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
      topButton.classList.add('show');
    } else {
      topButton.classList.remove('show');
    }
  });
  
  // 클릭 이벤트
  topButton.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

// Hero Slider (Swiper.js)
function initHeroSlider() {
  const heroSwiper = document.querySelector('.hero-swiper');
  if (!heroSwiper || typeof Swiper === 'undefined') return;

  let progressInterval = null;
  let currentProgress = 0;
  let isPaused = false;
  let currentDuration = 5000; // 첫 슬라이드는 5초

  try {
    const swiper = new Swiper('.hero-swiper', {
      effect: 'fade',
      speed: 1000,
      fadeEffect: {
        crossFade: true
      },
      autoplay: false, // autoplay 비활성화, 수동으로 제어
      simulateTouch: false, // 마우스 드래그 비활성화, 터치는 허용
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      loop: true,
      on: {
        init: function() {
          // 첫 슬라이드만 콘텐츠 표시
          const activeSlide = this.slides[this.activeIndex];
          showSlideContent(activeSlide);
          
          // 첫 번째 슬라이드 배경 이미지 줌 아웃 효과 시작
          const bgImage = activeSlide.querySelector('.hero-background');
          if (bgImage) {
            bgImage.style.transition = 'transform 5s ease-out';
            bgImage.style.transform = 'scale(1.0)';
          }
          
          // 첫 번째 슬라이드는 delay만 적용 (5초)
          currentDuration = 5000;
          startProgress(5000, this);
        },
        slideChange: function() {
          // 슬라이드 변경 시 모든 bullet 초기화 및 프로그레스 재시작
          resetAllBullets();
          // 두 번째 슬라이드부터는 delay + speed 적용 (6초)
          currentDuration = 6000;
          if (!isPaused) {
            startProgress(6000, this);
          }
        },
        slideChangeTransitionStart: function() {
          // 모든 슬라이드의 콘텐츠 요소 숨김
          this.slides.forEach(slide => {
            hideSlideContent(slide);
          });
        },
        slideChangeTransitionEnd: function() {
          // 활성 슬라이드의 콘텐츠만 표시
          const activeSlide = this.slides[this.activeIndex];
          showSlideContent(activeSlide);
          
          // 배경 이미지 줌 아웃 효과 - 먼저 리셋 후 애니메이션
          const bgImage = activeSlide.querySelector('.hero-background');
          if (bgImage) {
            bgImage.style.transition = 'none';
            bgImage.style.transform = 'scale(1.1)';
            // 강제 리플로우 후 애니메이션 시작
            bgImage.offsetHeight;
            bgImage.style.transition = 'transform 5s ease-out';
            bgImage.style.transform = 'scale(1.0)';
          }
        }
      }
    });
    
    // 재생/정지 토글 버튼 기능
    const autoplayToggle = document.querySelector('.hero-autoplay-toggle');
    if (autoplayToggle) {
      // 초기 상태 설정 (자동 재생 중)
      autoplayToggle.classList.remove('paused');
      autoplayToggle.setAttribute('aria-label', '자동 재생 정지');
      
      autoplayToggle.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        
        if (isPaused) {
          // 재생 - 현재 슬라이드에서 처음부터 시작
          isPaused = false;
          autoplayToggle.classList.remove('paused');
          autoplayToggle.setAttribute('aria-label', '자동 재생 정지');
          startProgress(currentDuration, swiper);
        } else {
          // 정지 - 타이머 0으로 초기화
          autoplayToggle.classList.add('paused');
          autoplayToggle.setAttribute('aria-label', '자동 재생 시작');
          isPaused = true;
          stopProgress();
          currentProgress = 0;
          const currentActiveBullet = document.querySelector('.swiper-pagination-bullet-active');
          if (currentActiveBullet) {
            currentActiveBullet.style.background = 'rgba(255, 255, 255, 0.3)';
          }
        }
      });
    }
    
    // 모든 bullet 초기화
    function resetAllBullets() {
      const allBullets = document.querySelectorAll('.swiper-pagination-bullet');
      allBullets.forEach(bullet => {
        bullet.style.background = 'rgba(255, 255, 255, 0.3)';
      });
    }
    
    // 프로그레스 시작
    function startProgress(duration, swiperInstance) {
      stopProgress();
      currentProgress = 0;
      isPaused = false;
      
      const startTime = Date.now();
      
      progressInterval = setInterval(() => {
        if (isPaused) {
          return; // 일시정지 상태면 업데이트하지 않음
        }
        
        const elapsed = Date.now() - startTime;
        currentProgress = Math.min((elapsed / duration) * 100, 100);
        
        // 현재 활성 bullet 찾기
        const currentActiveBullet = document.querySelector('.swiper-pagination-bullet-active');
        if (currentActiveBullet) {
          currentActiveBullet.style.background = `linear-gradient(to right, rgba(255, 255, 255, 1) ${currentProgress}%, rgba(255, 255, 255, 0.3) ${currentProgress}%)`;
        }
        
        // 100% 도달 시 즉시 다음 슬라이드로 전환
        if (currentProgress >= 100) {
          stopProgress();
          if (swiperInstance && !isPaused) {
            swiperInstance.slideNext();
          }
        }
      }, 16); // 60fps
    }
    
    // 프로그레스 정지
    function stopProgress() {
      if (progressInterval) {
        clearInterval(progressInterval);
        progressInterval = null;
      }
    }
    
    // 프로그레스 일시정지 (현재 상태 유지)
    function pauseProgress() {
      isPaused = true;
    }
    
    // 프로그레스 재개
    function resumeProgress(swiperInstance) {
      if (isPaused) {
        isPaused = false;
        
        // 프로그레스가 0이면 처음부터 시작
        if (currentProgress === 0) {
          startProgress(currentDuration, swiperInstance);
          return;
        }
        
        // 남은 시간 계산
        const remainingProgress = 100 - currentProgress;
        const remainingDuration = currentDuration * (remainingProgress / 100);
        
        const startTime = Date.now();
        const startProgress = currentProgress;
        
        // 기존 interval 정리
        stopProgress();
        
        progressInterval = setInterval(() => {
          if (isPaused) {
            return;
          }
          
          const elapsed = Date.now() - startTime;
          currentProgress = Math.min(startProgress + ((elapsed / remainingDuration) * remainingProgress), 100);
          
          const currentActiveBullet = document.querySelector('.swiper-pagination-bullet-active');
          if (currentActiveBullet) {
            currentActiveBullet.style.background = `linear-gradient(to right, rgba(255, 255, 255, 1) ${currentProgress}%, rgba(255, 255, 255, 0.3) ${currentProgress}%)`;
          }
          
          // 100% 도달 시 즉시 다음 슬라이드로 전환
          if (currentProgress >= 100) {
            stopProgress();
            if (swiperInstance && !isPaused) {
              swiperInstance.slideNext();
            }
          }
        }, 16);
      }
    }
    
    // 슬라이드 콘텐츠 숨김 함수
    function hideSlideContent(slide) {
      const content = slide.querySelector('.hero-content');
      if (!content) return;
      
      const elements = [
        content.querySelector('.hero-subtitle'),
        content.querySelector('.hero-title'),
        content.querySelector('.hero-description'),
        content.querySelector('.hero-actions')
      ];
      
      elements.forEach(el => {
        if (el) {
          el.style.opacity = '0';
          el.style.transform = 'translateY(30px)';
        }
      });
    }
    
    // 슬라이드 콘텐츠 표시 함수
    function showSlideContent(slide) {
      const content = slide.querySelector('.hero-content');
      if (!content) return;
      
      const subtitle = content.querySelector('.hero-subtitle');
      const title = content.querySelector('.hero-title');
      const description = content.querySelector('.hero-description');
      const actions = content.querySelector('.hero-actions');
      
      // 배경 이미지는 slideChangeTransitionEnd에서 처리
      
      // 순차적으로 요소 표시 (더 빠른 타이밍)
      setTimeout(() => {
        if (subtitle) {
          subtitle.style.transition = 'all 0.5s ease-out';
          subtitle.style.opacity = '1';
          subtitle.style.transform = 'translateY(0)';
        }
      }, 100);
      
      setTimeout(() => {
        if (title) {
          title.style.transition = 'all 0.5s ease-out';
          title.style.opacity = '1';
          title.style.transform = 'translateY(0)';
        }
      }, 250);
      
      setTimeout(() => {
        if (description) {
          description.style.transition = 'all 0.5s ease-out';
          description.style.opacity = '1';
          description.style.transform = 'translateY(0)';
        }
      }, 400);
      
      setTimeout(() => {
        if (actions) {
          actions.style.transition = 'all 0.5s ease-out';
          actions.style.opacity = '1';
          actions.style.transform = 'translateY(0)';
        }
      }, 550);
    }
  } catch (error) {
    console.error('Swiper initialization error:', error);
  }
}

// Scroll Animations with GSAP
function initScrollAnimations() {
  if (typeof gsap === 'undefined') {
    console.warn('GSAP not available, using fallback animations');
    return;
  }

  // Fade In animations (서브페이지에서는 initSubpageScrollAnimations에서 처리)
  const path = window.location.pathname;
  const isSubpage = !(path.endsWith('/') || path.endsWith('/index.html') || path === '');
  const fadeInElements = document.querySelectorAll('.fade-in.will-animate');
  if (fadeInElements.length > 0 && !isSubpage) {
    gsap.utils.toArray('.fade-in.will-animate').forEach(element => {
      gsap.from(element, {
        scrollTrigger: {
          trigger: element,
          start: 'top 85%',
          toggleActions: 'play none none none',
          onEnter: () => element.classList.add('active'),
        },
        opacity: 0,
        y: 50,
        duration: 0.8,
        ease: 'power2.out',
      });
    });
  }

  // Scale In animations
  const scaleInElements = document.querySelectorAll('.scale-in.will-animate');
  if (scaleInElements.length > 0) {
    gsap.utils.toArray('.scale-in.will-animate').forEach(element => {
      gsap.from(element, {
        scrollTrigger: {
          trigger: element,
          start: 'top 85%',
          toggleActions: 'play none none none',
          onEnter: () => element.classList.add('active'),
        },
        opacity: 0,
        scale: 0.8,
        duration: 1,
        ease: 'power2.out',
      });
    });
  }

  // Solution Cards - Stagger animation
  const solutionCards = document.querySelectorAll('.card-solution');
  if (solutionCards.length > 0) {
    gsap.from(solutionCards, {
      scrollTrigger: {
        trigger: '.solutions-section',
        start: 'top 70%',
        toggleActions: 'play none none none',
      },
      opacity: 0,
      y: 50,
      duration: 0.8,
      stagger: 0.1,
      ease: 'power2.out',
    });
  }

  // Project Cards - CSS only, no GSAP animation
  const projectCards = document.querySelectorAll('.card-project');
  if (projectCards.length > 0) {
    // Just make them visible, no animation
    projectCards.forEach(card => {
      card.style.opacity = '1';
      card.style.visibility = 'visible';
    });
  }

  // Timeline Items
  const timelineItems = document.querySelectorAll('.timeline-item');
  if (timelineItems.length > 0) {
    timelineItems.forEach((item, index) => {
      gsap.from(item, {
        scrollTrigger: {
          trigger: item,
          start: 'top 85%',
          toggleActions: 'play none none none',
        },
        opacity: 0,
        x: index % 2 === 0 ? -50 : 50,
        duration: 0.8,
        ease: 'power2.out',
      });
    });
  }

  // Subpage section scroll animations
  initSubpageScrollAnimations();
}

// Subpage Scroll Fade-In / Slide-Up Animations
function initSubpageScrollAnimations() {
  if (typeof gsap === 'undefined') return;

  // 이용약관, 개인정보처리방침, 메인페이지에서는 애니메이션 제외
  const path = window.location.pathname;
  if (path.includes('terms.html') || path.includes('privacy.html') || path.endsWith('/') || path.endsWith('/index.html') || path === '') return;

  // 섹션 컨테이너 셀렉터 (트리거 단위)
  const sectionSelectors = [
    '.support-steps',
    '.grid.grid-2',
    '.content-card',
    '.ceo-message-content',
    '.overview-section > .container',
    '.diagram-section .container',
    '.cases-section .container',
    '.solution-cta .container',
    '.platform-section .container',
    '.process-section .container',
    '.solutions-grid-section .container',
    '.content-section > .container > .filter-tabs',
    '.content-section > .container > .projects-grid',
    '.policy-section',
    '.location-info-title',
    '.location-info-grid',
  ];

  // 섹션 내 자식 요소 순서 (위에서 아래로 순차 등장)
  const childSelectors = [
    '.section-tag',
    '.support-steps',
    '.content-title',
    '.content-subtitle',
    '.overview-title',
    '.overview-subtitle',
    '.features-section-title',
    '.diagram-title',
    '.cases-title',
    '.contact-title',
    '.platform-description',
    '.policy-title',
    '.policy-subtitle',
    '.overview-text',
    '.content-text',
    '.company-content-inner',
    '.contact-description',
    '.contact-actions',
    'img',
    '.grid',
    '.overview-features',
    '.cases-grid',
    '.projects-grid',
    '.components-grid',
    '.gallery-grid',
    '.platform-features',
    '.process-steps',
    '.solutions-grid',
    '.policy-list',
    '.filter-tabs',
    '.diagram-container',
    '.ceo-message-content > div',
  ];

  const matchedSections = [];
  document.querySelectorAll(sectionSelectors.join(',')).forEach(section => {
    // 페이지 헤더, 히어로 내부 제외
    if (section.closest('.page-header') || section.closest('.hero')) return;

    // 이미 매칭된 섹션의 자식이면 건너뛰기 (중복 트리거 방지)
    const isNestedInMatched = matchedSections.some(ms => ms.contains(section));
    if (isNestedInMatched) return;
    matchedSections.push(section);

    // 섹션 내 애니메이션 대상 수집 (DOM 순서 유지)
    const animTargets = [];
    const walker = document.createTreeWalker(section, NodeFilter.SHOW_ELEMENT);
    let node;
    const matched = new Set();

    // 그리드 컨테이너 셀렉터 (전체를 하나의 블록으로 처리)
    const gridContainerSelectors = ['.support-steps', '.company-content-inner', '.grid', '.overview-features', '.cases-grid', '.projects-grid', '.components-grid', '.gallery-grid', '.platform-features', '.process-steps', '.solutions-grid', '.policy-list'];

    while ((node = walker.nextNode())) {
      if (matched.has(node)) continue;
      // 이미 매칭된 그리드 컨테이너의 자식이면 건너뛰기
      let isInsideMatched = false;
      for (const m of matched) {
        if (m.contains(node)) { isInsideMatched = true; break; }
      }
      if (isInsideMatched) continue;

      for (const sel of childSelectors) {
        if (node.matches && node.matches(sel)) {
          // img 태그가 그리드 아이템 내부에 있으면 건너뛰기
          if (sel === 'img' && node.closest('.case-item, .card-project, .icon-box, .feature-item, .component-item, .gallery-item, .solution-card, .process-step, .platform-feature-item')) continue;
          // 그리드 컨테이너는 전체를 하나의 블록으로 처리
          const isGrid = gridContainerSelectors.some(gs => node.matches(gs));
          animTargets.push({ type: 'single', el: node });
          matched.add(node);
          break;
        }
      }
    }

    if (animTargets.length === 0) return;

    // 모든 대상 초기 숨김
    animTargets.forEach(target => {
      gsap.set(target.el, { opacity: 0, y: 30 });
    });

    // 섹션이 뷰포트 80% 지점에 도달하면 내부 요소 순차 등장
    ScrollTrigger.create({
      trigger: section,
      start: 'top 80%',
      once: true,
      onEnter: () => {
        let delay = 0;
        animTargets.forEach(target => {
          gsap.to(target.el, {
            opacity: 1, y: 0,
            duration: 0.7,
            delay: delay,
            ease: 'power2.out',
          });
          delay += 0.18;
        });
      }
    });
  });
}

// Counter Animations
function initCounterAnimations() {
  const counters = document.querySelectorAll('.card-stat .number[data-target]');
  
  if (counters.length === 0) {
    console.warn('No counter elements found');
    return;
  }
  
  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
    console.warn('GSAP or ScrollTrigger not available, using fallback counter animation');
    // Fallback: Use Intersection Observer
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const counter = entry.target;
          const target = parseFloat(counter.getAttribute('data-target'));
          const originalText = counter.textContent;
          const numberMatch = originalText.match(/[\d,.]+/);
          if (!numberMatch) return;
          
          const suffix = originalText.substring(numberMatch.index + numberMatch[0].length);
          const duration = 2000; // 2 seconds
          const steps = 60;
          const increment = target / steps;
          const stepDuration = duration / steps;
          let current = 0;
          
          const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
              current = target;
              clearInterval(timer);
            }
            
            let displayValue;
            if (target % 1 === 0) {
              displayValue = Math.ceil(current);
            } else {
              displayValue = current.toFixed(1);
            }
            counter.textContent = displayValue + suffix;
          }, stepDuration);
          
          observer.unobserve(counter);
        }
      });
    }, { threshold: 0.5 });
    
    counters.forEach(counter => observer.observe(counter));
    return;
  }
  
  counters.forEach(counter => {
    const target = parseFloat(counter.getAttribute('data-target'));
    const originalText = counter.textContent;
    
    // Extract suffix (like +, %, 년 etc)
    const numberMatch = originalText.match(/[\d,.]+/);
    if (!numberMatch) return;
    
    const suffix = originalText.substring(numberMatch.index + numberMatch[0].length);
    
    // Set initial value to 0
    counter.textContent = '0' + suffix;
    
    ScrollTrigger.create({
      trigger: counter,
      start: 'top 80%',
      once: true,
      onEnter: () => {
        const obj = { value: 0 };
        gsap.to(obj, {
          value: target,
          duration: 2.5,
          ease: 'power2.out',
          onUpdate: function() {
            // Format number based on whether it's decimal or integer
            let currentValue;
            if (target % 1 === 0) {
              currentValue = Math.ceil(obj.value);
            } else {
              currentValue = obj.value.toFixed(1);
            }
            counter.textContent = currentValue + suffix;
          }
        });
      }
    });
  });
}

// Parallax Effect
function initParallax() {
  if (typeof gsap === 'undefined') return;

  // Hero parallax - 비활성화 (주석 처리)
  // const heroSlides = document.querySelectorAll('.hero-slide .hero-background');
  // if (heroSlides.length > 0) {
  //   heroSlides.forEach(bg => {
  //     gsap.to(bg, {
  //       scrollTrigger: {
  //         trigger: '.hero',
  //         start: 'top top',
  //         end: 'bottom top',
  //         scrub: 1,
  //       },
  //       y: '30%',
  //       ease: 'none',
  //     });
  //   });
  // }

  // Solution hero parallax
  const solutionHeroBackground = document.querySelector('.solution-hero-background');
  if (solutionHeroBackground) {
    gsap.to(solutionHeroBackground, {
      scrollTrigger: {
        trigger: '.solution-hero',
        start: 'top top',
        end: 'bottom top',
        scrub: 1,
      },
      y: '30%',
      ease: 'none',
    });
  }

  // Page header parallax
  const pageHeaderBackground = document.querySelector('.page-header-background');
  if (pageHeaderBackground) {
    gsap.to(pageHeaderBackground, {
      scrollTrigger: {
        trigger: '.page-header',
        start: 'top top',
        end: 'bottom top',
        scrub: 1,
      },
      y: '30%',
      ease: 'none',
    });
  }
}

// Smooth Scroll for anchor links
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href === '#' || href.length <= 1) return;
      
      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        if (typeof gsap !== 'undefined' && gsap.plugins && gsap.plugins.scrollTo) {
          gsap.to(window, {
            duration: 1,
            scrollTo: {
              y: target,
              offsetY: 80
            },
            ease: 'power2.inOut'
          });
        } else {
          // Fallback to native smooth scroll
          const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - 80;
          window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
          });
        }
      }
    });
  });
});

// Hover effects for cards
function initCardHoverEffects() {
  // Solution cards - CSS only, no GSAP override
  const solutionCards = document.querySelectorAll('.card-solution');
  solutionCards.forEach(card => {
    // Remove any inline styles that might interfere
    card.style.transform = '';
  });
  
  // Project cards - CSS only, no GSAP
  const projectCards = document.querySelectorAll('.card-project');
  projectCards.forEach(card => {
    // Remove any inline styles that might interfere
    card.style.transform = '';
  });
  
  // Stat cards - keep GSAP for these
  if (typeof gsap === 'undefined') {
    console.warn('GSAP not available for card hover effects');
    return;
  }
  
  const statCards = document.querySelectorAll('.card-stat');
  
  if (statCards.length === 0) return;
  
  statCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
      gsap.to(this, {
        y: -8,
        duration: 0.4,
        ease: 'power2.out',
        overwrite: 'auto'
      });
    });

    card.addEventListener('mouseleave', function() {
      gsap.to(this, {
        y: 0,
        duration: 0.4,
        ease: 'power2.out',
        overwrite: 'auto'
      });
    });
  });
}

// Client logo hover
function initClientLogoEffects() {
  const logos = document.querySelectorAll('.client-logo');
  
  logos.forEach(logo => {
    logo.addEventListener('mouseenter', function() {
      if (typeof gsap !== 'undefined') {
        gsap.to(this, {
          opacity: 1,
          scale: 1.1,
          duration: 0.3,
          ease: 'power2.out'
        });
      } else {
        this.style.opacity = '1';
        this.style.transform = 'scale(1.1)';
      }
    });

    logo.addEventListener('mouseleave', function() {
      if (typeof gsap !== 'undefined') {
        gsap.to(this, {
          opacity: 1,
          scale: 1,
          duration: 0.3,
          ease: 'power2.out'
        });
      } else {
        this.style.opacity = '1';
        this.style.transform = 'scale(1)';
      }
    });
  });
}

// Initialize hover effects
document.addEventListener('DOMContentLoaded', () => {
  initCardHoverEffects();
  initClientLogoEffects();
});

// Page load animation
window.addEventListener('load', () => {
  // body opacity를 명시적으로 1로 설정
  document.body.style.opacity = '1';
  
  if (typeof gsap !== 'undefined') {
    gsap.to('body', {
      opacity: 1,
      duration: 0.5,
      ease: 'power2.out',
      onComplete: () => {
        // 애니메이션 완료 후 확실하게 1로 설정
        document.body.style.opacity = '1';
      }
    });
  }
});

// Scroll progress indicator (optional)
function initScrollProgress() {
  const progressBar = document.createElement('div');
  progressBar.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: var(--color-accent-gold);
    z-index: 9999;
    transform-origin: left;
  `;
  document.body.appendChild(progressBar);

  gsap.to(progressBar, {
    scaleX: 1,
    ease: 'none',
    scrollTrigger: {
      start: 'top top',
      end: 'max',
      scrub: 0.3
    }
  });
}

// Uncomment to enable scroll progress
// initScrollProgress();


// Timeline Line Animation (for History Page)
function initTimelineAnimation() {
  const timeline = document.querySelector('.timeline');
  if (!timeline) return;
  
  const timelineItems = document.querySelectorAll('.timeline-item');
  if (timelineItems.length === 0) return;
  
  function updateTimelineProgress() {
    const rect = timeline.getBoundingClientRect();
    const windowHeight = window.innerHeight;
    const timelineTop = rect.top;
    const timelineHeight = rect.height;
    
    // 타임라인이 화면에 보이는지 확인
    if (timelineTop < windowHeight && rect.bottom > 0) {
      // 중앙 기준으로 스크롤 진행도 계산
      const centerOffset = windowHeight * 0.5; // 화면 중앙
      const scrolled = centerOffset - timelineTop;
      const progress = Math.max(0, Math.min(100, (scrolled / timelineHeight) * 100));
      
      // CSS 변수로 진행도 설정
      timeline.style.setProperty('--timeline-progress', `${progress}%`);
      
      // 각 타임라인 아이템의 활성화 상태 업데이트
      let activeYear = null;
      timelineItems.forEach(item => {
        const itemRect = item.getBoundingClientRect();
        const itemCenter = itemRect.top + itemRect.height / 2;
        const itemTop = itemRect.top;
        
        // 페이드 인 효과: 화면의 2/3 지점 (중간보다 아래)에 도달하면 표시
        // windowHeight * 0.67 = 화면 높이의 약 2/3 지점
        if (itemTop < windowHeight * 0.67) {
          item.classList.add('visible');
        }
        
        // 화면 중앙 근처에 있으면 활성화
        if (itemCenter < windowHeight * 0.6 && itemCenter > windowHeight * 0.4) {
          item.classList.add('active');
          item.classList.add('passed');
          // 활성화된 아이템의 연도 추출
          const yearElement = item.querySelector('.timeline-year');
          if (yearElement) {
            activeYear = parseInt(yearElement.textContent);
          }
        } else if (itemCenter >= windowHeight * 0.6) {
          // 아직 지나가지 않은 아이템
          item.classList.remove('active');
          item.classList.remove('passed');
        } else {
          // 이미 지나간 아이템 (passed 유지)
          item.classList.remove('active');
          item.classList.add('passed');
        }
      });
      
      // 탭 활성화 상태 업데이트
      if (activeYear) {
        updateActiveTab(activeYear);
      }
    }
  }
  
  // 스크롤 이벤트 리스너 (throttle 적용)
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        updateTimelineProgress();
        ticking = false;
      });
      ticking = true;
    }
  });
  
  window.addEventListener('resize', updateTimelineProgress);
  
  // 초기 실행
  updateTimelineProgress();
}

// 활성화된 연도에 따라 탭 업데이트
let isManualTabClick = false; // 수동 탭 클릭 플래그

function updateActiveTab(year) {
  // 수동 탭 클릭 중에는 자동 업데이트 건너뛰기
  if (isManualTabClick) return;
  
  const tabs = document.querySelectorAll('.timeline-tab');
  if (tabs.length === 0) return;
  
  tabs.forEach(tab => {
    const tabYear = parseInt(tab.getAttribute('data-year'));
    
    // 연도 범위에 따라 탭 활성화
    // 2025 ~ 2021: 현재~ 탭
    // 2020 ~ 2016: 2020~ 탭
    // 2015 이하: 2015~ 탭
    if (year >= 2021 && tabYear === 2025) {
      tab.classList.add('active');
    } else if (year >= 2016 && year <= 2020 && tabYear === 2020) {
      tab.classList.add('active');
    } else if (year <= 2015 && tabYear === 2015) {
      tab.classList.add('active');
    } else {
      tab.classList.remove('active');
    }
  });
}

// Timeline Tabs (for History Page)
function initTimelineTabs() {
  const tabs = document.querySelectorAll('.timeline-tab');
  if (tabs.length === 0) return;
  
  tabs.forEach(tab => {
    tab.addEventListener('click', function() {
      const year = this.getAttribute('data-year');
      const targetElement = document.getElementById(`year-${year}`);
      
      if (targetElement) {
        // 수동 클릭 플래그 설정
        isManualTabClick = true;
        
        // 탭 활성화 상태 변경
        tabs.forEach(t => t.classList.remove('active'));
        this.classList.add('active');
        
        // 스크롤 위치 계산 (탭 바 높이만 고려)
        const tabsHeight = document.querySelector('.timeline-tabs').offsetHeight;
        const offset = tabsHeight + 20; // 20px 여유
        
        const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - offset;
        
        // 부드러운 스크롤
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
        
        // 스크롤 완료 후 자동 업데이트 재개 (1초 후)
        setTimeout(() => {
          isManualTabClick = false;
        }, 1000);
      }
    });
  });
}

// Timeline Tabs Sticky Effect
function initTimelineTabsSticky() {
  const timelineTabs = document.querySelector('.timeline-tabs');
  if (!timelineTabs) return;
  
  // 탭 바의 초기 위치 저장
  const tabsOffsetTop = timelineTabs.offsetTop;
  
  function checkSticky() {
    if (window.pageYOffset >= tabsOffsetTop) {
      timelineTabs.classList.add('stuck');
    } else {
      timelineTabs.classList.remove('stuck');
    }
  }
  
  window.addEventListener('scroll', checkSticky);
  window.addEventListener('resize', () => {
    checkSticky();
  });
  
  // 초기 실행
  checkSticky();
}

// DOMContentLoaded에서 타임라인 애니메이션 초기화
document.addEventListener('DOMContentLoaded', () => {
  if (document.querySelector('.timeline')) {
    initTimelineAnimation();
    initTimelineTabs();
    initTimelineTabsSticky();
  }
});
