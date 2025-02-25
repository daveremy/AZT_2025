---
layout: page
title: Gear List
permalink: gear-list5/
---

<style>
.weight-summary {
  background: #f8f9fa;
  border-radius: 6px;
  padding: 0.75em;
  margin-bottom: 1.5em;
  text-align: center;
}

.weight-summary h2 {
  margin: 0;
  font-size: 1.2em;
}

.category-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1em;
  margin-bottom: 1.5em;
}

.category-card {
  background: white;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  padding: 0.75em;
}

.category-card h2 {
  margin: 0 0 0.5em 0;
  font-size: 1.1em;
  color: #2c3e50;
  border-bottom: 1px solid #eee;
  padding-bottom: 0.5em;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.category-card h2 .category-name {
  font-weight: 600;
}

.category-card h2 .weight {
  font-size: 0.9em;
  color: #666;
}

.subcategory {
  margin: 0.5em 0;
  padding: 0.4em;
  background: #f8f9fa;
  border-radius: 4px;
}

.subcategory h3 {
  margin: 0;
  font-size: 0.95em;
  color: #495057;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.weight {
  color: #666;
  font-weight: 500;
  font-size: 0.9em;
}

.gear-details {
  margin-top: 2em;
  margin-bottom: 1em;
  color: #2c3e50;
}
</style>

{% assign base_weight = 0 %}
{% for item in site.data.gear.items %}
  {% assign base_weight = base_weight | plus: item.weight_oz %}
{% endfor %}

<div class="weight-summary">
  <h2>Base Weight: {{ base_weight }} oz ({{ base_weight | divided_by: 16.0 | round: 2 }} lbs)</h2>
</div>

<div class="category-cards">
{% for tag in site.data.gear.tags %}
  {% if tag.parent == null %}
    {% assign category_weight = 0 %}
    {% for subtag in site.data.gear.tags %}
      {% if subtag.parent == tag.name %}
        {% for item in site.data.gear.items %}
          {% if item.tags contains subtag.name %}
            {% assign category_weight = category_weight | plus: item.weight_oz %}
          {% endif %}
        {% endfor %}
      {% endif %}
    {% endfor %}
    <div class="category-card">
      <h2><span class="category-name">{{ tag.name }}</span> <span class="weight">{{ category_weight }} oz</span></h2>
      {% for subtag in site.data.gear.tags %}
        {% if subtag.parent == tag.name %}
          {% assign subtag_weight = 0 %}
          {% for item in site.data.gear.items %}
            {% if item.tags contains subtag.name %}
              {% assign subtag_weight = subtag_weight | plus: item.weight_oz %}
            {% endif %}
          {% endfor %}
          <div class="subcategory">
            <h3>{{ subtag.name }} <span class="weight">{{ subtag_weight }} oz</span></h3>
          </div>
        {% endif %}
      {% endfor %}
    </div>
  {% endif %}
{% endfor %}
</div>

<h2 class="gear-details">Gear Details</h2>

| Category | Item | Weight (oz) | Notes |
|----------|------|-------------|-------|
{% for tag in site.data.gear.tags %}{% if tag.parent == null %}| **{{ tag.name }}** | | | |
{% for subtag in site.data.gear.tags %}{% if subtag.parent == tag.name %}| {{ subtag.name }} | | | |
{% for item in site.data.gear.items %}{% if item.tags contains subtag.name %}| | {% if item.url %}[{{ item.name }}]({{ item.url }}){% else %}{{ item.name }}{% endif %} | {{ item.weight_oz }} | {{ item.notes }} |
{% endif %}{% endfor %}{% endif %}{% endfor %}{% endif %}{% endfor %} 