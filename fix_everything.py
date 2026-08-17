import os
import re

# PART 1: Fix sub-pages
sub_folder = 'c:/Elevix Digital/services sub folder'
sub_pages = [
    'web-development.html',
    'app-development.html',
    'ai-automation.html',
    'design creative.html',
    'SEO services.html',
    'digital-marketing.html'
]

sub_replacements = {
    # Fix the Services button link
    "onclick=\"window.location.href='services.html'\"": "onclick=\"window.location.href='../services.html'\"",
    
    # Add mega menu links natively for the sub-folder
    '<h3 class="mega-col-title">WEB DEVELOPMENT</h3>': '<h3 class="mega-col-title" onclick="window.location.href=\'web-development.html\'" style="cursor: pointer;" title="Go to Web Development">WEB DEVELOPMENT</h3>',
    '<h3 class="mega-col-title">APP DEVELOPMENT</h3>': '<h3 class="mega-col-title" onclick="window.location.href=\'app-development.html\'" style="cursor: pointer;" title="Go to App Development">APP DEVELOPMENT</h3>',
    '<h3 class="mega-col-title">AI AUTOMATION</h3>': '<h3 class="mega-col-title" onclick="window.location.href=\'ai-automation.html\'" style="cursor: pointer;" title="Go to AI Automation">AI AUTOMATION</h3>',
    '<h3 class="mega-col-title">DESIGN &amp; CREATIVES</h3>': '<h3 class="mega-col-title" onclick="window.location.href=\'design%20creative.html\'" style="cursor: pointer;" title="Go to Design &amp; Creatives">DESIGN &amp; CREATIVES</h3>',
    '<h3 class="mega-col-title">SEO SERVICES</h3>': '<h3 class="mega-col-title" onclick="window.location.href=\'SEO%20services.html\'" style="cursor: pointer;" title="Go to SEO Services">SEO SERVICES</h3>',
    '<h3 class="mega-col-title">DIGITAL MARKETING</h3>': '<h3 class="mega-col-title" onclick="window.location.href=\'digital-marketing.html\'" style="cursor: pointer;" title="Go to Digital Marketing">DIGITAL MARKETING</h3>'
}

for page in sub_pages:
    path = os.path.join(sub_folder, page)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        for k, v in sub_replacements.items():
            content = content.replace(k, v)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {page}")


# PART 2: Fix services.html cards
services_path = 'c:/Elevix Digital/services.html'
with open(services_path, 'r', encoding='utf-8') as f:
    text = f.read()

# First, let's remove the onclick I mistakenly put on the <h3>s earlier so it's clean
text = re.sub(r' cursor-pointer transition-colors hover:text-\[#E8282B\]" onclick="window\.location\.href=\'[^\']*\'"', '"', text)

# Now, let's add the onclick to the gs-service-card wrappers.
# We will match the gs-service-card div and the h3 inside it to figure out which card it is.

def replace_card(match):
    div_start = match.group(1)
    inner_content = match.group(2)
    h3_text = match.group(3).strip()
    
    url = ""
    if "Web Development" in h3_text: url = "services%20sub%20folder/web-development.html"
    elif "App Development" in h3_text: url = "services%20sub%20folder/app-development.html"
    elif "AI Automation" in h3_text: url = "services%20sub%20folder/ai-automation.html"
    elif "Design & Creatives" in h3_text or "Design &amp; Creatives" in h3_text: url = "services%20sub%20folder/design%20creative.html"
    elif "SEO Services" in h3_text: url = "services%20sub%20folder/SEO%20services.html"
    elif "Digital Marketing" in h3_text: url = "services%20sub%20folder/digital-marketing.html"
    
    if url:
        # Add cursor-pointer and onclick to the div
        new_div_start = div_start.replace('class="gs-service-card', f'onclick="window.location.href=\'{url}\'" style="cursor:pointer;" class="gs-service-card')
        return new_div_start + inner_content + match.group(0)[len(div_start + inner_content):]
    return match.group(0)

# Regex to find the div start, inner content until the h3 text
text = re.sub(r'(<div class="gs-service-card[^>]*>)(.*?<h3[^>]*>)(.*?)(</h3>)', replace_card, text, flags=re.DOTALL)

with open(services_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed services.html cards")
