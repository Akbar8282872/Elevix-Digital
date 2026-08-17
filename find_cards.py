import re
with open('c:/Elevix Digital/services.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'<div class="gs-service-card[^"]*".*?</h3>', text, re.DOTALL)
for m in matches:
    print('---')
    print(m.group(0))
