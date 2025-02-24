---
layout: page
title: Gear List 2
permalink: gear-list2/
---

| Category | Item | Weight (oz) | Notes |
|----------|------|-------------|-------|
| Clothing | Outdoor Research Echo Hoody | 5.3 | Sun protection and base layer |
| Clothing | Ketl Vent Lightweight Shorts | 4.2 | Quick-drying hiking shorts |
| Clothing | Uniqlo Airism Boxers | 1.6 | Anti-chafe underwear |
| Clothing | Injinji Trail Midweight Mini-Crew | 1.8 | Midweight mini-crew height |
| Clothing | Adidas Terrex Free Hiker 2.0 | 22.0 | Non-GTX for better water crossings |
| Clothing | Baseball Cap | 2.8 | Sun protection |
| Clothing | Garmin Fenix 6 Pro Solar | 2.9 | GPS watch with solar charging |
| Clothing | Brynje Super Thermo Mesh T-Shirt | 2.8 | Mesh base layer for cold temps |
| Clothing | Patagonia Nano Puff Hoody | 9.8 | Primary insulation layer |
| Clothing | Frogg Toggs UltraLite2 Rain Jacket | 5.6 | Rain protection |
| Clothing | Zpacks Vertice Rain Pants | 4.8 | Waterproof-breathable, 1.5 oz/sqyd fabric |
| Clothing | Original Buff | 1.0 | Neck gaiter/face cover |
| Clothing | Performance Bike Gloves | 1.39 | Hand protection |
| Clothing | Injinji Trail Midweight Mini-Crew | 1.8 | Alternate day hiking socks |
| Clothing | Uniqlo Airism Boxers | 1.6 | Alternate day underwear |
| Clothing | Injinji Liner Crew | 0.8 | Sleep socks |
| Clothing | New Balance Running Shorts | 2.2 | Sleep shorts |
| Clothing | Helly Hansen Long Sleeve | 3.5 | Sleep shirt |
{% for category in site.data.gear.categories %}
{% for item_group in category[1].items %}
{% for item in item_group[1] %}
| {{ category[1].name }} | {% if item.url %}[{{ item.name }}]({{ item.url }}){% else %}{{ item.name }}{% endif %} | {{ item.weight_oz }} | {{ item.notes }} |
{% endfor %}
{% endfor %}
{% endfor %} 