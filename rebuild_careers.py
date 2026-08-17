import re

# 1. Read our-story.html for the perfect header/navbar and footer
with open('c:/Elevix Digital/our-story.html', 'r', encoding='utf-8') as f:
    story_content = f.read()

nav_end = story_content.find('</nav>') + 6
header_nav = story_content[:nav_end]

footer_start = story_content.find('<footer')
footer = story_content[footer_start:]

# 2. Read careers.html for the middle content
with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    careers_content = f.read()

# The hero section starts right after nav
hero_start = careers_content.find('<section id="hero-section"')

# The CTA section ends right before the footer
# Let's find the start of the footer in careers.html to know where the middle ends
careers_footer_start = careers_content.find('<footer')

if careers_footer_start == -1:
    # If no footer, just take everything to the end (excluding body/html closing tags if any)
    middle_content = careers_content[hero_start:]
    # Strip closing body/html
    middle_content = middle_content.replace('</body>', '').replace('</html>', '')
else:
    middle_content = careers_content[hero_start:careers_footer_start]

# 3. Assemble the perfect careers.html
perfect_careers = header_nav + "\n\n" + middle_content.strip() + "\n\n" + footer

# 4. Save it
with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(perfect_careers)

print("Perfectly rebuilt careers.html")
