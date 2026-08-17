import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find exactly the marquee div containing this.
# Look for a div with whitespace-nowrap that contains AUTOMATING THE IMPOSSIBLE, DAILY
marquee_matches = re.finditer(r'<div[^>]*>[\s\S]*?AUTOMATING THE IMPOSSIBLE, DAILY[\s\S]*?</div>', text)
for m in marquee_matches:
    if "whitespace-nowrap" in m.group(0):
        # Found the marquee inner container, let's find the parent container
        # We'll just search for the section or div right above it
        start_idx = text.rfind('<div class="bg-kinetic-red', 0, m.start())
        if start_idx != -1:
            end_idx = text.find('</div>\n    </div>', start_idx)
            if end_idx != -1:
                marquee_html = text[start_idx:end_idx + 17]
                print("FOUND MARQUEE TO DELETE:\n")
                print(marquee_html)
                
                # Let's just delete it
                new_text = text.replace(marquee_html, '')
                with open('c:/Elevix Digital/index.html', 'w', encoding='utf-8') as f2:
                    f2.write(new_text)
                print("\n\nSuccessfully deleted the marquee!")
                exit()
        
        # If we can't find a bg-kinetic-red wrapper, maybe it's just a marquee div
        print(m.group(0)[:300])

