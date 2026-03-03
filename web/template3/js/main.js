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
  
  initHeroSlider();
  initScrollAnimations();
  initCounterAnimations();
  initParallax();
});

// Hero Slider (Swiper.js)
function initHeroSlider() {
  const heroSwiper = document.querySelector('.hero-swiper');
  if (!heroSwiper || typeof Swiper === 'undefined') return;

  try {
    new Swiper('.hero-swiper', {
      effect: 'fade',
      speed: 1000,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      loop: true,
      fadeEffect: {
        crossFade: true
      },
    });
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

  // Fade In animations
  const fadeInElements = document.querySelectorAll('.fade-in.will-animate');
  if (fadeInElements.length > 0) {
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

  // Project Cards
  const projectCards = document.querySelectorAll('.card-project');
  if (projectCards.length > 0) {
    gsap.from(projectCards, {
      scrollTrigger: {
        trigger: '.projects-section',
        start: 'top 70%',
        toggleActions: 'play none none none',
      },
      opacity: 0,
      y: 50,
      duration: 0.8,
      stagger: 0.15,
      ease: 'power2.out',
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

  // Feature Items
  const featureItems = document.querySelectorAll('.feature-item');
  if (featureItems.length > 0) {
    gsap.from(featureItems, {
      scrollTrigger: {
        trigger: '.overview-features',
        start: 'top 70%',
        toggleActions: 'play none none none',
      },
      opacity: 0,
      y: 50,
      duration: 0.8,
      stagger: 0.2,
      ease: 'power2.out',
    });
  }
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
          const numberMatch = originalText.match(/[\d.]+/);
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
    const numberMatch = originalText.match(/[\d.]+/);
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

  // Hero parallax - Swiper slides
  const heroSlides = document.querySelectorAll('.hero-slide .hero-background');
  if (heroSlides.length > 0) {
    heroSlides.forEach(bg => {
      gsap.to(bg, {
        scrollTrigger: {
          trigger: '.hero',
          start: 'top top',
          end: 'bottom top',
          scrub: 1,
        },
        y: '30%',
        ease: 'none',
      });
    });
  }

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
  
  // Project and stat cards - keep GSAP for these
  if (typeof gsap === 'undefined') {
    console.warn('GSAP not available for card hover effects');
    return;
  }
  
  const cards = document.querySelectorAll('.card-project, .card-stat');
  
  if (cards.length === 0) return;
  
  cards.forEach(card => {
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
          opacity: 0.6,
          scale: 1,
          duration: 0.3,
          ease: 'power2.out'
        });
      } else {
        this.style.opacity = '0.6';
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
  if (typeof gsap !== 'undefined') {
    gsap.from('body', {
      opacity: 0,
      duration: 0.5,
      ease: 'power2.out'
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
