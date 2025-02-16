---
title: Section Overview
layout: page
---

# AZT Section Overview

<div class="section-timeline">
  <div class="progress-bar">
    <div class="progress" style="width: 0%"></div>
  </div>
  <div class="timeline">
    {% for i in (1..9) %}
      <div class="marker" style="left: {{ i | minus: 1 | times: 12.5 }}%"></div>
      <div class="label" style="left: {{ i | minus: 1 | times: 12.5 }}%">Section {{ i }}</div>
    {% endfor %}
  </div>
</div>

## Quick Stats
- Total Distance: 691.4 miles
- Total Days: 47-54
- Water Sources: 66
- Elevation Range: 2,200 ft to 8,800 ft

## All Sections

<div class="section-card">
  <h3>1. Border to Patagonia</h3>
  <div class="stats">
    <div class="stat-group">
      <span class="label">Distance</span>
      <span class="value">52.1 miles</span>
    </div>
    <div class="stat-group">
      <span class="label">Days</span>
      <span class="value">5-6</span>
    </div>
    <div class="stat-group">
      <span class="label">Water Sources</span>
      <span class="value">7</span>
    </div>
    <div class="stat-group elevation-stat" style="--elevation-color: var(--mid-elevation)">
      <span class="label">Elevation</span>
      <span class="value">4,264' to 6,601'</span>
    </div>
  </div>
  <div class="elevation-profile">
    <div class="profile-line" style="
      --start-color: var(--mid-elevation);
      --end-color: var(--high-elevation);
      --elevation-path: polygon(0 60%, 30% 40%, 50% 20%, 70% 30%, 100% 10%);
    "></div>
    <div class="elevation-labels">
      <span>4,264'</span>
      <span>6,601'</span>
    </div>
  </div>
  <p>Key Points: Coronado National Memorial, Parker Canyon Lake</p>
  <a href="sections/01-border-to-patagonia.html">View Details →</a>
</div>

<div class="section-card">
  <h3>2. Patagonia to Tucson</h3>
  <div class="stats">
    <div class="stat-group">
      <span class="label">Distance</span>
      <span class="value">94.5 miles</span>
    </div>
    <div class="stat-group">
      <span class="label">Days</span>
      <span class="value">7-8</span>
    </div>
    <div class="stat-group">
      <span class="label">Water Sources</span>
      <span class="value">8</span>
    </div>
    <div class="stat-group elevation-stat" style="--elevation-color: var(--mid-elevation)">
      <span class="label">Elevation</span>
      <span class="value">3,800' to 5,800'</span>
    </div>
  </div>
  <div class="elevation-profile">
    <div class="profile-line" style="
      --start-color: var(--low-elevation);
      --end-color: var(--mid-elevation);
      --elevation-path: polygon(0 70%, 20% 50%, 40% 30%, 60% 40%, 100% 20%);
    "></div>
    <div class="elevation-labels">
      <span>3,800'</span>
      <span>5,800'</span>
    </div>
  </div>
  <p>Key Points: Kentucky Camp, Las Cienegas, Colossal Cave</p>
  <a href="sections/02-patagonia-to-tucson.html">View Details →</a>
</div>

<div class="section-card">
  <h3>3. Tucson to Oracle</h3>
  <div class="stats">
    <div class="stat-group">
      <span class="label">Distance</span>
      <span class="value">82.4 miles</span>
    </div>
    <div class="stat-group">
      <span class="label">Days</span>
      <span class="value">6-7</span>
    </div>
    <div class="stat-group">
      <span class="label">Water Sources</span>
      <span class="value">9</span>
    </div>
    <div class="stat-group elevation-stat" style="--elevation-color: var(--very-high-elevation)">
      <span class="label">Elevation</span>
      <span class="value">2,700' to 8,800'</span>
    </div>
  </div>
  <div class="elevation-profile">
    <div class="profile-line" style="
      --start-color: var(--low-elevation);
      --end-color: var(--very-high-elevation);
      --elevation-path: polygon(0 90%, 20% 70%, 40% 40%, 60% 20%, 80% 10%, 100% 0%);
    "></div>
    <div class="elevation-labels">
      <span>2,700'</span>
      <span>8,800'</span>
    </div>
  </div>
  <p>Key Points: Saguaro NP, Mt. Lemmon, Oracle Ridge</p>
  <a href="sections/03-tucson-to-oracle.html">View Details →</a>
