---
hide:
  - navigation
  - toc
---

# Projects

{% set lang = i18n_page_locale %}
{% set categories = config.extra.project_categories %}
{% set projects = config.extra.projects %}

<div class="project-nav">
{% for cat in categories %}<a href="#{{ cat.id }}">{{ cat.title_en if lang == 'en' and cat.title_en else cat.title }}</a>{% endfor %}
</div>

{% for cat in categories %}
{% set cat_projects = projects | selectattr('category', 'equalto', cat.id) | list %}
{% if cat_projects %}
<h2 id="{{ cat.id }}" class="category-title">{{ cat.title_en if lang == 'en' and cat.title_en else cat.title }}</h2>
<div class="projects-grid">
{% for project in cat_projects %}
{% set description = project.description_en if lang == 'en' and project.description_en else project.description %}
{% set features = project.features_en if lang == 'en' and project.features_en else project.features %}
{% set pname = project.name_en if lang == 'en' and project.name_en else project.name %}
<div class="project-card">
  {% if project.images %}
  <div class="project-shot">
    <img class="shot-main" src="{{ project.images[0] }}" alt="{{ pname }} — screenshot" loading="lazy">
  </div>
  {% if project.images | length > 1 %}
  <div class="shot-thumbs">
    {% for img in project.images %}<button type="button" class="shot-thumb{% if loop.first %} active{% endif %}" data-src="{{ img }}"><img src="{{ img }}" alt="" loading="lazy"></button>{% endfor %}
  </div>
  {% endif %}
  {% endif %}
  <div class="project-header">
    <h3>{{ pname }}</h3>
    <div class="project-stack">{% for t in project.stack.split(',') %}<span class="chip">{{ t | trim }}</span>{% endfor %}</div>
  </div>
  <p class="project-desc">{{ description }}</p>
  <ul class="project-features">
    {% for feature in features %}
    <li>{{ feature }}</li>
    {% endfor %}
  </ul>
  {% if project.code %}
  <details class="project-code">
    <summary>{{ 'Code example' if lang == 'en' else 'Пример кода' }}</summary>
    <pre><code>{{ project.code | e }}</code></pre>
  </details>
  {% endif %}
  {% if project.github %}
  <a href="{{ project.github }}" class="project-link" target="_blank" rel="noopener">[ GitHub →]</a>
  {% endif %}
</div>
{% endfor %}
</div>
{% endif %}
{% endfor %}

<script>
document.querySelectorAll('.project-card').forEach(function (card) {
  var main = card.querySelector('.shot-main');
  card.querySelectorAll('.shot-thumb').forEach(function (btn) {
    btn.addEventListener('click', function () {
      main.src = btn.dataset.src;
      card.querySelectorAll('.shot-thumb').forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
    });
  });
});
</script>
