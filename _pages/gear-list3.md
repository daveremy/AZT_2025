---
layout: page
title: Gear List 3
permalink: gear-list3/
---

| Category | Item | Weight (oz) | Notes |
|----------|------|-------------|-------|
{% for category in site.data.gear.categories %}
| **{{ category[1].name }}** | | | | {% for item_group in category[1].items %} {% for item in item_group.items %} | | {% if item.url %}[{{ item.name }}]({{ item.url }}){% else %}{{ item.name }}{% endif %} | {{ item.weight_oz }} | {{ item.notes }} |
{% endfor %}
{% endfor %}
{% endfor %} 