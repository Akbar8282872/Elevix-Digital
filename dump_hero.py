import re
with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

hero_start = text.find('<section id="hero-section"')
hero_end = text.find('</section>', hero_start)
if hero_start != -1 and hero_end != -1:
    print(text[hero_start:hero_end+10][:2000])
