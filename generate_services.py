import os
import re

# Paths
root_dir = 'c:/Elevix Digital'
sub_dir = os.path.join(root_dir, 'services sub folder')
index_path = os.path.join(root_dir, 'index.html')

# Create sub directory
os.makedirs(sub_dir, exist_ok=True)

# Read index.html to extract head, nav, and footer
with open(index_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Extract Head and Nav
# We know the hero section starts right after the nav closes
hero_start = text.find('<section id="hero-section"')
if hero_start == -1:
    hero_start = text.find('<main')
head_and_nav = text[:hero_start]

# Extract Footer
footer_start = text.rfind('<footer')
footer = text[footer_start:]

# Function to adjust relative links
def adjust_links(html_content):
    # Adjust href attributes
    html_content = re.sub(r'href="([^"#]*(?:\.css|\.html))"', r'href="../\1"', html_content)
    # Don't double adjust if they already had ../ (though they shouldn't here)
    html_content = html_content.replace('../../', '../')
    
    # Adjust src attributes
    html_content = re.sub(r'src="([^"]*)"', r'src="../\1"', html_content)
    # Don't accidentally adjust http(s) links or data URIs
    html_content = html_content.replace('src="../http', 'src="http')
    html_content = html_content.replace('src="../data:', 'src="data:')
    
    return html_content

# Prepare content blocks
head_nav_adjusted = adjust_links(head_and_nav)
footer_adjusted = adjust_links(footer)

# Also ensure standard html pages link back to root properly (like index.html -> ../index.html)
# The regex above handles most href="..." but let's make sure our-story.html, case-studies.html etc are caught.

files_to_create = [
    'web-development.html',
    'app-development.html',
    'ai-automation.html',
    'design creative.html',
    'SEO services.html',
    'digital-marketing.html'
]

# Create the empty page template
page_template = f"""{head_nav_adjusted}
    <main class="min-h-screen pt-32 pb-24 px-6 bg-[#0a0a0a] flex items-center justify-center">
        <!-- Main content will go here later -->
        <h1 class="text-white font-display text-4xl">Service Content Coming Soon</h1>
    </main>

{footer_adjusted}"""

for filename in files_to_create:
    filepath = os.path.join(sub_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(page_template)
    print(f"Created: {filename}")

print("All 6 sub-pages created successfully.")
