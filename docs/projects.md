---
hide:
  - toc
---

# Проекты

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
<div class="project-card">
  {% if project.image %}
  <div class="project-shot">
    <img src="{{ project.image }}" alt="{{ project.name }} — screenshot" loading="lazy">
  </div>
  {% endif %}
  <div class="project-header">
    <h3>{{ project.name }}</h3>
    <span class="project-stack">{{ project.stack }}</span>
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

<style>
.project-nav {
  display: flex;
  gap: 0.8rem;
  flex-wrap: wrap;
  margin-bottom: 2.5rem;
}

.project-nav a {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.8rem;
  color: #cc0000;
  text-decoration: none !important;
  border: 1px solid #cc000044;
  padding: 0.3rem 0.9rem;
  transition: border-color 0.2s, color 0.2s;
}

.project-nav a:hover {
  border-color: #cc0000;
  color: #ffffff;
}

.category-title {
  font-family: 'Share Tech Mono', monospace;
  color: #cc0000 !important;
  border-bottom: 1px solid #cc000044;
  padding-bottom: 0.6rem;
  margin-top: 3rem;
  margin-bottom: 1.5rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  font-size: 1rem !important;
}

.category-title::after {
  display: none !important;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
  margin-bottom: 1rem;
}

.project-card {
  border: 1px solid #cc000033;
  padding: 1.5rem;
  background: #0a0000;
  transition: border-color 0.2s, box-shadow 0.2s;
  display: flex;
  flex-direction: column;
}

.project-card:hover {
  border-color: #cc0000;
  box-shadow: 0 0 20px #cc000022;
}

.project-shot {
  margin: -1.5rem -1.5rem 1.2rem -1.5rem;
  overflow: hidden;
  border-bottom: 1px solid #cc000033;
  background: #000000;
}

.project-shot img {
  width: 100%;
  display: block;
}

.project-header {
  display: flex;
  align-items: baseline;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 0.5rem;
}

.project-header h3 {
  margin: 0 !important;
}

.project-header h3::after {
  display: none !important;
}

.project-stack {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.75rem;
  color: #cc0000;
  border: 1px solid #cc000044;
  padding: 0.1rem 0.5rem;
  white-space: nowrap;
}

.project-desc {
  color: #aaaaaa;
  margin-bottom: 0.8rem;
}

.project-features {
  color: #dddddd;
  padding-left: 1.2rem;
  margin-bottom: 1rem;
}

.project-features li {
  margin-bottom: 0.3rem;
  font-size: 0.9rem;
}

.project-code {
  margin-bottom: 1rem;
  border: 1px solid #cc000033;
  background: #050000;
}

.project-code summary {
  cursor: pointer;
  padding: 0.5rem 0.8rem;
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.8rem;
  color: #ff6666;
  user-select: none;
  list-style: none;
}

.project-code summary::-webkit-details-marker {
  display: none;
}

.project-code summary::before {
  content: '▶ ';
  font-size: 0.7rem;
}

.project-code[open] summary::before {
  content: '▼ ';
}

.project-code summary:hover {
  color: #ffffff;
}

.project-code pre {
  margin: 0;
  padding: 0.8rem;
  overflow-x: auto;
  border-top: 1px solid #cc000033;
}

.project-code code {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.8rem;
  line-height: 1.5;
  color: #dddddd;
  white-space: pre;
}

.project-link {
  font-family: 'Share Tech Mono', monospace;
  color: #ff6666 !important;
  text-decoration: none !important;
  border: none !important;
  transition: color 0.2s;
  margin-top: auto;
}

.project-link:hover {
  color: #ffffff !important;
}
</style>
