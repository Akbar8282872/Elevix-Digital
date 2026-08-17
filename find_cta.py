import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find any text that looks like a CTA right before a footer.
# Often they have "READY TO", "ELEVATE", "SCALE", etc.
for match in re.finditer(r'<h1[^>]*>([\s\S]{1,200})</h1>', text):
    if "READY" in match.group(1).upper() or "ELEVATE" in match.group(1).upper() or "AUTOMATE" in match.group(1).upper():
        print("Found H1:", match.group(1).strip())

# Also let's print the actual start of the active footer to see what is above it
footer_idx = text.find('<footer id="footer"')
if footer_idx != -1:
    print("\n--- Content right before <footer id=\"footer\" ---")
    print(text[footer_idx-500:footer_idx])

