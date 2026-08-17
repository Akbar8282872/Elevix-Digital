import re

with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix bottom button clipping by removing vertical overflow hiding
# Change 'overflow-hidden' to 'overflow-x-hidden' on the hero section.
# This prevents the background from causing horizontal scroll, but allows infinite vertical expansion!
text = text.replace(
    'class="relative min-h-screen flex flex-col pt-40 pb-32 overflow-hidden bg-[#0a0a0a] z-10"',
    'class="relative min-h-screen flex flex-col pt-40 pb-32 overflow-x-hidden bg-[#0a0a0a] z-10"'
)

# Also let's push the breadcrumb down a lot more to ensure it totally clears the navbar hit-area.
# And add aggressive onclick JavaScript handlers since the user specifically asked for JS as a fallback!
breadcrumb_old = '''<div class="relative z-50 font-display text-[13px] text-[#71717a] mt-24 mb-12 flex items-center gap-2">
                    <a href="index.html" class="hover:text-white transition-colors cursor-pointer">Home</a> 
                    <span class="text-white/20">/</span> 
                    <a href="careers.html" class="hover:text-white transition-colors text-white font-medium cursor-pointer">Career</a>
                </div>'''

breadcrumb_new = '''<div class="relative z-50 font-display text-[13px] text-[#71717a] mt-32 mb-12 flex items-center gap-2">
                    <a href="index.html" onclick="window.location.href='index.html'; return false;" class="hover:text-white transition-colors cursor-pointer relative z-50 pointer-events-auto block px-2 py-1">Home</a> 
                    <span class="text-white/20">/</span> 
                    <a href="careers.html" onclick="window.location.href='careers.html'; return false;" class="hover:text-white transition-colors text-white font-medium cursor-pointer relative z-50 pointer-events-auto block px-2 py-1">Career</a>
                </div>'''

text = text.replace(breadcrumb_old, breadcrumb_new)

with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied ultimate fixes for clipped buttons and JS breadcrumbs!")
