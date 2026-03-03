// Main JavaScript - Template3 with GSAP

// GSAP Configuration
gsap.registerPlugin(ScrollTrigger);

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  initHeroSlider();
  initScrollAnimations();
  initCounterAnimations();
  initParallax();
});

// Hero Slider (Swiper.js)
function initHeroSlider() {
  const heroSwiper = document.querySelector('.hero-swiper');
  if (!heroSwiper) return;

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
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    loop: true,
  });
}

// Scroll Animations with GSAP
function initScrollAnimations() {
  // Fade In animations
  gsap.utils.toArray('.fade-in').forEach(element => {
    gsap.from(element, {
      scrollTrigger: {
        trigger: element,
        start: 'top 80%',
        toggleActions: 'play none none none',
      },
      opacity: 0,
      y: 50,
      duration: 0.8,
      ease: 'power2.out',
    });
  });

  // Scale In animations
  gsap.utils.toArray('.scale-in').forEach(element => {
    gsap.from(element, {
      scrollTrigger: {
        trigger: element,
        start: 'top 80%',
        toggleActions: 'play none none none',
      },
      opacity: 0,
      scale: 0.8,
      duration: 1,
      ease: 'power2.out',
    });
  });

  // Solution Cards - Stagger animation
  const solutionCards = document.querySelectorAll('.card-solution');
  if (solutionCards.length > 0) {
    gsap.from(solutionCards, {
      scrollTrigger: {
        trigger: '.solutions-section',
        start: 'top 70%',
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
          start: 'top 80%',
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
  const counters = document.querySelectorAll('.card-stat .number');
  
  counters.forEach(counter => {
    const target = parseInt(counter.textContent.replace(/[^0-9]/g, ''));
    const suffix = counter.textContent.replace(/[0-9]/g, '');
    
    ScrollTrigger.create({
      trigger: counter,
      start: 'top 80%',
      once: true,
      onEnter: () => {
        gsap.to(counter, {
          textContent: target,
          duration: 2,
          ease: 'power1.out',
          snap: { textContent: 1 },
          onUpdate: function() {
            counter.textContent = Math.ceil(counter.textContent) + suffix;
          }
        });
      }
    });
  });
}

// Parallax Effect
function initParallax() {
  // Hero parallax
  const heroBackground = document.querySelector('.hero-background');
  if (heroBackground) {
    gsap.to(heroBackground, {
      scrollTrigger: {
        trigger: '.hero',
        start: 'top top',
        end: 'bottom top',
        scrub: true,
      },
      y: (i, target) => -target.offsetHeight * 0.3,
      ease: 'none',
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
        scrub: true,
      },
      y: (i, target) => -target.offsetHeight * 0.3,
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
        scrub: true,
      },
      y: (i, target) => -target.offsetHeight * 0.3,
      ease: 'none',
    });
  }
}

// Smooth Scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      gsap.to(window, {
        duration: 1,
        scrollTo: {
          y: target,
          offsetY: 80
        },
        ease: 'power2.inOut'
      });
    }
  });
});

// Hover effects for cards
document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('mouseenter', function() {
    gsap.to(this, {
      scale: 1.05,
      duration: 0.4,
      ease: 'power2.out'
    });
  });

  card.addEventListener('mouseleave', function() {
    gsap.to(this, {
      scale: 1,
      duration: 0.4,
      ease: 'power2.out'
    });
  });
});

// Client logo hover
document.querySelectorAll('.client-logo').forEach(logo => {
  logo.addEventListener('mouseenter', function() {
    gsap.to(this, {
      filter: 'grayscale(0%) brightness(1)',
      duration: 0.3,
      ease: 'power2.out'
    });
  });

  logo.addEventListener('mouseleave', function() {
    gsap.to(this, {
      filter: 'grayscale(100%) brightness(0.5)',
      duration: 0.3,
      ease: 'power2.out'
    });
  });
});

// Page load animation
window.addEventListener('load', () => {
  gsap.from('body', {
    opacity: 0,
    duration: 0.5,
    ease: 'power2.out'
  });
});

// Scroll progress indicator (optional)
function initScrollProgress() {
  const progressBar = document.createElement('div');
  progressBar.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--color-accent-gold), var(--color-accent-cyan));
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
