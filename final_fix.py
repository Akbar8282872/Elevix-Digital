import re

with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix the Hero Inner Container spacing
# We will replace min-h-[70vh] pt-12 md:pt-0 with mt-32 md:mt-48 mb-24 (which worked visually last time)
text = text.replace(
    'class="relative z-10 w-full max-w-7xl mx-auto px-6 md:px-12 lg:px-24 flex flex-col md:flex-row items-center justify-between min-h-[70vh] pt-12 md:pt-0"',
    'class="relative z-10 w-full max-w-7xl mx-auto px-6 md:px-12 lg:px-24 flex flex-col md:flex-row items-center justify-between mt-32 md:mt-48 mb-24"'
)

# 2. Fix the text (Elevix -> Neogen, PAKISTAN LAHORE -> INFOPARK KOCHI)
text = text.replace('Elevix hires exceptional people first', 'Neogen hires exceptional people first')
text = text.replace('PAKISTAN LAHORE', 'INFOPARK KOCHI')

# 3. Safely delete Marquee and Arbisoft
marquee_start = text.find('<!-- Top Marquee Banner -->')
results_start = text.find('<!-- Results / Case Studies Section -->')

if marquee_start != -1 and results_start != -1:
    text = text[:marquee_start] + text[results_start:]
    print("Safely deleted everything between Marquee Banner and Results section.")
else:
    print("Could not find boundaries to delete marquee/arbisoft safely.")

with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Careers page finalized successfully.")
