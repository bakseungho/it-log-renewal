# Template3 사용자 인터랙션 개선 사항

## 🎬 1. 히어로 섹션 애니메이션

### 1.1 텍스트 슬라이드 업 + 페이드 인 (순차적)

**구현 방법**:
```javascript
// Swiper 슬라이드 전환 시 실행
swiper.on('slideChange', function() {
  const activeSlide = swiper.slides[swiper.activeIndex];
  const elements = activeSlide.querySelectorAll('.hero-subtitle, .hero-title, .hero-description, .hero-actions');
  
  elements.forEach((el, index) => {
    gsap.fromTo(el, 
      {
        opacity: 0,
        y: 30
      },
      {
        opacity: 1,
        y: 0,
        duration: 0.8,
        delay: index * 0.2, // 0.2초씩 순차 딜레이
        ease: 'power2.out'
      }
    );
  });
});
```

**타이밍**:
- 서브타이틀: 0.2초 딜레이
- 타이틀: 0.4초 딜레이
- 설명: 0.6초 딜레이
- CTA 버튼: 0.8초 딜레이

**추가 효과 (타이틀 단어별 애니메이션)**:
```javascript
// 타이틀을 단어별로 분리하여 애니메이션
const titleWords = title.textContent.split(' ');
title.innerHTML = titleWords.map(word => 
  `<span class="word">${word}</span>`
).join(' ');

gsap.from('.hero-title .word', {
  opacity: 0,
  y: 20,
  duration: 0.6,
  stagger: 0.1, // 단어별 0.1초 딜레이
  delay: 0.4,
  ease: 'power2.out'
});
```

---

### 1.2 배경 이미지 줌아웃 효과

**구현 방법**:
```css
/* CSS 애니메이션 */
.hero-background {
  animation: zoomOut 6s ease-out forwards;
}

@keyframes zoomOut {
  from {
    transform: scale(1.1);
  }
  to {
    transform: scale(1.0);
  }
}
```

**또는 GSAP 사용**:
```javascript
swiper.on('slideChange', function() {
  const activeSlide = swiper.slides[swiper.activeIndex];
  const background = activeSlide.querySelector('.hero-background');
  
  gsap.fromTo(background,
    { scale: 1.1 },
    { 
      scale: 1.0,
      duration: 6,
      ease: 'power1.out'
    }
  );
});
```

---

### 1.3 슬라이드 전환 타이밍 조정

**현재**: 5초 자동 전환
**개선**: 6초 자동 전환

```javascript
new Swiper('.hero-swiper', {
  autoplay: {
    delay: 6000, // 5000 → 6000
    disableOnInteraction: false,
  },
  speed: 1000,
  // ... 기타 설정
});
```

**이유**: 사용자가 콘텐츠를 충분히 읽을 시간 확보

---

## 🖱️ 2. 버튼 인터랙션

### 2.1 Primary 버튼

**Hover 효과**:
```css
.btn-primary {
  background: linear-gradient(135deg, #0066FF 0%, #00D9FF 100%);
  transition: all 0.3s ease;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 102, 255, 0.4);
}

.btn-primary:active {
  transform: translateY(0);
  box-shadow: 0 4px 12px rgba(0, 102, 255, 0.3);
}
```

**로딩 상태**:
```css
.btn-primary.loading {
  pointer-events: none;
  opacity: 0.7;
}

.btn-primary.loading::after {
  content: '';
  width: 16px;
  height: 16px;
  border: 2px solid #ffffff;
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  display: inline-block;
  margin-left: 8px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

---

### 2.2 Outline 버튼

**Hover 효과**:
```css
.btn-outline {
  background: transparent;
  border: 2px solid rgba(255, 255, 255, 0.3);
  color: #ffffff;
  transition: all 0.3s ease;
}

.btn-outline:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.6);
  transform: translateY(-2px);
}
```

---

### 2.3 버튼 리플 효과 (선택적)

```javascript
// 클릭 시 리플 효과
document.querySelectorAll('.btn').forEach(button => {
  button.addEventListener('click', function(e) {
    const ripple = document.createElement('span');
    ripple.classList.add('ripple');
    
    const rect = this.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = e.clientX - rect.left - size / 2;
    const y = e.clientY - rect.top - size / 2;
    
    ripple.style.width = ripple.style.height = size + 'px';
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    
    this.appendChild(ripple);
    
    setTimeout(() => ripple.remove(), 600);
  });
});
```

```css
.btn {
  position: relative;
  overflow: hidden;
}

