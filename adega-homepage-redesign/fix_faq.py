import re

with open('faq.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix accordion-header
content = content.replace('padding: 2.2rem 0;', 'padding: 1.4rem 0;')

# Fix accordion-question CSS
q_css_old = '''    .accordion-question {
      flex: 1;
      text-align: left;
      line-height: 1.4;
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: 1.5rem;
      font-weight: 500;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #fff;
      transition: color 0.3s ease;
      padding-right: 2rem;
      white-space: normal;
      word-break: break-word;
    }'''

q_css_new = '''    .accordion-question {
      flex: 1;
      text-align: left;
      line-height: 1.4;
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: clamp(1rem, 1.8vw, 1.2rem);
      font-weight: 400;
      color: #fff;
      transition: color 0.3s ease;
      padding-right: 2rem;
      white-space: normal;
      word-break: break-word;
    }'''
content = content.replace(q_css_old, q_css_new)

# Fix accordion-icon CSS
icon_css_old = '''    .accordion-icon {
      position: relative;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      border: 1px solid rgba(250, 135, 34, 0.4);
      flex-shrink: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      transition: border-color 0.3s ease;
    }

    .accordion-item:hover .accordion-icon,
    .accordion-item.active .accordion-icon {
      border-color: var(--primary-orange);
    }

    .accordion-icon::before,
    .accordion-icon::after {
      content: '';
      position: absolute;
      background: var(--primary-orange);
      transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }

    .accordion-icon::before {
      width: 12px;
      height: 1px;
    }

    .accordion-icon::after {
      width: 1px;
      height: 12px;
    }

    .accordion-item.active .accordion-icon::before {
      transform: rotate(90deg);
      opacity: 0; 
    }

    .accordion-item.active .accordion-icon::after {
      transform: rotate(180deg);
    }'''

icon_css_new = '''    .accordion-icon {
      position: relative;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      border: 1px solid rgba(246, 134, 37, 0.35);
      flex-shrink: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .accordion-item.active .accordion-icon {
      transform: rotate(45deg);
      background: rgba(246, 134, 37, 0.12);
      border-color: var(--primary-orange);
    }
    
    .accordion-icon svg {
      color: var(--primary-orange);
      transition: color 0.3s;
    }'''
content = content.replace(icon_css_old, icon_css_new)

# Inject SVG into the HTML
svg_html = '''<span class="accordion-icon" aria-hidden="true">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19" /><line x1="5" y1="12" x2="19" y2="12" /></svg>
            </span>'''
content = content.replace('<span class="accordion-icon"></span>', svg_html)

with open('faq.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("FAQ updated!")
