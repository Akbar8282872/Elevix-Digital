import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find the exact string that starts the marquee
marquee_start = text.find('<div class="bg-kinetic-red text-white py-2 overflow-hidden whitespace-nowrap')
if marquee_start != -1:
    # We need to find the matching closing div for this marquee.
    # It has nested divs, so let's just find the end of the text "AUTOMATING THE IMPOSSIBLE" and look for the next </div></div>
    idx = text.find('AUTOMATING THE IMPOSSIBLE', marquee_start)
    end_idx = text.find('</div>\n    </div>', idx)
    if end_idx != -1:
        marquee_html = text[marquee_start:end_idx + 17]
        print("FOUND MARQUEE:\n")
        print(marquee_html)
        
        # Now remove it
        new_text = text.replace(marquee_html, '')
        with open('c:/Elevix Digital/index.html', 'w', encoding='utf-8') as f2:
            f2.write(new_text)
        print("\n\nSuccessfully removed the marquee from index.html!")
