---
layout: page
title: Trail Passages
permalink: /passages/
---

<style>
.passage-grid {
  display: grid;
  gap: 2em;
  margin: 2em 0;
}

.passage-card {
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 1.5em;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.passage-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1em;
}

.passage-title {
  margin: 0;
}

.passage-number {
  background: #f8f9fa;
  padding: 0.3em 0.6em;
  border-radius: 4px;
  font-size: 0.9em;
  color: #666;
}

.passage-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1em;
  margin: 1em 0;
  font-size: 0.9em;
}

.stat-item {
  background: #f8f9fa;
  padding: 0.8em;
  border-radius: 4px;
  text-align: center;
}

.stat-label {
  color: #666;
  font-size: 0.9em;
  margin-bottom: 0.3em;
}

.stat-value {
  font-weight: 500;
  color: #2c3e50;
}

.access-points {
  margin-top: 1em;
}

.access-point {
  margin: 0.5em 0;
  padding: 0.8em;
  background: #f8f9fa;
  border-radius: 4px;
  display: flex;
  align-items: center;
  gap: 1em;
}

.access-point h4 {
  margin: 0;
  color: #2c3e50;
  flex: 1;
}

.coordinates-link {
  font-size: 0.9em;
  color: #0366d6;
  text-decoration: none;
  white-space: nowrap;
}

.coordinates-link:hover {
  text-decoration: underline;
}

.access-point-notes {
  margin-top: 0.5em;
  font-size: 0.9em;
  color: #666;
}

.resources {
  margin-top: 1em;
  display: flex;
  gap: 0.8em;
}

.resource-link {
  display: inline-block;
  padding: 0.4em 0.8em;
  background: #e9ecef;
  border-radius: 4px;
  text-decoration: none;
  color: #495057;
  font-size: 0.9em;
}

.resource-link:hover {
  background: #dee2e6;
}
</style>

# Arizona Trail Passages

This page provides detailed information about each passage of the Arizona Trail, including distances, elevations, access points, and resources. Data is sourced from the [Arizona Trail Association](https://aztrail.org/explore/passages/).

<div class="passage-grid">
{% for passage in site.data.passages.passages %}
  <div class="passage-card">
    <div class="passage-header">
      <h2 class="passage-title">{{ passage.name }}</h2>
      <span class="passage-number">Passage {{ passage.number }}</span>
    </div>
    
    <div class="passage-stats">
      <div class="stat-item">
        <div class="stat-label">Distance</div>
        <div class="stat-value">{{ passage.length_miles }} miles</div>
      </div>
      <div class="stat-item">
        <div class="stat-label">Elevation Range</div>
        <div class="stat-value">{{ passage.elevation.min_ft | round }}' - {{ passage.elevation.max_ft | round }}'</div>
      </div>
      <div class="stat-item">
        <div class="stat-label">Total Gain</div>
        <div class="stat-value">{{ passage.elevation.total_gain_ft | round }}′</div>
      </div>
      <div class="stat-item">
        <div class="stat-label">Total Loss</div>
        <div class="stat-value">{{ passage.elevation.total_loss_ft | round }}′</div>
      </div>
      <div class="stat-item">
        <div class="stat-label">Avg Grade</div>
        <div class="stat-value">{{ passage.elevation.avg_grade_pct }}%</div>
      </div>
    </div>

    <div class="access-points">
      <h3>Access Points</h3>
      {% for point in passage.access_points %}
        <div class="access-point">
          <h4>{{ point.name }} ({{ point.type | capitalize }})</h4>
          {% if point.coordinates %}
            <a href="https://www.google.com/maps?q={{ point.coordinates.latitude }},{{ point.coordinates.longitude }}" 
               class="coordinates-link" 
               target="_blank" 
               title="{{ point.coordinates.latitude }}°N, {{ point.coordinates.longitude }}°W">
              📍 Map
            </a>
          {% endif %}
        </div>
        {% if point.notes %}
          <div class="access-point-notes">
            <ul>
              {% for note in point.notes %}
                <li>{{ note }}</li>
              {% endfor %}
            </ul>
          </div>
        {% endif %}
      {% endfor %}
    </div>

    <div class="resources">
      <a href="{{ passage.resources.info_page }}" class="resource-link" target="_blank">Info Page</a>
      {% if passage.resources.map_url %}
        <a href="{{ passage.resources.map_url }}" class="resource-link" target="_blank">Map</a>
      {% endif %}
      {% if passage.resources.profile_url %}
        <a href="{{ passage.resources.profile_url }}" class="resource-link" target="_blank">Profile</a>
      {% endif %}
      {% if passage.resources.track_url %}
        <a href="{{ passage.resources.track_url }}" class="resource-link" target="_blank">Track</a>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>

<script>
// Round numbers to 1 decimal place
document.querySelectorAll('.stat-value').forEach(el => {
  const text = el.textContent;
  if (text.includes('%')) {
    el.textContent = parseFloat(text).toFixed(1) + '%';
  }
});
</script> 