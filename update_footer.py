import re

# Read our-story.html to extract the correct footer
with open('c:/Elevix Digital/our-story.html', 'r', encoding='utf-8') as f:
    story_content = f.read()

# Extract the footer from our-story.html
footer_start_story = story_content.find("<!-- Footer -->")
if footer_start_story == -1:
    print("Could not find Footer in our-story.html")
    exit(1)

# Extract everything from <!-- Footer --> to the end of the file (or end of footer)
# Assuming it ends near the bottom of the body
footer_content = story_content[footer_start_story:]
# Remove closing tags if they are part of it, but usually footer is before scripts
# Let's just find </main> or </body> to stop
body_end = footer_content.find("</body>")
if body_end != -1:
    footer_content = footer_content[:body_end]

# Read careers.html
with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    careers_content = f.read()

# Find the footer in careers.html
# It might start with <!-- New Massive Grid Footer --> or <!-- Footer -->
footer_start_careers = careers_content.find("<!-- New Massive Grid Footer -->")
if footer_start_careers == -1:
    footer_start_careers = careers_content.find("<!-- Footer -->")

if footer_start_careers == -1:
    print("Could not find footer in careers.html")
    exit(1)

# Find where to end replacing in careers.html
body_end_careers = careers_content.find("</body>", footer_start_careers)
if body_end_careers == -1:
    print("Could not find </body> in careers.html")
    exit(1)

# Replace the old footer in careers.html with the new footer from our-story.html
new_careers_content = careers_content[:footer_start_careers] + footer_content + "\n" + careers_content[body_end_careers:]

with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(new_careers_content)

print("Successfully updated footer in careers.html to match our-story.html!")
