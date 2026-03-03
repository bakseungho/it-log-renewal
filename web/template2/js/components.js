// Components - Template2
// UI 컴포넌트 초기화 및 관리

// Header Component
class Header {
  constructor() {
    this.header = document.querySelector('.header');
    this.hamburger = document.querySelector('.hamburger');
    this.mobileMenu = document.querySelector('.mobile-menu');
    this.mobileBackdrop = document.querySelector('.mobile-menu-backdrop');
    this.mobileNavLinks = document.querySelectorAll('.mobile-nav-link');
    
    this.init();
  }
  
  init() {
    this.handleScroll();
    this.handleMobileMenu();
    this.handleDropdowns();
    
    window.addEventListener('scroll', throttle(() => this.handleScroll(), 100));
  }
  
  handleScroll() {
    if (window.scrollY > 50) {
      this.header?.classList.add('scrolled');
    } else {
      this.header?.classList.remove('scrolled');
    }
  }
  
  handleMobileMenu() {
    this.hamburger?.addEventListener('click', () => this.toggleMobileMenu());
    this.mobileBackdrop?.addEventListener('click', () => this.closeMobileMenu());
    
    // ESC 키로 메뉴 닫기
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && this.mobileMenu?.classList.contains('active')) {
        this.closeMobileMenu();
      }
    });
  }
  
  toggleMobileMenu() {
    this.hamburger?.classList.toggle('active');
    this.mobileMenu?.classList.toggle('active');
    this.mobileBackdrop?.classList.toggle('active');
    document.body.style.overflow = this.mobileMenu?.classList.contains('active') ? 'hidden' : '';
  }
  
  closeMobileMenu() {
    this.hamburger?.classList.remove('active');
    this.mobileMenu?.classList.remove('active');
    this.mobileBackdrop?.classList.remove('active');
    document.body.style.overflow = '';
  }
  
  handleDropdowns() {
    this.mobileNavLinks.forEach(link => {
      link.addEventListener('click', (e) => {
        const parent = link.parentElement;
        const dropdown = parent.querySelector('.mobile-dropdown');
        
        if (dropdown) {
          e.preventDefault();
          link.classList.toggle('active');
          dropdown.classList.toggle('active');
        }
      });
    });
  }
}

// Hero Slider Component
class HeroSlider {
  constructor(selector) {
    this.slider = document.querySelector(selector);
    if (!this.slider) return;
    
    this.slides = this.slider.querySelectorAll('.hero-slide');
    this.prevBtn = this.slider.querySelector('.hero-arrow-prev');
    this.nextBtn = this.slider.querySelector('.hero-arrow-next');
    this.indicators = this.slider.querySelectorAll('.hero-indicator');
    
    this.currentSlide = 0;
    this.autoplayInterval = null;
    this.autoplayDelay = 5000;
    
    this.init();
  }
  
  init() {
    if (this.slides.length === 0) return;
    
    this.showSlide(0);
    this.startAutoplay();
    
    this.prevBtn?.addEventListener('click', () => this.prevSlide());
    this.nextBtn?.addEventListener('click', () => this.nextSlide());
    
    this.indicators.forEach((indicator, index) => {
      indicator.addEventListener('click', () => this.goToSlide(index));
    });
    
    // 마우스 호버 시 자동 재생 일시 정지
    this.slider.addEventListener('mouseenter', () => this.stopAutoplay());
    this.slider.addEventListener('mouseleave', () => this.startAutoplay());
  }
  
  showSlide(index) {
    this.slides.forEach(slide => slide.classList.remove('active'));
    this.indicators.forEach(indicator => indicator.classList.remove('active'));
    
    this.slides[index]?.classList.add('active');
    this.indicators[index]?.classList.add('active');
    this.currentSlide = index;
  }
  
  nextSlide() {
    const next = (this.currentSlide + 1) % this.slides.length;
    this.goToSlide(next);
  }
  
  prevSlide() {
    const prev = (this.currentSlide - 1 + this.slides.length) % this.slides.length;
    this.goToSlide(prev);
  }
  
  goToSlide(index) {
    this.showSlide(index);
    this.resetAutoplay();
  }
  
  startAutoplay() {
    this.autoplayInterval = setInterval(() => this.nextSlide(), this.autoplayDelay);
  }
  
  stopAutoplay() {
    if (this.autoplayInterval) {
      clearInterval(this.autoplayInterval);
      this.autoplayInterval = null;
    }
  }
  
  resetAutoplay() {
    this.stopAutoplay();
    this.startAutoplay();
  }
}

// Scroll Animation Component
class ScrollAnimation {
  constructor() {
    this.elements = document.querySelectorAll('.fade-in-up');
    this.init();
  }
  
  init() {
    if (this.elements.length === 0) return;
    
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
      }
    );
    
    this.elements.forEach(el => observer.observe(el));
  }
}

// Counter Animation Component
class CounterAnimation {
  constructor() {
    this.counters = document.querySelectorAll('.counter-number');
    this.init();
  }
  
