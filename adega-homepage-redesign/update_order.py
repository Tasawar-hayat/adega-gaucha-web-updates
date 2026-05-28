# -*- coding: utf-8 -*-
import re

with open('online_order.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update primary button to white
html = html.replace('''    .btn-primary {
      background-color: var(--primary);
      color: #000;
      border: 1px solid var(--primary);
    }

    .btn-primary:hover {
      background-color: var(--primary-hover);
      border-color: var(--primary-hover);
      transform: translateY(-4px);
      box-shadow: 0 10px 20px rgba(246, 134, 37, 0.25);
    }''', '''    .btn-primary {
      background-color: #ffffff;
      color: #000000;
      border: 1px solid #ffffff;
    }

    .btn-primary:hover {
      background-color: var(--primary);
      border-color: var(--primary);
      color: #000000;
      transform: translateY(-4px);
      box-shadow: 0 10px 25px rgba(246, 134, 37, 0.35);
    }''')

# Add smoother animation to the image
html = html.replace('''    .order-visual {
      flex: 0.9;
      position: relative;
    }''', '''    @keyframes slow-float {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-12px); }
    }

    .order-visual {
      flex: 0.9;
      position: relative;
      animation: slow-float 7s ease-in-out infinite;
    }''')

# Enhance mobile responsiveness
html = html.replace('''    @media(max-width: 992px) {
      .order-container { flex-direction: column; text-align: center; }
      .order-content { max-width: 100%; display: flex; flex-direction: column; align-items: center; }
      .order-desc { max-width: 600px; }
      .order-visual { width: 90%; margin-top: 2rem; }
      .floating-card.top-right { right: -10px; }
      .floating-card.bottom-left { left: -10px; }
    }

    @media(max-width: 600px) {
      .order-features { grid-template-columns: 1fr; gap: 10px; text-align: left; width: 100%; max-width: 300px; }
      .order-buttons { width: 100%; flex-direction: column; gap: 1rem; }
      .btn { width: 100%; }
      .floating-card { padding: 12px 16px; }
      .fc-icon { width: 30px; height: 30px; }
      .fc-text h4 { font-size: 0.95rem; }
      .floating-card.top-right { top: -10px; right: -5px; }
      .floating-card.bottom-left { bottom: -15px; left: -5px; }
    }''', '''    @media(max-width: 992px) {
      .order-container { flex-direction: column; text-align: center; width: 100%; }
      .order-content { max-width: 100%; display: flex; flex-direction: column; align-items: center; width: 100%; }
      .order-desc { max-width: 100%; padding: 0 10px; }
      .order-visual { width: 100%; max-width: 600px; margin-top: 2rem; }
      .floating-card.top-right { right: 5%; }
      .floating-card.bottom-left { left: 5%; }
    }

    @media(max-width: 600px) {
      #adega-online-order { padding: 60px 15px; }
      .order-features { grid-template-columns: 1fr; gap: 15px; text-align: left; width: 100%; max-width: 320px; margin-bottom: 2rem; }
      .order-buttons { width: 100%; flex-direction: column; gap: 1rem; }
      .btn { width: 100%; padding: 18px 24px; font-size: 1rem; }
      .order-title { font-size: 2.6rem; }
      
      .order-visual { width: 100%; margin-top: 1rem; }
      .order-img-wrap { border-radius: 12px; }
      .floating-card { padding: 10px 14px; gap: 10px; }
      .fc-icon { width: 32px; height: 32px; }
      .fc-text h4 { font-size: 0.9rem; }
      .fc-text p { font-size: 0.65rem; }
      .floating-card.top-right { top: -15px; right: 0; }
      .floating-card.bottom-left { bottom: -15px; left: 0; }
    }''')

with open('online_order.html', 'w', encoding='utf-8') as f:
    f.write(html)
