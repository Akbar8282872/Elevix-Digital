import re
with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'<li class="mega-col-item">.*?</li>', text, re.DOTALL)
for m in matches:
    print(m.group(0).strip())
