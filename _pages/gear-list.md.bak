---
layout: page
title: Gear List
permalink: gear-list/
---

<link rel="stylesheet" href="{{ site.baseurl }}/assets/css/gear-list.css?v=7">

<style>
.packing-links {
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 1em;
  margin: 2em 0;
}

.packing-links h2 {
  margin-top: 0;
  color: #2c3e50;
}

.packing-links ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.packing-links li {
  margin: 0.5em 0;
}

.packing-links a {
  color: #0366d6;
  text-decoration: none;
  font-weight: 500;
}

.packing-links a:hover {
  text-decoration: underline;
}
</style>

<div class="summary-section">
<div class="total-weight">
{% include calculate_base_weight.html %}
Base Weight: {{ total_weight_oz | round: 2 }} oz ({{ base_weight_lbs_rounded }} lbs)
</div>

<div class="conditions">
Spring (March-May) • Desert to Alpine • 20°F to 90°F
</div>

<div class="weight-categories">
{% assign grouped_categories = site.data.gear.categories | group_by_exp: "category", "category[0]" %}

{% for category in site.data.gear.categories %}
<div class="category-card">
<h3>{{ category[1].name | replace: '_', ' ' }}</h3>
<ul class="category-items">
{% for item_group in category[1].items %}
  {% assign group_weight = 0 %}
  {% for item in item_group[1] %}
    {% assign group_weight = group_weight | plus: item.weight_oz %}
  {% endfor %}
  {% assign group_weight_lbs = group_weight | divided_by: 16.0 | round: 2 %}
  <li><a href="#{{ item_group[0] }}"><strong>{{ item_group[0] | capitalize | replace: '_', ' ' }}</strong>: {{ group_weight }} oz ({{ group_weight_lbs }} lbs)</a></li>
{% endfor %}
</ul>
</div>
{% endfor %}
</div>
</div>

<div class="packing-links">
<h2>Packing Resources</h2>
<ul>
<li><a href="{{ site.baseurl }}/packing-your-backpack/">General Packing Strategy</a> - Detailed guide on how to pack efficiently</li>
<li><a href="{{ site.baseurl }}/pack-checklist/">Interactive Packing Checklist</a> - Step-by-step checklist for consistent packing</li>
</ul>
</div>

{% for category in site.data.gear.categories %}
<h2>{{ category[1].name }}</h2>

{% for item_group in category[1].items %}
<h3 id="{{ item_group.name | slugify }}">{{ item_group.name }}</h3>

| What | Weight (oz) | Notes |
|------|-------------|-------|
{% for item in item_group.items %}
| {% if item.url %}[{{ item.name }}]({{ item.url }}){% else %}{{ item.name }}{% endif %} | {{ item.weight_oz }} | {{ item.notes }} |
{% endfor %}

{% endfor %}
{% endfor %}

| Category | Item | Weight (oz) | Notes |
|----------|------|-------------|-------|
{% assign total_weight = 0 %}
{% for category in site.data.gear.categories %}
{% assign category_weight = 0 %}
{% for item_group in category[1].items %}
{% for item in item_group.items %}
| {{ category[1].name }} | {% if item.url %}[{{ item.name }}]({{ item.url }}){% else %}{{ item.name }}{% endif %} | {{ item.weight_oz }} | {{ item.notes }} |
{% assign category_weight = category_weight | plus: item.weight_oz %}
{% endfor %}
{% endfor %}
| **{{ category[1].name }} Total** | | **{{ category_weight }} oz** | |
{% assign total_weight = total_weight | plus: category_weight %}
{% endfor %}
| **Overall Total** | | **{{ total_weight }} oz** | |