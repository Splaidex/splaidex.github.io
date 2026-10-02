---
hide:
  - navigation
  - toc
---

<h1 class="visually-hidden">SplaidEX — Python-разработчик</h1>

<div id="terminal">
  <div id="terminal-body">
    <p class="t-line"><span class="t-prompt">splaidex@portfolio:~$</span> <span class="t-cmd" id="cmd1"></span><span class="t-cursor" id="cur1">█</span></p>
    <div id="output1" style="display:none">
      <p class="t-output t-highlight">Python-разработчик. Vibe-coder. Строю инструменты.</p>
    </div>
    <p class="t-line" id="line2" style="display:none"><span class="t-prompt">splaidex@portfolio:~$</span> <span class="t-cmd" id="cmd2"></span><span class="t-cursor" id="cur2">█</span></p>
    <div id="output2" style="display:none">
      <p class="t-output t-highlight">PyQt6 · Telegram-боты · API · CUDA · Автоматизация</p>
    </div>
    <p class="t-line" id="line3" style="display:none"><span class="t-prompt">splaidex@portfolio:~$</span> <span class="t-cmd" id="cmd3"></span><span class="t-cursor" id="cur3">█</span></p>
    <div id="output3" style="display:none">
      <div class="t-buttons">
        <a href="projects/" class="t-btn">[ Проекты ] <span class="t-arrow">◀</span></a>
        <a href="about/" class="t-btn">[ Обо мне ] <span class="t-arrow">◀</span></a>
      </div>
    </div>
  </div>
</div>

<section class="home-section reveal">
<div class="stats">
  <div class="stat"><span class="stat-num">3+</span><span class="stat-label">года в Python</span></div>
  <div class="stat"><span class="stat-num">6</span><span class="stat-label">desktop-приложений</span></div>
  <div class="stat"><span class="stat-num">11+</span><span class="stat-label">технологий в стеке</span></div>
</div>
</section>

<section class="home-section reveal">
<h2 class="section-title"><span>//</span> Что делаю</h2>
<div class="services">
  <div class="service"><span class="service-num">01</span><h3>Desktop-приложения</h3><p>GUI на PyQt6 с анимациями, превью и понятным интерфейсом — не просто скрипт в консоли.</p></div>
  <div class="service"><span class="service-num">02</span><h3>Telegram-боты</h3><p>Боты для уведомлений, приёма заявок, выгрузок и автоматизации рабочих чатов.</p></div>
  <div class="service"><span class="service-num">03</span><h3>Парсинг и API</h3><p>Сбор данных с сайтов и сервисов, работа с REST и Steam API, выгрузка в CSV / JSON.</p></div>
  <div class="service"><span class="service-num">04</span><h3>Автоматизация</h3><p>Скрипты, которые снимают рутину: обработка файлов, медиа, отчёты, многопоточность.</p></div>
</div>
</section>

<section class="home-section reveal">
<h2 class="section-title"><span>//</span> Избранные проекты</h2>
<div class="featured">
{% for project in config.extra.projects[:3] %}
  <a class="featured-card" href="projects/#{{ project.category }}">
    {% if project.images %}<img src="{{ project.images[0] }}" alt="{{ project.name }}" loading="lazy">{% endif %}
    <div class="featured-body">
      <h3>{{ project.name }}</h3>
      <p>{{ project.description }}</p>
      <span class="featured-stack">{{ project.stack }}</span>
      <span class="featured-more">подробнее →</span>
    </div>
  </a>
{% endfor %}
</div>
<a href="projects/" class="t-btn all-link">[ Все проекты → ]</a>
</section>

<section class="home-section reveal">
<h2 class="section-title"><span>//</span> Как работаю</h2>
<div class="steps">
  <div class="step"><span class="step-num">01</span><h3>Задача</h3><p>Обсуждаем, что нужно и какой результат считаем готовым.</p></div>
  <div class="step"><span class="step-num">02</span><h3>Прототип</h3><p>Быстро собираю рабочую версию, чтобы было что пощупать.</p></div>
  <div class="step"><span class="step-num">03</span><h3>Доработка</h3><p>Правки, полировка интерфейса, обработка краевых случаев.</p></div>
  <div class="step"><span class="step-num">04</span><h3>Сдача</h3><p>Готовый инструмент + инструкция. Поддержка после сдачи.</p></div>
</div>
</section>

<section class="home-section reveal cta">
<h2>Есть задача?</h2>
<p>Опиши, что нужно автоматизировать, — отвечу в Telegram.</p>
<a href="https://t.me/imwaited" class="cta-btn" target="_blank" rel="noopener">[ Написать в Telegram ]</a>
</section>

<script>
function typeText(elementId, text, speed, callback) {
  let i = 0;
  const el = document.getElementById(elementId);
  const interval = setInterval(() => {
    el.textContent += text[i];
    i++;
    if (i >= text.length) {
      clearInterval(interval);
      if (callback) callback();
    }
  }, speed);
}

function hideCursor(id) {
  const el = document.getElementById(id);
  if (el) el.style.display = 'none';
}

function showEl(id) {
  document.getElementById(id).style.display = 'block';
}

document.addEventListener('DOMContentLoaded', function() {
  const reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.15 });
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add('visible'));
  }

  let arrowVisible = true;
  setInterval(() => {
    arrowVisible = !arrowVisible;
    document.querySelectorAll('.t-arrow').forEach(el => {
      el.style.opacity = arrowVisible ? '1' : '0';
    });
  }, 800);

  setTimeout(() => {
    typeText('cmd1', 'whoami', 80, () => {
      hideCursor('cur1');
      showEl('output1');
      setTimeout(() => {
        showEl('line2');
        typeText('cmd2', 'cat skills.txt', 80, () => {
          hideCursor('cur2');
          showEl('output2');
          setTimeout(() => {
            showEl('line3');
            typeText('cmd3', 'ls ./portfolio', 80, () => {
              hideCursor('cur3');
              showEl('output3');
            });
          }, 400);
        });
      }, 400);
    });
  }, 800);
});
</script>