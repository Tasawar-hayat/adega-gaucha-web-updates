import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS
old_css_pattern = r'/\*\s*=========================================\s*NEW SPLIT HERO SECTION \(Screenshot Match\)\s*=========================================\s*\*/.*?(?=\s*</style>)'
new_css = '''/* =========================================
   NEW SPLIT HERO SECTION (Screenshot Match)
   ========================================= */
#adega-hero-v4 {
    --black: #000000;
    --charcoal: #0a0a08;
    --charcoal-mid: #121212;
    --charcoal-lt: #1a1a1a;
    --gold: #F68625;
    --gold-light: #ff9d47;
    --gold-dim: #cc6b1c;
    --brand-orange: #F68625;
    --cream: #FFF9F5;
    --cream-dim: rgba(255, 249, 245, 0.7);
    --white: #ffffff;
    --font-display: 'Cormorant Garamond', Georgia, serif;
    --font-body: 'Barlow', sans-serif;
    --font-label: 'Barlow Condensed', sans-serif;
    --ease-expo: cubic-bezier(0.16, 1, 0.3, 1);
    --radius-sm: 4px;
    --radius-md: 12px;
    --radius-full: 9999px;
    
    position: relative;
    min-height: 100vh;
    background: var(--black);
    color: var(--cream);
    font-family: var(--font-body);
    overflow: hidden;
}

#adega-hero-v4 * { box-sizing: border-box; }

@keyframes heroFadeInV4 { from { opacity: 0; } to { opacity: 1; } }
@keyframes heroFadeUpV4 { from { opacity: 0; transform: translateY(24px); } to { opacity: 1; transform: none; } }
@keyframes heroPulseV4 { 0% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.6); opacity: 0.4; } 100% { transform: scale(1); opacity: 1; } }
@keyframes heroFloatV4 { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
@keyframes heroRingPulseV4 { 0%, 100% { opacity: 0.2; transform: translate(-50%, -50%) scale(1); } 50% { opacity: 0.5; transform: translate(-50%, -50%) scale(1.02); } }
@keyframes heroScrollDropV4 { 0% { transform: scaleY(0); transform-origin: top; } 50% { transform: scaleY(1); transform-origin: top; } 51% { transform: scaleY(1); transform-origin: bottom; } 100% { transform: scaleY(0); transform-origin: bottom; } }

#adega-hero-v4 .hero {
    position: relative;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

#adega-hero-v4 .hero-slider {
    position: absolute;
    inset: 0;
    opacity: 0.7;
    background: var(--black);
}

#adega-hero-v4 .hero-slide {
    position: absolute;
    inset: 0;
    background-size: cover;
    background-position: center;
    opacity: 0;
    transition: opacity 1.5s ease-in-out, transform 8s ease;
    transform: scale(1.05);
}

#adega-hero-v4 .hero-slide.active {
    opacity: 1;
    transform: scale(1);
}

#adega-hero-v4 .hero-overlay {
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 70% 90% at 50% 60%, rgba(0, 0, 0, 0.1) 0%, rgba(0, 0, 0, 0.4) 100%), 
                linear-gradient(180deg, rgba(0, 0, 0, 0.2) 0%, rgba(0, 0, 0, 0) 40%, rgba(0, 0, 0, 0.6) 100%);
}

#adega-hero-v4 .hero-ring {
    position: absolute;
    border-radius: 50%;
    border: 1px solid rgba(246, 134, 37, 0.12);
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    animation: heroRingPulseV4 6s ease-in-out infinite;
}

#adega-hero-v4 .hero-ring:nth-child(1) { width: 520px; height: 520px; animation-delay: 0s; }
#adega-hero-v4 .hero-ring:nth-child(2) { width: 720px; height: 720px; animation-delay: 1s; border-color: rgba(246, 134, 37, 0.08); }
#adega-hero-v4 .hero-ring:nth-child(3) { width: 920px; height: 920px; animation-delay: 2s; border-color: rgba(246, 134, 37, 0.05); }

#adega-hero-v4 .hero-content {
    position: relative;
    z-index: 2;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 165px 2rem 2rem;
    gap: 1.5rem;
}

#adega-hero-v4 .hero-eyebrow {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    font-family: var(--font-label);
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    color: var(--brand-orange);
    opacity: 0;
    animation: heroFadeInV4 1.2s var(--ease-expo) 0.4s forwards;
}
#adega-hero-v4 .hero-eyebrow::before, #adega-hero-v4 .hero-eyebrow::after { content: ''; display: block; width: 40px; height: 1px; background: linear-gradient(to right, transparent, var(--brand-orange)); opacity: 0.4; }
#adega-hero-v4 .hero-eyebrow::after { background: linear-gradient(to left, transparent, var(--brand-orange)); }

#adega-hero-v4 .hero-title {
    font-family: var(--font-display);
    font-size: clamp(4rem, 10vw, 7.5rem);
    font-weight: 300;
    line-height: 0.8;
    color: var(--white);
    margin: 0;
    opacity: 0;
    animation: heroFadeUpV4 1.2s var(--ease-expo) 0.6s forwards;
}

#adega-hero-v4 .hero-title span {
    display: block;
    font-family: var(--font-label);
    font-size: clamp(0.8rem, 1.5vw, 1rem);
    font-weight: 700;
    letter-spacing: 0.4em;
    text-transform: uppercase;
    color: var(--brand-orange);
    margin-bottom: 1rem;
}

#adega-hero-v4 .hero-title em { font-style: italic; color: var(--brand-orange); display: block; margin-top: 0.2rem; }

#adega-hero-v4 .hero-email-capture {
    margin-top: 2rem;
    width: 100%;
    max-width: 600px;
    background: rgba(255, 255, 255, 0.04);
    backdrop-filter: blur(20px);
    padding: 2rem;
    border: 1px solid rgba(255, 249, 245, 0.1);
    border-radius: var(--radius-md);
    opacity: 0;
    animation: heroFadeUpV4 1s var(--ease-expo) 1.1s forwards, heroFloatV4 6s ease-in-out infinite 2s;
    box-shadow: 0 40px 100px rgba(0, 0, 0, 0.8);
}

#adega-hero-v4 .email-form { display: flex; gap: 0.8rem; flex-wrap: wrap; }
#adega-hero-v4 .email-form input { flex: 1; min-width: 200px; padding: 0.9rem 1.2rem; border-radius: var(--radius-sm); border: 1px solid rgba(255, 249, 245, 0.15); background: rgba(0, 0, 0, 0.3); color: var(--cream); outline: none; transition: all 0.3s; }
#adega-hero-v4 .email-form input:focus { border-color: var(--brand-orange); background: rgba(0, 0, 0, 0.6); }

#adega-hero-v4 .btn-primary { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.9rem 2rem; background: var(--brand-orange); color: var(--white); font-family: var(--font-label); font-size: 0.75rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; border-radius: var(--radius-sm); transition: all 0.3s; text-decoration: none; border: none; cursor: pointer; }
#adega-hero-v4 .btn-primary:hover { background: #e57615; transform: translateY(-2px); }

#adega-hero-v4 .fomo-tag { font-family: var(--font-label); font-size: 0.6rem; font-weight: 700; color: var(--brand-orange); letter-spacing: 0.05em; text-transform: uppercase; display: flex; align-items: center; justify-content: center; gap: 0.6rem; margin-top: 1rem; }
#adega-hero-v4 .pulse-dot { width: 6px; height: 6px; background: var(--brand-orange); border-radius: 50%; animation: heroPulseV4 2s infinite; }

#adega-hero-v4 .hero-scroll { position: absolute; bottom: 2rem; left: 50%; transform: translateX(-50%); display: flex; flex-direction: column; align-items: center; gap: 0.5rem; opacity: 0; animation: heroFadeUpV4 1s var(--ease-expo) 1.5s forwards; }
#adega-hero-v4 .hero-scroll span { font-family: var(--font-label); font-size: 0.6rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--gold-dim); }
#adega-hero-v4 .scroll-line { width: 1px; height: 30px; background: linear-gradient(180deg, var(--gold-dim), transparent); animation: heroScrollDropV4 2s ease-in-out infinite; }

@media (max-width: 768px) {
    #adega-hero-v4 .hero-content { padding-top: 140px; padding-inline: 1.5rem; }
    #adega-hero-v4 .hero-title { font-size: clamp(3.2rem, 12vw, 4.5rem); line-height: 0.95; }
    
    #adega-hero-v4 .hero-email-capture { padding: 1.5rem; margin-top: 1.5rem; }
    #adega-hero-v4 .email-form { flex-direction: column; gap: 0.8rem; }
    #adega-hero-v4 .email-form input, 
    #adega-hero-v4 .btn-primary { 
        width: 100%; 
        font-size: 0.85rem; 
        text-align: center;
        justify-content: center;
    }
    
    #adega-hero-v4 .fomo-tag { 
        flex-direction: row; 
        align-items: center;
        justify-content: center;
        gap: 0.5rem; 
        line-height: 1.2; 
        text-align: center;
        margin-top: 1.2rem;
    }
    #adega-hero-v4 .pulse-dot { margin-bottom: 0; flex-shrink: 0; }
    
    #adega-hero-v4 .hero-scroll { bottom: 2rem; }
}
'''
content = re.sub(old_css_pattern, new_css, content, flags=re.DOTALL)

