# -*- coding: utf-8 -*-
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Adega Gaucha | Premium Gallery Reels</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Oswald:wght@300;400;500;600&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
  
  <style>
/* =========================================
   ADEGA GAUCHA - PREMIUM DARK MODE THEME
   ========================================= */
:root {
  --primary-orange: #F68625;
  --dark-bg: #0d0d0d;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

html, body {
  font-family: 'Inter', sans-serif;
  background-color: var(--dark-bg);
  color: #fff;
  -webkit-font-smoothing: antialiased;
}

/* =========================================
   GALLERY REELS SECTION
   ========================================= */
.gallery-section {
  width: 100%;
  padding: 80px 20px;
  background-color: var(--dark-bg);
}

.gallery-container {
  max-width: 1280px;
  margin: 0 auto;
}

/* HEADER */
.gallery-header {
  text-align: center;
  margin-bottom: 60px;
  animation: ag-fadeUp 1s ease forwards;
}

.gallery-title {
  font-family: 'Oswald', sans-serif;
  font-size: 3.2rem;
  font-weight: 300;
  text-transform: uppercase;
  line-height: 1.2;
  color: #fff;
  letter-spacing: 2px;
  margin-bottom: 0.5rem;
}

.gallery-hashtag {
  font-family: 'Jost', sans-serif;
  font-size: 2.2rem;
  color: var(--primary-orange);
  font-style: italic;
  font-weight: 400;
  margin-bottom: 1.5rem;
  letter-spacing: 1px;
}

.gallery-desc {
  font-family: 'Inter', sans-serif;
  font-size: 1.05rem;
  line-height: 1.8;
  color: rgba(255,255,255,0.75);
  font-weight: 300;
  max-width: 850px;
  margin: 0 auto;
}

.gallery-desc strong {
  font-weight: 600;
  color: #fff;
}

/* =========================================
   REELS GRID LAYOUT (3 Items)
   ========================================= */
.reels-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
}

.reel-card {
  position: relative;
  display: block;
  border-radius: 16px;
  overflow: hidden;
  background-color: #1a1a1a;
  border: 1px solid var(--primary-orange);
  aspect-ratio: 9 / 16; /* Instagram Reel standard aspect ratio */
  box-shadow: 0 10px 30px rgba(0,0,0,0.5);
  transition: transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94), box-shadow 0.4s;
  cursor: pointer;
}

.reel-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(246, 134, 37, 0.15);
}

.reel-card video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  pointer-events: none; /* Ensures clicking anywhere hits the <a> tag */
  transition: opacity 0.3s;
}

/* Overlay gradient for better text/icon visibility */
.reel-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.7) 0%, transparent 40%, transparent 70%, rgba(0,0,0,0.4) 100%);
  pointer-events: none;
  z-index: 2;
}

/* Instagram Icon */
.ig-icon {
  position: absolute;
  top: 15px;
  right: 15px;
  z-index: 3;
  color: #fff;
  opacity: 0.9;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5));
}

/* Play Icon Overlay (Shows on hover) */
.play-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(0.8);
  color: rgba(255,255,255,0.8);
  opacity: 0;
  z-index: 3;
  transition: all 0.3s ease;
  filter: drop-shadow(0 4px 10px rgba(0,0,0,0.5));
}

.reel-card:hover .play-icon {
  opacity: 1;
  transform: translate(-50%, -50%) scale(1);
}

@keyframes ag-fadeUp {
  0% { opacity: 0; transform: translateY(20px); }
  100% { opacity: 1; transform: translateY(0); }
}

/* =========================================
   RESPONSIVENESS
   ========================================= */

/* TABLET: 3 Columns */
@media(max-width: 1024px) {
  .reels-grid {
    gap: 20px;
  }
}

/* MOBILE: Stack vertically */
@media(max-width: 768px) {
  .gallery-section { padding: 50px 20px; }
  .gallery-title { font-size: 2.5rem; }
  .reels-grid {
    grid-template-columns: repeat(1, 1fr); /* 1 column on mobile so reels aren't too small */
    gap: 24px;
    max-width: 400px;
    margin: 0 auto; /* Center the column on mobile */
  }
}
  </style>
</head>
<body>

  <!-- GALLERY SECTION -->
  <section class="gallery-section">
    <div class="gallery-container">
      
      <!-- HEADER -->
      <div class="gallery-header">
        <h2 class="gallery-title">Experience The Flavor</h2>
        <div class="gallery-hashtag">#adegagaucha</div>
        <p class="gallery-desc">
          Watch our chefs in action and see what makes the Adega Gaucha experience unforgettable. Hover over a video to play, and click to view it on Instagram to like, comment, and follow us!
        </p>
      </div>

      <!-- REELS GRID -->
      <div class="reels-grid">
        
        <!-- Reel 1 -->
        <a href="https://www.instagram.com/journeyswithjulian/reel/DYpu7WHAAYd/" target="_blank" rel="noopener noreferrer" class="reel-card">
          <video src="https://adegagaucha.com/wp-content/uploads/2026/05/As-conexoes-certas-sao-capazes-de-ampliar-a-visao-e-acelerar-negocios.Alguns-movimentos-nao-cabe.mp4" poster="https://adegagaucha.com/wp-content/uploads/2026/03/5.png" muted loop playsinline></video>
          <div class="reel-overlay"></div>
          <svg class="ig-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
          <svg class="play-icon" width="48" height="48" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
        </a>

        <!-- Reel 2 -->
        <a href="https://www.instagram.com/adega.gaucha/reel/DYr3nePgXrI/" target="_blank" rel="noopener noreferrer" class="reel-card">
          <video src="https://adegagaucha.com/wp-content/uploads/2026/05/🎉-Celebrate-Your-Birthday-at-Adega-Gaucha-🎂🥩Your-birthday-deserves-churrasco-good-company-.mp4" poster="https://adegagaucha.com/wp-content/uploads/2025/10/Lamb_Chop.png" muted loop playsinline></video>
          <div class="reel-overlay"></div>
          <svg class="ig-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
          <svg class="play-icon" width="48" height="48" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
        </a>

        <!-- Reel 3 -->
        <a href="https://www.instagram.com/adega.gaucha/reel/DYnOldVCKLA/" target="_blank" rel="noopener noreferrer" class="reel-card">
          <video src="https://adegagaucha.com/wp-content/uploads/2026/05/🥘-Saturdays-just-got-a-whole-lot-tastierOur-Gourmet-Table-Takeover-Paella-Edition-is-happenin.mp4" poster="https://adegagaucha.com/wp-content/uploads/2025/12/Tomahawk-7-scaled.jpg" muted loop playsinline></video>
          <div class="reel-overlay"></div>
          <svg class="ig-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
          <svg class="play-icon" width="48" height="48" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
        </a>

      </div>
    </div>
  </section>

  <script>
    // AUTO-PLAY ON HOVER LOGIC
    document.addEventListener('DOMContentLoaded', () => {
      const reelCards = document.querySelectorAll('.reel-card');
      
      reelCards.forEach(card => {
        const video = card.querySelector('video');
        if(!video) return;

        // Ensure videos are loaded correctly for autoplay
        video.load();

        // On Mouse Enter -> Play
        card.addEventListener('mouseenter', () => {
          video.play().catch(e => console.log('Video play prevented:', e));
        });

        // On Mouse Leave -> Pause and reset to start
        card.addEventListener('mouseleave', () => {
          video.pause();
          video.currentTime = 0; // Optional: Resets video to beginning
        });
      });
    });
  </script>

</body>
</html>
'''

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

