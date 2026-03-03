// Main - Template2
// 메인 초기화 및 전역 설정

// Intersection Observer를 사용한 스크롤 애니메이션
function initScrollAnimation() {
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  // .fade-in-up 요소들 관찰
  document.querySelectorAll('.fade-in-up').forEach(element => {
    observer.observe(element);
  });
}

// 카운터 애니메이션
function initCounterAnimation() {
  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counter = entry.target;
        const targetText = counter.textContent;
        const targetNumber = parseInt(targetText.replace(/[^0-9.]/g, ''));
        const isDecimal = targetText.includes('.');
        const suffix = targetText.replace(/[0-9.,]/g, '');
        
        let current = 0;
        const increment = targetNumber / 60; // 약 1초 동안 애니메이션
        const duration = 1500;
        const startTime = Date.now();
        
        const updateCounter = () => {
          const elapsed = Date.now() - startTime;
          const progress = Math.min(elapsed / duration, 1);
          
          current = targetNumber * progress;
          
          if (isDecimal) {
            counter.textContent = current.toFixed(1) + suffix;
          } else {
            counter.textContent = Math.floor(current).toLocaleString() + suffix;
          }
          
          if (progress < 1) {
            requestAnimationFrame(updateCounter);
          }
        };
        
        updateCounter();
        counterObserver.unobserve(counter);
      }
    });
  }, { threshold: 0.5 });
  
  document.querySelectorAll('.counter-number').forEach(counter => {
    counterObserver.observe(counter);
  });
}

// Swiper 초기화 (CDN 로드 후)
function initSwiper() {
  if (typeof Swiper === 'undefined') {
    console.warn('Swiper not loaded');
    return;
  }
  
  // 히어로 슬라이더
  const heroSwiper = document.querySelector('.hero-swiper');
  if (heroSwiper) {
    new Swiper('.hero-swiper', {
      loop: true,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false
      },
      effect: 'fade',
      fadeEffect: {
        crossFade: true
      },
      pagination: {
        el: '.hero-indicators',
        clickable: true,
        bulletClass: 'hero-indicator',
        bulletActiveClass: 'active'
      },
      navigation: {
        nextEl: '.hero-arrow-next',
        prevEl: '.hero-arrow-prev'
      }
    });
  }
}

// 카카오맵 초기화
function initKakaoMap() {
  if (typeof kakao === 'undefined' || !kakao.maps) {
    console.warn('Kakao Maps not loaded');
    return;
  }
  
  const mapContainer = document.getElementById('kakao-map');
  if (!mapContainer) return;
  
  // 회사 위치 좌표 (실제 좌표로 변경 필요)
  const position = new kakao.maps.LatLng(37.5665, 126.9780);
  
  const mapOptions = {
    center: position,
    level: 3
  };
  
  const map = new kakao.maps.Map(mapContainer, mapOptions);
  
  // 마커 생성
  const marker = new kakao.maps.Marker({
    position: position,
    map: map
  });
  
  // 인포윈도우 생성
  const infowindow = new kakao.maps.InfoWindow({
    content: '<div style="padding:10px;">(주)아이티로그</div>'
  });
  
  infowindow.open(map, marker);
}

// 이미지 라이트박스
function initLightbox() {
  const images = document.querySelectorAll('[data-lightbox]');
  
  images.forEach(img => {
    img.style.cursor = 'pointer';
    img.addEventListener('click', () => {
      const lightbox = createLightbox(img.src, img.alt);
      document.body.appendChild(lightbox);
    });
  });
}

function createLightbox(src, alt) {
  const lightbox = document.createElement('div');
  lightbox.className = 'lightbox';
  lightbox.innerHTML = `
    <div class="lightbox-backdrop"></div>
    <div class="lightbox-content">
      <button class="lightbox-close">&times;</button>
      <img src="${src}" alt="${alt}">
    </div>
  `;
  
  // 스타일 추가
  const style = document.createElement('style');
  style.textContent = `
    .lightbox {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .lightbox-backdrop {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.9);
    }
    .lightbox-content {
      position: relative;
      max-width: 90%;
      max-height: 90%;
      z-index: 1;
    }
    .lightbox-content img {
      max-width: 100%;
      max-height: 90vh;
      object-fit: contain;
    }
    .lightbox-close {
      position: absolute;
      top: -40px;
      right: 0;
      background: none;
      border: none;
      color: white;
      font-size: 40px;
      cursor: pointer;
      line-height: 1;
    }
  `;
  document.head.appendChild(style);
  
  // 닫기 이벤트
  const close = () => {
    lightbox.remove();
    style.remove();
  };
  
  lightbox.querySelector('.lightbox-backdrop').addEventListener('click', close);
  lightbox.querySelector('.lightbox-close').addEventListener('click', close);
  
  document.addEventListener('keydown', function escHandler(e) {
    if (e.key === 'Escape') {
      close();
      document.removeEventListener('keydown', escHandler);
    }
  });
  
  return lightbox;
}

// 스무스 스크롤 링크
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#') return;
      
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        const headerHeight = document.querySelector('.header')?.offsetHeight || 0;
        smoothScrollTo(target, headerHeight);
      }
    });
  });
}

// 페이지 로드 완료 후 초기화
window.addEventListener('load', () => {
  // 스크롤 애니메이션 초기화
  initScrollAnimation();
  initCounterAnimation();
  
  // 외부 라이브러리 초기화
  initSwiper();
  initKakaoMap();
  
  // 기능 초기화
  initLightbox();
  initSmoothScroll();
  
  // 페이지 로딩 완료 표시
  document.body.classList.add('loaded');
});

// 페이지 언로드 시 정리
window.addEventListener('beforeunload', () => {
  // 필요한 정리 작업
});
