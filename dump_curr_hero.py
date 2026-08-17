with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()
hero_idx = text.find('<section id="hero-section"')
hero_end = text.find('</section>', hero_idx)
print(text[hero_idx:hero_end+10])
