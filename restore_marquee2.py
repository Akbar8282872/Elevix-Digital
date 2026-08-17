import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open('c:/Elevix Digital/backup_marquee.html', 'r', encoding='utf-8') as f:
    marquee_html = f.read()

# Let's find exactly where <section id="services" is
services_idx = text.find('<section id="services"')

if services_idx != -1:
    text = text[:services_idx] + marquee_html + "\n\n    " + text[services_idx:]
    with open('c:/Elevix Digital/index.html', 'w', encoding='utf-8') as f2:
        f2.write(text)
    print("Successfully restored marquee above services section!")
else:
    print("Could not find services section!")
