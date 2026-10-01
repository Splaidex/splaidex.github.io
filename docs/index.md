---
hide:
  - navigation
  - toc
---

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
  <div class="stat"><span class="stat-num">3</span><span class="stat-label">desktop-приложения</span></div>
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
{% for project in config.extra.projects %}
  <a class="featured-card" href="projects/#{{ project.category }}">
    {% if project.image %}<img src="{{ project.image }}" alt="{{ project.name }}" loading="lazy">{% endif %}
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

<style>
#terminal {
  max-width: 760px;
  margin: 6rem auto 4.5rem;
  padding: 2rem;
  border: 1px solid #cc000044;
  background: #000;
  box-shadow: 0 0 40px #cc000022;
}

.t-line {
  margin: 0.4rem 0;
  font-family: 'Share Tech Mono', monospace;
  font-size: 1.1rem;
}

.t-prompt { color: #cc0000; }
.t-cmd { color: #ffffff; }

.t-cursor {
  color: #cc0000;
  animation: blink 1s step-end infinite;
}

.t-output {
  color: #aaaaaa;
  font-family: 'Share Tech Mono', monospace;
  font-size: 1rem;
  margin: 0.2rem 0 0.8rem 1rem;
}

.t-highlight {
  color: #ffffff;
  font-size: 1.15rem;
  text-shadow: 0 0 8px #ffffff22;
}

.t-buttons {
  display: flex;
  gap: 1.5rem;
  margin: 0.5rem 0 0.5rem 1rem;
}

.t-btn {
  font-family: 'Share Tech Mono', monospace;
  font-size: 1rem;
  color: #ff6666 !important;
  border: none !important;
  padding: 0.4rem 1.2rem;
  text-decoration: none !important;
  background: transparent;
  transition: color 0.2s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.t-btn:hover {
  color: #ffffff !important;
  border-color: #ff6666 !important;
  box-shadow: 0 0 16px #cc000088;
}

.t-arrow {
  color: #ff6666;
  font-size: 0.8rem;
}

@keyframes blink {
  50% { opacity: 0; }
}

.home-section {
  max-width: 1000px;
  margin: 0 auto 4.5rem;
}

.section-title {
  font-family: 'Share Tech Mono', monospace;
  font-size: 1.1rem !important;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  border-bottom: 1px solid #cc000044;
  padding-bottom: 0.6rem;
  margin-bottom: 1.5rem !important;
}

.section-title span { color: #cc0000; }

.stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  border: 1px solid #cc000033;
  background: #0a0000;
}

.stat {
  padding: 1.4rem 1rem;
  text-align: center;
  border-right: 1px solid #cc000033;
}

.stat:last-child { border-right: none; }

.stat-num {
  display: block;
  font-family: 'Share Tech Mono', monospace;
  font-size: 2.2rem;
  color: #cc0000;
  text-shadow: 0 0 12px #cc000066;
  line-height: 1.1;
}

.stat-label {
  color: #aaaaaa;
  font-size: 0.95rem;
}

.services, .steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 1.2rem;
}

.service, .step {
  border: 1px solid #cc000033;
  background: #0a0000;
  padding: 1.3rem;
  transition: border-color 0.2s, box-shadow 0.2s, transform 0.2s;
}

.service:hover, .step:hover {
  border-color: #cc0000;
  box-shadow: 0 0 20px #cc000022;
  transform: translateY(-3px);
}

.service h3, .step h3 {
  margin: 0.4rem 0 0.5rem !important;
  font-size: 1.05rem !important;
}

.service p, .step p {
  color: #aaaaaa;
  margin: 0;
  font-size: 0.95rem;
}

.service-num, .step-num {
  font-family: 'Share Tech Mono', monospace;
  color: #cc0000;
  font-size: 0.85rem;
}

.featured {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.2rem;
  margin-bottom: 1.5rem;
}

.featured-card {
  display: flex;
  flex-direction: column;
  border: 1px solid #cc000033;
  background: #0a0000;
  color: inherit !important;
  text-decoration: none !important;
  transition: border-color 0.2s, box-shadow 0.2s, transform 0.2s;
}

.featured-card:hover {
  border-color: #cc0000;
  box-shadow: 0 0 24px #cc000033;
  transform: translateY(-3px);
  text-shadow: none !important;
}

.featured-card img {
  width: 100%;
  display: block;
  border-bottom: 1px solid #cc000033;
}

.featured-body {
  padding: 1.1rem 1.2rem 1.2rem;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.featured-body h3 { margin: 0 0 0.4rem !important; }

.featured-body p {
  color: #aaaaaa;
  margin: 0 0 0.9rem;
  font-size: 0.95rem;
}

.featured-stack {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.75rem;
  color: #cc0000;
  margin-top: auto;
}

.featured-more {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.8rem;
  color: #ff6666;
  margin-top: 0.5rem;
}

.featured-card:hover .featured-more { color: #ffffff; }

.all-link {
  display: inline-flex !important;
  padding-left: 0 !important;
}

.cta {
  text-align: center;
  border: 1px solid #cc000044;
  background: radial-gradient(ellipse at center, #1a0000 0%, #000 70%);
  padding: 3rem 1.5rem;
  box-shadow: 0 0 40px #cc000022;
}

.cta h2 {
  font-size: 1.8rem !important;
  margin: 0 0 0.6rem !important;
}

.cta p {
  color: #aaaaaa;
  margin: 0 0 1.6rem;
}

.cta-btn {
  display: inline-block;
  font-family: 'Share Tech Mono', monospace;
  color: #ffffff !important;
  background: #cc0000;
  padding: 0.7rem 1.6rem;
  text-decoration: none !important;
  box-shadow: 0 0 16px #cc000066;
  transition: background 0.2s, box-shadow 0.2s;
}

.cta-btn:hover {
  background: #ee0000;
  box-shadow: 0 0 28px #ff000099;
  text-shadow: none !important;
}

.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.7s ease, transform 0.7s ease;
}

.reveal.visible {
  opacity: 1;
  transform: none;
}

@media (prefers-reduced-motion: reduce) {
  .reveal { opacity: 1; transform: none; transition: none; }
}
@media (max-width: 600px) {
  #terminal {
    margin: 2rem 1rem;
    padding: 1rem;
  }

  .t-buttons {
    flex-direction: column;
    gap: 0.8rem;
  }

  .t-btn {
    font-size: 0.9rem;
    justify-content: center;
  }

  .t-line, .t-output, .t-highlight {
    font-size: 0.85rem !important;
    word-break: break-word;
  }

  .stats { grid-template-columns: 1fr; }

  .stat {
    border-right: none;
    border-bottom: 1px solid #cc000033;
  }

  .stat:last-child { border-bottom: none; }

  .home-section { margin-bottom: 3rem; }
}
</style>

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