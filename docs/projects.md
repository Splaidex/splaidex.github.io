---
hide:
  - toc
---

# Проекты

{% set data = load_yaml("projects.yml") %}
{% for project in data.projects %}
<div class="project-card">
  <div class="project-header">
    <h2>{{ project.name }}</h2>
    <span class="project-stack">{{ project.stack }}</span>
  </div>
  <p class="project-desc">{{ project.description }}</p>
  <ul class="project-features">
    {% for feature in project.features %}
    <li>{{ feature }}</li>
    {% endfor %}
  </ul>
  {% if project.github %}
  <a href="{{ project.github }}" class="project-link" target="_blank">[ GitHub →]</a>
  {% endif %}
</div>
{% endfor %}

<style>
.project-card {
  border: 1px solid #cc000033;
  padding: 1.5rem;
  margin-bottom: 2rem;
  background: #0a0000;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.project-card:hover {
  border-color: #cc0000;
  box-shadow: 0 0 20px #cc000022;
}

.project-header {
  display: flex;
  align-items: baseline;
  gap: 1rem;
  margin-bottom: 0.5rem;
}

.project-header h2 {
  margin: 0 !important;
}

.project-header h2::after {
  display: none !important;
}

.project-stack {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.8rem;
  color: #cc0000;
  border: 1px solid #cc000044;
  padding: 0.1rem 0.5rem;
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
}

.project-link {
  font-family: 'Share Tech Mono', monospace;
  color: #ff6666 !important;
  text-decoration: none !important;
  border: none !important;
  transition: color 0.2s;
}

.project-link:hover {
  color: #ffffff !important;
}
</style>