.ripple {
  position: absolute;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.5);
  transform: scale(0);
  animation: ripple-animation 0.6s ease-out;
}

@keyframes ripple-animation {
  to {
    transform: scale(4);
    opacity: 0;
  }
}
```

---

## 🃏 3. 카드 인터랙션

### 3.1 솔루션 카드

**Hover 효과**:
```css
.card-solution {
  transition: all 0.3s ease;
  cursor: pointer;
}

.card-solution:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 40px rgba(0, 102, 255, 0.2);
  border-color: rgba(0, 102, 255, 0.3);
}

/* 아이콘 회전 효과 */
.card-solution:hover .icon {
  transform: scale(1.1) rotate(5deg);
  transition: transform 0.3s ease;
}

/* 화살표 이동 효과 */
.card-solution:hover .btn-text::after {
  content: ' →';
  transform: translateX(4px);
  transition: transform 0.3s ease;
}
```

**GSAP 버전**:
```javascript
document.querySelectorAll('.card-solution').forEach(card => {
  card.addEventListener('mouseenter', function() {
    gsap.to(this, {
      y: -8,
      duration: 0.3,
      ease: 'power2.out'
    });
    
    gsap.to(this.querySelector('.icon'), {
      scale: 1.1,
      rotation: 5,
      duration: 0.3,
      ease: 'back.out(1.7)'
    });
  });
  
  card.addEventListener('mouseleave', function() {
    gsap.to(this, {
      y: 0,
      duration: 0.3,
      ease: 'power2.out'
    });
    
    gsap.to(this.querySelector('.icon'), {
      scale: 1,
      rotation: 0,
      duration: 0.3,
      ease: 'power2.out'
    });
  });
});
```

---

### 3.2 시공사례 카드

**Hover 효과 (이미지 줌인 + 오버레이)**:
```css
.card-project {
  overflow: hidden;
  cursor: pointer;
}

.card-project .image {
  transition: transform 0.5s ease;
}

.card-project:hover .image {
  transform: scale(1.05);
}

/* 오버레이 표시 */
.card-project::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 102, 255, 0.8);
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 1;
}

.card-project:hover::before {
  opacity: 1;
}

/* "자세히 보기" 텍스트 */
.card-project::after {
  content: '자세히 보기';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #ffffff;
  font-size: 1.25rem;
  font-weight: 600;
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 2;
}

.card-project:hover::after {
  opacity: 1;
}
```

---

### 3.3 숫자 카운터 애니메이션

**현재 구현**: GSAP ScrollTrigger 사용
**개선**: 더 부드러운 이징 함수

```javascript
ScrollTrigger.create({
  trigger: '.trust-stats',
  start: 'top 80%',
  once: true,
  onEnter: () => {
    document.querySelectorAll('.card-stat .number').forEach(counter => {
      const target = parseFloat(counter.getAttribute('data-target'));
      const suffix = counter.textContent.replace(/[\d.]/g, '');
      
      gsap.to({ value: 0 }, {
        value: target,
        duration: 2.5,
        ease: 'power2.out', // 또는 'expo.out'
        onUpdate: function() {
          const current = this.targets()[0].value;
          const formatted = target % 1 === 0 
            ? Math.ceil(current) 
            : current.toFixed(1);
          counter.textContent = formatted + suffix;
        }
      });
    });
  }
});
```

---

## 🎯 4. 필터링 인터랙션

### 4.1 시공사례 필터 탭

**HTML 구조**:
```html
<div class="filter-tabs">
  <button class="filter-tab active" data-filter="all">전체</button>
  <button class="filter-tab" data-filter="ai">AI 영상</button>
  <button class="filter-tab" data-filter="crane">타워크레인</button>
  <button class="filter-tab" data-filter="access">출입통제</button>
  <button class="filter-tab" data-filter="sensor">환경센서</button>
  <button class="filter-tab" data-filter="safety">통합안전</button>
