import os
import re

files_to_update = [
    'index.html',
    'services.html',
    'our-story.html',
    'blog.html',
    'case-studies.html',
    'careers.html'
]

contact_us_pattern = re.compile(r'<a href="#" class="([^"]*)">Contact Us</a>')
lets_talk_pattern = re.compile(r'<button class="bg-kinetic-red([^"]*)">\s*Let\'s Talk\s*</button>')

for filename in files_to_update:
    filepath = os.path.join('c:/Elevix Digital', filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace Contact Us link
        content = contact_us_pattern.sub(r'<a href="contact.html" class="\1">Contact Us</a>', content)
        
        # Replace Let's Talk button
        content = lets_talk_pattern.sub(r'<button onclick="window.location.href=\'contact.html\'" class="bg-kinetic-red\1">\n                Let\'s Talk\n            </button>', content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated links in {filename}")

print("All files processed.")
