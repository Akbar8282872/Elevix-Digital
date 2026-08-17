import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('<!-- Top Marquee Banner -->')
if start_idx != -1:
    # Find the end of this block. It's a div.
    # The next thing after it is probably another section like <!-- Next Section --> or something.
    # Let's just find the next <!-- 
    end_idx = text.find('<!--', start_idx + 30)
    if end_idx != -1:
        marquee_html = text[start_idx:end_idx]
        print("FOUND TO DELETE:")
        print(marquee_html[:150] + "...(truncated)...")
        
        new_text = text.replace(marquee_html, '')
        with open('c:/Elevix Digital/index.html', 'w', encoding='utf-8') as f2:
            f2.write(new_text)
        print("\nSuccessfully removed the Top Marquee Banner from index.html!")
    else:
        print("Could not find the end of the banner block.")
else:
    print("Could not find <!-- Top Marquee Banner -->")
