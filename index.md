---
layout: default
title: My AZT 2025 Plan
---

<div class="hero-section">
  <img src="{{ site.baseurl }}/assets/images/azt-hero.jpg" alt="Arizona Trail Hero Image" class="hero-image">
  <div class="hero-content">
    <h1>My Arizona Trail Adventure</h1>
    <p class="subtitle">800 Miles of Desert, Mountains, and Canyons</p>
    <div class="countdown">
      <p>Go Time: March 15, 2025 (<span id="countdown">Loading...</span>)</p>
    </div>
    
    <div class="stats-container">
      <div class="stat-box">
        <h3>800</h3>
        <p>Miles to Walk</p>
      </div>
      <div class="stat-box">
        <h3>45-50</h3>
        <p>Days on Trail</p>
      </div>
      <div class="stat-box">
        <h3>96,000</h3>
        <p>Feet to Climb</p>
      </div>
    </div>
    
    <p class="photo-credit">{{ site.image_credits.hero }}</p>
  </div>
</div>

<div class="trail-overview">
  <h2>The Plan</h2>
  <p>Starting March 15, heading NOBO from Mexico to Utah. 800 miles through everything Arizona's got - desert, forests, canyons, you name it. Beth's joining for the Grand Canyon R2R on May 15 (can't wait!). Got my gear dialed, food planned, and ready to crush some miles.</p>
</div>

<div class="elevation-overview">
  <img src="{{ site.baseurl }}/assets/images/elevation/azt_elevation_profile.png" alt="AZT Full Elevation Profile" class="full-elevation-profile">
  <p class="caption">The Route: Mexico ➔ Utah (gonna be some climbing!)</p>
</div>

<div class="quick-links">
  <h2>Quick Links</h2>
  <div class="link-grid">
    <a href="{{ site.baseurl }}/gear-list" class="link-card">
      <h3>🎒 My Gear</h3>
      <p>13.12 lbs base weight</p>
    </a>
    <a href="{{ site.baseurl }}/food-plan" class="link-card">
      <h3>🍎 Food Plan</h3>
      <p>2600-3300 cal/day</p>
    </a>
    <a href="{{ site.baseurl }}/water-strategies" class="link-card">
      <h3>💧 Water Plan</h3>
      <p>Desert to mountains</p>
    </a>
    <a href="{{ site.baseurl }}/pre-departure-checklist" class="link-card">
      <h3>✅ Checklist</h3>
      <p>Don't forget stuff!</p>
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
      <h3>{{ section.title }}</h3>
      <div class="section-stats">
        <span>{{ section.distance }} miles</span>
        <span>{{ section.elevation }} ft gain</span>
        <span>{{ section.days }} days planned</span>
      </div>
      <p>{{ section.description | truncate: 100 }}</p>
      <a href="{{ section.url | prepend: site.baseurl }}" class="section-link">Section Details →</a>
    </div>
    {% endunless %}
    {% endfor %}
  </div>
</div>

<div class="preparation-status">
  <h2>Where I'm At</h2>
  <div class="status-grid">
    <div class="status-item">
      <h3>✅ Done</h3>
      <ul>
        <li>Core gear tested</li>
        <li>Route planned</li>
        <li>Permits secured</li>
        <li>Training ongoing</li>
      </ul>
    </div>
    <div class="status-item">
      <h3>🚧 In Progress</h3>
      <ul>
        <li>Food planning</li>
        <li>Mail drops</li>
        <li>Final gear tweaks</li>
      </ul>
    </div>
    <div class="status-item">
      <h3>⏳ Coming Up</h3>
      <ul>
        <li>Last shakedown hike</li>
        <li>Pack mail drops</li>
        <li>Final gear check</li>
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

*Living document - updates coming as prep continues* 