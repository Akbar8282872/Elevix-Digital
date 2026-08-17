import re

# 1. Grab the CTA section from careers.html
with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    careers_html = f.read()

cta_idx = careers_html.find('<!-- NEW CTA SECTION -->')
cta_end = careers_html.find('</section>', cta_idx) + 10
cta_block = careers_html[cta_idx:cta_end]

# 2. Inject it into index.html
with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# See if the CTA is already there to avoid duplicates
if "READY TO AUTOMATE THE IMPOSSIBLE?" in index_html:
    print("CTA already exists in index.html! Removing old one first.")
    # Actually, we didn't find it in the previous script, so it shouldn't exist.

# Find the footer
footer_idx = index_html.find('<footer id="footer"')
if footer_idx == -1:
    print("Error: Could not find footer in index.html")
else:
    # Inject right before the footer
    new_index = index_html[:footer_idx] + "\n\n" + cta_block + "\n\n    " + index_html[footer_idx:]
    with open('c:/Elevix Digital/index.html', 'w', encoding='utf-8') as f:
        f.write(new_index)
    print("Successfully injected CTA banner into index.html!")
