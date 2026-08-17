import re
with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'<h3 class="mega-col-title".*?</h3>', text)
for m in matches:
    print(m.group(0))
