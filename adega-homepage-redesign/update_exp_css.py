import re

with open('experience.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update .exp-card border
html = html.replace('''    .exp-card {
      position: relative;
      border-radius: 20px;
      background: rgba(20, 20, 20, 0.6);
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      border: 1px solid rgba(255, 255, 255, 0.05);''', '''    .exp-card {
      position: relative;
      border-radius: 20px;
      background: rgba(20, 20, 20, 0.6);
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      border: 1px solid rgba(246, 134, 37, 0.5);''')

# 2. Update .exp-card:hover transform and box shadow
html = html.replace('''    /* Hover States */
    .exp-card:hover {
      transform: translateY(-12px);
      border-color: var(--primary-orange);
      box-shadow: 0 30px 60px rgba(0,0,0,0.8), 0 0 30px rgba(246, 134, 37, 0.25);
    }''', '''    /* Hover States */
    .exp-card:hover {
      transform: translateY(-12px) scale(1.03);
      border-color: var(--primary-orange);
      box-shadow: 0 40px 80px rgba(0,0,0,0.9), 0 0 40px rgba(246, 134, 37, 0.35);
    }''')

# 3. Update overlay gradient on hover to make it softer
html = html.replace('''    .exp-card:hover .card-overlay {
      background: linear-gradient(to top, rgba(5,5,5,1) 0%, rgba(246, 134, 37, 0.3) 100%);
    }''', '''    .exp-card:hover .card-overlay {
      background: linear-gradient(to top, rgba(5,5,5,0.95) 0%, rgba(5,5,5,0.2) 50%, rgba(246, 134, 37, 0.15) 100%);
    }''')

with open('experience.html', 'w', encoding='utf-8') as f:
    f.write(html)
