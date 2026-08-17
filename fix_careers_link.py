import os
import re

html_files = [f for f in os.listdir('c:/Elevix Digital') if f.endswith('.html')]

for filename in html_files:
    filepath = os.path.join('c:/Elevix Digital', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace href="#" with href="careers.html" for the Careers link
    # It looks like: <a href="#" class="text-on-secondary-container text-[14px] font-medium hover:text-white transition-colors">Careers</a>
    new_content = re.sub(
        r'<a href="#"([^>]*>Careers</a>)',
        r'<a href="careers.html"\1',
        content
    )
    new_content = re.sub(
        r'<a href="#"([^>]*>CAREERS</a>)',
        r'<a href="careers.html"\1',
        new_content
    )
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed Careers link in {filename}")

print("Done fixing careers links.")
