import re
with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

hero_start = text.find('<section id="hero-section"')
hero_end = text.find('</section>', hero_start)
if hero_start != -1 and hero_end != -1:
    with open('c:/Elevix Digital/scratch_hero.html', 'w', encoding='utf-8') as out:
        out.write(text[hero_start:hero_end+10])
