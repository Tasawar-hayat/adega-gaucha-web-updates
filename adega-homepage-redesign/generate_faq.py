# -*- coding: utf-8 -*-
html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adega Gaucha | Premium FAQs</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600&family=Barlow:wght@300;400;500&family=Cormorant+Garamond:wght@300;400;500&display=swap" rel="stylesheet">
</head>
<body style="margin: 0; background: #000;">

<div id="adega-faq-v2" class="adegagaucha-section">
    <style>
        #adega-faq-v2 {
            --black: #000000;
            --charcoal: #0a0a08;
            --gold: #F68625;
            --gold-light: #ff9d47;
            --brand-orange: #F68625;
            --cream: #FFF9F5;
            --cream-dim: rgba(255, 249, 245, 0.7);
            --font-display: 'Cormorant Garamond', Georgia, serif;
            --font-body: 'Barlow', sans-serif;
            --font-label: 'Barlow Condensed', sans-serif;
            --ease-expo: cubic-bezier(0.16, 1, 0.3, 1);
            --gutter: 24px;

            background: var(--black);
            color: var(--cream);
            font-family: var(--font-body);
            overflow: hidden;
            position: relative;
        }

        #adega-faq-v2 * { box-sizing: border-box; }

        #adega-faq-v2 .container { width: min(1280px, 100% - var(--gutter) * 2); margin-inline: auto; }

        #adega-faq-v2 .label { font-family: var(--font-label); font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; color: var(--brand-orange); display: block; margin-bottom: 0.5rem; }

        #adega-faq-v2 .section-title { font-family: var(--font-display); font-size: clamp(2.4rem, 5vw, 4rem); font-weight: 300; line-height: 1.1; color: var(--cream); margin: 0; }
        #adega-faq-v2 .section-title em { font-style: italic; color: var(--brand-orange); }

        #adega-faq-v2 .reveal { opacity: 0; transform: translateY(32px); transition: opacity 0.8s var(--ease-expo), transform 0.8s var(--ease-expo); will-change: transform, opacity; }
        #adega-faq-v2 .reveal.visible { opacity: 1; transform: none; }
        
        #adega-faq-v2 .delay-1 { transition-delay: 0.1s; }
        #adega-faq-v2 .delay-2 { transition-delay: 0.2s; }
        #adega-faq-v2 .delay-3 { transition-delay: 0.3s; }
        #adega-faq-v2 .delay-4 { transition-delay: 0.4s; }

        #adega-faq-v2 .faq { padding: clamp(80px, 12vw, 140px) 0; }
        
        #adega-faq-v2 .faq-grid { display: grid; grid-template-columns: 1fr 1.6fr; gap: clamp(3rem, 6vw, 6rem); align-items: start; }
        #adega-faq-v2 .faq-left { position: sticky; top: 2rem; }
        #adega-faq-v2 .faq-left-sub { font-size: 0.95rem; font-weight: 300; color: rgba(245, 240, 232, 0.6); line-height: 1.7; margin-top: 1rem; }
        #adega-faq-v2 .faq-cta { margin-top: 2rem; display: inline-flex; align-items: center; gap: 0.5rem; font-family: var(--font-label); font-size: 0.75rem; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: var(--gold); border-bottom: 1px solid rgba(246, 134, 37, 0.35); padding-bottom: 0.2rem; transition: all 0.3s; cursor: pointer; text-decoration: none; }
        #adega-faq-v2 .faq-cta:hover { color: var(--gold-light); border-color: var(--gold); }

        #adega-faq-v2 .faq-list { display: flex; flex-direction: column; }
        #adega-faq-v2 .faq-item { border-bottom: 1px solid rgba(246, 134, 37, 0.12); overflow: hidden; }
        
        #adega-faq-v2 .faq-q { display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: 1.4rem 0; cursor: pointer; font-family: var(--font-display); font-size: clamp(1rem, 1.8vw, 1.2rem); font-weight: 400; color: var(--cream); transition: color 0.3s; text-align: left; width: 100%; border: none; background: none; outline: none; }
        #adega-faq-v2 .faq-q:hover { color: var(--gold-light); }
        #adega-faq-v2 .faq-item.open .faq-q { color: var(--gold-light); }
        
        #adega-faq-v2 .faq-icon { flex-shrink: 0; width: 24px; height: 24px; border-radius: 50%; border: 1px solid rgba(246, 134, 37, 0.35); display: flex; align-items: center; justify-content: center; transition: all 0.4s var(--ease-expo); }
        #adega-faq-v2 .faq-item.open .faq-icon { transform: rotate(45deg); background: rgba(246, 134, 37, 0.12); border-color: var(--gold); }
        #adega-faq-v2 .faq-icon svg { color: var(--gold); }
        
        #adega-faq-v2 .faq-a-wrap { display: grid; grid-template-rows: 0fr; transition: grid-template-rows 0.45s var(--ease-expo); }
        #adega-faq-v2 .faq-item.open .faq-a-wrap { grid-template-rows: 1fr; }
        #adega-faq-v2 .faq-a-inner { overflow: hidden; }
        #adega-faq-v2 .faq-a { padding-bottom: 1.4rem; font-size: 0.95rem; font-weight: 300; color: rgba(245, 240, 232, 0.65); line-height: 1.7; margin: 0; }
        #adega-faq-v2 .faq-a strong { color: var(--gold); font-weight: 500; }

        @media (max-width: 1024px) {
            #adega-faq-v2 { overflow-x: hidden; }
            #adega-faq-v2 .faq { padding: 50px 0; }
            #adega-faq-v2 .container { 
                width: 100% !important; 
                max-width: 100% !important; 
                padding: 0 20px !important; 
                margin: 0 !important;
                display: block !important;
            }
            #adega-faq-v2 .faq-grid { 
                display: block !important; 
                width: 100% !important;
            }
            #adega-faq-v2 .faq-left { 
                text-align: center !important; 
                margin-bottom: 2.5rem;
                width: 100% !important;
            }
            #adega-faq-v2 .faq-q { 
                font-size: 1rem !important; 
                padding: 1.2rem 0 !important; 
                line-height: 1.4 !important;
                display: flex !important;
                align-items: flex-start !important;
                text-align: left !important;
                white-space: normal !important;
                width: 100% !important;
            }
            #adega-faq-v2 .faq-a { 
                font-size: 0.9rem !important; 
                text-align: left !important; 
                padding-right: 10px !important;
            }
            #adega-faq-v2 .faq-cta { 
                margin: 1.5rem auto 0 !important; 
                display: inline-flex !important;
                text-align: center !important;
            }
            #adega-faq-v2 .section-title { font-size: 2.2rem !important; }
        }

        @media (max-width: 480px) {
            #adega-faq-v2 .section-title { font-size: 1.8rem !important; }
            #adega-faq-v2 .faq-q { font-size: 0.9rem !important; }
        }
    </style>

    <section class="faq" id="faq">
        <div class="container">
            <div class="faq-grid">
                <div class="faq-left reveal">
                    <span class="label">Knowledge Base</span>
                    <h2 class="section-title">Got <em>Questions?</em></h2>
                    <p class="faq-left-sub">Everything you need to know about dining at Adega Gaucha, from our authentic Churrasco experience to private event bookings and dress codes.</p>
                    <a href="https://adegagaucha.com/reservations" class="faq-cta">Reserve your spot</a>
                </div>

                <div class="faq-list">
                    {faq_items}
                </div>
            </div>
        </div>
    </section>

    <script>
        (function() {
            const scope = document.querySelector('#adega-faq-v2');
            if (!scope) return;

            const revealObs = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        revealObs.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1 });
            scope.querySelectorAll('.reveal').forEach(el => revealObs.observe(el));

            scope.querySelectorAll('.faq-q').forEach(btn => {
                btn.addEventListener('click', function () {
                    const item = this.closest('.faq-item');
                    const wasOpen = item.classList.contains('open');
                    scope.querySelectorAll('.faq-item.open').forEach(el => {
                        el.classList.remove('open');
                        el.querySelector('.faq-q').setAttribute('aria-expanded', 'false');
                    });
                    if (!wasOpen) {
                        item.classList.add('open');
                        this.setAttribute('aria-expanded', 'true');
                    }
                });
            });
        })();
    </script>
