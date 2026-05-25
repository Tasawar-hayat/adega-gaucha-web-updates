import re

file_path = r'c:\Users\DIGITAL META\Downloads\reviews-FINAL.html'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace emojis
    emoji_replacements = {
        "⭐": '<i class="rv-icon rv-icon-star"></i>',
        "🌟": '<i class="rv-icon rv-icon-star"></i>',
        "🥩": '<i class="rv-icon rv-icon-steak"></i>',
        "🔥": '<i class="rv-icon rv-icon-fire"></i>',
        "🥂": '<i class="rv-icon rv-icon-cheers"></i>',
        "🎉": '<i class="rv-icon rv-icon-party"></i>',
        "📍": '<i class="rv-icon rv-icon-pin"></i>',
        "🤝": '<i class="rv-icon rv-icon-handshake"></i>'
    }

    for emoji, icon in emoji_replacements.items():
        content = content.replace(emoji, icon)

    # Remove old card animation
    content = re.sub(r'animation:\s*cardIn.*?;', '', content)

    # Add CSS for icons and animations
    css_to_add = """
/* ─── BRAND ICONS & ANIMATIONS ───────────────────────── */
.rv-icon {
  display: inline-block;
  width: 1.3em;
  height: 1.3em;
  vertical-align: sub;
  background-color: var(--gold);
  -webkit-mask-size: contain;
  -webkit-mask-repeat: no-repeat;
  -webkit-mask-position: center;
  margin: 0 4px;
}
.rv-icon-star { -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z'/%3E%3C/svg%3E"); }
.rv-icon-fire { -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M17.5 11.2c-.6-.7-1.3-1.4-1.3-2.5 0-1.3.8-2.3 2-2.9-.6-2.5-2.8-4.3-5.5-4.8-.4-.1-.8.2-.8.6v.2c0 .4-.2.8-.5 1.1-.3.3-.8.4-1.2.3-3-1-5.1 1.1-6.1 2.9-.7 1.4-1 3.1-.7 4.8.1.7.3 1.3.6 2 .3.6.8 1.1 1.4 1.4.6.3 1.2.4 1.9.4.2 0 .4 0 .6-.1.6-.2 1.3.1 1.6.6.3.5.3 1.2 0 1.7-.2.4-.6.6-1 .7-2.3.4-4.2 2-5 4.2h18c-.8-2.1-2.7-3.7-5-4.2-.4-.1-.8-.3-1-.7-.3-.5-.3-1.2 0-1.7.3-.5 1-.8 1.6-.6.2 0 .4.1.6.1.7 0 1.3-.1 1.9-.4.6-.3 1.1-.8 1.4-1.4.3-.7.5-1.3.6-2 .3-1.7 0-3.4-.7-4.8z'/%3E%3C/svg%3E"); }
.rv-icon-steak { -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2L4 6v6c0 5.5 3.8 10.7 8 12 4.2-1.3 8-6.5 8-12V6l-8-4z'/%3E%3C/svg%3E"); } 
.rv-icon-cheers { -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M21 4h-2V3c0-.6-.4-1-1-1H6C5.4 2 5 2.4 5 3v1H3c-.6 0-1 .4-1 1v3c0 2.8 2.2 5 5 5h1.2c.4 1.6 1.6 2.8 3.2 3.2V20H9c-.6 0-1 .4-1 1v1h8v-1c0-.6-.4-1-1-1h-2.4v-3.8c1.6-.4 2.8-1.6 3.2-3.2H17c2.8 0 5-2.2 5-5V5c0-.6-.4-1-1-1z'/%3E%3C/svg%3E"); }
.rv-icon-party { -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2l2 6 6 2-6 2-2 6-2-6-6-2 6-2 2-6z'/%3E%3C/svg%3E"); } 
.rv-icon-pin { -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z'/%3E%3C/svg%3E"); }
.rv-icon-handshake { -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v4h-2zm0 6h2v2h-2z'/%3E%3C/svg%3E"); }

/* Scroll Animation Classes */
.rv-card, .rv-featured, .rv-stat {
  opacity: 0;
  transform: translateY(30px);
}
.rv-card.animate-in, .rv-featured.animate-in, .rv-stat.animate-in {
  animation: scrollFadeIn 0.8s var(--ease-expo) forwards;
}

@keyframes scrollFadeIn {
  from { opacity: 0; transform: translateY(30px); }
  to   { opacity: 1; transform: translateY(0); }
}
</style>
"""
    if "/* ─── BRAND ICONS & ANIMATIONS ───────────────────────── */" not in content:
        content = content.replace("</style>", css_to_add)

    js_to_add = """
<script>
document.addEventListener("DOMContentLoaded", () => {
  const elementsToAnimate = document.querySelectorAll('.rv-card, .rv-featured, .rv-stat');
  
  const observer = new IntersectionObserver((entries) => {
    let delay = 0;
    entries.forEach((entry) => {
      if(entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add('animate-in');
        }, delay);
        delay += 100; // Staggered delay for grid elements
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.05, rootMargin: "0px 0px -50px 0px" });

  elementsToAnimate.forEach(el => observer.observe(el));
});
</script>
</body>
"""
    if "elementsToAnimate" not in content:
        content = content.replace("</body>", js_to_add)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Success: Updated HTML with icons and animations.")
except Exception as e:
    print("Error:", e)
