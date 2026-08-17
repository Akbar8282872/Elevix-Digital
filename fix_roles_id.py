import re

with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see all occurrences of <section class="...">
sections = re.findall(r'<section[^>]*>', text)

# We know the first section is the hero.
# The second section is "Why Us" (added previously).
# The third section is the roles.

# We will just replace the 3rd section tag to include id="roles"
if len(sections) > 2:
    third_section = sections[2]
    if 'id="roles"' not in third_section:
        new_third = third_section.replace('<section ', '<section id="roles" ')
        text = text.replace(third_section, new_third, 1)

with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added id='roles' to the 3rd section!")
