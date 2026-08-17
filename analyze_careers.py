import re
with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = list(re.finditer(r'<section.*?>', text, re.IGNORECASE))
for i in range(len(matches)):
    start = matches[i].start()
    end = matches[i+1].start() if i+1 < len(matches) else text.find('<footer')
    section_html = text[start:end]
    print(f"Section {i}: length {len(section_html)}, tag: {matches[i].group(0)[:50]}")
    
    # print a snippet of the text inside the section to identify it
    snippet = re.sub(r'<[^>]+>', ' ', section_html)
    snippet = re.sub(r'\s+', ' ', snippet).strip()
    print(f"  Snippet: {snippet[:100]}")
