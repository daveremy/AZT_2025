---
layout: page
title: Gear List 5
permalink: gear-list5/
---

| Category | Item | Weight (oz) | Notes |
|----------|------|-------------|-------|
{% for tag in site.data.gear.tags %}{% if tag.parent == null %}| **{{ tag.name }}** | | | |
{% for subtag in site.data.gear.tags %}{% if subtag.parent == tag.name %}| {{ subtag.name }} | | | |
{% for item in site.data.gear.items %}{% if item.tags contains subtag.name %}| | {% if item.url %}[{{ item.name }}]({{ item.url }}){% else %}{{ item.name }}{% endif %} | {{ item.weight_oz }} | {{ item.notes }} |
{% endif %}{% endfor %}{% endif %}{% endfor %}{% endif %}{% endfor %} 