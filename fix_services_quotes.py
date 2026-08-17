import os
import re

html_files = [f for f in os.listdir('c:/Elevix Digital') if f.endswith('.html')]

for filename in html_files:
    filepath = os.path.join('c:/Elevix Digital', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to remove backslashes from inside onclick="window.location.href=\'services.html\'"
    new_content = re.sub(r'onclick="window\.location\.href=\\\'([^\']+)\\\'"', r'onclick="window.location.href=\'\1\'"', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filename}")

print("Done fixing services quotes via regex.")
