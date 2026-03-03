/**
 * (주)아이티로그 홈페이지 리뉴얼 - Components
 * 재사용 가능한 컴포넌트 로직
 */
'use strict';

// ========== Mobile Menu ==========
const MobileMenu = {
  init() {
    this.menuButton = document.querySelector('.js-menu-toggle');
    this.menu = document.querySelector('.js-mobile-menu');
    this.submenuToggles = document.querySelectorAll('.js-mobile-submenu-toggle');
    
    if (!this.menuButton || !this.menu) return;
    
    this.bindEvents();
  },

  bindEvents() {
    // Menu toggle
    this.menuButton.addEventListener('click', () => this.toggle());
    
    // Submenu toggles
    this.submenuToggles.forEach(toggle => {
      toggle.addEventListener('click', (e) => this.toggleSubmenu(e));
    });
    
    // Close on outside click
    document.addEventListener('click', (e) => this.handleOutsideClick(e));
    
    // Close on ESC key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && this.menu.classList.contains('is-open')) {
        this.close();
      }
    });
  },

  toggle() {
    const isExpanded = this.menuButton.getAttribute('aria-expanded') === 'true';
    this.menuButton.setAttribute('aria-expanded', !isExpanded);
    this.menu.classList.toggle('is-open');
    document.body.classList.toggle('menu-open');
    
    // Update aria-label
    this.menuButton.setAttribute('aria-label', isExpanded ? '메뉴 열기' : '메뉴 닫기');
  },

  toggleSubmenu(e) {
    const button = e.currentTarget;
    const submenu = button.nextElementSibling;
    const isExpanded = button.getAttribute('aria-expanded') === 'true';
    
    button.setAttribute('aria-expanded', !isExpanded);
    submenu.classList.toggle('is-open');
  },

  handleOutsideClick(e) {
    if (!e.target.closest('.js-mobile-menu') && 
        !e.target.closest('.js-menu-toggle') &&
        this.menu.classList.contains('is-open')) {
      this.close();
    }
  },

  close() {
    this.menuButton.setAttribute('aria-expanded', 'false');
    this.menuButton.setAttribute('aria-label', '메뉴 열기');
    this.menu.classList.remove('is-open');
    document.body.classList.remove('menu-open');
  }
};

// ========== Scroll Header ==========
const ScrollHeader = {
  init() {
    this.header = document.querySelector('.header');
    this.lastScroll = 0;
    this.scrollThreshold = 100;
    
    if (!this.header) return;
    
    this.bindEvents();
  },

  bindEvents() {
    window.addEventListener('scroll', Utils.throttle(() => this.handleScroll(), 100));
  },

  handleScroll() {
    const currentScroll = Utils.getScrollPosition();
    
    // Add scrolled class
    if (currentScroll > this.scrollThreshold) {
      this.header.classList.add('header--scrolled');
    } else {
      this.header.classList.remove('header--scrolled');
    }
    
    // Hide/show header on scroll
    if (currentScroll > this.lastScroll && currentScroll > 300) {
      this.header.classList.add('header--hidden');
    } else {
      this.header.classList.remove('header--hidden');
    }
    
    this.lastScroll = currentScroll;
  }
};

// ========== Back to Top Button ==========
const BackToTop = {
  init() {
    this.button = document.querySelector('.js-back-to-top');
    
    if (!this.button) return;
    
    this.bindEvents();
  },

  bindEvents() {
    window.addEventListener('scroll', Utils.throttle(() => this.handleScroll(), 100));
    this.button.addEventListener('click', () => this.scrollToTop());
  },

  handleScroll() {
    const scrollPosition = Utils.getScrollPosition();
    
    if (scrollPosition > 300) {
      this.button.classList.add('visible');
    } else {
      this.button.classList.remove('visible');
    }
  },

  scrollToTop() {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }
};

