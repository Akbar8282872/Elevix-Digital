import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('AUTOMATING THE IMPOSSIBLE, DAILY.')
if idx != -1:
    start_idx = text.rfind('<div class="text-kinetic-red', 0, idx)
    end_idx = text.find('</div>', idx)
    if start_idx != -1 and end_idx != -1:
        html_to_delete = text[start_idx:end_idx+6]
        print("FOUND TO DELETE:")
        print(html_to_delete)
        
        new_text = text.replace(html_to_delete, '')
        with open('c:/Elevix Digital/index.html', 'w', encoding='utf-8') as f2:
            f2.write(new_text)
        print("\n\nSuccessfully deleted the subtitle banner!")
