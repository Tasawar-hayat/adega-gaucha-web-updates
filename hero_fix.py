import re

file_path = r'c:\Users\DIGITAL META\Downloads\reviews-FINAL.html'
output_widget_path = r'c:\Users\DIGITAL META\Downloads\elementor-reviews-widget.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Double check Gaúcha removal
content = content.replace('Gaúcha', 'Gaucha')
content = content.replace('gaúcha', 'gaucha')

# 2. Fix Hero Mobile Spacing
mobile_hero_css = """
@media (max-width: 768px) {
  .rv-hero {
    min-height: auto !important;
    padding-top: 80px !important; /* Elementor header spacing fallback */
    padding-bottom: 20px !important;
  }
  .rv-hero-inner {
    padding-top: 20px !important;
    padding-bottom: 20px !important;
  }
  .rv-hero h1 {
    font-size: clamp(32px, 9vw, 42px) !important;
    margin-bottom: 16px !important;
  }
  .rv-hero-intro {
    font-size: 15px !important;
    margin-bottom: 24px !important;
  }
  .rv-hero-scroll {
    display: none !important; /* Hide scroll indicator on mobile to save space */
  }
}
"""

if 'padding-top: 80px !important;' not in content:
    content = content.replace('/* Mobile Polish */', mobile_hero_css + '\n/* Mobile Polish */')

# 3. Add more attractiveness and animations
hero_anim_css = """
/* Hero Animations */
.rv-hero-tag, .rv-hero h1, .rv-hero-intro, .rv-hero-stars {
  opacity: 0;
  animation: heroSlideUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
.rv-hero-tag { animation-delay: 0.1s; }
.rv-hero h1 { animation-delay: 0.3s; }
.rv-hero-intro { animation-delay: 0.5s; }
.rv-hero-stars { animation-delay: 0.7s; }

@keyframes heroSlideUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Floating animation for stars */
.rv-hero-stars-icons svg {
  animation: floatStar 2.5s ease-in-out infinite alternate;
}
.rv-hero-stars-icons svg:nth-child(2) { animation-delay: 0.2s; }
.rv-hero-stars-icons svg:nth-child(3) { animation-delay: 0.4s; }
.rv-hero-stars-icons svg:nth-child(4) { animation-delay: 0.6s; }
.rv-hero-stars-icons svg:nth-child(5) { animation-delay: 0.8s; }

@keyframes floatStar {
  0% { transform: translateY(0) scale(1); filter: drop-shadow(0 0 0px rgba(246,134,37,0)); }
  100% { transform: translateY(-4px) scale(1.15); filter: drop-shadow(0 4px 8px rgba(246,134,37,0.5)); color: var(--orange-light); }
}

/* Card image placeholder shimmer if needed */
.rv-avatar {
  position: relative;
  overflow: hidden;
}
.rv-avatar::after {
  content: '';
  position: absolute;
  top: 0; left: -100%;
  width: 50%; height: 100%;
  background: linear-gradient(to right, rgba(255,255,255,0) 0%, rgba(255,255,255,0.2) 50%, rgba(255,255,255,0) 100%);
  transform: skewX(-25deg);
  animation: shimmer 4s infinite;
}
@keyframes shimmer {
  0% { left: -100%; }
  20% { left: 200%; }
  100% { left: 200%; }
}
"""

if 'heroSlideUp' not in content:
    content = content.replace('</style>', hero_anim_css + '\n</style>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML file updated with Hero fixes and new animations.")

# Re-extract widget HTML
style_match = re.search(r'<style>.*?</style>', content, re.DOTALL)
styles = style_match.group(0) if style_match else ''

body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
body_content = body_match.group(1) if body_match else ''

widget_html = f"{styles}\n\n{body_content}".strip()

with open(output_widget_path, 'w', encoding='utf-8') as f:
    f.write(widget_html)

print("Extracted widget file updated.")
