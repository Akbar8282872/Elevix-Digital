import re

with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Adjust Hero inner container to fix "too up"
# Original: class="relative z-10 w-full max-w-7xl mx-auto px-6 md:px-12 lg:px-24 flex flex-col md:flex-row items-center justify-between min-h-[70vh] pt-12 md:pt-0"
text = text.replace(
    'class="relative z-10 w-full max-w-7xl mx-auto px-6 md:px-12 lg:px-24 flex flex-col md:flex-row items-center justify-between min-h-[70vh] pt-12 md:pt-0"',
    'class="relative z-10 w-full max-w-7xl mx-auto px-6 md:px-12 lg:px-24 flex flex-col md:flex-row items-center justify-between mt-32 md:mt-48 mb-24"'
)

# 2. Remove Marquee banner
marquee_start = text.find('<!-- Top Marquee Banner -->')
if marquee_start != -1:
    marquee_end = text.find('</div>', text.find('</div>', text.find('</div>', marquee_start) + 1) + 1) + 6
    # It might be safer to just use regex or find the exact ending div.
    # We know the marquee structure has a parent div and an inner div.
    pass

# Let's use regex to remove the marquee banner safely
marquee_pattern = r'<!-- Top Marquee Banner -->.*?</div>\s*</div>'
text = re.sub(marquee_pattern, '', text, flags=re.DOTALL | re.IGNORECASE)

# 3. Remove "Partner Logos Section" or "Technologies line arbisoft system"
arbisoft_idx = text.lower().find('arbisoft')
if arbisoft_idx != -1:
    # Find the section or div wrapping it
    # We will look for <div class="w-full overflow-hidden bg-[#050505]... 
    # Or <section...
    ticker_start = text.rfind('<div class="w-full', 0, arbisoft_idx)
    # If the ticker is inside a section or just a standalone div
    # Let's see if it has a comment above it
    comment_start = text.rfind('<!--', max(0, ticker_start-100), ticker_start)
    if comment_start != -1:
        ticker_start = comment_start
        
    ticker_end = text.find('</div>', arbisoft_idx)
    # we need to close the divs. usually it's a few nested divs. 
    # Let's just find the next <!-- to know where the next section starts
    next_comment = text.find('<!--', arbisoft_idx)
    if next_comment != -1:
        text = text[:ticker_start] + text[next_comment:]
    else:
        print("Couldn't find next section to cut ticker")
else:
    print("Arbisoft not found")

with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated careers.html layout and removed requested sections.")
