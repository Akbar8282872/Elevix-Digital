with open('c:/Elevix Digital/services.html', 'r', encoding='utf-8') as f:
    text = f.read()

hero_start = text.find('<section class="relative min-h-[90vh]')
if hero_start == -1:
    hero_start = text.find('<section')
hero_end = text.find('<!-- Actual Content', hero_start)
if hero_end == -1:
    hero_end = hero_start + 1500

print(text[hero_start:hero_end])
