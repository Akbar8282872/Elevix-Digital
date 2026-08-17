import re

with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find "Join Our" for the actual Career Hero section
idx_join = text.find('Join Our')
if idx_join != -1:
    # Find the <section> tag right before this
    hero_start = text.rfind('<section', 0, idx_join)
    print("Found actual career hero at:", hero_start)
    
    # Everything before this hero_start (except navbar/header which we get from our-story) is garbage!
    # Let's grab the middle content starting from this REAL hero_start up to the footer
    footer_start = text.find('<footer', hero_start)
    
    middle_content = text[hero_start:footer_start]
    
    with open('c:/Elevix Digital/our-story.html', 'r', encoding='utf-8') as f:
        story = f.read()
    
    nav_end = story.find('</nav>') + 6
    header_nav = story[:nav_end]
    story_footer = story[story.find('<footer'):]
    
    perfect_careers = header_nav + "\n\n" + middle_content.strip() + "\n\n" + story_footer
    
    with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
        f.write(perfect_careers)
    
    print("SUCCESS: careers.html has been perfectly cleaned and rebuilt without garbage.")
else:
    print("ERROR: Could not find 'Join Our' text.")