</div>

<div class="section-card">
  <h3>4. Oracle to Superior</h3>
  <div class="stats">
    <div class="stat-group">
      <span class="label">Distance</span>
      <span class="value">51.4 miles</span>
    </div>
    <div class="stat-group">
      <span class="label">Days</span>
      <span class="value">4</span>
    </div>
    <div class="stat-group">
      <span class="label">Water Sources</span>
      <span class="value">5</span>
    </div>
    <div class="stat-group elevation-stat" style="--elevation-color: var(--mid-elevation)">
      <span class="label">Elevation</span>
      <span class="value">2,400' to 4,800'</span>
    </div>
  </div>
  <div class="elevation-profile">
    <div class="profile-line" style="
      --start-color: var(--low-elevation);
      --end-color: var(--mid-elevation);
      --elevation-path: polygon(0 80%, 30% 60%, 50% 40%, 70% 30%, 100% 40%);
    "></div>
    <div class="elevation-labels">
      <span>2,400'</span>
      <span>4,800'</span>
    </div>
  </div>
  <p>Key Points: Oracle State Park, Antelope Peak</p>
  <a href="sections/04-oracle-to-superior.html">View Details →</a>
</div>

<div class="section-card">
  <h3>5. Superior to Pine</h3>
  <div class="stats">
    <div class="stat-group">
      <span class="label">Distance</span>
      <span class="value">119.3 miles</span>
    </div>
    <div class="stat-group">
      <span class="label">Days</span>
      <span class="value">8-9</span>
    </div>
    <div class="stat-group">
      <span class="label">Water Sources</span>
      <span class="value">9</span>
    </div>
    <div class="stat-group elevation-stat" style="--elevation-color: var(--high-elevation)">
      <span class="label">Elevation</span>
      <span class="value">2,200' to 6,500'</span>
    </div>
  </div>
  <div class="elevation-profile">
    <div class="profile-line" style="
      --start-color: var(--low-elevation);
      --end-color: var(--high-elevation);
      --elevation-path: polygon(0 95%, 20% 80%, 40% 50%, 60% 30%, 80% 20%, 100% 15%);
    "></div>
    <div class="elevation-labels">
      <span>2,200'</span>
      <span>6,500'</span>
    </div>
  </div>
  <p>Key Points: Reavis Ranch, Roosevelt Lake, Four Peaks</p>
  <a href="sections/05-superior-to-pine.html">View Details →</a>
</div>

<div class="section-card">
  <h3>6. Pine to Mormon Lake</h3>
  <div class="stats">
    <div class="stat-group">
      <span class="label">Distance</span>
      <span class="value">85.8 miles</span>
    </div>
    <div class="stat-group">
      <span class="label">Days</span>
      <span class="value">5-6</span>
    </div>
    <div class="stat-group">
      <span class="label">Water Sources</span>
      <span class="value">7</span>
    </div>
    <div class="stat-group elevation-stat" style="--elevation-color: var(--very-high-elevation)">
      <span class="label">Elevation</span>
      <span class="value">6,500' to 8,000'</span>
    </div>
  </div>
  <div class="elevation-profile">
    <div class="profile-line" style="
      --start-color: var(--high-elevation);
      --end-color: var(--very-high-elevation);
      --elevation-path: polygon(0 40%, 20% 30%, 40% 20%, 60% 15%, 80% 10%, 100% 5%);
    "></div>
    <div class="elevation-labels">
      <span>6,500'</span>
      <span>8,000'</span>
    </div>
  </div>
  <p>Key Points: Blue Ridge, Happy Jack, Lake Mary</p>
  <a href="sections/06-pine-to-mormon-lake.html">View Details →</a>
</div>

