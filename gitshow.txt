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

<div class="category-card">
<h3>Core Systems</h3>
<ul class="category-items">
{% for item_group in site.data.gear.categories.big_three.items %}
  {% assign group_weight = 0 %}
  {% for item in item_group[1] %}
    {% assign group_weight = group_weight | plus: item.weight_oz %}
  {% endfor %}
  {% assign group_weight_lbs = group_weight | divided_by: 16.0 | round: 2 %}
  <li><a href="#{{ item_group[0] }}"><strong>{{ item_group[0] | capitalize }}</strong>: {{ group_weight }} oz ({{ group_weight_lbs }} lbs)</a></li>
{% endfor %}
</ul>
</div>

<div class="category-card">
<h3>Clothing</h3>
<ul class="category-items">
{% assign worn_weight = 0 %}
{% for item in site.data.gear.categories.worn_clothing.items.clothes %}
  {% assign worn_weight = worn_weight | plus: item.weight_oz %}
{% endfor %}
{% assign worn_weight_lbs = worn_weight | divided_by: 16.0 | round: 2 %}
<li><a href="#worn_clothing"><strong>Worn Clothes</strong>: {{ worn_weight }} oz ({{ worn_weight_lbs }} lbs)</a></li>

{% assign packed_weight = 0 %}
{% for item in site.data.gear.categories.packed_clothing.items.clothes %}
  {% assign packed_weight = packed_weight | plus: item.weight_oz %}
{% endfor %}
{% assign packed_weight_lbs = packed_weight | divided_by: 16.0 | round: 2 %}
<li><a href="#packed_clothes"><strong>Packed Clothes</strong>: {{ packed_weight }} oz ({{ packed_weight_lbs }} lbs)</a></li>
</ul>
</div>

<div class="category-card">
<h3>Essential Gear</h3>
<ul class="category-items">
{% for item_group in site.data.gear.categories.kitchen_water.items %}
  {% assign group_weight = 0 %}
  {% for item in item_group[1] %}
    {% assign group_weight = group_weight | plus: item.weight_oz %}
  {% endfor %}
  {% assign group_weight_lbs = group_weight | divided_by: 16.0 | round: 2 %}
  <li><a href="#{{ item_group[0] }}"><strong>{{ item_group[0] | capitalize }}</strong>: {{ group_weight }} oz ({{ group_weight_lbs }} lbs)</a></li>
{% endfor %}
{% for item_group in site.data.gear.categories.hiking_gear.items %}
  {% assign group_weight = 0 %}
  {% for item in item_group[1] %}
    {% assign group_weight = group_weight | plus: item.weight_oz %}
  {% endfor %}
  {% assign group_weight_lbs = group_weight | divided_by: 16.0 | round: 2 %}
  <li><a href="#{{ item_group[0] }}"><strong>{{ item_group[0] | capitalize }}</strong>: {{ group_weight }} oz ({{ group_weight_lbs }} lbs)</a></li>
{% endfor %}
</ul>
</div>

<div class="category-card">
<h3>Electronics & Camera</h3>
<ul class="category-items">
{% for item_group in site.data.gear.categories.electronics.items %}
  {% assign group_weight = 0 %}
  {% for item in item_group[1] %}
    {% assign group_weight = group_weight | plus: item.weight_oz %}
  {% endfor %}
  {% assign group_weight_lbs = group_weight | divided_by: 16.0 | round: 2 %}
  <li><a href="#{{ item_group[0] }}"><strong>{{ item_group[0] | capitalize }}</strong>: {{ group_weight }} oz ({{ group_weight_lbs }} lbs)</a></li>
{% endfor %}
{% for item_group in site.data.gear.categories.camera.items %}
  {% assign group_weight = 0 %}
  {% for item in item_group[1] %}
    {% assign group_weight = group_weight | plus: item.weight_oz %}
  {% endfor %}
  {% assign group_weight_lbs = group_weight | divided_by: 16.0 | round: 2 %}
  <li><a href="#{{ item_group[0] }}"><strong>{{ item_group[0] | capitalize }}</strong>: {{ group_weight }} oz ({{ group_weight_lbs }} lbs)</a></li>
{% endfor %}
</ul>
</div>

<div class="category-card">
<h3>Small Items</h3>
<ul class="category-items">
{% for item_group in site.data.gear.categories.first_aid.items %}
  {% assign group_weight = 0 %}
  {% for item in item_group[1] %}
    {% assign group_weight = group_weight | plus: item.weight_oz %}
  {% endfor %}
  {% assign group_weight_lbs = group_weight | divided_by: 16.0 | round: 2 %}
  <li><a href="#{{ item_group[0] }}"><strong>{{ item_group[0] | capitalize }}</strong>: {{ group_weight }} oz ({{ group_weight_lbs }} lbs)</a></li>
{% endfor %}
{% for item_group in site.data.gear.categories.small_stuff.items %}
  {% assign group_weight = 0 %}
  {% for item in item_group[1] %}
    {% assign group_weight = group_weight | plus: item.weight_oz %}
  {% endfor %}
  {% assign group_weight_lbs = group_weight | divided_by: 16.0 | round: 2 %}
  <li><a href="#{{ item_group[0] }}"><strong>{{ item_group[0] | capitalize }}</strong>: {{ group_weight }} oz ({{ group_weight_lbs }} lbs)</a></li>
{% endfor %}
</ul>
</div>

</div>
</div>

<div class="packing-links">
<h2>Packing Resources</h2>
<ul>
<li><a href="{{ site.baseurl }}/packing-your-backpack/">General Packing Strategy</a> - Detailed guide on how to pack efficiently</li>
<li><a href="{{ site.baseurl }}/pack-checklist/">Interactive Packing Checklist</a> - Step-by-step checklist for consistent packing</li>
</ul>
</div>

<div class="still-needed">
<h2>Still Needed</h2>
<ul>
<li>Consumables:
  <ul>
    <li>Fuel canisters (estimate 1 per 10-12 days)</li>
    <li>First aid refills</li>
    <li>Sunscreen</li>
    <li>Hand sanitizer</li>
  </ul>
</li>
<li>Seasonal/Variable:
  <ul>
    <li>Extra water capacity for desert sections</li>
    <li>Microspikes (if needed for early season snow)</li>
    <li>Bug head net (if needed in spring)</li>
  </ul>
</li>
</ul>
</div>

{% for category in site.data.gear.categories %}
<h2>{{ category[1].name }}</h2>

{% if category[0] == "worn_clothing" or category[0] == "packed_clothing" %}
<h3 id="{{ category[0] }}">{{ category[1].name }}</h3>

| What | Weight (oz) | Notes |
|------|-------------|-------|
{% for item in category[1].items.clothes %}| {% if item.url %}[{{ item.name }}]({{ item.url }}){% else %}{{ item.name }}{% endif %} | {{ item.weight_oz }} | {{ item.notes }} |
{% endfor %}

{% else %}
{% for item_group in category[1].items %}
<h3 id="{{ item_group[0] }}">{{ item_group[0] | capitalize }}</h3>

| What | Weight (oz) | Notes |
|------|-------------|-------|
{% for item in item_group[1] %}| {% if item.url %}[{{ item.name }}]({{ item.url }}){% else %}{{ item.name }}{% endif %} | {{ item.weight_oz }} | {{ item.notes }} |
{% endfor %}

{% endfor %}
{% endif %}
{% endfor %} 