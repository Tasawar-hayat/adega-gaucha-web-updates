import re

file_path = r'c:\Users\DIGITAL META\Downloads\reviews-FINAL.html'
output_widget_path = r'c:\Users\DIGITAL META\Downloads\elementor-reviews-widget.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove 'ú' sign from Gaúcha
content = content.replace('Gaúcha', 'Gaucha')
content = content.replace('gaúcha', 'gaucha')

# 2. Add extra shine and mobile polish
# Mobile friendly grid: Ensure grid-template-columns adjusts for mobile perfectly
content = content.replace('grid-template-columns: repeat(3, 1fr);', 'grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));')

# Add subtle shine to stats as well
content = content.replace('.rv-stat:hover { background: var(--orange-bg); }', '.rv-stat:hover { background: var(--orange-bg); box-shadow: inset 0 0 20px rgba(246,134,37,0.1); }')

css_shine = """
/* Shine Effect */
.rv-card::after {
  content: '';
  position: absolute;
  top: 0; left: -100%;
  width: 50%; height: 100%;
  background: linear-gradient(to right, rgba(255,255,255,0) 0%, rgba(255,255,255,0.04) 50%, rgba(255,255,255,0) 100%);
  transform: skewX(-25deg);
  transition: all 0.75s ease;
  z-index: 1;
  pointer-events: none;
}
.rv-card:hover::after {
  left: 200%;
  transition: all 0.75s ease;
}

/* Mobile Polish */
@media (max-width: 992px) {
  .rv-stats-inner {
    grid-template-columns: repeat(2, 1fr);
  }
  .rv-stat {
    border-bottom: 1px solid rgba(255,255,255,0.06);
  }
  .rv-stat:nth-child(even) {
    border-right: none;
  }
}

@media (max-width: 768px) {
  .rv-filter-wrap {
    flex-direction: column;
    align-items: flex-start;
  }
  .rv-filter-tabs {
    flex-wrap: wrap;
    justify-content: flex-start;
    width: 100%;
    border-radius: var(--r-md);
  }
  .rv-tab {
    flex: 1 1 auto;
    text-align: center;
    border-radius: var(--r-md);
  }
  .rv-results-bar {
    flex-direction: column;
    align-items: flex-start;
  }
  .rv-featured {
    grid-template-columns: 1fr;
    gap: 20px;
    padding: 24px;
  }
  .rv-featured::before {
    top: -20px; right: -20px;
  }
  .rv-featured-quote {
    font-size: 40px;
  }
  .rv-reputation-inner {
    grid-template-columns: 1fr;
  }
  .rv-hero h1 {
    font-size: clamp(36px, 10vw, 50px);
  }
}
"""

if 'Shine Effect' not in content:
    content = content.replace('</style>', css_shine + '\n</style>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("1. HTML file updated: Removed accent marks and added shine/mobile enhancements.")

# Re-extract widget HTML
style_match = re.search(r'<style>.*?</style>', content, re.DOTALL)
styles = style_match.group(0) if style_match else ''

body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
body_content = body_match.group(1) if body_match else ''

widget_html = f"{styles}\n\n{body_content}".strip()

with open(output_widget_path, 'w', encoding='utf-8') as f:
    f.write(widget_html)

print("2. Extracted widget file updated.")