# Replace HTML
old_html_pattern = r'<!-- NEW SPLIT-SCREEN HERO SECTION -->.*?(?=</body>)'
new_html = '''<!-- ADEGA GAUCHA - HERO SECTION (ORIGINAL MATCH - ELEMENTOR OPTIMIZED) -->
  <div id="adega-hero-v4" class="adegagaucha-section">
      <div class="hero">
          <div class="hero-slider" id="adegaHeroSlider">
              <div class="hero-slide active" style="background-image: url('https://adegagaucha.com/wp-content/uploads/2025/10/edit-41-scaled.png')"></div>
              <div class="hero-slide" style="background-image: url('https://adegagaucha.com/wp-content/uploads/2025/10/edit-31-scaled.png')"></div>
              <div class="hero-slide" style="background-image: url('https://adegagaucha.com/wp-content/uploads/2024/10/Adega_Gaucha_Thanksgiving_2024_November_Nov_28th-1.png')"></div>
              <div class="hero-slide" style="background-image: url('https://adegagaucha.com/wp-content/uploads/2025/05/Steak-Picanha-Brazilian-Steakhouse-in-Deerfield-Beach.webp')"></div>
          </div>
          <div class="hero-overlay"></div>
          <div class="hero-ring"></div>
          <div class="hero-ring"></div>
          <div class="hero-ring"></div>
      
          <div class="hero-content">
              <h1 class="hero-title">
                  Dunwoody
                  <em>Atlanta</em>
              </h1>
              <div class="hero-email-capture">
                  <form class="email-form">
                      <input type="email" placeholder="Enter your email address" required>
                      <button type="submit" class="btn-primary">Get Early Access</button>
                  </form>
                  <div class="fomo-tag"><span class="pulse-dot"></span>SECURE YOUR SPOT: The first 100 sign-ups get a VIP Invitation</div>
              </div>
          </div>
          <div class="hero-scroll"><span>Scroll</span><div class="scroll-line"></div></div>
      </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      // Toggle mobile menu drawer
      const mobileToggle = document.getElementById('ag-mobile-toggle');
      const mobileDrawer = document.getElementById('ag-mobile-drawer');
      const drawerClose = document.getElementById('ag-drawer-close');
      const drawerOverlay = document.getElementById('ag-drawer-overlay');

      function openDrawer() {
        if(mobileDrawer) mobileDrawer.classList.add('active');
        if(drawerOverlay) drawerOverlay.classList.add('active');
      }

      function closeDrawer() {
        if(mobileDrawer) mobileDrawer.classList.remove('active');
        if(drawerOverlay) drawerOverlay.classList.remove('active');
      }

      if(mobileToggle) mobileToggle.addEventListener('click', openDrawer);
      if(drawerClose) drawerClose.addEventListener('click', closeDrawer);
      if(drawerOverlay) drawerOverlay.addEventListener('click', closeDrawer);

      // Handle slider for adega-hero-v4
      const heroV4 = document.querySelector('#adega-hero-v4');
      if (heroV4) {
          const slides = heroV4.querySelectorAll('.hero-slide');
          if (slides.length > 0) {
              let currentSlide = 0;
              setInterval(() => {
                  slides[currentSlide].classList.remove('active');
                  currentSlide = (currentSlide + 1) % slides.length;
                  slides[currentSlide].classList.add('active');
              }, 6000);
          }
      }
    });
  </script>
'''

content = re.sub(old_html_pattern, new_html, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Replacement successful.')
