---
layout: default
title: Dave Remy's AZT 2025 Thru-Hike Plan
---

<div class="hero-section">
  <img src="{{ site.baseurl }}/assets/images/azt-hero.jpg" alt="Arizona Trail Hero Image" class="hero-image">
  <div class="hero-content">
    <h1>Dave Remy's Arizona Trail 2025</h1>
    <p class="subtitle">A Personal Journey: 800 Miles Through the Heart of Arizona</p>
    <div class="countdown">
      <p>Trail Start: March 15, 2025 (<span id="countdown">Loading...</span>)</p>
    </div>
    
    <div class="stats-container">
      <div class="stat-box">
        <h3>800</h3>
        <p>Total Miles</p>
      </div>
      <div class="stat-box">
        <h3>45-50</h3>
        <p>Days Planned</p>
      </div>
      <div class="stat-box">
        <h3>96,000</h3>
        <p>Feet of Elevation</p>
      </div>
    </div>
    
    <p class="photo-credit">{{ site.image_credits.hero }}</p>
  </div>
</div>

<div class="main-navigation">
  <div class="nav-grid">
    <a href="{{ '/about/' | relative_url }}" class="nav-item">
      <h3>About</h3>
      <p>Learn about my journey and mentorship</p>
    </a>
    <a href="{{ '/overall-plan/' | relative_url }}" class="nav-item">
      <h3>Overall Plan</h3>
      <p>The big picture strategy</p>
    </a>
    <a href="{{ '/logistics/' | relative_url }}" class="nav-item">
      <h3>Logistics</h3>
      <p>Transportation and coordination</p>
    </a>
    <a href="{{ '/food-plan/' | relative_url }}" class="nav-item">
      <h3>Food Plan</h3>
      <p>Meal planning and resupply strategy</p>
    </a>
    <a href="{{ '/water-strategies/' | relative_url }}" class="nav-item">
      <h3>Water</h3>
      <p>Water sources and management</p>
    </a>
    <a href="{{ '/pre-departure-checklist/' | relative_url }}" class="nav-item">
      <h3>Checklist</h3>
      <p>Pre-departure preparation</p>
    </a>
  </div>
</div>

<div class="trail-overview">
  <h2>My Journey</h2>
  <p>Starting March 15, 2025, I'll be embarking on a northbound thru-hike of the Arizona Trail (AZT). This 800-mile scenic trail stretches from Mexico to Utah, showcasing Arizona's diverse landscapes from desert to pine forests, from canyons to peaks. My wife Beth will join me for the iconic Grand Canyon rim-to-rim section on May 15, making this journey even more special.</p>
</div>

<div class="elevation-overview">
  <img src="{{ site.baseurl }}/assets/images/elevation/azt_elevation_profile.png" alt="AZT Full Elevation Profile" class="full-elevation-profile">
  <p class="caption">My Route: Mexico Border to Utah Border (800 miles)</p>
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
          <span class="section-number">{{ section.section_number }}</span>
          <h3>{{ section.title }}</h3>
        </div>
      </div>
      <div class="section-content">
        <div class="section-details">
          <p class="distance">{{ section.distance }} miles</p>
          <a href="{{ section.url | relative_url }}" class="section-link">View Details →</a>
        </div>
      </div>
    </div>
    {% endunless %}
    {% endfor %}
  </div>
</div>

<div class="planning-section">
  <h2>My Planning Resources</h2>
  <div class="resource-grid">
    <div class="resource-card">
      <h3>Trail Preparation</h3>
      <ul>
        <li><a href="{{ '/pre-departure-checklist/' | relative_url }}">Pre-Departure Checklist</a></li>
        <li><a href="{{ '/immediate-actions/' | relative_url }}">Immediate Actions</a></li>
        <li><a href="{{ '/overall-plan/' | relative_url }}">Overall Strategy</a></li>
        <li><a href="{{ '/gear-list/' | relative_url }}">Gear List</a></li>
      </ul>
    </div>
    <div class="resource-card">
      <h3>Trail Resources</h3>
      <ul>
        <li><a href="{{ '/water-strategies/' | relative_url }}">Water Strategies</a></li>
        <li><a href="https://aztrail.org/explore/water-sources/" target="_blank">AZT Water Report</a></li>
        <li><a href="https://aztrail.org/explore/current-trail-conditions/" target="_blank">Current Conditions</a></li>
      </ul>
    </div>
  </div>
</div>

<script>
function updateCountdown() {
    const startDate = new Date('2025-03-15T00:00:00');
    const now = new Date();
    const diff = startDate - now;
    
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    document.getElementById('countdown').textContent = days + ' days away';
}

updateCountdown();
setInterval(updateCountdown, 86400000); // Update once per day
</script> 