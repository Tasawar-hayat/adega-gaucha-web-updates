import sys

with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

css_start_idx = -1
css_end_idx = -1

for i, line in enumerate(lines):
    if "/* TDB REPLICA HERO LAYOUT */" in line:
        css_start_idx = i
    if "/* =========================================" in line and css_start_idx != -1:
        css_end_idx = i
        break

html_start_idx = -1
html_end_idx = -1

for i, line in enumerate(lines):
    if "<!-- TdB Replica Hero Main Content -->" in line:
        html_start_idx = i
    if "</section>" in line and html_start_idx != -1:
        html_end_idx = i
        break

new_css = """/* ADEGA GAUCHA PREMIUM HERO LAYOUT */
.ag-premium-layout {
  position: relative;
  z-index: 5;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100vh;
  padding: 2rem;
}

.ag-premium-box {
  background: rgba(10, 10, 10, 0.45);
  backdrop-filter: blur(25px);
  -webkit-backdrop-filter: blur(25px);
  border-radius: 20px;
  padding: 3rem;
  width: 100%;
  max-width: 520px;
  box-shadow: 0 25px 60px rgba(0,0,0,0.8), inset 0 0 0 1px rgba(255,255,255,0.15);
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: all 0.4s ease;
}

.ag-premium-box:hover {
  box-shadow: 0 30px 70px rgba(0,0,0,0.9), inset 0 0 0 1px rgba(250, 135, 34, 0.3);
}

.ag-premium-box h2 {
  font-family: 'Oswald', sans-serif;
  color: #fff;
  font-size: 2rem;
  font-weight: 500;
  text-transform: uppercase;
  margin-bottom: 2rem;
  letter-spacing: 2px;
}

.ag-form-group {
  width: 100%;
  margin-bottom: 2rem;
  text-align: left;
}

.ag-form-group label {
  display: block;
  color: rgba(255,255,255,0.8);
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 0.95rem;
  margin-bottom: 10px;
  letter-spacing: 1px;
}

.ag-dropdown-wrapper {
  position: relative;
  width: 100%;
}

.ag-select {
  width: 100%;
  appearance: none;
  background: rgba(0,0,0,0.5);
  color: #fff;
  border: 1px solid rgba(255,255,255,0.1);
  padding: 16px 20px;
  font-size: 1.05rem;
  font-family: 'Inter', sans-serif;
  font-weight: 300;
  cursor: pointer;
  border-radius: 10px;
  transition: all 0.3s ease;
}

.ag-select:focus, .ag-select:hover {
  outline: none;
  border-color: var(--primary-orange);
  background: rgba(0,0,0,0.7);
}

.ag-arrow {
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  color: rgba(255,255,255,0.5);
  pointer-events: none;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.ag-select:hover + .ag-arrow, .ag-select:focus + .ag-arrow {
  color: var(--primary-orange);
}

.ag-btn-primary {
  width: 100%;
  background: var(--primary-orange);
  color: #fff;
  border: none;
  padding: 16px;
  font-size: 1.05rem;
  font-weight: 600;
  font-family: 'Inter', sans-serif;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px;
  border-radius: 10px;
  transition: all 0.3s ease;
  margin-bottom: 1.2rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  box-shadow: 0 10px 25px rgba(250, 135, 34, 0.4);
}

.ag-btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 35px rgba(250, 135, 34, 0.6);
  background: #ff983f;
}

.ag-btn-primary span, .ag-btn-secondary span {
  transition: transform 0.3s ease;
}
.ag-btn-primary:hover span, .ag-btn-secondary:hover span {
  transform: translateX(5px);
}

.ag-btn-secondary {
  width: 100%;
  background: rgba(0,0,0,0.4);
  color: #fff;
  border: 1px solid rgba(255,255,255,0.15);
  padding: 16px;
  font-size: 0.95rem;
  font-weight: 500;
  font-family: 'Inter', sans-serif;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px;
  border-radius: 10px;
  transition: all 0.3s ease;
  text-transform: uppercase;
  text-decoration: none;
  letter-spacing: 1px;
}

.ag-btn-secondary:hover {
  background: rgba(250, 135, 34, 0.1);
  border-color: var(--primary-orange);
  color: var(--primary-orange);
}

/* MOBILE RESPONSIVENESS */
@media(max-width: 768px) {
  .ag-premium-box { padding: 2rem 1.5rem; max-width: 90%; border-radius: 16px; }
  .ag-premium-box h2 { font-size: 1.6rem; margin-bottom: 1.5rem; }
  .ag-btn-primary, .ag-btn-secondary { padding: 14px; font-size: 0.95rem; }
  .ag-select { padding: 14px 18px; font-size: 1rem; }
}

@media(max-width: 480px) {
  .ag-premium-layout { padding: 1rem; }
  .ag-premium-box { padding: 1.8rem 1.2rem; max-width: 100%; width: 95%; }
  .ag-premium-box h2 { font-size: 1.4rem; }
}
"""

new_html = """    <!-- Adega Gaucha Premium Hero Content -->
    <div class="ag-premium-layout">
      
      <!-- Central Reservation Box -->
      <div class="ag-premium-box">
        <h2>RESERVE A TABLE</h2>
        
        <div class="ag-form-group">
          <label>Choose Your Location</label>
          <div class="ag-dropdown-wrapper">
            <select class="ag-select" id="ag-location-select">
              <option value="orlando">Orlando</option>
              <option value="kissimmee">Kissimmee</option>
              <option value="deerfieldbeach">Deerfield Beach</option>
            </select>
            <div class="ag-arrow">▼</div>
          </div>
        </div>

        <button class="ag-btn-primary" onclick="window.open('https://adegagaucha.com/reservations/' + document.getElementById('ag-location-select').value, '_blank')">
          FIND A TABLE <span>➔</span>
        </button>

        <a href="https://adegagaucha.com/group-dining/" target="_blank" class="ag-btn-secondary">
          HOST AN EVENT FOR 20+ GUESTS <span>➔</span>
        </a>
      </div>
    </div>
"""

if css_start_idx != -1 and css_end_idx != -1 and html_start_idx != -1 and html_end_idx != -1:
    new_lines = lines[:css_start_idx] + [new_css + "\n"] + lines[css_end_idx:html_start_idx] + [new_html] + lines[html_end_idx:]
    with open("index.html", "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("Success!")
else:
    print(f"CSS: {css_start_idx}-{css_end_idx}, HTML: {html_start_idx}-{html_end_idx}")
