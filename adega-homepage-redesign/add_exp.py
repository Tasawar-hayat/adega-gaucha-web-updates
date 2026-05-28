<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Adega Gaucha | Honors</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Oswald:wght@400;600;700;800&family=Jost:wght@300;400;600&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --primary-orange: #F68625;
      --dark-bg: #050505;
      --font-heading: 'Oswald', 'Inter', sans-serif;
      --font-body: 'Inter', sans-serif;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    html, body {
      font-family: var(--font-body);
      background-color: var(--dark-bg);
      background: radial-gradient(circle at 50% 10%, rgba(246, 134, 37, 0.08) 0%, transparent 60%),
                  radial-gradient(circle at 10% 70%, rgba(246, 134, 37, 0.04) 0%, transparent 50%),
                  #050505;
      color: #fff;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }

    .awards-section {
      width: 100%;
      padding: 4rem 2rem;
      position: relative;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .awards-header {
      text-align: center;
      margin-bottom: 5rem;
      opacity: 0;
      transform: translateY(30px);
      animation: fadeUp 1s ease forwards;
    }

    .awards-header-subtitle {
      font-family: 'Jost', sans-serif;
      font-size: 1.1rem;
      color: var(--primary-orange);
      letter-spacing: 5px;
      text-transform: uppercase;
      font-weight: 300;
      margin-bottom: 0.8rem;
    }

    .awards-header-title {
      font-family: var(--font-heading);
      font-size: 2.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 2px;
      line-height: 1.1;
    }

    .header-accent {
      width: 80px;
      height: 4px;
      background-color: var(--primary-orange);
      margin: 1.5rem auto 0 auto;
      border-radius: 2px;
      box-shadow: 0 0 10px rgba(250, 135, 34, 0.5);
    }

    /* GLASSMORPHIC TROPHY GRID */
    .awards-container {
      max-width: 1200px;
      width: 100%;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 3rem;
      position: relative;
      z-index: 1;
    }

    .trophy-card {
      position: relative;
      background: rgba(255, 255, 255, 0.02);
      backdrop-filter: blur(25px);
      -webkit-backdrop-filter: blur(25px);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 24px;
      padding: 3rem 2.5rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      cursor: pointer;
      transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
      box-shadow: 0 20px 40px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.08);
      opacity: 0;
      transform: translateY(40px);
      overflow: hidden; /* Contains the rising embers */
    }

    .trophy-card.reveal {
      opacity: 1;
      transform: translateY(0);
    }

    /* Fiery Molten Border outline pseudo-element */
    .trophy-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      border-radius: 24px;
      border: 2px solid transparent;
      transition: all 0.4s ease;
      z-index: 3;
      pointer-events: none;
    }

    /* Hover States - Fiery Molten Igniting Border */
    .trophy-card:hover {
      transform: translateY(-12px);
      box-shadow: 0 30px 60px rgba(0,0,0,0.9), 
                  0 0 35px rgba(246, 134, 37, 0.25), 
                  inset 0 0 15px rgba(246, 134, 37, 0.15);
    }

    .trophy-card:hover::before {
      border-color: #ff5e00;
      box-shadow: 0 0 15px #ff5e00, 
                  inset 0 0 15px #ff5e00, 
                  0 0 30px #ff9d00;
      animation: firePulse 1.5s infinite ease-in-out;
    }

    /* Pedestal Frame */
    .pedestal-frame {
      width: 155px;
      height: 155px;
      display: flex;
      justify-content: center;
      align-items: center;
      border-radius: 50%;
      background: rgba(10, 10, 10, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 18px;
      margin-bottom: 2.5rem;
      transition: all 0.4s ease;
      box-shadow: inset 0 0 15px rgba(0,0,0,0.8);
      position: relative;
      z-index: 2;
    }

    .pedestal-glow {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      border-radius: 50%;
      background: var(--primary-orange);
      filter: blur(25px);
      opacity: 0;
      z-index: -1;
      transition: opacity 0.4s ease;
    }

    .trophy-card:hover .pedestal-frame {
      border-color: var(--primary-orange);
      transform: scale(1.05) rotate(3deg);
      box-shadow: inset 0 0 20px rgba(246, 134, 37, 0.2), 0 0 15px rgba(246, 134, 37, 0.3);
    }

    .trophy-card:hover .pedestal-glow {
      opacity: 0.25;
    }

    .pedestal-frame img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      filter: drop-shadow(0 8px 10px rgba(0,0,0,0.6));
    }

    /* Accolade Content */
    .trophy-content {
      position: relative;
      z-index: 2;
    }

    .trophy-title {
      font-family: var(--font-heading);
      font-size: 2rem;
      font-weight: 600;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: #fff;
      line-height: 1.2;
      margin-bottom: 0.6rem;
      transition: color 0.3s ease;
    }

    .trophy-subtitle {
      font-family: 'Jost', sans-serif;
      font-size: 1.1rem;
      color: rgba(255, 255, 255, 0.4);
      letter-spacing: 3px;
      text-transform: uppercase;
      font-weight: 300;
      transition: color 0.3s ease;
    }

    .trophy-card:hover .trophy-title {
      color: var(--primary-orange);
    }

    .trophy-card:hover .trophy-subtitle {
      color: rgba(255, 255, 255, 0.85);
    }

    /* HARDWARE-ACCELERATED FLOATING EMBERS */
    .ember-wrap {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      z-index: 1;
      pointer-events: none;
      overflow: hidden;
    }

    .ember {
      position: absolute;
      bottom: -10px;
      width: 5px;
      height: 5px;
      background: #ff5e00;
      border-radius: 50%;
      box-shadow: 0 0 10px #ff5e00, 0 0 20px #ff9d00;
      opacity: 0;
      filter: blur(0.5px);
      transform: translate3d(0, 0, 0);
      will-change: transform, opacity;
    }

    /* Dynamic spark triggers only when card is hovered */
    .trophy-card:hover .ember:nth-child(1) {
      animation: emberFloat1 2.5s infinite ease-out;
    }
    .trophy-card:hover .ember:nth-child(2) {
      animation: emberFloat2 2.8s infinite ease-out 0.6s;
    }
    .trophy-card:hover .ember:nth-child(3) {
      animation: emberFloat3 2.2s infinite ease-out 1.2s;
    }

    /* SUMMARY CAPTION */
    .awards-summary {
      max-width: 950px;
      width: 100%;
      margin: 6rem auto 0 auto;
      text-align: center;
      font-family: var(--font-body);
      font-size: 1.2rem;
      line-height: 1.9;
      color: rgba(255, 255, 255, 0.7);
      font-weight: 300;
      padding: 0 2rem;
      opacity: 0;
      transform: translateY(30px);
      position: relative;
      z-index: 2;
    }

    .awards-summary.reveal {
      opacity: 1;
      transform: translateY(0);
      transition: all 0.8s ease 0.4s;
    }

    .awards-summary strong {
      color: #fff;
      font-weight: 600;
    }

    .awards-summary .highlight {
      color: var(--primary-orange);
    }

    .awards-summary span {
      display: block;
      margin-top: 1.5rem;
      font-size: 1rem;
      color: rgba(255, 255, 255, 0.5);
      font-family: 'Jost', sans-serif;
      text-transform: uppercase;
      letter-spacing: 2px;
    }

    /* KEYFRAME SEQUENCES */
    @keyframes fadeUp {
      to { opacity: 1; transform: translateY(0); }
    }

    @keyframes firePulse {
      0%, 100% {
        box-shadow: 0 0 15px #ff5e00, inset 0 0 15px #ff5e00, 0 0 30px #ff9d00;
      }
      50% {
        box-shadow: 0 0 25px #ff5e00, inset 0 0 20px #ff5e00, 0 0 45px #ffb300;
      }
    }

    @keyframes emberFloat1 {
      0% {
        transform: translate3d(0, 0, 0) scale(1);
        opacity: 0;
        left: 20%;
      }
      10% { opacity: 1; }
      80% { opacity: 0.8; }
      100% {
        transform: translate3d(-30px, -450px, 0) scale(0);
        opacity: 0;
        left: 20%;
      }
    }

    @keyframes emberFloat2 {
      0% {
        transform: translate3d(0, 0, 0) scale(0.8);
        opacity: 0;
        left: 50%;
      }
      10% { opacity: 1; }
      80% { opacity: 0.8; }
      100% {
        transform: translate3d(40px, -450px, 0) scale(0);
        opacity: 0;
        left: 50%;
      }
    }

    @keyframes emberFloat3 {
      0% {
        transform: translate3d(0, 0, 0) scale(1.2);
        opacity: 0;
        left: 80%;
      }
      10% { opacity: 1; }
      80% { opacity: 0.8; }
      100% {
        transform: translate3d(-20px, -450px, 0) scale(0);
        opacity: 0;
        left: 80%;
      }
    }

    /* RESPONSIVENESS */
    @media(max-width: 950px) {
      .awards-container {
        grid-template-columns: 1fr;
        gap: 2.5rem;
      }
      .trophy-card {
        padding: 3rem 2rem;
      }
      .awards-header-title {
        font-size: 2.8rem;
      }
      .pedestal-frame {
        width: 130px;
        height: 130px;
        margin-bottom: 2rem;
      }
      .awards-summary {
        font-size: 1.1rem;
        margin-top: 4rem;
      }
    }
  </style>
