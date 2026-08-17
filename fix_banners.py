import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open('c:/Elevix Digital/backup_marquee.html', 'r', encoding='utf-8') as f:
    marquee_html = f.read()

# 1. DELETE the HUGE Pre-Footer Banner (which has "AUTOMATING THE IMPOSSIBLE,")
banner_idx = text.find('<!-- HUGE Pre-Footer Banner -->')
if banner_idx != -1:
    end_banner_idx = text.find('<!--', banner_idx + 10)
    if end_banner_idx != -1:
        text = text[:banner_idx] + text[end_banner_idx:]
        print("Successfully deleted HUGE Pre-Footer Banner.")
    else:
        print("Could not find end of HUGE Pre-Footer Banner.")
else:
    print("Could not find HUGE Pre-Footer Banner.")

# 2. RESTORE Top Marquee Banner above Technologies portion
# Let's find "Technologies" or "Tech Stack"
tech_idx = text.find('<!-- TECHNOLOGIES')
if tech_idx == -1:
    tech_idx = text.find('<!-- Stack')
    if tech_idx == -1:
        tech_idx = text.find('id="tech"')
        if tech_idx == -1:
            tech_idx = text.find('id="technologies"')
            if tech_idx == -1:
                # the user said "tecnologies portion". It might be "Our Stack" or something.
                # Let's just find "technologies" case insensitive
                tech_match = re.search(r'<section[^>]*>[\s\S]*?technolog[\s\S]*?</section>', text, re.IGNORECASE)
                if tech_match:
                    tech_idx = tech_match.start()

if tech_idx != -1:
    # Let's find the start of the section containing technologies to inject BEFORE it
    section_start = text.rfind('<section', 0, tech_idx)
    if section_start != -1:
        text = text[:section_start] + marquee_html + "\n\n    " + text[section_start:]
        print("Successfully restored Top Marquee Banner above technologies.")
else:
    print("Could not find Technologies section!")

with open('c:/Elevix Digital/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

