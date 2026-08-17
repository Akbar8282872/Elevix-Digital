import re

with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the remainder of the partner logos ticker
arb_idx = text.lower().find('arbisoft')
if arb_idx != -1:
    ticker_start = text.rfind('<div', 0, text.rfind('<div', 0, text.rfind('<div', 0, arb_idx))) # go back a few divs
    # Actually, we know the next section is "<!-- Results / Case Studies Section -->"
    results_idx = text.find('<!-- Results / Case Studies Section -->', arb_idx)
    
    # We can just use regex to remove everything from where we failed to cut down to the Results comment.
    # We'll just look for a comment before the remaining logos
    comment_idx = text.rfind('<!--', 0, arb_idx)
    if comment_idx != -1 and results_idx != -1:
        text = text[:comment_idx] + text[results_idx:]
    else:
        # If no comment before it, just remove from <div class="w-full"
        div_start = text.rfind('<div class="w-full', 0, arb_idx)
        if div_start != -1 and results_idx != -1:
             text = text[:div_start] + text[results_idx:]

with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Arbisoft section removed cleanly.")
