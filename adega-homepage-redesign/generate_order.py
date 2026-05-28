# -*- coding: utf-8 -*-
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Adega Gaucha | Premium Online Order</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Oswald:wght@300;400;500;600&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
</head>
<body style="margin: 0; background: #000;">

<!-- ADEGA GAUCHA - ONLINE ORDER SECTION -->
<div id="adega-online-order" class="adegagaucha-section">
  <style>
    #adega-online-order {
      --primary: #F68625;
      --primary-hover: #ff9d47;
      --bg-dark: #0a0a08;
      --text-light: #FFF9F5;
      --text-dim: rgba(255, 249, 245, 0.65);
      
      background-color: var(--bg-dark);
      position: relative;
      overflow: hidden;
      padding: clamp(80px, 10vw, 140px) 20px;
      font-family: 'Inter', sans-serif;
      color: var(--text-light);
    }

    #adega-online-order * { box-sizing: border-box; }

    /* Subtle ambient glow behind the image */
    #adega-online-order::after {
      content: '';
      position: absolute;
      top: 20%;
      right: -10%;
      width: 800px;
      height: 800px;
      background: radial-gradient(circle, rgba(246, 134, 37, 0.08) 0%, transparent 60%);
      pointer-events: none;
      z-index: 0;
    }

    .order-container {
      max-width: 1280px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      gap: clamp(40px, 8vw, 80px);
      position: relative;
      z-index: 1;
    }

    .order-content {
      flex: 1.1;
    }

    .order-visual {
      flex: 0.9;
      position: relative;
    }

    .order-img-wrap {
      position: relative;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 40px 80px rgba(0,0,0,0.8);
      border: 1px solid rgba(255,255,255,0.05);
    }

    .order-img-wrap::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, rgba(0,0,0,0.4) 0%, transparent 50%);
      pointer-events: none;
    }

    .order-visual img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transform: scale(1.05);
      transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform;
    }

    .order-visual:hover img {
      transform: scale(1.0);
    }

    /* Floating mini-cards */
    .floating-card {
      position: absolute;
      background: rgba(20, 20, 20, 0.85);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(246, 134, 37, 0.2);
      padding: 16px 24px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      gap: 15px;
      box-shadow: 0 15px 35px rgba(0,0,0,0.5);
      z-index: 3;
      animation: float 6s ease-in-out infinite;
    }

    .floating-card.top-right {
      top: -20px;
      right: -30px;
      animation-delay: 0s;
    }

    .floating-card.bottom-left {
      bottom: -30px;
      left: -30px;
      animation-delay: 3s;
    }

    .fc-icon {
      width: 40px;
      height: 40px;
      background: rgba(246, 134, 37, 0.1);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--primary);
    }

    .fc-text h4 {
      font-family: 'Oswald', sans-serif;
      font-size: 1.1rem;
      margin: 0 0 2px 0;
      letter-spacing: 1px;
      text-transform: uppercase;
      font-weight: 500;
    }

    .fc-text p {
      margin: 0;
      font-size: 0.75rem;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    @keyframes float {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-10px); }
    }

    /* Typography & Buttons */
    .order-badge {
      display: inline-block;
      padding: 6px 14px;
      background: rgba(246, 134, 37, 0.1);
      border: 1px solid rgba(246, 134, 37, 0.3);
      color: var(--primary);
      border-radius: 50px;
      font-family: 'Inter', sans-serif;
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      margin-bottom: 1.5rem;
    }

    .order-title {
      font-family: 'Oswald', sans-serif;
      font-size: clamp(3rem, 5vw, 4.5rem);
      font-weight: 300;
      line-height: 1.1;
      margin: 0 0 1.5rem 0;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .order-title span {
      color: var(--primary);
      font-style: italic;
    }

    .order-desc {
      font-size: 1.1rem;
      color: var(--text-dim);
      line-height: 1.8;
      margin-bottom: 2.5rem;
      font-weight: 300;
      max-width: 550px;
    }

    .order-features {
      list-style: none;
      padding: 0;
      margin: 0 0 3rem 0;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 15px;
    }

    .order-features li {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.95rem;
      color: var(--text-light);
    }

    .order-features svg {
      color: var(--primary);
      flex-shrink: 0;
    }

    .order-buttons {
      display: flex;
      gap: 1.5rem;
      flex-wrap: wrap;
    }

    .btn {
      padding: 16px 32px;
      font-family: 'Inter', sans-serif;
      font-size: 0.9rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      text-decoration: none;
      border-radius: 4px;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      cursor: pointer;
    }

    .btn-primary {
      background-color: var(--primary);
      color: #000;
      border: 1px solid var(--primary);
    }

    .btn-primary:hover {
      background-color: var(--primary-hover);
      border-color: var(--primary-hover);
      transform: translateY(-4px);
      box-shadow: 0 10px 20px rgba(246, 134, 37, 0.25);
    }

    .btn-secondary {
      background-color: transparent;
      color: var(--text-light);
      border: 1px solid rgba(255,255,255,0.2);
    }

    .btn-secondary:hover {
      border-color: var(--primary);
      color: var(--primary);
      transform: translateY(-4px);
      background-color: rgba(246, 134, 37, 0.05);
    }

    /* Simple Intersection Observer Reveal */
    .reveal {
      opacity: 0;
      transform: translateY(30px);
      transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .reveal.active {
      opacity: 1;
      transform: translateY(0);
    }
    .d-1 { transition-delay: 0.1s; }
    .d-2 { transition-delay: 0.2s; }
    .d-3 { transition-delay: 0.3s; }

    @media(max-width: 992px) {
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
    }
  </style>

  <div class="order-container">
    
    <!-- LEFT CONTENT -->
    <div class="order-content">
      <span class="order-badge reveal">Online Ordering</span>
      <h2 class="order-title reveal d-1">Bring The <span>Adega</span> Experience Home</h2>
      <p class="order-desc reveal d-2">
        Craving authentic Churrasco but prefer a cozy night in? Enjoy our perfectly fire-roasted meats, gourmet sides, and signature desserts delivered straight to your door, or packaged perfectly for quick pickup.
      </p>
      
      <ul class="order-features reveal d-3">
        <li>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
          Premium Cuts Packaged Fresh
        </li>
        <li>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
          Fast & Reliable Delivery
        </li>
        <li>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
          Curbside Pickup Available
        </li>
        <li>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
          Gourmet Salad Bar Options
        </li>
      </ul>

      <div class="order-buttons reveal d-3">
        <!-- Replace href with actual ordering link -->
        <a href="#order-pickup" class="btn btn-primary">
          Order for Pickup
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="M12 5l7 7-7 7"></path></svg>
        </a>
        <a href="#order-delivery" class="btn btn-secondary">
          Order Delivery
        </a>
      </div>
    </div>

    <!-- RIGHT VISUAL -->
    <div class="order-visual reveal d-2">
      <!-- Floating Tag 1 -->
      <div class="floating-card top-right">
        <div class="fc-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
        </div>
        <div class="fc-text">
          <h4>No Fees</h4>
          <p>On Direct Orders</p>
        </div>
      </div>

      <!-- Main Image (Highly optimized webp) -->
      <div class="order-img-wrap">
        <img src="https://adegagaucha.com/wp-content/uploads/2025/02/Menu_Adega_Gaucha_Lunch_Tomahawk.webp" alt="Adega Gaucha Premium Online Order" loading="lazy">
      </div>

      <!-- Floating Tag 2 -->
      <div class="floating-card bottom-left">
        <div class="fc-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
        </div>
        <div class="fc-text">
          <h4>Ready Fast</h4>
          <p>Fresh & Hot</p>
        </div>
      </div>
    </div>

  </div>

  <!-- Script for reveal animation -->
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const reveals = document.querySelectorAll("#adega-online-order .reveal");
      const obs = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add("active");
            obs.unobserve(entry.target);
          }
        });
      }, { threshold: 0.15 });
      
      reveals.forEach(el => obs.observe(el));
    });
  </script>
</div>

</body>
</html>
'''

with open('online_order.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

