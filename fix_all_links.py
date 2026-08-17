import os

html_files = [
    'index.html',
    'services.html',
    'our-story.html',
    'case-studies.html',
    'blog.html',
    'careers.html',
    'contact.html'
]

# Fix the spaces in the mega menu onclick URLs
replacements = {
    "'services sub folder/web-development.html'": "'services%20sub%20folder/web-development.html'",
    "'services sub folder/app-development.html'": "'services%20sub%20folder/app-development.html'",
    "'services sub folder/ai-automation.html'": "'services%20sub%20folder/ai-automation.html'",
    "'services sub folder/design creative.html'": "'services%20sub%20folder/design%20creative.html'",
    "'services sub folder/SEO services.html'": "'services%20sub%20folder/SEO%20services.html'",
    "'services sub folder/digital-marketing.html'": "'services%20sub%20folder/digital-marketing.html'"
}

for file in html_files:
    path = f'c:/Elevix Digital/{file}'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        for k, v in replacements.items():
            content = content.replace(k, v)
            
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

# Now attach the links to the 6 large blocks in services.html
services_path = 'c:/Elevix Digital/services.html'
with open(services_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The headings in services.html body are:
# <h3 class="font-display text-[28px] font-bold text-white mb-4 relative z-10">Web Development</h3>

block_replacements = {
    '<h3 class="font-display text-[28px] font-bold text-white mb-4 relative z-10">Web Development</h3>': '<h3 class="font-display text-[28px] font-bold text-white mb-4 relative z-10 cursor-pointer transition-colors hover:text-[#E8282B]" onclick="window.location.href=\'services%20sub%20folder/web-development.html\'">Web Development</h3>',
    
    '<h3 class="font-display text-[28px] font-bold text-white mb-4 relative z-10">App Development</h3>': '<h3 class="font-display text-[28px] font-bold text-white mb-4 relative z-10 cursor-pointer transition-colors hover:text-[#E8282B]" onclick="window.location.href=\'services%20sub%20folder/app-development.html\'">App Development</h3>',
    
    '<h3 class="font-display text-[28px] font-bold text-white mb-4 relative z-10">AI Automation</h3>': '<h3 class="font-display text-[28px] font-bold text-white mb-4 relative z-10 cursor-pointer transition-colors hover:text-[#E8282B]" onclick="window.location.href=\'services%20sub%20folder/ai-automation.html\'">AI Automation</h3>',
    
    '<h3 class="font-display text-[28px] font-bold text-white mb-4 relative z-10">Design &amp; Creatives</h3>': '<h3 class="font-display text-[28px] font-bold text-white mb-4 relative z-10 cursor-pointer transition-colors hover:text-[#E8282B]" onclick="window.location.href=\'services%20sub%20folder/design%20creative.html\'">Design &amp; Creatives</h3>',
    
    '<h3 class="font-display text-[28px] font-bold text-white mb-4 relative z-10">SEO Services</h3>': '<h3 class="font-display text-[28px] font-bold text-white mb-4 relative z-10 cursor-pointer transition-colors hover:text-[#E8282B]" onclick="window.location.href=\'services%20sub%20folder/SEO%20services.html\'">SEO Services</h3>',
    
    '<h3 class="font-display text-[28px] font-bold text-white mb-4 relative z-10">Digital Marketing</h3>': '<h3 class="font-display text-[28px] font-bold text-white mb-4 relative z-10 cursor-pointer transition-colors hover:text-[#E8282B]" onclick="window.location.href=\'services%20sub%20folder/digital-marketing.html\'">Digital Marketing</h3>'
}

for k, v in block_replacements.items():
    content = content.replace(k, v)

# Also there might be a version with raw & instead of &amp;
block_replacements_raw = {
    '<h3 class="font-display text-[28px] font-bold text-white mb-4 relative z-10">Design & Creatives</h3>': '<h3 class="font-display text-[28px] font-bold text-white mb-4 relative z-10 cursor-pointer transition-colors hover:text-[#E8282B]" onclick="window.location.href=\'services%20sub%20folder/design%20creative.html\'">Design & Creatives</h3>'
}

for k, v in block_replacements_raw.items():
    content = content.replace(k, v)

with open(services_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated URLs encoding and added links to services.html blocks!')
