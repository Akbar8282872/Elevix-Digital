import re

with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Push down the breadcrumb
# The breadcrumb div is `<div class="font-display text-[13px] text-[#71717a] mb-12 flex items-center gap-2">`
text = text.replace(
    'class="font-display text-[13px] text-[#71717a] mb-12 flex items-center gap-2"',
    'class="font-display text-[13px] text-[#71717a] mt-10 mb-12 flex items-center gap-2"'
)

# 2. Fix the roles section ID so buttons work
sections = re.findall(r'<section[^>]*>', text)
if len(sections) > 2:
    third_section = sections[2]
    if 'id="roles"' not in third_section:
        new_third = third_section.replace('<section ', '<section id="roles" ')
        text = text.replace(third_section, new_third, 1)

with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Breadcrumb pushed down and roles section ID fixed!")
