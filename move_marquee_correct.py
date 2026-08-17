import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The marquee banner string is exact in backup_marquee.html
with open('c:/Elevix Digital/backup_marquee.html', 'r', encoding='utf-8') as f:
    marquee_html = f.read()

# First, remove the marquee banner from wherever it currently is in index.html
# We can just search for "<!-- Top Marquee Banner -->" and remove everything until the next "<!--"
start_idx = text.find('<!-- Top Marquee Banner -->')
if start_idx != -1:
    end_idx = text.find('<!--', start_idx + 10)
    if end_idx != -1:
        # Delete it from its current place
        text = text[:start_idx] + text[end_idx:]
        print("Removed marquee from its current location.")

# Now, find the hero section and inject it right AFTER it closes
hero_start = text.find('<section id="hero-section"')
if hero_start != -1:
    hero_end = text.find('</section>', hero_start)
    if hero_end != -1:
        hero_end += len('</section>')
        # Inject right after hero section
        text = text[:hero_end] + "\n\n    " + marquee_html + "\n\n    " + text[hero_end:]
        with open('c:/Elevix Digital/index.html', 'w', encoding='utf-8') as f2:
            f2.write(text)
        print("Successfully injected marquee directly under the hero section!")
    else:
        print("Could not find </section> for hero-section")
else:
    print("Could not find <section id='hero-section'")
