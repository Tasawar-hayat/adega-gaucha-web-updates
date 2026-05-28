import sys

with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 1. Update .ag-premium-box CSS
for i, line in enumerate(lines):
    if ".ag-premium-box {" in line:
        # We need to replace the next few lines
        # Find the transition: all 0.4s ease;
        start_idx = i
        end_idx = i
        for j in range(i, len(lines)):
            if "transition: all 0.4s ease;" in lines[j]:
                end_idx = j
                break
        
        new_box_css = """.ag-premium-box {
  background: rgba(10, 10, 10, 0.45);
  backdrop-filter: blur(25px);
  -webkit-backdrop-filter: blur(25px);
  border-radius: 20px;
  padding: 3rem;
  width: 100%;
  max-width: 520px;
  position: absolute;
  bottom: 60px;
  left: 50%;
  /* Fire Animation Start State */
  opacity: 0;
  transform: translateX(-50%) translateY(50px) scale(0.9);
  animation: boxReveal 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) 0.6s forwards;
  box-shadow: 0 25px 60px rgba(0,0,0,0.8), inset 0 0 0 1px rgba(255,255,255,0.15);
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: box-shadow 0.4s ease;
}

@keyframes boxReveal {
  to {
    opacity: 1;
    transform: translateX(-50%) translateY(0) scale(1);
  }
}
"""
        lines[start_idx:end_idx+2] = [new_box_css]
        break

# 2. Add Fire Embers CSS before </style>
for i, line in enumerate(lines):
    if "</style>" in line:
        fire_css = """
/* Fire Embers Animation */
.fire-spark-container {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100%;
  max-width: 600px;
  height: 400px;
  pointer-events: none;
  z-index: 6;
  overflow: visible;
}

.ember {
  position: absolute;
  bottom: -20px;
  width: 5px;
  height: 5px;
  background: #ff5e00;
  border-radius: 50%;
  box-shadow: 0 0 10px #ff5e00, 0 0 20px #ff9d00;
  opacity: 0;
  filter: blur(1px);
}

@keyframes flyUp {
  0% {
    transform: translateY(0) translateX(0) scale(1);
    opacity: 1;
  }
  100% {
    transform: translateY(var(--fly-y)) translateX(var(--fly-x)) scale(0);
    opacity: 0;
  }
}
"""
        lines.insert(i, fire_css)
        break

# 3. Add Ember Container in HTML
for i, line in enumerate(lines):
    if '<!-- Central Reservation Box -->' in line:
        ember_html = '      <!-- Fire Embers Container -->\n      <div class="fire-spark-container" id="ember-container"></div>\n\n'
        lines.insert(i, ember_html)
        break

# 4. Add JS Logic
for i, line in enumerate(lines):
    if "document.addEventListener('DOMContentLoaded', function() {" in line:
        js_code = """
    // Fire Ember Generation
    const emberContainer = document.getElementById('ember-container');
    if (emberContainer) {
      for (let i = 0; i < 40; i++) {
        const ember = document.createElement('div');
        ember.classList.add('ember');
        
        // Randomize starting X position (center-weighted)
        const left = 50 + (Math.random() - 0.5) * 60;
        ember.style.left = left + '%';
        
        // Randomize animation variables
        const flyY = -150 - Math.random() * 300 + 'px';
        const flyX = (Math.random() - 0.5) * 200 + 'px';
        const duration = 0.6 + Math.random() * 0.8 + 's';
        const delay = Math.random() * 0.3 + 's';
        
        ember.style.setProperty('--fly-y', flyY);
        ember.style.setProperty('--fly-x', flyX);
        ember.style.animation = `flyUp ${duration} cubic-bezier(0.2, 0.8, 0.2, 1) ${delay} forwards`;
        
        // Color variation (orange to yellow)
        if (Math.random() > 0.6) {
          ember.style.background = '#ffb300';
          ember.style.boxShadow = '0 0 10px #ffb300, 0 0 20px #fff';
        }
        
        emberContainer.appendChild(ember);
      }
    }
"""
        lines.insert(i + 1, js_code)
        break

with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(lines)
