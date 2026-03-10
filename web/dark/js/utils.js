// Utility Functions - Template3

// Smooth Scroll
function smoothScroll(target, duration = 1000) {
  const targetElement = document.querySelector(target);
  if (!targetElement) return;

  const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset;
  const startPosition = window.pageYOffset;
  const distance = targetPosition - startPosition;
  let startTime = null;

  function animation(currentTime) {
    if (startTime === null) startTime = currentTime;
    const timeElapsed = currentTime - startTime;
    const run = ease(timeElapsed, startPosition, distance, duration);
    window.scrollTo(0, run);
    if (timeElapsed < duration) requestAnimationFrame(animation);
  }

  function ease(t, b, c, d) {
    t /= d / 2;
    if (t < 1) return c / 2 * t * t + b;
    t--;
    return -c / 2 * (t * (t - 2) - 1) + b;
  }

  requestAnimationFrame(animation);
}

// Debounce
function debounce(func, wait = 300) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// Throttle
function throttle(func, limit = 300) {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

// Lazy Load Images
function lazyLoadImages() {
  const images = document.querySelectorAll('img[data-src]');
  
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.removeAttribute('data-src');
        observer.unobserve(img);
      }
    });
  });

  images.forEach(img => imageObserver.observe(img));
}

// Counter Animation
function animateCounter(element, target, duration = 2000) {
  const start = 0;
  const increment = target / (duration / 16);
  let current = start;

  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      element.textContent = Math.ceil(target);
      clearInterval(timer);
    } else {
      element.textContent = Math.ceil(current);
    }
  }, 16);
}

// Format Number
function formatNumber(num) {
  return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// Validate Email
function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}

// Validate Phone
function validatePhone(phone) {
  const re = /^[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}$/;
  return re.test(phone);
}

// Show Message
function showMessage(message, type = 'success') {
  const messageEl = document.createElement('div');
  messageEl.className = `message message-${type}`;
  messageEl.textContent = message;
  
  document.body.appendChild(messageEl);
  
  setTimeout(() => {
    messageEl.style.opacity = '0';
    setTimeout(() => messageEl.remove(), 300);
  }, 3000);
}

// Get Query Parameter
function getQueryParam(param) {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get(param);
}

// Set Cookie
function setCookie(name, value, days = 7) {
  const expires = new Date();
  expires.setTime(expires.getTime() + days * 24 * 60 * 60 * 1000);
  document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
}

// Get Cookie
function getCookie(name) {
  const nameEQ = name + "=";
  const ca = document.cookie.split(';');
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) === ' ') c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
}

// Delete Cookie
function deleteCookie(name) {
  document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:01 GMT;path=/`;
}

// Check if Element in Viewport
function isInViewport(element) {
  const rect = element.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}

// Get Scroll Percentage
function getScrollPercentage() {
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  return (scrollTop / scrollHeight) * 100;
}

// Export functions
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    smoothScroll,
    debounce,
    throttle,
    lazyLoadImages,
    animateCounter,
    formatNumber,
    validateEmail,
    validatePhone,
    showMessage,
    getQueryParam,
    setCookie,
    getCookie,
    deleteCookie,
    isInViewport,
    getScrollPercentage
  };
}
