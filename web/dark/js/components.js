// Components - Template3

// Header Navigation
class HeaderNav {
  constructor() {
    this.header = document.querySelector('.header');
    this.mobileToggle = document.querySelector('.header-mobile-toggle');
    this.mobileMenu = document.querySelector('.header-mobile-menu');
    this.init();
  }

  init() {
    this.handleScroll();
    this.handleMobileMenu();
    this.handleDropdown();
  }

  handleScroll() {
    let lastScroll = 0;
    
    window.addEventListener('scroll', throttle(() => {
      const currentScroll = window.pageYOffset;
      
      if (currentScroll > 100) {
        this.header.classList.add('scrolled');
      } else {
        this.header.classList.remove('scrolled');
      }
      
      // Hide/show header on scroll
      if (currentScroll > lastScroll && currentScroll > 300) {
        this.header.style.transform = 'translateY(-100%)';
      } else {
        this.header.style.transform = 'translateY(0)';
      }
      
      lastScroll = currentScroll;
    }, 100));
  }

  handleMobileMenu() {
    if (!this.mobileToggle || !this.mobileMenu) return;

    this.mobileToggle.addEventListener('click', () => {
      this.mobileToggle.classList.toggle('active');
      this.mobileMenu.classList.toggle('active');
      document.body.style.overflow = this.mobileMenu.classList.contains('active') ? 'hidden' : '';
    });

    // Close on link click
    const links = this.mobileMenu.querySelectorAll('a');
    links.forEach(link => {
      link.addEventListener('click', () => {
        this.mobileToggle.classList.remove('active');
        this.mobileMenu.classList.remove('active');
        document.body.style.overflow = '';
      });
    });
  }

  handleDropdown() {
    const dropdowns = document.querySelectorAll('.header-dropdown');
    
    dropdowns.forEach(dropdown => {
      dropdown.addEventListener('mouseenter', () => {
        const menu = dropdown.querySelector('.header-dropdown-menu');
        if (menu) {
          menu.style.display = 'block';
        }
      });

      dropdown.addEventListener('mouseleave', () => {
        const menu = dropdown.querySelector('.header-dropdown-menu');
        if (menu) {
          menu.style.display = 'none';
        }
      });
    });
  }
}

// Form Validation
class FormValidator {
  constructor(formSelector) {
    this.form = document.querySelector(formSelector);
    if (this.form) {
      this.init();
    }
  }

  init() {
    this.form.addEventListener('submit', (e) => this.handleSubmit(e));
    
    // Real-time validation
    const inputs = this.form.querySelectorAll('input, textarea, select');
    inputs.forEach(input => {
      input.addEventListener('blur', () => this.validateField(input));
    });
  }

  handleSubmit(e) {
    e.preventDefault();
    
    if (this.validateForm()) {
      this.submitForm();
    }
  }

  validateForm() {
    let isValid = true;
    const inputs = this.form.querySelectorAll('[required]');
    
    inputs.forEach(input => {
      if (!this.validateField(input)) {
        isValid = false;
      }
    });
    
    return isValid;
  }

  validateField(field) {
    const value = field.value.trim();
    const type = field.type;
    const name = field.name;
    
    // Remove previous error
    this.removeError(field);
    
    // Required check
    if (field.hasAttribute('required') && !value) {
      this.showError(field, '필수 입력 항목입니다.');
      return false;
    }
    
    // Email validation
    if (type === 'email' && value && !validateEmail(value)) {
      this.showError(field, '올바른 이메일 형식이 아닙니다.');
      return false;
    }
    
    // Phone validation
    if (type === 'tel' && value && !validatePhone(value)) {
      this.showError(field, '올바른 전화번호 형식이 아닙니다. (예: 02-1234-5678)');
      return false;
    }
    
    return true;
  }

  showError(field, message) {
    field.classList.add('error');
    
    const errorEl = document.createElement('div');
    errorEl.className = 'field-error';
    errorEl.textContent = message;
    errorEl.style.color = 'var(--color-error)';
    errorEl.style.fontSize = 'var(--font-size-body-sm)';
    errorEl.style.marginTop = '8px';
    
    field.parentElement.appendChild(errorEl);
  }

  removeError(field) {
    field.classList.remove('error');
    const errorEl = field.parentElement.querySelector('.field-error');
    if (errorEl) {
      errorEl.remove();
    }
  }

  async submitForm() {
    const formData = new FormData(this.form);
    const submitBtn = this.form.querySelector('[type="submit"]');
    
    // Show loading
    submitBtn.disabled = true;
    submitBtn.textContent = '전송 중...';
    
    try {
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1500));
      