</div>
```

**CSS**:
```css
.filter-tab {
  padding: 12px 24px;
  background: rgba(26, 26, 26, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #a0a0a0;
  cursor: pointer;
  transition: all 0.3s ease;
}

.filter-tab:hover {
  background: rgba(42, 42, 42, 0.9);
  color: #ffffff;
}

.filter-tab.active {
  background: rgba(0, 102, 255, 0.2);
  border-color: #0066FF;
  color: #0066FF;
}
```

**JavaScript (필터링 로직)**:
```javascript
const filterTabs = document.querySelectorAll('.filter-tab');
const projectCards = document.querySelectorAll('.card-project');

filterTabs.forEach(tab => {
  tab.addEventListener('click', function() {
    // 활성 탭 변경
    filterTabs.forEach(t => t.classList.remove('active'));
    this.classList.add('active');
    
    const filter = this.getAttribute('data-filter');
    
    // 카드 필터링 애니메이션
    projectCards.forEach(card => {
      const category = card.getAttribute('data-category');
      
      if (filter === 'all' || category === filter) {
        gsap.to(card, {
          opacity: 1,
          scale: 1,
          duration: 0.3,
          display: 'block'
        });
      } else {
        gsap.to(card, {
          opacity: 0,
          scale: 0.8,
          duration: 0.3,
          onComplete: () => {
            card.style.display = 'none';
          }
        });
      }
    });
  });
});
```

---

## 📜 5. 스크롤 인터랙션

### 5.1 스크롤 진행 표시 바 (선택적)

```javascript
function initScrollProgress() {
  const progressBar = document.createElement('div');
  progressBar.className = 'scroll-progress';
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
```

```css
.scroll-progress {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background: linear-gradient(90deg, #0066FF 0%, #00D9FF 100%);
  transform-origin: left;
  transform: scaleX(0);
  z-index: 9999;
}
```

---

### 5.2 Sticky CTA 버튼 (선택적)

```javascript
// 스크롤 시 CTA 버튼 표시
ScrollTrigger.create({
  start: 'top -100',
  end: 'max',
  onUpdate: (self) => {
    const stickyCTA = document.querySelector('.sticky-cta');
    if (self.direction === 1 && self.progress > 0.1) {
      // 아래로 스크롤
      stickyCTA.classList.add('visible');
    } else if (self.direction === -1 || self.progress < 0.1) {
      // 위로 스크롤 또는 상단 근처
      stickyCTA.classList.remove('visible');
    }
  }
});
```

```css
.sticky-cta {
  position: fixed;
  bottom: 24px;
  right: 24px;
  transform: translateY(100px);
  opacity: 0;
  transition: all 0.3s ease;
  z-index: 1000;
}

.sticky-cta.visible {
  transform: translateY(0);
  opacity: 1;
}
```

---

### 5.3 부드러운 앵커 스크롤

**현재 구현**: GSAP ScrollToPlugin 사용
**개선**: 오프셋 조정 및 콜백 추가

```javascript
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const href = this.getAttribute('href');
    if (href === '#' || href.length <= 1) return;
    
    e.preventDefault();
    const target = document.querySelector(href);
    
    if (target) {
      gsap.to(window, {
        duration: 1,
        scrollTo: {
          y: target,
          offsetY: 80 // 헤더 높이만큼 오프셋
        },
        ease: 'power2.inOut',
        onComplete: () => {
          // 스크롤 완료 후 포커스 이동 (접근성)
          target.setAttribute('tabindex', '-1');
          target.focus();
        }
      });
    }
  });
});
```

---

## 🎨 6. 로딩 상태 인터랙션

### 6.1 페이지 로드 애니메이션

```javascript
window.addEventListener('load', () => {
  // 로딩 오버레이 페이드 아웃
  const loader = document.querySelector('.page-loader');
  if (loader) {
    gsap.to(loader, {
      opacity: 0,
      duration: 0.5,
      onComplete: () => loader.remove()
    });
  }
  
  // 페이지 콘텐츠 페이드 인
  gsap.from('body', {
    opacity: 0,
    duration: 0.5,
    ease: 'power2.out'
  });
});
```

```html
<!-- HTML에 추가 -->
<div class="page-loader">
  <div class="loader-spinner"></div>
</div>
```

```css
.page-loader {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #0a0a0a;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10000;
}

