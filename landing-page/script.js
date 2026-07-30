
function getMetric(name) {
  return Number(localStorage.getItem(name) || 0);
}
function setMetric(name, value) {
  localStorage.setItem(name, String(value));
}


const ctaCount         = document.getElementById('ctaCount');
const ctaTableCount    = document.getElementById('ctaTableCount');
const demoCountCell    = document.getElementById('demoCount');
const recognitionCount = document.getElementById('recognitionCount');
const demoMessage      = document.getElementById('demoMessage');

function refreshMetrics() {
  ctaCount.textContent         = getMetric('ctaClicks');
  ctaTableCount.textContent    = getMetric('ctaClicks');
  demoCountCell.textContent    = getMetric('demoAttempts');
  recognitionCount.textContent = getMetric('imageRecognitions');
}


document.getElementById('ctaButton').addEventListener('click', () => {
  setMetric('ctaClicks', getMetric('ctaClicks') + 1);
  refreshMetrics();
  window.open('rsubuddy/frontend.html', '_blank');   
});


document.getElementById('learnBtn').addEventListener('click', () => {
  document.getElementById('features').scrollIntoView({ behavior: 'smooth' });
});


document.getElementById('demoButton').addEventListener('click', () => {
  setMetric('demoAttempts', getMetric('demoAttempts') + 1);
  refreshMetrics();
  demoMessage.textContent = '🚀 Opening Campus Navigator…';
  setTimeout(() => {
    window.open('rsubuddy/frontend.html', '_blank');
    demoMessage.textContent = '✅ Chatbot opened in a new tab!';
    setTimeout(() => demoMessage.textContent = '', 3000);
  }, 400);
});




function animateCounter(el, target, duration = 1200) {
  let start = 0;
  const step = target / (duration / 16);
  const timer = setInterval(() => {
    start += step;
    if (start >= target) { el.textContent = target; clearInterval(timer); }
    else el.textContent = Math.floor(start);
  }, 16);
}


const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');

      if (entry.target.id === 'buildings-grid') {
        animateCounter(document.getElementById('buildingCount'), 7);
      }
    }
  });
}, { threshold: 0.1 });


document.addEventListener('DOMContentLoaded', () => {
  refreshMetrics();

  document.querySelectorAll('.section, .buildings-grid').forEach(el => observer.observe(el));
});