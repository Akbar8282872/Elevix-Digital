import os

files = ['index.html', 'our-story.html', 'services.html', 'case-studies.html']
for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace href="#results" with href="case-studies.html" where it says "Case Studies"
        # Since the nav is identical, we can just replace exactly that href in the nav context.
        # But wait, maybe the user wants it to link to case-studies.html.
        content = content.replace('<a href="#results" class="text-on-secondary-container text-[14px] font-medium hover:text-white transition-colors">Case Studies</a>',
                                  '<a href="case-studies.html" class="text-on-secondary-container text-[14px] font-medium hover:text-white transition-colors">Case Studies</a>')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