// ========== Smooth Scroll Links ==========
const SmoothScrollLinks = {
  init() {
    this.links = document.querySelectorAll('a[href^="#"]');
    
    if (!this.links.length) return;
    
    this.bindEvents();
  },

  bindEvents() {
    this.links.forEach(link => {
      link.addEventListener('click', (e) => this.handleClick(e));
    });
  },

  handleClick(e) {
    const href = e.currentTarget.getAttribute('href');
    
    if (href === '#' || href === '#!') return;
    
    e.preventDefault();
    
    const target = document.querySelector(href);
    if (!target) return;
    
    // Close mobile menu if open
    const mobileMenu = document.querySelector('.js-mobile-menu');
    if (mobileMenu && mobileMenu.classList.contains('is-open')) {
      MobileMenu.close();
    }
    
    // Smooth scroll to target
    const headerHeight = document.querySelector('.header')?.offsetHeight || 0;
    const targetPosition = target.offsetTop - headerHeight;
    
    window.scrollTo({
      top: targetPosition,
      behavior: 'smooth'
    });
  }
};

// ========== Form Validation ==========
const FormValidation = {
  init() {
    this.forms = document.querySelectorAll('form[data-validate]');
    
    if (!this.forms.length) return;
    
    this.bindEvents();
  },

  bindEvents() {
    this.forms.forEach(form => {
      // Real-time validation on blur
      const inputs = form.querySelectorAll('input, textarea, select');
      inputs.forEach(input => {
        input.addEventListener('blur', () => this.validateField(input));
        input.addEventListener('input', () => this.clearError(input));
      });
      
      // Form submission
      form.addEventListener('submit', (e) => this.handleSubmit(e));
    });
  },

  validateField(field) {
    const value = field.value.trim();
    const type = field.type;
    const required = field.hasAttribute('required') || field.hasAttribute('aria-required');
    
    // Clear previous error
    this.clearError(field);
    
    // Required check
    if (required && !value) {
      this.showError(field, '이 항목은 필수입니다');
      return false;
    }
    
    // Email validation
    if (type === 'email' && value && !Utils.validateEmail(value)) {
      this.showError(field, '올바른 이메일 주소를 입력해주세요');
      return false;
    }
    
    // Phone validation
    if (type === 'tel' && value) {
      const phoneRegex = /^[0-9-+()]*$/;
      if (!phoneRegex.test(value)) {
        this.showError(field, '올바른 전화번호를 입력해주세요');
        return false;
      }
    }
    
    // Min length check
    const minLength = field.getAttribute('minlength');
    if (minLength && value.length < parseInt(minLength)) {
      this.showError(field, `최소 ${minLength}자 이상 입력해주세요`);
      return false;
    }
    
    return true;
  },

  showError(field, message) {
    field.classList.add('error');
    field.setAttribute('aria-invalid', 'true');
    
    // Create or update error message
    let errorElement = field.parentElement.querySelector('.form-error');
    if (!errorElement) {
      errorElement = document.createElement('span');
      errorElement.className = 'form-error';
      errorElement.setAttribute('role', 'alert');
      field.parentElement.appendChild(errorElement);
    }
    errorElement.textContent = message;
  },

  clearError(field) {
    field.classList.remove('error');
    field.setAttribute('aria-invalid', 'false');
    
    const errorElement = field.parentElement.querySelector('.form-error');
    if (errorElement) {
      errorElement.remove();
    }
  },

  handleSubmit(e) {
    e.preventDefault();
    
    const form = e.target;
    const inputs = form.querySelectorAll('input, textarea, select');
    let isValid = true;
    
    // Validate all fields
    inputs.forEach(input => {
      if (!this.validateField(input)) {
        isValid = false;
      }
    });
    
    if (!isValid) {
      // Focus first error field
      const firstError = form.querySelector('.error');
      if (firstError) {
        firstError.focus();
      }
      return;
    }
    
    // Form is valid, submit
    console.log('Form is valid, submitting...');
    // Add your form submission logic here
  }
};

