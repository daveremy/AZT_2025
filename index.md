---
layout: default
title: My AZT 2025 Plan
---

<style>
.quick-links {
  margin: 2em 0;
  padding: 1em;
}

.link-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5em;
  margin-top: 1em;
}

.link-card {
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 1em;
  text-decoration: none;
  color: inherit;
  transition: transform 0.2s;
}

.link-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.link-card h3 {
  margin: 0 0 0.5em 0;
  color: #2c3e50;
}

.link-card p {
  margin: 0;
  color: #666;
}

.section-grid {
  margin: 2em 0;
}

.sections-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5em;
  margin-top: 1em;
}

.section-card {
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.section-image {
  height: 150px;
  background-size: cover;
  background-position: center;
  position: relative;
}

.section-image-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 1em;
  background: linear-gradient(transparent, rgba(0,0,0,0.7));
  color: white;
}

.section-image-overlay h3 {
  margin: 0;
  font-size: 1.2em;
}

.section-content {
  padding: 1.5em;
}

.section-details {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1em;
}

.section-stats {
  display: flex;
  gap: 1em;
  margin: 0.5em 0;
  font-size: 0.9em;
  color: #666;
}

.section-link {
  display: inline-block;
  color: #0366d6;
  text-decoration: none;
}

.section-link:hover {
  text-decoration: underline;
}
</style>

{% assign base_weight = site.data.gear.categories %}
{% include calculate_base_weight.html %}

<div class="hero-section">
  <img src="{{ site.baseurl }}/assets/images/azt-hero.jpg" alt="Arizona Trail Hero Image" class="hero-image">
  <div class="hero-content">
    <h1>My Arizona Trail Adventure</h1>
    <p class="subtitle">{{ site.data.trail_stats.total_distance }} Miles of Desert, Mountains, and Canyons</p>
    <div class="countdown">
      <p>Starting: {{ site.data.trail_stats.timeline.start_date | date: "%B %-d, %Y" }} (<span id="countdown">Loading...</span>)</p>
    </div>
    
    <div class="stats-container">
      <div class="stat-box">
        <h3>{{ site.data.trail_stats.total_distance }}</h3>
        <p>Trail Miles</p>
      </div>
      <div class="stat-box">
        <h3>{{ site.data.trail_stats.total_days }}</h3>
        <p>Days Planned</p>
      </div>
      <div class="stat-box">
        <h3>{{ base_weight_lbs_rounded }}</h3>
        <p>Base Weight (lbs)</p>
      </div>
    </div>
    
    <p class="photo-credit">{{ site.image_credits.hero }}</p>
  </div>
</div>

<div class="trail-overview">
  <h2>The Plan</h2>
  <p>Beginning {{ site.data.trail_stats.timeline.start_date | date: "%B %-d" }}, I'll be hiking northbound from Mexico to Utah. The journey covers {{ site.data.trail_stats.total_distance }} miles through Arizona's diverse landscapes - from desert lowlands to alpine forests, through canyons and mountain ranges. My wife Beth will join me for the Grand Canyon rim-to-rim section on May 15, which will be a special highlight of the trek.</p>
</div>

<div class="elevation-overview">
  <img src="{{ site.baseurl }}/assets/images/elevation/azt_elevation_profile.png" alt="AZT Full Elevation Profile" class="full-elevation-profile">
  <p class="caption">The Route: Mexico to Utah ({{ site.data.trail_stats.elevation.lowest_point }}' to {{ site.data.trail_stats.elevation.highest_point }}' elevation)</p>
</div>

<div class="quick-links">
  <h2>Planning Resources</h2>
  <div class="link-grid">
    <a href="{{ site.baseurl }}/gear-list" class="link-card">
      <h3>🎒 Gear List</h3>
      <p>{{ base_weight_lbs_rounded }} lbs base weight</p>
    </a>
    <a href="{{ site.baseurl }}/food-plan" class="link-card">
      <h3>🍎 Food Strategy</h3>
      <p>{{ site.data.trail_stats.resupply.total_points }} resupply points</p>
    </a>
    <a href="{{ site.baseurl }}/water-strategies" class="link-card">
      <h3>💧 Water Planning</h3>
      <p>{{ site.data.trail_stats.water.max_capacity }}L capacity</p>
    </a>
    <a href="{{ site.baseurl }}/pre-departure-checklist" class="link-card">
      <h3>✅ Pre-Departure</h3>
      <p>Final preparations</p>
    </a>
    <a href="{{ site.baseurl }}/passages" class="link-card">
      <h3>🗺️ Trail Passages</h3>
      <p>{{ site.data.passages.passages.size }} official passages</p>
    </a>
    <a href="{{ site.baseurl }}/shakedown-hikes" class="link-card">
      <h3>🏃‍♂️ Shakedown Hikes</h3>
      <p>Test runs and gear checks</p>
    </a>
    <a href="{{ site.baseurl }}/timeline" class="link-card">
      <h3>📅 Estimated Timeline</h3>
      <p>Key dates and milestones</p>
    </a>
  </div>
</div>

<div class="section-grid">
  <h2>Trail Sections</h2>
  <div class="sections-container">
    {% for section in site.data.sections %}
    <div class="section-card">
      <div class="section-image" style="background-image: url('{{ site.baseurl }}/assets/images/elevation/{{ section.number | prepend: '0' | slice: -2, 2 }}_elevation.png')">
        <div class="section-image-overlay">
          <h3>{{ section.title }}</h3>
        </div>
      </div>
      <div class="section-content">
        <div class="section-stats">
          <span>{{ section.distance }} miles</span>
          <span>{{ section.days }} days</span>
          <span>{{ section.daily_mileage }} mpd</span>
        </div>
        <div class="section-details">
          <a href="{{ site.baseurl }}/sections/{{ section.number | prepend: '0' | slice: -2, 2 }}_{{ section.title | replace: ' ', '_' | downcase }}" class="section-link">View Details →</a>
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
</div>

<div class="preparation-status">
  <h2>Preparation Status</h2>
  <div class="status-grid">
    <div class="status-item">
      <h3>✅ Completed</h3>
      <ul>
        <li>Equipment testing</li>
        <li>Route planning</li>
        <li>Permit acquisition</li>
        <li>Training program</li>
      </ul>
    </div>
    <div class="status-item">
      <h3>🚧 In Progress</h3>
      <ul>
        <li>Food planning</li>
        <li>Mail drop preparation</li>
        <li>Equipment refinement</li>
      </ul>
    </div>
    <div class="status-item">
      <h3>⏳ Upcoming</h3>
      <ul>
        <li>Final shakedown hike</li>
        <li>Mail drop packaging</li>
        <li>Equipment verification</li>
      </ul>
    </div>
  </div>
</div>

<script>
  // Countdown Timer
  function updateCountdown() {
    const startDate = new Date('{{ site.data.trail_stats.timeline.start_date }}T07:00:00');
    const now = new Date();
    const diff = startDate - now;
    
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    
    document.getElementById('countdown').innerHTML = `${days} days, ${hours} hours`;
  }
  
  updateCountdown();
  setInterval(updateCountdown, 3600000); // Update every hour
</script>

*This plan will be updated as preparation continues* 