      showMessage('문의가 성공적으로 접수되었습니다.', 'success');
      this.form.reset();
    } catch (error) {
      showMessage('오류가 발생했습니다. 다시 시도해주세요.', 'error');
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = '상담 신청';
    }
  }
}

// Lightbox
class Lightbox {
  constructor() {
    this.lightbox = null;
    this.currentIndex = 0;
    this.images = [];
    this.init();
  }

  init() {
    this.createLightbox();
    this.bindEvents();
  }

  createLightbox() {
    this.lightbox = document.createElement('div');
    this.lightbox.className = 'lightbox';
    this.lightbox.innerHTML = `
      <div class="lightbox-overlay"></div>
      <div class="lightbox-content">
        <button class="lightbox-close">&times;</button>
        <button class="lightbox-prev">&larr;</button>
        <img class="lightbox-image" src="" alt="">
        <button class="lightbox-next">&rarr;</button>
      </div>
    `;
    
    // Add styles
    const style = document.createElement('style');
    style.textContent = `
      .lightbox {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 9999;
        display: none;
      }
      .lightbox.active {
        display: block;
      }
      .lightbox-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.95);
      }
      .lightbox-content {
        position: relative;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      .lightbox-image {
        max-width: 90%;
        max-height: 90%;
        object-fit: contain;
      }
      .lightbox-close,
      .lightbox-prev,
      .lightbox-next {
        position: absolute;
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: none;
        font-size: 32px;
        width: 50px;
        height: 50px;
        cursor: pointer;
        transition: background 0.3s;
      }
      .lightbox-close:hover,
      .lightbox-prev:hover,
      .lightbox-next:hover {
        background: rgba(255, 255, 255, 0.2);
      }
      .lightbox-close {
        top: 20px;
        right: 20px;
      }
      .lightbox-prev {
        left: 20px;
      }
      .lightbox-next {
        right: 20px;
      }
    `;
    
    document.head.appendChild(style);
    document.body.appendChild(this.lightbox);
  }

  bindEvents() {
    // Gallery items
    document.addEventListener('click', (e) => {
      if (e.target.closest('.gallery-item')) {
        const item = e.target.closest('.gallery-item');
        const img = item.querySelector('img');
        if (img) {
          this.open(img.src);
        }
      }
    });

    // Close
    this.lightbox.querySelector('.lightbox-close').addEventListener('click', () => this.close());
    this.lightbox.querySelector('.lightbox-overlay').addEventListener('click', () => this.close());

    // Navigation
    this.lightbox.querySelector('.lightbox-prev').addEventListener('click', () => this.prev());
    this.lightbox.querySelector('.lightbox-next').addEventListener('click', () => this.next());

    // Keyboard
    document.addEventListener('keydown', (e) => {
      if (!this.lightbox.classList.contains('active')) return;
      
      if (e.key === 'Escape') this.close();
      if (e.key === 'ArrowLeft') this.prev();
      if (e.key === 'ArrowRight') this.next();
    });
  }

  open(src) {
    this.lightbox.querySelector('.lightbox-image').src = src;
    this.lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  close() {
    this.lightbox.classList.remove('active');
    document.body.style.overflow = '';
  }

  prev() {
    // Implement if needed
  }

  next() {
    // Implement if needed
  }
}

// Scroll Animations
class ScrollAnimations {
  constructor() {
    this.elements = document.querySelectorAll('.fade-in, .scale-in');
    if (this.elements.length > 0) {
      this.init();
    }
  }

  init() {
    // Only use IntersectionObserver if GSAP is not available
    if (typeof gsap === 'undefined') {
      console.log('Using IntersectionObserver for animations');
      this.observe();
    } else {
      // GSAP will handle animations, but ensure elements are marked
      this.elements.forEach(el => {
        if (!el.classList.contains('will-animate')) {
          // If not marked by main.js, make visible immediately
          el.style.opacity = '1';
          el.style.transform = 'none';
        }
      });
    }
  }

  observe() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'none';
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    });

    this.elements.forEach(el => {
      // Ensure elements are visible by default
      if (!el.classList.contains('will-animate')) {
        el.style.opacity = '1';
        el.style.transform = 'none';
      } else {
        observer.observe(el);
      }
    });
  }
}

// Initialize components
document.addEventListener('DOMContentLoaded', () => {
  // Initialize header navigation
  new HeaderNav();
  
  // Initialize form validation if form exists
  const contactForm = document.querySelector('#contact-form');
  if (contactForm) {
    new FormValidator('#contact-form');
  }
  
  // Initialize lightbox
  new Lightbox();
  
  // Initialize scroll animations (fallback for non-GSAP)
  new ScrollAnimations();
  
  // Lazy load images
  lazyLoadImages();
});