// ========== Tabs Component ==========
const Tabs = {
  init() {
    this.tabButtons = document.querySelectorAll('[role="tab"]');
    
    if (!this.tabButtons.length) return;
    
    this.bindEvents();
  },

  bindEvents() {
    this.tabButtons.forEach(button => {
      button.addEventListener('click', (e) => this.handleTabClick(e));
      button.addEventListener('keydown', (e) => this.handleKeyboard(e));
    });
  },

  handleTabClick(e) {
    const button = e.currentTarget;
    const targetId = button.getAttribute('aria-controls');
    const tabList = button.closest('[role="tablist"]');
    
    // Deactivate all tabs
    tabList.querySelectorAll('[role="tab"]').forEach(tab => {
      tab.setAttribute('aria-selected', 'false');
      tab.classList.remove('active');
    });
    
    // Hide all panels
    const panels = document.querySelectorAll('[role="tabpanel"]');
    panels.forEach(panel => {
      panel.setAttribute('hidden', 'true');
      panel.classList.remove('active');
    });
    
    // Activate selected tab
    button.setAttribute('aria-selected', 'true');
    button.classList.add('active');
    
    // Show selected panel
    const targetPanel = document.getElementById(targetId);
    if (targetPanel) {
      targetPanel.removeAttribute('hidden');
      targetPanel.classList.add('active');
    }
  },

  handleKeyboard(e) {
    const button = e.currentTarget;
    const tabList = button.closest('[role="tablist"]');
    const tabs = Array.from(tabList.querySelectorAll('[role="tab"]'));
    const currentIndex = tabs.indexOf(button);
    
    let nextTab;
    
    switch(e.key) {
      case 'ArrowLeft':
        e.preventDefault();
        nextTab = currentIndex > 0 ? tabs[currentIndex - 1] : tabs[tabs.length - 1];
        break;
      case 'ArrowRight':
        e.preventDefault();
        nextTab = currentIndex < tabs.length - 1 ? tabs[currentIndex + 1] : tabs[0];
        break;
      case 'Home':
        e.preventDefault();
        nextTab = tabs[0];
        break;
      case 'End':
        e.preventDefault();
        nextTab = tabs[tabs.length - 1];
        break;
    }
    
    if (nextTab) {
      nextTab.focus();
      nextTab.click();
    }
  }
};

// ========== Accordion Component ==========
const Accordion = {
  init() {
    this.triggers = document.querySelectorAll('.accordion__trigger');
    
    if (!this.triggers.length) return;
    
    this.bindEvents();
  },

  bindEvents() {
    this.triggers.forEach(trigger => {
      trigger.addEventListener('click', (e) => this.handleClick(e));
    });
  },

  handleClick(e) {
    const trigger = e.currentTarget;
    const content = trigger.nextElementSibling;
    const isExpanded = trigger.getAttribute('aria-expanded') === 'true';
    
    trigger.setAttribute('aria-expanded', !isExpanded);
    
    if (isExpanded) {
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + 'px';
    }
  }
};

// ========== Modal Component ==========
const Modal = {
  init() {
    this.triggers = document.querySelectorAll('[data-modal-trigger]');
    this.modals = document.querySelectorAll('.modal');
    
    if (!this.triggers.length && !this.modals.length) return;
    
    this.bindEvents();
  },

  bindEvents() {
    // Modal triggers
    this.triggers.forEach(trigger => {
      trigger.addEventListener('click', (e) => this.open(e));
    });
    
    // Close buttons
    document.querySelectorAll('.modal__close, [data-modal-close]').forEach(btn => {
      btn.addEventListener('click', (e) => this.close(e));
    });
    
    // Backdrop click
    document.querySelectorAll('.modal-backdrop').forEach(backdrop => {
      backdrop.addEventListener('click', (e) => {
        if (e.target === backdrop) {
          this.close(e);
        }
      });
    });
    
    // ESC key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        const activeModal = document.querySelector('.modal.active');
        if (activeModal) {
          this.closeModal(activeModal);
        }
      }
    });
  },

  open(e) {
    e.preventDefault();
    const trigger = e.currentTarget;
    const modalId = trigger.getAttribute('data-modal-trigger');
    const modal = document.getElementById(modalId);
    const backdrop = modal?.previousElementSibling;
    
    if (modal && backdrop) {
      backdrop.classList.add('active');
      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
      
      // Focus first focusable element
      const focusable = modal.querySelector('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
      if (focusable) {
        focusable.focus();
      }
    }
  },

  close(e) {
    const modal = e.target.closest('.modal');
    if (modal) {
      this.closeModal(modal);
    }
  },

  closeModal(modal) {
    const backdrop = modal.previousElementSibling;
    
    if (backdrop) {
      backdrop.classList.remove('active');
    }
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
};
