import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open('c:/Elevix Digital/backup_marquee.html', 'r', encoding='utf-8') as f:
    marquee_html = f.read()

# Let's find exactly the section containing "TECHNOLOGIES" or "TECH STACK"
m = re.search(r'<section[^>]*>[\s\S]*?technolog[\s\S]*?</section>', text, re.IGNORECASE)
if m:
    section_start = m.start()
    text = text[:section_start] + marquee_html + "\n\n    " + text[section_start:]
    with open('c:/Elevix Digital/index.html', 'w', encoding='utf-8') as f2:
        f2.write(text)
    print("Successfully restored marquee above technologies section!")
else:
    print("Could not find technologies section!")