</div>
</body>
</html>
'''

questions = [
    ("What is a Churrascaria?", "A Churrascaria is a traditional Brazilian steakhouse where meats are roasted over an open fire. Our gauchos (chefs) bring fire-roasted meats directly to your table on large skewers and carve them perfectly onto your plate."),
    ("What is included in the 17-cut Rodizio experience?", 'The full Rodizio experience gives you unlimited tableside service of 17 signature fire-roasted meats—including our famous Picanha, Filet Mignon, and Lamb Chops. It also includes limitless access to our Gourmet Salad Bar, authentic hot side dishes, and fresh Brazilian cheese bread (Pão de Queijo).<br><a href="https://adegagaucha.com/menu" class="faq-cta" style="margin-top:0.5rem">View Our Menu &rarr;</a>'),
    ("Do I need to make a reservation?", 'While walk-in guests are always welcome, we highly recommend making a reservation, particularly for weekend dining or larger groups. Reserving your table ensures a seamless, uninterrupted dining experience from the moment you arrive.<br><a href="https://adegagaucha.com/reservations" class="faq-cta" style="margin-top:0.5rem">Reserve Your Table &rarr;</a>'),
    ("Does Adega Gaucha offer Halal options?", "Yes, we proudly offer Halal-certified meat options! Simply notify our team when booking your reservation, and our chefs will ensure your Halal selections are specially prepared to accommodate your dietary needs."),
    ("Are there vegetarian or vegan options available?", "Absolutely. Our expansive Gourmet Salad Bar features over 40 fresh, seasonal items including roasted vegetables, imported artisan cheeses, exotic salads, and hot side dishes, providing a rich and satisfying meal for our vegetarian and vegan guests."),
    ("What is the pricing range at Adega Gaucha?", "Our pricing varies slightly depending on the location and whether you are joining us for lunch or dinner. Guests can choose between the full Rodizio meat experience or the Gourmet Table-only option. Please select your preferred location on our website to view precise pricing details."),
    ("Can I host a private event or corporate dinner?", "Yes, we offer elegantly appointed private and semi-private dining rooms at all our locations. These spaces are perfect for corporate meetings, weddings, birthdays, and milestone family celebrations."),
    ("Which Adega Gaucha location should I choose?", 'We currently boast stunning locations in Orlando, Kissimmee, and Deerfield Beach. Because every location delivers the exact same premium Rodizio experience, we recommend choosing the one that is most convenient for your stay in Florida!<br><a href="https://adegagaucha.com/locations" class="faq-cta" style="margin-top:0.5rem">Choose Nearest Location &rarr;</a>'),
    ("What is the dress code?", "We suggest smart casual attire to match our premium dining atmosphere. Ultimately, we want you to feel comfortable and relaxed while enjoying your unforgettable dining experience with family and friends.")
]

faq_items_html = ""
for i, (q, a) in enumerate(questions):
    delay_class = "delay-1"
    if i % 4 == 1: delay_class = "delay-2"
    elif i % 4 == 2: delay_class = "delay-3"
    elif i % 4 == 3: delay_class = "delay-4"
    
    faq_items_html += f'''
                    <div class="faq-item reveal {delay_class}">
                        <button class="faq-q" aria-expanded="false">
                            {q}
                            <span class="faq-icon" aria-hidden="true">
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19" /><line x1="5" y1="12" x2="19" y2="12" /></svg>
                            </span>
                        </button>
                        <div class="faq-a-wrap">
                            <div class="faq-a-inner">
                                <p class="faq-a">{a}</p>
                            </div>
                        </div>
                    </div>'''

final_html = html_template.replace('{faq_items}', faq_items_html)

with open('faq.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

# Also update temp_faq.html just in case
with open('temp_faq.html', 'w', encoding='utf-8') as f:
    f.write(final_html)