</head>
<body>

  <!-- AWARDS SECTION -->
  <section class="awards-section">
    
    <div class="awards-header">
      <div class="awards-header-subtitle">Award-Winning Excellence</div>
      <h2 class="awards-header-title">Honors </h2>
      <div class="header-accent"></div>
    </div>
    
    <div class="awards-container" id="trophy-grid">
      
      <!-- TROPHY 1: TripAdvisor -->
      <div class="trophy-card" style="transition-delay: 0.1s;">
        <!-- Embedded GPU-accelerated embers -->
        <div class="ember-wrap">
          <div class="ember"></div>
          <div class="ember"></div>
          <div class="ember"></div>
        </div>
        <div class="pedestal-frame">
          <div class="pedestal-glow"></div>
          <img src="https://adegagaucha.com/wp-content/uploads/2025/10/2025-tripadvisor-1.png" alt="Tripadvisor Badge">
        </div>
        <div class="trophy-content">
          <h3 class="trophy-title">Tripadvisor</h3>
          <span class="trophy-subtitle">Traveler's Choice</span>
        </div>
      </div>

      <!-- TROPHY 2: OpenTable -->
      <div class="trophy-card" style="transition-delay: 0.2s;">
        <!-- Embedded GPU-accelerated embers -->
        <div class="ember-wrap">
          <div class="ember"></div>
          <div class="ember"></div>
          <div class="ember"></div>
        </div>
        <div class="pedestal-frame">
          <div class="pedestal-glow"></div>
          <img src="https://adegagaucha.com/wp-content/uploads/2025/02/Adega_Gaucha_Open_Table_Diners_Choice_2023_2024_2025-2.png" alt="OpenTable Diners Choice Badge">
        </div>
        <div class="trophy-content">
          <h3 class="trophy-title">OpenTable</h3>
          <span class="trophy-subtitle">Diner's Choice</span>
        </div>
      </div>

      <!-- TROPHY 3: Best of Florida -->
      <div class="trophy-card" style="transition-delay: 0.3s;">
        <!-- Embedded GPU-accelerated embers -->
        <div class="ember-wrap">
          <div class="ember"></div>
          <div class="ember"></div>
          <div class="ember"></div>
        </div>
        <div class="pedestal-frame">
          <div class="pedestal-glow"></div>
          <img src="https://adegagaucha.com/wp-content/uploads/2025/10/BOFL-Seal-2025-Regional-RGBforWeb-1.png" alt="Best of Florida Badge">
        </div>
        <div class="trophy-content">
          <h3 class="trophy-title">Best of Florida</h3>
          <span class="trophy-subtitle">Regional Winner</span>
        </div>
      </div>

    </div>
    
    <!-- AWARDS SUMMARY TEXT -->
    <div class="awards-summary" id="awards-summary">
      Proud winners of <strong>OpenTable's Diners' Choice 2025</strong>, <strong>TripAdvisor Travelers' Choice 2023/2024/2025</strong>, <strong>Best of Florida 2023</strong>,<br>
      and now honored as <strong class="highlight">Best of Florida 2025 – Regional Winner!</strong>
      <span>Celebrating our absolute commitment to authentic Brazilian flavors and world-class service.</span>
    </div>
  </section>

  <script>
    document.addEventListener("DOMContentLoaded", () => {
      // IntersectionObserver to fade up trophy cards and summary
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('reveal');
          }
        });
      }, { threshold: 0.15 });

      const cards = document.querySelectorAll('.trophy-card');
      cards.forEach(card => observer.observe(card));

      const summary = document.getElementById('awards-summary');
      if (summary) observer.observe(summary);
    });
  </script>

</body>
</html>
