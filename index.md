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

<div class="hero-section">
  <img src="{{ site.baseurl }}/assets/images/azt-hero.jpg" alt="Arizona Trail Hero Image" class="hero-image">
  <div class="hero-content">
    <h1>My Arizona Trail Adventure</h1>
    <p class="subtitle">800 Miles of Desert, Mountains, and Canyons</p>
    <div class="countdown">
      <p>Starting: March 15, 2025 (<span id="countdown">Loading...</span>)</p>
    </div>
    
    <div class="stats-container">
      <div class="stat-box">
        <h3>800</h3>
        <p>Trail Miles</p>
      </div>
      <div class="stat-box">
        <h3>45-50</h3>
        <p>Days Planned</p>
      </div>
      <div class="stat-box">
        <h3>{{ site.data.gear_stats.base_weight_lbs }}</h3>
        <p>Base Weight (lbs)</p>
      </div>
    </div>
    
    <p class="photo-credit">{{ site.image_credits.hero }}</p>
  </div>
</div>

<div class="trail-overview">
  <h2>The Plan</h2>
  <p>Beginning March 15, I'll be hiking northbound from Mexico to Utah. The journey covers 800 miles through Arizona's diverse landscapes - from desert lowlands to alpine forests, through canyons and mountain ranges. My wife Beth will join me for the Grand Canyon rim-to-rim section on May 15, which will be a special highlight of the trek.</p>
</div>

<div class="elevation-overview">
  <img src="{{ site.baseurl }}/assets/images/elevation/azt_elevation_profile.png" alt="AZT Full Elevation Profile" class="full-elevation-profile">
  <p class="caption">The Route: Mexico to Utah (with significant elevation changes)</p>
</div>

<div class="quick-links">
  <h2>Planning Resources</h2>
  <div class="link-grid">
    <a href="{{ site.baseurl }}/gear-list" class="link-card">
      <h3>🎒 Gear List</h3>
      <p>13.12 lbs base weight</p>
    </a>
    <a href="{{ site.baseurl }}/food-plan" class="link-card">
      <h3>🍎 Food Strategy</h3>
      <p>2600-3300 calories/day</p>
    </a>
    <a href="{{ site.baseurl }}/water-strategies" class="link-card">
      <h3>💧 Water Planning</h3>
      <p>Source to source</p>
    </a>
    <a href="{{ site.baseurl }}/pre-departure-checklist" class="link-card">
      <h3>✅ Pre-Departure</h3>
      <p>Final preparations</p>
    </a>
  </div>
</div>

<div class="section-grid">
  <h2>Trail Sections</h2>
  <div class="sections-container">
    {% assign sorted_sections = site.sections | sort: "section_number" %}
    {% for section in sorted_sections %}
    {% unless section.path contains "template" %}
    <div class="section-card">
      <div class="section-image" style="background-image: url('{{ site.baseurl }}/assets/images/elevation/{{ section.section_number | prepend: '0' | slice: -2, 2 }}_elevation.png')">
        <div class="section-image-overlay">
          <h3>{{ section.title }}</h3>
        </div>
      </div>
      <div class="section-content">
        <div class="section-stats">
          <span>{{ section.distance }} miles</span>
          <span>{{ section.elevation }} ft gain</span>
          <span>{{ section.days }} days planned</span>
        </div>
        <p>{{ section.description | truncate: 100 }}</p>
        <div class="section-details">
          <a href="{{ section.url | prepend: site.baseurl }}" class="section-link">View Details →</a>
        </div>
      </div>
    </div>
    {% endunless %}
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
    const startDate = new Date('2025-03-15T07:00:00');
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