.loader-spinner {
  width: 48px;
  height: 48px;
  border: 4px solid rgba(0, 102, 255, 0.2);
  border-top-color: #0066FF;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
```

---

## 🔔 7. 피드백 인터랙션

### 7.1 폼 제출 피드백

```javascript
// 문의하기 폼 제출
document.querySelector('.contact-form').addEventListener('submit', async function(e) {
  e.preventDefault();
  
  const submitBtn = this.querySelector('.btn-submit');
  submitBtn.classList.add('loading');
  submitBtn.disabled = true;
  
  try {
    // API 호출
    const response = await fetch('/api/contact', {
      method: 'POST',
      body: new FormData(this)
    });
    
    if (response.ok) {
      // 성공 메시지
      showNotification('문의가 성공적으로 전송되었습니다!', 'success');
      this.reset();
    } else {
      throw new Error('전송 실패');
    }
  } catch (error) {
    // 에러 메시지
    showNotification('전송 중 오류가 발생했습니다. 다시 시도해주세요.', 'error');
  } finally {
    submitBtn.classList.remove('loading');
    submitBtn.disabled = false;
  }
});
```

---

### 7.2 토스트 알림

```javascript
function showNotification(message, type = 'info') {
  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.textContent = message;
  
  document.body.appendChild(toast);
  
  gsap.fromTo(toast,
    { opacity: 0, y: -20 },
    { 
      opacity: 1, 
      y: 0, 
      duration: 0.3,
      onComplete: () => {
        setTimeout(() => {
          gsap.to(toast, {
            opacity: 0,
            y: -20,
            duration: 0.3,
            onComplete: () => toast.remove()
          });
        }, 3000);
      }
    }
  );
}
```

```css
.toast {
  position: fixed;
  top: 24px;
  right: 24px;
  padding: 16px 24px;
  border-radius: 8px;
  color: #ffffff;
  font-weight: 500;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
  z-index: 10000;
}

.toast-success {
  background: linear-gradient(135deg, #00ff88 0%, #00cc6a 100%);
}

.toast-error {
  background: linear-gradient(135deg, #ff4444 0%, #cc0000 100%);
}

.toast-info {
  background: linear-gradient(135deg, #0066FF 0%, #00D9FF 100%);
}
```

---

## ♿ 8. 접근성 인터랙션

### 8.1 키보드 네비게이션

```javascript
// 포커스 표시 강화
document.addEventListener('keydown', function(e) {
  if (e.key === 'Tab') {
    document.body.classList.add('keyboard-nav');
  }
});

document.addEventListener('mousedown', function() {
  document.body.classList.remove('keyboard-nav');
});
```

```css
/* 키보드 네비게이션 시에만 포커스 표시 */
.keyboard-nav *:focus {
  outline: 2px solid #0066FF;
  outline-offset: 2px;
}

/* 마우스 사용 시 포커스 표시 제거 */
*:focus {
  outline: none;
}
```

---

### 8.2 Skip to Content 링크

```html
<a href="#main-content" class="skip-link">본문으로 건너뛰기</a>
```

```css
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #0066FF;
  color: #ffffff;
  padding: 8px 16px;
  text-decoration: none;
  z-index: 10000;
}

.skip-link:focus {
  top: 0;
}
```

---

## 📱 9. 모바일 인터랙션

### 9.1 터치 피드백

```css
/* 터치 시 하이라이트 제거 */
* {
  -webkit-tap-highlight-color: transparent;
}

/* 커스텀 터치 피드백 */
.btn:active,
.card:active {
  transform: scale(0.98);
  transition: transform 0.1s ease;
}
```

---

### 9.2 스와이프 제스처 (시공사례)

```javascript
// Hammer.js 또는 Swiper 사용
const projectsContainer = document.querySelector('.projects-grid');

if (window.innerWidth <= 767) {
  new Swiper('.projects-grid', {
    slidesPerView: 1.2,
    spaceBetween: 20,
    freeMode: true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true
    }
  });
}
```

---

## 🎯 10. 성능 최적화 인터랙션

### 10.1 Lazy Loading 이미지

```javascript
// Intersection Observer 사용
const imageObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.classList.add('loaded');
      observer.unobserve(img);
    }
  });
});

document.querySelectorAll('img[data-src]').forEach(img => {
  imageObserver.observe(img);
});
```

```css
img[data-src] {
  opacity: 0;
  transition: opacity 0.3s ease;
}

img.loaded {
  opacity: 1;
}
```

---

### 10.2 애니메이션 최적화

```css
/* GPU 가속 활용 */
.animated-element {
  will-change: transform, opacity;
  transform: translateZ(0);
}

/* 애니메이션 완료 후 will-change 제거 */
.animated-element.complete {
  will-change: auto;
}
```

---

**참고**: 모든 인터랙션은 사용자 경험과 성능을 고려하여 선택적으로 적용하세요.
