import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find exactly the marquee div containing this.
idx = text.find('<span class="mx-6">AUTOMATING THE IMPOSSIBLE, DAILY</span>')
if idx != -1:
    # We found the span. Let's find the section that encloses it.
    section_start = text.rfind('<div class="bg-kinetic-red', 0, idx)
    if section_start == -1:
        # Maybe the banner is NOT bg-kinetic-red?
        section_start = text.rfind('<div class="w-full relative overflow-hidden', 0, idx)
        if section_start == -1:
            section_start = text.rfind('<div', 0, idx - 500) # just grab a parent
            
    # let's just print a large chunk around the match
    print("MATCH SURROUNDINGS:")
    print(text[idx-500:idx+500])
