---
hide:
  - toc
---

# Projects

{% set data = config.extra.projects %}
{% for project in data %}
<div class="project-card">
  <div class="project-header">
    <h2>{{ project.name }}</h2>
    <span class="project-stack">{{ project.stack }}</span>
  </div>
  <p class="project-desc">{{ project.description_en }}</p>
  <ul class="project-features">
    {% for feature in project.features_en %}
    <li>{{ feature }}</li>
    {% endfor %}
  </ul>
  {% if project.github %}
  <a href="{{ project.github }}" class="project-link" target="_blank">[ GitHub →]</a>
  {% endif %}
</div>
{% endfor %}