import json

with open(r'c:\Elevix Digital\our-story.html', 'r', encoding='utf-8') as f:
    our_story = f.read()

start_marker = '<!-- Huge CTA Banner -->'
end_marker = '</body>'
start_idx = our_story.find(start_marker)
end_idx = our_story.find(end_marker, start_idx)
cta_and_footer = our_story[start_idx:end_idx]

# Fix relative paths since web-development.html is in 'services sub folder'
cta_and_footer = cta_and_footer.replace('src="services.js"', 'src="../services.js"')
cta_and_footer = cta_and_footer.replace('href="careers.html"', 'href="../careers.html"')
cta_and_footer = cta_and_footer.replace('href="blog.html"', 'href="../blog.html"')
cta_and_footer = cta_and_footer.replace('href="our-story.html"', 'href="../our-story.html"')
cta_and_footer = cta_and_footer.replace('href="case-studies.html"', 'href="../case-studies.html"')

with open(r'c:\Elevix Digital\services sub folder\web-development.html', 'r', encoding='utf-8') as f:
    web_dev = f.read()

rep_start = web_dev.find('<!-- FOOTER RESTORED FROM SERVICES.HTML -->')
rep_end = web_dev.find('</body>', rep_start)

# Replace the old footer with the new CTA + Footer block
new_web_dev = web_dev[:rep_start] + cta_and_footer + '\n    ' + web_dev[rep_end:]

with open(r'c:\Elevix Digital\services sub folder\web-development.html', 'w', encoding='utf-8') as f:
    f.write(new_web_dev)

print("Replacement complete.")
