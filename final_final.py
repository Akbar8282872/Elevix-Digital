import re

with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Give the hero section more bottom padding so the buttons aren't cut off.
text = text.replace(
    'class="relative min-h-screen flex items-center justify-center pt-24 pb-10 overflow-hidden bg-[#0a0a0a] z-10"',
    'class="relative min-h-screen flex items-center justify-center pt-24 pb-32 lg:pb-48 overflow-hidden bg-[#0a0a0a] z-10"'
)

# 2. Make the breadcrumb z-20 so it is definitely clickable, and turn 'Career' into a working link.
breadcrumb_old = '''<div class="font-display text-[13px] text-[#71717a] mt-10 mb-12 flex items-center gap-2">
                    <a href="index.html" class="hover:text-white transition-colors">Home</a> 
                    <span class="text-white/20">/</span> 
                    <span class="text-white font-medium">Career</span>
                </div>'''

breadcrumb_new = '''<div class="relative z-20 font-display text-[13px] text-[#71717a] mt-10 mb-12 flex items-center gap-2">
                    <a href="index.html" class="hover:text-white transition-colors cursor-pointer">Home</a> 
                    <span class="text-white/20">/</span> 
                    <a href="careers.html" class="hover:text-white transition-colors text-white font-medium cursor-pointer">Career</a>
                </div>'''
text = text.replace(breadcrumb_old, breadcrumb_new)

with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied final button and padding tweaks to hero section!")
