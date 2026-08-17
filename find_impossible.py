import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'.{0,50}automate the impossible.{0,50}', text, re.IGNORECASE):
    print("MATCH 1:", m.group(0))

for m in re.finditer(r'.{0,50}automating the impossible.{0,50}', text, re.IGNORECASE):
    print("MATCH 2:", m.group(0))