  init() {
    if (this.counters.length === 0) return;
    
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            this.animateCounter(entry.target);
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );
    
    this.counters.forEach(counter => observer.observe(counter));
  }
  
  animateCounter(element) {
    const target = parseInt(element.textContent.replace(/[^0-9]/g, ''));
    const duration = 2000;
    const increment = target / (duration / 16);
    let current = 0;
    
    const updateCounter = () => {
      current += increment;
      if (current < target) {
        element.textContent = Math.floor(current).toLocaleString() + '+';
        requestAnimationFrame(updateCounter);
      } else {
        element.textContent = target.toLocaleString() + '+';
      }
    };
    
    updateCounter();
  }
}

// Back to Top Button Component
class BackToTop {
  constructor() {
    this.button = document.querySelector('.back-to-top');
    if (!this.button) return;
    
    this.init();
  }
  
  init() {
    window.addEventListener('scroll', throttle(() => this.handleScroll(), 100));
    this.button.addEventListener('click', () => this.scrollToTop());
  }
  
  handleScroll() {
    if (window.scrollY > 300) {
      this.button.classList.add('visible');
    } else {
      this.button.classList.remove('visible');
    }
  }
  
  scrollToTop() {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }
}

// Form Validation Component
class FormValidation {
  constructor(formSelector) {
    this.form = document.querySelector(formSelector);
    if (!this.form) return;
    
    this.init();
  }
  
  init() {
    this.form.addEventListener('submit', (e) => this.handleSubmit(e));
    
    // 실시간 유효성 검사
    const inputs = this.form.querySelectorAll('input, textarea');
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
    let isValid = true;
    let errorMessage = '';
    
    // 필수 입력 확인
    if (field.hasAttribute('required') && !value) {
      isValid = false;
      errorMessage = '필수 입력 항목입니다.';
    }
    
    // 이메일 유효성 검사
    if (type === 'email' && value && !validateEmail(value)) {
      isValid = false;
      errorMessage = '올바른 이메일 형식이 아닙니다.';
    }
    
    // 전화번호 유효성 검사
    if (name === 'phone' && value && !validatePhone(value)) {
      isValid = false;
      errorMessage = '올바른 전화번호 형식이 아닙니다.';
    }
    
    // 최소 길이 확인
    if (field.hasAttribute('minlength')) {
      const minLength = parseInt(field.getAttribute('minlength'));
      if (value.length < minLength) {
        isValid = false;
        errorMessage = `최소 ${minLength}자 이상 입력해주세요.`;
      }
    }
    
    this.showFieldError(field, isValid, errorMessage);
    return isValid;
  }
  
  showFieldError(field, isValid, message) {
    const formGroup = field.closest('.form-group');
    let errorElement = formGroup?.querySelector('.form-error');
    
    if (!isValid) {
      field.classList.add('error');
      
      if (!errorElement) {
        errorElement = document.createElement('div');
        errorElement.className = 'form-error';
        formGroup?.appendChild(errorElement);
      }
      
      errorElement.textContent = message;
    } else {
      field.classList.remove('error');
      if (errorElement) {
        errorElement.remove();
      }
    }
  }
  
  async submitForm() {
    const formData = new FormData(this.form);
    const submitButton = this.form.querySelector('[type="submit"]');
    
    // 버튼 비활성화
    submitButton.disabled = true;
    submitButton.textContent = '전송 중...';
    
    try {
      // FormSubmit 또는 다른 서비스로 전송
      // 실제 구현 시 엔드포인트 URL 설정 필요
      const response = await fetch(this.form.action, {
        method: 'POST',
        body: formData
      });
      
      if (response.ok) {
        this.showAlert('success', '문의가 성공적으로 전송되었습니다.');
        this.form.reset();
      } else {
        throw new Error('전송 실패');
      }
    } catch (error) {
      this.showAlert('error', '문의 전송에 실패했습니다. 다시 시도해주세요.');
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = '문의하기';
    }
  }
  
  showAlert(type, message) {
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;
    
    this.form.insertBefore(alert, this.form.firstChild);
    
    setTimeout(() => alert.remove(), 5000);
  }
}

// 초기화
document.addEventListener('DOMContentLoaded', () => {
  // 공통 컴포넌트 초기화
  new Header();
  new ScrollAnimation();
  new BackToTop();
  
  // 페이지별 컴포넌트 초기화
  if (document.querySelector('.hero')) {
    new HeroSlider('.hero');
  }
  
  if (document.querySelector('.counter-number')) {
    new CounterAnimation();
  }
  
  if (document.querySelector('#contact-form')) {
    new FormValidation('#contact-form');
  }
  
  // 현재 페이지 활성화
  setActiveNavItem();
  
  // 레이지 로딩 (네이티브 지원 안 되는 경우)
  if ('loading' in HTMLImageElement.prototype === false) {
    lazyLoadImages();
  }
});
