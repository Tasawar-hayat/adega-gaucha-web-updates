import sys

with open("index.html", "r") as f:
    lines = f.readlines()

new_html = """    <!-- TdB Replica Hero Main Content -->
    <div class="tdb-hero-layout">
      <!-- Centered Logo -->
      <img src="https://adegagaucha.com/wp-content/uploads/2023/11/adega-gaucha-logo-white.png" alt="Adega Gaucha" class="tdb-logo">
      
      <!-- Central Reservation Box -->
      <div class="tdb-reservation-box">
        <h2>RESERVE A TABLE</h2>
        
        <div class="tdb-form-group">
          <label>Choose Your Location</label>
          <div class="tdb-dropdown-wrapper">
            <select class="tdb-select" id="tdb-location-select">
              <option value="orlando">Orlando</option>
              <option value="kissimmee">Kissimmee</option>
              <option value="deerfieldbeach">Deerfield Beach</option>
            </select>
            <div class="tdb-arrow">↓</div>
          </div>
        </div>

        <button class="tdb-btn-primary" onclick="window.open('https://adegagaucha.com/reservations/' + document.getElementById('tdb-location-select').value, '_blank')">
          FIND A TABLE <span>➔</span>
        </button>

        <a href="https://adegagaucha.com/group-dining/" target="_blank" class="tdb-btn-secondary">
          HOST AN EVENT FOR 15+ GUESTS <span>➔</span>
        </a>
      </div>
    </div>
"""

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if "<!-- Hero Main Content -->" in line:
        start_idx = i
    if "</script>" in line and start_idx != -1 and i > start_idx:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    new_lines = lines[:start_idx] + [new_html] + lines[end_idx+1:]
    with open("index.html", "w") as f:
        f.writelines(new_lines)
    print("HTML replaced successfully!")
else:
    print("Could not find start or end index.")
    print(f"Start: {start_idx}, End: {end_idx}")
