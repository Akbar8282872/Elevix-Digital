import re

with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Lift the hero section by reducing top margin and increasing bottom margin
text = text.replace(
    'class="relative z-10 w-full max-w-7xl mx-auto px-6 md:px-12 lg:px-24 flex flex-col md:flex-row items-center justify-between mt-20 md:mt-24 mb-12"',
    'class="relative z-10 w-full max-w-7xl mx-auto px-6 md:px-12 lg:px-24 flex flex-col md:flex-row items-center justify-between mt-8 md:mt-12 mb-24 md:mb-32"'
)

# 2. Fix the font sizes and force "Build systems," to stay on one line
text = text.replace(
    'class="font-display text-[55px] sm:text-[60px] md:text-[75px] font-bold tracking-tight leading-[1.05] text-white mb-6"',
    'class="font-display text-[42px] sm:text-[50px] md:text-[60px] lg:text-[70px] font-bold tracking-tight leading-[1.05] text-white mb-6"'
)
text = text.replace(
    'Build systems,<br/>not hustle.',
    '<span class="whitespace-nowrap">Build systems,</span><br/>not hustle.'
)

with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied final tweaks to hero section!")
