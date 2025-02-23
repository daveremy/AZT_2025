---
layout: page
title: Pack Checklist
permalink: /pack-checklist/
---

<style>
.checklist {
  max-width: 800px;
  margin: 0 auto;
}

.checklist input[type="checkbox"] {
  margin-right: 8px;
}

.checklist-item {
  display: flex;
  align-items: center;
  padding: 4px 0;
}

.checklist-item:hover {
  background: #f8f9fa;
}

.section {
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 16px;
  margin: 16px 0;
  background: white;
}

.section h2, .section h3 {
  margin-top: 0;
}

.progress-bar {
  width: 100%;
  height: 20px;
  background-color: #e9ecef;
  border-radius: 10px;
  margin: 16px 0;
  overflow: hidden;
}

.progress {
  height: 100%;
  background-color: #28a745;
  transition: width 0.3s ease;
}

.progress-text {
  text-align: center;
  font-size: 0.9em;
  color: #6c757d;
}

.reset-button {
  display: block;
  margin: 20px auto;
  padding: 8px 16px;
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.reset-button:hover {
  background-color: #c82333;
}

/* Print styles */
@media print {
  .reset-button {
    display: none;
  }
  
  .section {
    break-inside: avoid;
    border: none;
    padding: 8px 0;
  }
  
  .checklist-item {
    break-inside: avoid;
  }
}
</style>

<div class="checklist">

<div class="progress-bar">
  <div class="progress" id="progress"></div>
</div>
<div class="progress-text" id="progress-text">0% Complete</div>

<h1>Pack Checklist</h1>

<p>A detailed, step-by-step guide for packing my backpack. This ensures consistent packing and helps verify I haven't forgotten anything.</p>

<div class="section">
<h2>Before Starting</h2>

<div class="checklist-item">1. <input type="checkbox" class="pack-item"> Lay out all gear on a flat surface</div>
<div class="checklist-item">2. <input type="checkbox" class="pack-item"> Check weather forecast</div>
<div class="checklist-item">3. <input type="checkbox" class="pack-item"> Have 3 gallon ziplocks and 2 quart ziplocks ready</div>
<div class="checklist-item">4. <input type="checkbox" class="pack-item"> Ensure pack is completely empty</div>
</div>

<div class="section">
<h2>Organized Bags</h2>

<h3>Electronics Bag (Quart Ziplock #1)</h3>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> 2x Nitecore NB10000 batteries</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> 2x USB-C cables</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> RovyVon Aurora A5 G4 light</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Insta360 X4 extra battery</div>

<h3>Toiletries Bag (Quart Ziplock #2)</h3>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> VIVAGO bamboo toothbrush</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Crest travel toothpaste</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Medications in pill pocket</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Hand sanitizer (small)</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Lip balm</div>

<h3>Sleep Clothes Bag (Gallon Ziplock #1)</h3>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Helly Hansen long sleeve</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> New Balance running shorts</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Injinji liner crew socks</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Uniqlo Airism boxers (sleep pair)</div>

<h3>Bathroom Kit (Gallon Ziplock #2)</h3>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> TheTentLab Deuce trowel</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Pre-dried wipes</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> TP</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Hand sanitizer (dedicated)</div>

<h3>Wet Weather Bag (Gallon Ziplock #3)</h3>
<em>Only when rain expected:</em>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Pack liner (garbage bag)</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Rain jacket</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Rain pants</div>
</div>

<div class="section">
<h2>Packing Order (Bottom to Top)</h2>

<h3>Bottom Section (Sleep System)</h3>
<div class="checklist-item">1. <input type="checkbox" class="pack-item"> Line with garbage bag if rain expected</div>
<div class="checklist-item">2. <input type="checkbox" class="pack-item"> Zpacks Solo quilt (in stuff sack)</div>
<div class="checklist-item">3. <input type="checkbox" class="pack-item"> Thermarest NeoAir XLite NXT</div>
<div class="checklist-item">4. <input type="checkbox" class="pack-item"> Sleep clothes bag</div>
<div class="checklist-item">5. <input type="checkbox" class="pack-item"> Camp flips</div>
<div class="checklist-item">6. <input type="checkbox" class="pack-item"> Groundsheet</div>

<h3>Middle Section (Heavy Items)</h3>
<div class="checklist-item">1. <input type="checkbox" class="pack-item"> Ursack with food (against back)</div>
<div class="checklist-item">2. <input type="checkbox" class="pack-item"> Firemaple cook system:</div>
   <div class="checklist-item" style="margin-left: 20px">- <input type="checkbox" class="pack-item"> Pot with stove inside</div>
   <div class="checklist-item" style="margin-left: 20px">- <input type="checkbox" class="pack-item"> Fuel canister</div>
   <div class="checklist-item" style="margin-left: 20px">- <input type="checkbox" class="pack-item"> Spork</div>
   <div class="checklist-item" style="margin-left: 20px">- <input type="checkbox" class="pack-item"> X-mug</div>
<div class="checklist-item">3. <input type="checkbox" class="pack-item"> Platypus 2L bladder (for dirty/pre-strained water, needs filtering before use)</div>
<div class="checklist-item">4. <input type="checkbox" class="pack-item"> Patagonia Nano Puff (when not wearing)</div>
<div class="checklist-item">5. <input type="checkbox" class="pack-item"> Brynje base layer</div>

<h3>Top Section (Quick Access)</h3>
<div class="checklist-item">1. <input type="checkbox" class="pack-item"> Electronics bag</div>
<div class="checklist-item">2. <input type="checkbox" class="pack-item"> Toiletries bag</div>
<div class="checklist-item">3. <input type="checkbox" class="pack-item"> Bathroom kit</div>
<div class="checklist-item">4. <input type="checkbox" class="pack-item"> First aid items</div>
<div class="checklist-item">5. <input type="checkbox" class="pack-item"> Buff</div>
<div class="checklist-item">6. <input type="checkbox" class="pack-item"> Bike gloves</div>
<div class="checklist-item">7. <input type="checkbox" class="pack-item"> Alternate socks/underwear</div>

<h3>Outside Mesh Pocket</h3>
<div class="checklist-item">1. <input type="checkbox" class="pack-item"> Tent body and poles (if wet)</div>
<div class="checklist-item">2. <input type="checkbox" class="pack-item"> Wet gear that needs to dry</div>
<div class="checklist-item">3. <input type="checkbox" class="pack-item"> Trekology pillow</div>
<div class="checklist-item">4. <input type="checkbox" class="pack-item"> Water filter</div>
</div>

<div class="section">
<h2>Specific Pocket Setup</h2>

<h3>Hip Belt Pockets</h3>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Left pocket: snacks, sunscreen, and small items</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Right pocket: phone and essentials</div>

<h3>Shoulder Strap Setup</h3>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Magnetic selfie stick holster on left strap</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Insta360 X4 mounted in magnetic holster</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Verify Insta360 lens cap is secure</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> InReach Mini 2 on right strap mount</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> 1L Smartwater bottle in right strap holder</div>

<h3>Side Pockets</h3>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Left side QuickPocket: easy access to larger items</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Left side main pocket: 1L Smartwater bottle and trekking poles when not in use</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Right side pocket: 1L Smartwater bottle</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Small zippered pocket behind right side pocket: valuables</div>

<h3>Front Mesh Pocket</h3>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Rain gear for quick access</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Wet tent when needed</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Items needed during the day</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Wet gear that needs to dry</div>
</div>

<div class="section">
<h2>First Aid</h2>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Leukotape P strip (for blister prevention/treatment)</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Medications in pill pockets:</div>
<div class="checklist-item" style="margin-left: 20px">- <input type="checkbox" class="pack-item"> Ibuprofen</div>
<div class="checklist-item" style="margin-left: 20px">- <input type="checkbox" class="pack-item"> Acetaminophen</div>
<div class="checklist-item" style="margin-left: 20px">- <input type="checkbox" class="pack-item"> Benadryl</div>
<div class="checklist-item" style="margin-left: 20px">- <input type="checkbox" class="pack-item"> Imodium</div>
<div class="checklist-item" style="margin-left: 20px">- <input type="checkbox" class="pack-item"> Pepto</div>
<div class="checklist-item" style="margin-left: 20px">- <input type="checkbox" class="pack-item"> Melatonin</div>
</div>

<div class="section">
<h2>Final Checks</h2>

<div class="checklist-item">1. <input type="checkbox" class="pack-item"> Bounce test - everything secure?</div>
<div class="checklist-item">2. <input type="checkbox" class="pack-item"> All zippers closed?</div>
<div class="checklist-item">3. <input type="checkbox" class="pack-item"> Compression straps adjusted?</div>
<div class="checklist-item">4. <input type="checkbox" class="pack-item"> Hip belt even on both sides?</div>
<div class="checklist-item">5. <input type="checkbox" class="pack-item"> Load lifters adjusted?</div>
<div class="checklist-item">6. <input type="checkbox" class="pack-item"> Nothing loose/dangling?</div>
</div>

<div class="section">
<h2>Weather-Specific Adjustments</h2>

<h3>For Rain</h3>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Pack liner installed</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Rain gear at top</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Electronics double-bagged</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Dry bags for critical items</div>

<h3>For Cold</h3>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Puffy accessible</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Gloves handy</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Warm layers near top</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Brynje base layer available</div>

<h3>For Desert</h3>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Extra water capacity ready</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Sun protection accessible</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Filter easy to reach</div>
<div class="checklist-item">- <input type="checkbox" class="pack-item"> Ventilation maximized</div>
</div>

<div class="section">
<h2>Pre-Hike Verification</h2>

<div class="checklist-item">1. <input type="checkbox" class="pack-item"> Weigh fully packed bag</div>
<div class="checklist-item">2. <input type="checkbox" class="pack-item"> Walk test for 5 minutes</div>
<div class="checklist-item">3. <input type="checkbox" class="pack-item"> Check strap comfort</div>
<div class="checklist-item">4. <input type="checkbox" class="pack-item"> Verify quick-access items</div>
<div class="checklist-item">5. <input type="checkbox" class="pack-item"> Test water bottle reach</div>
<div class="checklist-item">6. <input type="checkbox" class="pack-item"> Practice tent setup access</div>
</div>

<button class="reset-button" onclick="resetChecklist()">Reset Checklist</button>

</div>

<script>
function updateProgress() {
  const total = document.querySelectorAll('.pack-item').length;
  const checked = document.querySelectorAll('.pack-item:checked').length;
  const percent = Math.round((checked / total) * 100);
  
  document.getElementById('progress').style.width = percent + '%';
  document.getElementById('progress-text').textContent = percent + '% Complete';
  
  // Save state
  const checkboxes = document.querySelectorAll('.pack-item');
  const state = Array.from(checkboxes).map(cb => cb.checked);
  localStorage.setItem('packingChecklist', JSON.stringify(state));
}

function resetChecklist() {
  document.querySelectorAll('.pack-item').forEach(cb => cb.checked = false);
  updateProgress();
}

// Load saved state
document.addEventListener('DOMContentLoaded', function() {
  const saved = localStorage.getItem('packingChecklist');
  if (saved) {
    const state = JSON.parse(saved);
    const checkboxes = document.querySelectorAll('.pack-item');
    checkboxes.forEach((cb, i) => cb.checked = state[i]);
    updateProgress();
  }
  
  // Add change listeners
  document.querySelectorAll('.pack-item').forEach(cb => {
    cb.addEventListener('change', updateProgress);
  });
});
</script>

<em>Remember: A well-packed bag makes for easier hiking. Take time to pack deliberately and consistently.</em> 