---
layout: section
section_number: X
---

{% assign section = site.data.sections | where: "number", page.section_number | first %}

# {{ section.title }} (Passages X-Y)

## Overview
- Distance: {{ section.distance }} miles
- Estimated Days: {{ section.days }}
- Daily Mileage: {{ section.daily_mileage }} miles
- Elevation Range: {{ section.elevation_range.low }}' to {{ section.elevation_range.high }}'
- Total Elevation Gain: {{ section.elevation_gain }}'
- Total Elevation Loss: {{ section.elevation_loss }}'
- Best Season: March-May, September-November

## Trail Description
{{ section.description }}

[Additional trail description specific to this section...]

## Daily Breakdown
{% for day in section.daily_breakdown %}
Day {{ day.day }} ({{ day.miles }} miles):
- {{ day.start }} to {{ day.end }}
- Elevation Gain: +{{ day.elevation_gain }} ft
- Elevation Loss: -{{ day.elevation_loss }} ft
- Key Points: {% for point in day.key_points %}{{ point }}{% unless forloop.last %}, {% endunless %}{% endfor %}
- Water: {% for source in day.water_sources %}{{ source }}{% unless forloop.last %}, {% endunless %}{% endfor %}

{% endfor %}

## Key Points
- Start Point: {{ section.daily_breakdown[0].start }}
- End Point: {{ section.daily_breakdown[-1].end }}
- Major Landmarks:
  - [List major landmarks]

## Water Sources
| Mile | Source | Notes | Reliability |
|------|---------|-------|-------------|
{% for source in section.water_sources %}| {{ source.mile }} | {{ source.name }} | {{ source.notes }} | {{ source.reliability }} |
{% endfor %}

### Water Strategy
- **Start Water**: {{ section.water_strategy.start_water }}
- **Critical Carries**:
{% for carry in section.water_strategy.critical_carries %}  - {{ carry.name }}: {{ carry.distance }} miles{% if carry.notes %} ({{ carry.notes }}){% endif %}
{% endfor %}
- **Recommended Minimum Carry**:
  - Morning start: {{ section.water_strategy.recommended_carry.morning_start }}
  - Dry camping: {{ section.water_strategy.recommended_carry.dry_camping }}
  - Hot weather: {{ section.water_strategy.recommended_carry.hot_weather }}
- **Planning Tips**:
{% for tip in section.water_strategy.planning_tips %}  - {{ tip }}
{% endfor %}

## Camping
### Daily Camp Recommendations
{% for day in section.daily_breakdown %}
Day {{ day.day }} ({{ day.miles }} miles):
{% if day.camping.primary %}
- Primary: Mile {{ day.camping.primary.mile }}: {{ day.camping.primary.location }}
{% for note in day.camping.primary.notes %}  - {{ note }}
{% endfor %}{% endif %}
{% if day.camping.backup %}
- Backup: Mile {{ day.camping.backup.mile }}: {{ day.camping.backup.location }}
{% for note in day.camping.backup.notes %}  - {{ note }}
{% endfor %}{% endif %}

{% endfor %}

### Camping Tips
[General camping advice for this section]

## Resupply
[Resupply details specific to this section]

## Bail Options
[List bail points and access information]

## Special Considerations
[Section-specific considerations and warnings]

{% if section.zero_day %}
## Rest and Zero Days
- Zero day in {{ section.zero_day.location }} (Day {{ section.zero_day.day_number }})
- Duration: {{ section.zero_day.duration }} day{% if section.zero_day.duration > 1 %}s{% endif %}
- Recommended activities:
{% for activity in section.zero_day.activities %}  - {{ activity }}
{% endfor %}
- Accommodation options:
{% for option in section.zero_day.accommodation %}  - {{ option.name }} ({{ option.price }})
{% endfor %}
{% endif %} 