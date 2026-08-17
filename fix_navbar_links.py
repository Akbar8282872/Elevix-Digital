import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace <a href="#">Careers</a> with <a href="careers.html">Careers</a>
def replace_careers(match):
    return match.group(0).replace('href="#"', 'href="careers.html"')

def replace_contact(match):
    return match.group(0).replace('href="#"', 'href="contact.html"')

text = re.sub(r'<a href="#"[^>]*>\s*Careers\s*</a>', replace_careers, text)
text = re.sub(r'<a href="#"[^>]*>\s*Contact Us\s*</a>', replace_contact, text)
# Handle possible case differences or nested spans just in case
text = re.sub(r'<a href="#"[^>]*>\s*<span[^>]*>\s*Careers\s*</span>\s*</a>', replace_careers, text)
text = re.sub(r'<a href="#"[^>]*>\s*<span[^>]*>\s*Contact Us\s*</span>\s*</a>', replace_contact, text)

# Just do a blanket replace if the text inside the <a> tag contains the target words
matches = re.finditer(r'<a href="#"([^>]*)>(.*?)</a>', text, re.DOTALL | re.IGNORECASE)
for m in matches:
    inner = m.group(2)
    original_a = m.group(0)
    if 'Career' in inner:
        new_a = original_a.replace('href="#"', 'href="careers.html"')
        text = text.replace(original_a, new_a)
    elif 'Contact' in inner:
        new_a = original_a.replace('href="#"', 'href="contact.html"')
        text = text.replace(original_a, new_a)

with open('c:/Elevix Digital/index.html', 'w', encoding='utf-8') as f2:
    f2.write(text)

print("Fixed links for Careers and Contact Us!")
