import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I saved the correct blocks in backup_marquee.html
with open('c:/Elevix Digital/backup_marquee.html', 'r', encoding='utf-8') as f:
    backup_html = f.read()

# backup_html contains BOTH '<!-- Top Marquee Banner -->' and '<!-- Trusted By Ticker -->'
# Let's split them just so we know what they are.
marquee_start = backup_html.find('<!-- Top Marquee Banner -->')
ticker_start = backup_html.find('<!-- Trusted By Ticker -->')

marquee_block = backup_html[marquee_start:ticker_start].strip()
ticker_block = backup_html[ticker_start:].strip()

# Now let's remove ALL existing instances of both from index.html!
# Since the exact HTML string might have slight differences in whitespace from writing/reading,
# we'll use a regex to aggressively strip them.

# 1. Remove Top Marquee Banner
text = re.sub(r'<!-- Top Marquee Banner -->[\s\S]*?</div>\s*</div>', '', text)

# 2. Remove Trusted By Ticker
text = re.sub(r'<!-- Trusted By Ticker -->[\s\S]*?</div>\s*</div>\s*</div>', '', text)

# 3. Just to be absolutely safe, let's also remove any rogue "AUTOMATING THE IMPOSSIBLE, DAILY" marquees
text = re.sub(r'<div[^>]*bg-kinetic-red[^>]*>[\s\S]*?AUTOMATING THE IMPOSSIBLE, DAILY[\s\S]*?</div>\s*</div>', '', text)

# Now inject ONE clean copy of both directly under the hero section!
hero_start = text.find('<section id="hero-section"')
hero_end = text.find('</section>', hero_start)
if hero_end != -1:
    hero_end += len('</section>')
    
    # Inject both blocks
    combined_blocks = f"\n\n    {marquee_block}\n\n    {ticker_block}\n\n"
    text = text[:hero_end] + combined_blocks + text[hero_end:]
    
    with open('c:/Elevix Digital/index.html', 'w', encoding='utf-8') as f2:
        f2.write(text)
    print("Successfully cleaned up duplicates and injected exactly ONE copy under the Hero section.")
else:
    print("Could not find the end of the hero section.")

