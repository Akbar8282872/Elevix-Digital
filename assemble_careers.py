import re

# Read our-story for nav and footer
with open('c:/Elevix Digital/our-story.html', 'r', encoding='utf-8') as f:
    story = f.read()

nav_end = story.find('</nav>') + 6
header_nav = story[:nav_end]
story_footer = story[story.find('<footer'):]

# Read careers for the Hero, Roles, and Team
with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    careers_text = f.read()

matches = list(re.finditer(r'<section.*?>', careers_text, re.IGNORECASE))
def get_section(idx):
    start = matches[idx].start()
    end = matches[idx+1].start() if idx+1 < len(matches) else careers_text.find('<footer')
    return careers_text[start:end]

career_hero = get_section(0)
career_roles = get_section(10)
career_team = get_section(12)

# Read blog.html for the CTA section at the bottom
with open('c:/Elevix Digital/blog.html', 'r', encoding='utf-8') as f:
    blog = f.read()

# The CTA section in blog is near the bottom
blog_matches = list(re.finditer(r'<section.*?>', blog, re.IGNORECASE))
cta_section = ""
for i in range(len(blog_matches)):
    start = blog_matches[i].start()
    end = blog_matches[i+1].start() if i+1 < len(blog_matches) else blog.find('<footer')
    sec_html = blog[start:end]
    if 'Automating the impossible' in sec_html or 'Accepting clients 2026' in sec_html:
        cta_section = sec_html
        break

# Assemble
perfect_careers = (
    header_nav + "\n\n" +
    career_hero + "\n\n" +
    career_roles + "\n\n" +
    career_team + "\n\n" +
    cta_section + "\n\n" +
    story_footer
)

with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(perfect_careers)

print("SUCCESS: Perfectly assembled careers.html without any garbage!")
