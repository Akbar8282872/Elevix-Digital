import re

with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix the Hero Section clipping
# Remove items-center and justify-center, replace with flex-col pt-48. 
# This anchors the content to the top instead of the vertical middle, 
# ensuring that tall content pushes the bottom down naturally instead of clipping it.
text = text.replace(
    'class="relative min-h-screen flex items-center justify-center pt-24 pb-32 lg:pb-48 overflow-hidden bg-[#0a0a0a] z-10"',
    'class="relative min-h-screen flex flex-col pt-40 pb-32 overflow-hidden bg-[#0a0a0a] z-10"'
)

# Also reduce the inner container margins since we are using pt-40 on the section
text = text.replace(
    'class="relative z-10 w-full max-w-7xl mx-auto px-6 md:px-12 lg:px-24 flex flex-col md:flex-row items-start justify-between mt-16 md:mt-24 mb-16 md:mb-24"',
    'class="relative z-10 w-full max-w-7xl mx-auto px-6 md:px-12 lg:px-24 flex flex-col md:flex-row items-start justify-between mt-8 mb-12"'
)

# 2. Fix the breadcrumb clickability (it was likely blocked by the invisible navbar hit-area)
# Push it down with mt-24 and give it z-50 to ensure it's on top of everything
text = text.replace(
    '<div class="relative z-20 font-display text-[13px] text-[#71717a] mt-10 mb-12 flex items-center gap-2">',
    '<div class="relative z-50 font-display text-[13px] text-[#71717a] mt-24 mb-12 flex items-center gap-2">'
)

with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied fixes for clipped buttons and breadcrumb clickability!")
