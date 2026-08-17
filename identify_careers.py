import re
with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = list(re.finditer(r'<section.*?>', text, re.IGNORECASE))
for i in range(len(matches)):
    start = matches[i].start()
    end = matches[i+1].start() if i+1 < len(matches) else text.find('<footer')
    section_html = text[start:end]
    
    tags = []
    if 'Vibe-coder' in section_html: tags.append('ROLES')
    if 'Aziz Cheema' in section_html: tags.append('TEAM')
    if 'AUTOMATING THE IMPOSSIBLE' in section_html.upper(): tags.append('CTA')
    
    if tags:
        print(f"Section {i}: {', '.join(tags)}")
