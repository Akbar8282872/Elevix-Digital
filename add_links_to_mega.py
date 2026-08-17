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

replacements = {
    '<h3 class="mega-col-title">WEB DEVELOPMENT</h3>': '<h3 class="mega-col-title" onclick="window.location.href=\'services sub folder/web-development.html\'" style="cursor: pointer;" title="Go to Web Development">WEB DEVELOPMENT</h3>',
    '<h3 class="mega-col-title">APP DEVELOPMENT</h3>': '<h3 class="mega-col-title" onclick="window.location.href=\'services sub folder/app-development.html\'" style="cursor: pointer;" title="Go to App Development">APP DEVELOPMENT</h3>',
    '<h3 class="mega-col-title">AI AUTOMATION</h3>': '<h3 class="mega-col-title" onclick="window.location.href=\'services sub folder/ai-automation.html\'" style="cursor: pointer;" title="Go to AI Automation">AI AUTOMATION</h3>',
    '<h3 class="mega-col-title">DESIGN &amp; CREATIVES</h3>': '<h3 class="mega-col-title" onclick="window.location.href=\'services sub folder/design creative.html\'" style="cursor: pointer;" title="Go to Design &amp; Creatives">DESIGN &amp; CREATIVES</h3>',
    '<h3 class="mega-col-title">SEO SERVICES</h3>': '<h3 class="mega-col-title" onclick="window.location.href=\'services sub folder/SEO services.html\'" style="cursor: pointer;" title="Go to SEO Services">SEO SERVICES</h3>',
    '<h3 class="mega-col-title">DIGITAL MARKETING</h3>': '<h3 class="mega-col-title" onclick="window.location.href=\'services sub folder/digital-marketing.html\'" style="cursor: pointer;" title="Go to Digital Marketing">DIGITAL MARKETING</h3>'
}

for file in html_files:
    path = f'c:/Elevix Digital/{file}'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        for k, v in replacements.items():
            content = content.replace(k, v)
            
        if content != original_content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated {file}')
        else:
            print(f'No changes needed for {file} (or titles not found)')
