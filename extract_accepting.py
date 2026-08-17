import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'.{0,100}ACCEPTING CLIENTS.{0,100}', text, re.IGNORECASE)
with open('c:/Elevix Digital/accepting_clients.txt', 'w', encoding='utf-8') as out:
    for i, m in enumerate(matches):
        out.write(f'MATCH {i+1}:\n')
        out.write(text[m.start()-500:m.start()+500] + "\n====================\n")
