import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove the red top border
target_html = 'border-top:2px solid #E8282B;'
replacement_html = 'border-top:1px solid rgba(255,255,255,0.07);'
text = text.replace(target_html, replacement_html)

# 2. Make the list items more prominent
# We are targeting: font-size: 9.5px; color: rgba(255,255,255,0.45);
target_css = "font-size: 9.5px; color: rgba(255,255,255,0.45);"
replacement_css = "font-size: 11px; color: rgba(255,255,255,0.7);"
text = text.replace(target_css, replacement_css)

with open('c:/Elevix Digital/index.html', 'w', encoding='utf-8') as f2:
    f2.write(text)

print("Updated Mega Menu styles successfully!")