<div class="section-card">
  <h3>7. Mormon Lake to South Rim</h3>
  <div class="stats">
    <div class="stat-group">
      <span class="label">Distance</span>
      <span class="value">101.5 miles</span>
    </div>
    <div class="stat-group">
      <span class="label">Days</span>
      <span class="value">6-7</span>
    </div>
    <div class="stat-group">
      <span class="label">Water Sources</span>
      <span class="value">8</span>
    </div>
    <div class="stat-group elevation-stat" style="--elevation-color: var(--very-high-elevation)">
      <span class="label">Elevation</span>
      <span class="value">6,500' to 8,800'</span>
    </div>
  </div>
  <div class="elevation-profile">
    <div class="profile-line" style="
      --start-color: var(--high-elevation);
      --end-color: var(--very-high-elevation);
      --elevation-path: polygon(0 40%, 30% 30%, 50% 20%, 70% 10%, 100% 0%);
    "></div>
    <div class="elevation-labels">
      <span>6,500'</span>
      <span>8,800'</span>
    </div>
  </div>
  <p>Key Points: Flagstaff, San Francisco Peaks, Tusayan</p>
  <a href="sections/07-mormon-lake-to-south-rim.html">View Details →</a>
</div>

<div class="section-card">
  <h3>8. Grand Canyon R2R</h3>
  <div class="stats">
    <div class="stat-group">
      <span class="label">Distance</span>
      <span class="value">24.0 miles</span>
    </div>
    <div class="stat-group">
      <span class="label">Days</span>
      <span class="value">1</span>
    </div>
    <div class="stat-group">
      <span class="label">Water Sources</span>
      <span class="value">6</span>
    </div>
    <div class="stat-group elevation-stat" style="--elevation-color: var(--very-high-elevation)">
      <span class="label">Elevation</span>
      <span class="value">2,480' to 8,250'</span>
    </div>
  </div>
  <div class="elevation-profile">
    <div class="profile-line" style="
      --start-color: var(--low-elevation);
      --end-color: var(--very-high-elevation);
      --elevation-path: polygon(0 0%, 30% 90%, 50% 100%, 70% 90%, 100% 0%);
    "></div>
    <div class="elevation-labels">
      <span>2,480'</span>
      <span>8,250'</span>
    </div>
  </div>
  <p>Key Points: Phantom Ranch, Colorado River</p>
  <a href="sections/08-grand-canyon-r2r.html">View Details →</a>
</div>

<div class="section-card">
  <h3>9. North Rim to Utah</h3>
  <div class="stats">
    <div class="stat-group">
      <span class="label">Distance</span>
      <span class="value">80.4 miles</span>
    </div>
    <div class="stat-group">
      <span class="label">Days</span>
      <span class="value">5-6</span>
    </div>
    <div class="stat-group">
      <span class="label">Water Sources</span>
      <span class="value">6</span>
    </div>
    <div class="stat-group elevation-stat" style="--elevation-color: var(--high-elevation)">
      <span class="label">Elevation</span>
      <span class="value">8,250' to 4,600'</span>
    </div>
  </div>
  <div class="elevation-profile">
    <div class="profile-line" style="
      --start-color: var(--very-high-elevation);
      --end-color: var(--mid-elevation);
      --elevation-path: polygon(0 0%, 20% 20%, 40% 40%, 60% 50%, 100% 70%);
    "></div>
    <div class="elevation-labels">
      <span>8,250'</span>
      <span>4,600'</span>
    </div>
  </div>
  <p>Key Points: Kaibab Plateau, Jacob Lake</p>
  <a href="sections/09-north-rim-to-utah.html">View Details →</a>
</div>

## Key Resupply Points
1. Patagonia (Mile 52.1)
2. Tucson (Mile 146.6)
3. Oracle (Mile 229.0)
4. Superior (Mile 325.1)
5. Roosevelt Lake (Mile 399.7)
6. Pine (Mile 485.5)
7. Mormon Lake (Mile 575.3)
8. Flagstaff (Mile 622.7)
9. Tusayan (Mile 669.1)
10. Jacob Lake (Mile 716.5)

## Water Considerations
- Longest waterless stretches:
  - Oracle State Park to Freeman Tank: 19.5 miles
  - Kelly Tank to Cedar Ranch: 22.3 miles
  - Crane Lake to Stateline: 23.6 miles
- Most reliable water:
  - Towns
  - Major rivers/creeks
  - Developed springs
- Seasonal concerns:
  - Spring snowmelt
  - Summer monsoons
  - Fall dry season 