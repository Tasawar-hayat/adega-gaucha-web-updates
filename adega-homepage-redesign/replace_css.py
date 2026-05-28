import sys

with open("index.html", "r") as f:
    lines = f.readlines()

new_css = """/* TDB REPLICA HERO LAYOUT */
.tdb-hero-layout {
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

.tdb-logo {
  width: 380px;
  max-width: 90%;
  margin-bottom: 3rem;
  filter: drop-shadow(0 2px 10px rgba(0,0,0,0.5));
}

.tdb-reservation-box {
  background: rgba(10, 10, 10, 0.75);
  backdrop-filter: blur(15px);
  -webkit-backdrop-filter: blur(15px);
  border-radius: 8px;
  padding: 2.5rem;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 15px 40px rgba(0,0,0,0.8);
  border: 1px solid rgba(255,255,255,0.05);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.tdb-reservation-box h2 {
  font-family: 'Oswald', sans-serif;
  color: #fff;
  font-size: 1.8rem;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 1.5rem;
  letter-spacing: 1px;
}

.tdb-form-group {
  width: 100%;
  margin-bottom: 1.5rem;
  text-align: left;
}

.tdb-form-group label {
  display: block;
  color: #fff;
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 0.95rem;
  margin-bottom: 8px;
}

.tdb-dropdown-wrapper {
  position: relative;
  width: 100%;
}

.tdb-select {
  width: 100%;
  appearance: none;
  background: #1a1a1a;
  color: #fff;
  border: 1px solid #333;
  padding: 12px 15px;
  font-size: 1rem;
  font-family: 'Inter', sans-serif;
  cursor: pointer;
  border-radius: 4px;
}

.tdb-select:focus {
  outline: none;
  border-color: #555;
}

.tdb-arrow {
  position: absolute;
  right: 15px;
  top: 50%;
  transform: translateY(-50%);
  color: #dcb360; /* Gold arrow */
  pointer-events: none;
  font-size: 1.2rem;
  font-weight: bold;
}

.tdb-btn-primary {
  width: 100%;
  background: #9d0a0e; /* Crimson red */
  color: #fff;
  border: none;
  padding: 14px;
  font-size: 1rem;
  font-weight: 700;
  font-family: 'Inter', sans-serif;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  border-radius: 4px;
  transition: background 0.3s;
  margin-bottom: 1rem;
  text-transform: uppercase;
}

.tdb-btn-primary:hover {
  background: #7a080b;
}

.tdb-btn-secondary {
  width: 100%;
  background: #151515;
  color: #fff;
  border: 1px solid rgba(255,255,255,0.2);
  padding: 14px;
  font-size: 0.9rem;
  font-weight: 700;
  font-family: 'Inter', sans-serif;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  border-radius: 4px;
  transition: all 0.3s;
  text-transform: uppercase;
  text-decoration: none;
}

.tdb-btn-secondary:hover {
  background: #222;
  border-color: rgba(255,255,255,0.5);
}

/* MOBILE RESPONSIVENESS */
@media(max-width: 768px) {
  .tdb-logo { width: 280px; margin-bottom: 2rem; }
  .tdb-reservation-box { padding: 1.5rem; }
  .tdb-reservation-box h2 { font-size: 1.5rem; }
}
"""

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if line.startswith(".hero-main {"):
        start_idx = i
    if "/* =========================================" in line and "HERO BAR" in lines[i+1]:
        end_idx = i

if start_idx != -1 and end_idx != -1:
    new_lines = lines[:start_idx] + [new_css + "\n"] + lines[end_idx:]
    with open("index.html", "w") as f:
        f.writelines(new_lines)
    print("CSS replaced successfully!")
else:
    print("Could not find start or end index.")
    print(f"Start: {start_idx}, End: {end_idx}")
