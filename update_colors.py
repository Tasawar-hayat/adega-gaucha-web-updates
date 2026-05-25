import re
import os

file_path = r'c:\Users\DIGITAL META\Downloads\reviews-FINAL.html'
output_widget_path = r'c:\Users\DIGITAL META\Downloads\elementor-reviews-widget.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace variable definitions
content = content.replace('--gold:         #c8a55a;', '--orange:       #F68625;')
content = content.replace('--gold-light:   #dfc082;', '--orange-light: #ffaa5e;')
content = content.replace('--gold-dim:     #9a7d3f;', '--orange-dim:   #d86c12;')
content = content.replace('--gold-pale:    #f0e4c4;', '--orange-pale:  #ffdfc2;')
content = content.replace('--gold-bg:      rgba(200,165,90,0.08);', '--orange-bg:    rgba(246,134,37,0.08);')
content = content.replace('--gold-border:  rgba(200,165,90,0.22);', '--orange-border: rgba(246,134,37,0.35);')

# Replace variable usages
content = content.replace('var(--gold)', 'var(--orange)')
content = content.replace('var(--gold-light)', 'var(--orange-light)')
content = content.replace('var(--gold-dim)', 'var(--orange-dim)')
content = content.replace('var(--gold-pale)', 'var(--orange-pale)')
content = content.replace('var(--gold-bg)', 'var(--orange-bg)')
content = content.replace('var(--gold-border)', 'var(--orange-border)')

# Replace hardcoded colors in SVGs and gradients
content = content.replace('%23c8a55a', '%23F68625') # URL-encoded gold to orange
content = content.replace('rgba(200,165,90,', 'rgba(246,134,37,')
content = content.replace('rgba(200, 165, 90,', 'rgba(246,134,37,')

# Add extra beautifications / animations
# Enhance hover on .rv-card
content = content.replace('box-shadow: 0 16px 40px rgba(0,0,0,0.35);', 'box-shadow: 0 20px 50px rgba(246,134,37,0.15);')
content = content.replace('transform: translateY(-4px);', 'transform: translateY(-6px) scale(1.02);')

# Enhance background glow in featured section
content = content.replace('background: radial-gradient(circle, rgba(200,165,90,0.08) 0%, transparent 70%);', 'background: radial-gradient(circle, rgba(246,134,37,0.15) 0%, transparent 70%);')

# Make the featured badge pulse and add icon animation
css_additions = """
.rv-featured-badge {
  animation: badgePulse 2s infinite;
}
@keyframes badgePulse {
  0% { box-shadow: 0 0 0 0 rgba(246,134,37, 0.6); }
  70% { box-shadow: 0 0 0 12px rgba(246,134,37, 0); }
  100% { box-shadow: 0 0 0 0 rgba(246,134,37, 0); }
}

.rv-icon {
  transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.rv-card:hover .rv-icon {
  transform: scale(1.25) rotate(8deg);
}

.rv-visit-tag {
  transition: all 0.3s ease;
}
.rv-card:hover .rv-visit-tag {
  background: var(--orange);
  color: var(--white);
  box-shadow: 0 4px 10px rgba(246,134,37,0.3);
}

/* Enhancing top line on cards */
.rv-card::before {
  background: linear-gradient(90deg, transparent, var(--orange), transparent);
  height: 3px;
}
"""

if 'badgePulse' not in content:
    content = content.replace('</style>', css_additions + '\n</style>')

# Ensure brand icon background uses orange (if hardcoded)
content = content.replace('background-color: var(--gold);', 'background-color: var(--orange);')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("1. HTML file updated with Orange branding and animations.")

# Re-extract widget HTML
style_match = re.search(r'<style>.*?</style>', content, re.DOTALL)
styles = style_match.group(0) if style_match else ''

body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
body_content = body_match.group(1) if body_match else ''

widget_html = f"{styles}\n\n{body_content}".strip()

with open(output_widget_path, 'w', encoding='utf-8') as f:
    f.write(widget_html)

print("2. Extracted widget file updated at:", output_widget_path)
