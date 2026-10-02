---
hide:
  - navigation
  - toc
---

<h1 class="visually-hidden">SplaidEX — Python developer</h1>

<div id="terminal">
  <div id="terminal-body">
    <p class="t-line"><span class="t-prompt">splaidex@portfolio:~$</span> <span class="t-cmd" id="cmd1"></span><span class="t-cursor" id="cur1">█</span></p>
    <div id="output1" style="display:none">
      <p class="t-output t-highlight">Python developer. Vibe-coder. I build tools.</p>
    </div>
    <p class="t-line" id="line2" style="display:none"><span class="t-prompt">splaidex@portfolio:~$</span> <span class="t-cmd" id="cmd2"></span><span class="t-cursor" id="cur2">█</span></p>
    <div id="output2" style="display:none">
      <p class="t-output t-highlight">PyQt6 · Telegram bots · API · CUDA · Automation</p>
    </div>
    <p class="t-line" id="line3" style="display:none"><span class="t-prompt">splaidex@portfolio:~$</span> <span class="t-cmd" id="cmd3"></span><span class="t-cursor" id="cur3">█</span></p>
    <div id="output3" style="display:none">
      <div class="t-buttons">
        <a href="projects/" class="t-btn">[ Projects ] <span class="t-arrow">◀</span></a>
        <a href="about/" class="t-btn">[ About ] <span class="t-arrow">◀</span></a>
      </div>
    </div>
  </div>
</div>

<section class="home-section reveal">
<div class="stats">
  <div class="stat"><span class="stat-num">3+</span><span class="stat-label">years of Python</span></div>
  <div class="stat"><span class="stat-num">6</span><span class="stat-label">desktop apps</span></div>
  <div class="stat"><span class="stat-num">11+</span><span class="stat-label">technologies in the stack</span></div>
</div>
</section>

<section class="home-section reveal">
<h2 class="section-title"><span>//</span> What I do</h2>
<div class="services">
  <div class="service"><span class="service-num">01</span><h3>Desktop apps</h3><p>PyQt6 GUIs with animations, previews and a clear interface — not just a console script.</p></div>
  <div class="service"><span class="service-num">02</span><h3>Telegram bots</h3><p>Bots for notifications, order intake, data exports and work-chat automation.</p></div>
  <div class="service"><span class="service-num">03</span><h3>Scraping & APIs</h3><p>Collecting data from sites and services, REST and Steam API, export to CSV / JSON.</p></div>
  <div class="service"><span class="service-num">04</span><h3>Automation</h3><p>Scripts that kill routine: file and media processing, reports, multithreading.</p></div>
</div>
</section>

<section class="home-section reveal">
<h2 class="section-title"><span>//</span> Featured projects</h2>
<div class="featured">
{% for project in config.extra.projects[:3] %}
  <a class="featured-card" href="projects/#{{ project.category }}">
    {% if project.images %}<img src="{{ project.images[0] }}" alt="{{ project.name }}" loading="lazy">{% endif %}
    <div class="featured-body">
      <h3>{{ project.name_en or project.name }}</h3>
      <p>{{ project.description_en if project.description_en else project.description }}</p>
      <span class="featured-stack">{{ project.stack }}</span>
      <span class="featured-more">details →</span>
    </div>
  </a>
{% endfor %}
</div>
<a href="projects/" class="t-btn all-link">[ All projects → ]</a>
</section>

<section class="home-section reveal">
<h2 class="section-title"><span>//</span> How I work</h2>
<div class="steps">
  <div class="step"><span class="step-num">01</span><h3>Brief</h3><p>We discuss what you need and what counts as done.</p></div>
  <div class="step"><span class="step-num">02</span><h3>Prototype</h3><p>I quickly build a working version you can try.</p></div>
  <div class="step"><span class="step-num">03</span><h3>Polish</h3><p>Revisions, UI polish, edge cases handled.</p></div>
  <div class="step"><span class="step-num">04</span><h3>Delivery</h3><p>Finished tool + instructions. Support after delivery.</p></div>
</div>
</section>

<section class="home-section reveal cta">
<h2>Got a task?</h2>
<p>Describe what you want automated — I'll reply on Telegram.</p>
<a href="https://t.me/imwaited" class="cta-btn" target="_blank" rel="noopener">[ Message on Telegram ]</a>
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