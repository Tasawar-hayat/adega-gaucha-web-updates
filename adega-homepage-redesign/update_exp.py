import sys

with open("experience.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

css_to_add = """
    /* =========================================
   NEW EXPERIENCE SPLIT LAYOUT
   ========================================= */
    .experience-section-new {
      background-color: transparent;
      color: #fff;
      padding: 2rem 5%;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      margin-bottom: 4rem;
    }

    .experience-container {
      max-width: 1200px;
      width: 100%;
      display: flex;
      flex-direction: row;
      align-items: center;
      gap: 4rem;
    }

    .experience-text {
      flex: 1;
      opacity: 0;
      transform: translateY(40px);
      transition: opacity 1s ease, transform 1s ease;
    }

    .experience-text.reveal {
      opacity: 1;
      transform: translateY(0);
    }

    .experience-accent {
      width: 60px;
      height: 4px;
      background-color: var(--primary-orange);
      margin-bottom: 1.5rem;
      box-shadow: 0 0 10px rgba(250, 135, 34, 0.5);
    }

    .experience-desc {
      font-family: 'Inter', sans-serif;
      font-size: 1.1rem;
      line-height: 1.8;
      color: rgba(255,255,255,0.8);
      margin-bottom: 2.5rem;
    }

    .experience-image-wrap {
      flex: 1;
      position: relative;
      opacity: 0;
      transform: translateX(40px);
      transition: opacity 1s ease 0.3s, transform 1s ease 0.3s;
    }

    .experience-image-wrap.reveal {
      opacity: 1;
      transform: translateX(0);
    }

    .experience-image {
      width: 100%;
      border-radius: 15px;
      box-shadow: 0 20px 50px rgba(0,0,0,0.8);
      display: block;
    }

    .experience-image-glow {
      position: absolute;
      top: -10px;
      bottom: -10px;
      left: -10px;
      right: -10px;
      background: linear-gradient(45deg, var(--primary-orange), transparent);
      z-index: -1;
      filter: blur(20px);
      opacity: 0.3;
      border-radius: 20px;
    }

    .ag-btn-secondary {
      background: transparent;
      color: #fff;
      border: 2px solid #fff;
      padding: 15px 30px;
      font-size: 0.95rem;
      font-weight: 600;
      letter-spacing: 2px;
      text-transform: uppercase;
      border-radius: 30px;
      cursor: pointer;
      transition: all 0.3s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
    }

    .ag-btn-secondary:hover {
      background: rgba(255, 255, 255, 0.1);
      transform: translateY(-2px);
    }

    @media (max-width: 900px) {
      .experience-container {
        flex-direction: column-reverse;
        text-align: center;
        gap: 2.5rem;
      }
      .experience-accent {
        margin: 0 auto 1.5rem auto;
      }
      .experience-image-wrap {
        transform: translateY(40px);
      }
    }
"""

html_to_add = """
      <!-- NEW SPLIT-SCREEN EXPERIENCE CONTENT -->
      <div class="experience-section-new">
        <div class="experience-container">
          <div class="experience-text" id="exp-text">
            <div class="experience-accent"></div>
            <p class="experience-desc">
              Embark on a culinary journey rooted in the centuries-old tradition of Southern Brazil. 
              Experience the art of Churrasco with our continuous tableside service, featuring prime cuts 
              of fire-roasted meats perfectly seasoned and carved directly onto your plate by our authentic Gauchos.
            </p>
            <a href="https://adegagaucha.com/menu/" class="ag-btn-secondary">
              EXPLORE OUR MENU <span>➔</span>
            </a>
          </div>
          <div class="experience-image-wrap" id="exp-image">
            <div class="experience-image-glow"></div>
            <img src="churrasco_experience.png" alt="Gaucho carving Picanha tableside" class="experience-image">
          </div>
        </div>
      </div>
"""

js_to_add = """
      // Scroll Reveal Observer for new content
      const observerExp = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('reveal');
          }
        });
      }, { threshold: 0.2 });
      
      const expText = document.getElementById('exp-text');
      const expImage = document.getElementById('exp-image');
      if(expText) observerExp.observe(expText);
      if(expImage) observerExp.observe(expImage);
"""

for i, line in enumerate(lines):
    if "</style>" in line:
        lines.insert(i, css_to_add)
        break

for i, line in enumerate(lines):
    if "<!-- PREMIUM STATS ROW -->" in line:
        lines.insert(i, html_to_add)
        break

for i, line in enumerate(lines):
    if "const statsContainer = document.getElementById('stats-container');" in line:
        lines.insert(i, js_to_add)
        break

with open("experience.html", "w", encoding="utf-8") as f:
    f.writelines(lines)
