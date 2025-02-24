---
layout: page
title: Gear List 4
permalink: gear-list4/
---

| Category |
{% for tag in site.data.gear.tags %}
{% if tag.parent == null %} | **{{ tag.name }}** | {% endif %} {% endfor %}