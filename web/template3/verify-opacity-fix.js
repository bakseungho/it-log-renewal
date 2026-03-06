/**
 * Opacity Fix Verification Script
 * 
 * 이 스크립트를 브라우저 콘솔에서 실행하여 opacity 수정이 제대로 적용되었는지 확인할 수 있습니다.
 * 
 * 사용법:
 * 1. 브라우저에서 index.html 또는 솔루션 페이지 열기
 * 2. F12를 눌러 개발자 도구 열기
 * 3. Console 탭으로 이동
 * 4. 이 파일의 내용을 복사하여 붙여넣기
 * 5. Enter를 눌러 실행
 */

(function() {
  console.log('='.repeat(60));
  console.log('Template3 Opacity Fix Verification');
  console.log('='.repeat(60));
  
  const results = {
    passed: [],
    failed: [],
    warnings: []
  };
  
  // Test 1: fade-in 요소들
  console.log('\n[Test 1] Checking fade-in elements...');
  const fadeInElements = document.querySelectorAll('.fade-in');
  console.log(`Found ${fadeInElements.length} fade-in elements`);
  
  fadeInElements.forEach((el, i) => {
    const styles = window.getComputedStyle(el);
    const opacity = parseFloat(styles.opacity);
    const visibility = styles.visibility;
    
    if (opacity >= 0.9 && visibility !== 'hidden') {
      results.passed.push(`fade-in element ${i}: visible (opacity: ${opacity})`);
    } else {
      results.failed.push(`fade-in element ${i}: NOT visible (opacity: ${opacity}, visibility: ${visibility})`);
      el.style.border = '3px solid red';
    }
  });
  
  // Test 2: 프로젝트 카드
  console.log('\n[Test 2] Checking project cards...');
  const projectCards = document.querySelectorAll('.card-project');
  console.log(`Found ${projectCards.length} project cards`);
  
  projectCards.forEach((el, i) => {
    const styles = window.getComputedStyle(el);
    const opacity = parseFloat(styles.opacity);
    const visibility = styles.visibility;
    
    if (opacity >= 0.9 && visibility !== 'hidden') {
      results.passed.push(`project card ${i}: visible (opacity: ${opacity})`);
    } else {
      results.failed.push(`project card ${i}: NOT visible (opacity: ${opacity}, visibility: ${visibility})`);
      el.style.border = '3px solid red';
    }
  });
  
  // Test 3: 솔루션 카드
  console.log('\n[Test 3] Checking solution cards...');
  const solutionCards = document.querySelectorAll('.card-solution');
  console.log(`Found ${solutionCards.length} solution cards`);
  
  solutionCards.forEach((el, i) => {
    const styles = window.getComputedStyle(el);
    const opacity = parseFloat(styles.opacity);
    const visibility = styles.visibility;
    
    if (opacity >= 0.9 && visibility !== 'hidden') {
      results.passed.push(`solution card ${i}: visible (opacity: ${opacity})`);
    } else {
      results.failed.push(`solution card ${i}: NOT visible (opacity: ${opacity}, visibility: ${visibility})`);
      el.style.border = '3px solid red';
    }
  });
  
  // Test 4: 통계 카드
  console.log('\n[Test 4] Checking stat cards...');
  const statCards = document.querySelectorAll('.card-stat');
  console.log(`Found ${statCards.length} stat cards`);
  
  statCards.forEach((el, i) => {
    const styles = window.getComputedStyle(el);
    const opacity = parseFloat(styles.opacity);
    const visibility = styles.visibility;
    
    if (opacity >= 0.9 && visibility !== 'hidden') {
      results.passed.push(`stat card ${i}: visible (opacity: ${opacity})`);
    } else {
      results.failed.push(`stat card ${i}: NOT visible (opacity: ${opacity}, visibility: ${visibility})`);
      el.style.border = '3px solid red';
    }
  });
  
  // Test 5: feature-item
  console.log('\n[Test 5] Checking feature items...');
  const featureItems = document.querySelectorAll('.feature-item');
  console.log(`Found ${featureItems.length} feature items`);
  
  featureItems.forEach((el, i) => {
    const styles = window.getComputedStyle(el);
    const opacity = parseFloat(styles.opacity);
    const visibility = styles.visibility;
    
    if (opacity >= 0.9 && visibility !== 'hidden') {
      results.passed.push(`feature item ${i}: visible (opacity: ${opacity})`);
    } else {
      results.failed.push(`feature item ${i}: NOT visible (opacity: ${opacity}, visibility: ${visibility})`);
      el.style.border = '3px solid red';
    }
  });
  
  // Test 6: case-item
  console.log('\n[Test 6] Checking case items...');
  const caseItems = document.querySelectorAll('.case-item');
  console.log(`Found ${caseItems.length} case items`);
  
  caseItems.forEach((el, i) => {
    const styles = window.getComputedStyle(el);
    const opacity = parseFloat(styles.opacity);
    const visibility = styles.visibility;
    
    if (opacity >= 0.9 && visibility !== 'hidden') {
      results.passed.push(`case item ${i}: visible (opacity: ${opacity})`);
    } else {
      results.failed.push(`case item ${i}: NOT visible (opacity: ${opacity}, visibility: ${visibility})`);
      el.style.border = '3px solid red';
    }
  });
  
  // Test 7: overview-content
  console.log('\n[Test 7] Checking overview content...');
  const overviewContent = document.querySelectorAll('.overview-content');
  console.log(`Found ${overviewContent.length} overview content sections`);
  
  overviewContent.forEach((el, i) => {
    const styles = window.getComputedStyle(el);
    const opacity = parseFloat(styles.opacity);
    const visibility = styles.visibility;
    
    if (opacity >= 0.9 && visibility !== 'hidden') {
      results.passed.push(`overview content ${i}: visible (opacity: ${opacity})`);
    } else {
      results.failed.push(`overview content ${i}: NOT visible (opacity: ${opacity}, visibility: ${visibility})`);
      el.style.border = '3px solid red';
    }
  });
  
  // Test 8: diagram-container
  console.log('\n[Test 8] Checking diagram containers...');
  const diagramContainers = document.querySelectorAll('.diagram-container');
  console.log(`Found ${diagramContainers.length} diagram containers`);
  
  diagramContainers.forEach((el, i) => {
    const styles = window.getComputedStyle(el);
    const opacity = parseFloat(styles.opacity);
    const visibility = styles.visibility;
    
    if (opacity >= 0.9 && visibility !== 'hidden') {
      results.passed.push(`diagram container ${i}: visible (opacity: ${opacity})`);
    } else {
      results.failed.push(`diagram container ${i}: NOT visible (opacity: ${opacity}, visibility: ${visibility})`);
      el.style.border = '3px solid red';
    }
  });
  
  // GSAP 확인
  console.log('\n[GSAP Check]');
  if (typeof gsap !== 'undefined') {
    results.warnings.push('GSAP is loaded - animations should work');
    console.log('✓ GSAP is loaded');
  } else {
    results.warnings.push('GSAP is NOT loaded - using fallback');
    console.log('⚠ GSAP is NOT loaded (fallback should work)');
  }
  
  // 결과 출력
  console.log('\n' + '='.repeat(60));
  console.log('RESULTS');
  console.log('='.repeat(60));
  
  console.log(`\n✓ PASSED: ${results.passed.length} tests`);
  if (results.passed.length > 0 && results.passed.length <= 10) {
    results.passed.forEach(msg => console.log(`  - ${msg}`));
  } else if (results.passed.length > 10) {
    console.log(`  (showing first 5 of ${results.passed.length})`);
    results.passed.slice(0, 5).forEach(msg => console.log(`  - ${msg}`));
  }
  
  if (results.failed.length > 0) {
    console.log(`\n✗ FAILED: ${results.failed.length} tests`);
    results.failed.forEach(msg => console.error(`  - ${msg}`));
    console.log('\n⚠ Failed elements are marked with RED BORDER');
  }
  
  if (results.warnings.length > 0) {
    console.log(`\n⚠ WARNINGS: ${results.warnings.length}`);
    results.warnings.forEach(msg => console.warn(`  - ${msg}`));
  }
  
  // 최종 판정
  console.log('\n' + '='.repeat(60));
  if (results.failed.length === 0) {
    console.log('%c✓ ALL TESTS PASSED!', 'color: #10b981; font-size: 20px; font-weight: bold;');
    console.log('All elements are visible. Opacity fix is working correctly.');
  } else {
    console.log('%c✗ SOME TESTS FAILED', 'color: #ef4444; font-size: 20px; font-weight: bold;');
    console.log('Some elements are not visible. Check the failed tests above.');
  }
  console.log('='.repeat(60));
  
  // 반환값
  return {
    total: results.passed.length + results.failed.length,
    passed: results.passed.length,
    failed: results.failed.length,
    warnings: results.warnings.length,
    success: results.failed.length === 0
  };
})();
