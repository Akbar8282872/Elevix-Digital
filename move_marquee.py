import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Find the marquee banner and extract it while removing it from its current location
start_idx = text.find('<!-- Top Marquee Banner -->')
if start_idx != -1:
    end_idx = text.find('<!--', start_idx + 10)
    
    # Check if we found the next comment, else just find the closing div
    if end_idx == -1:
        # Fallback to finding the closing div of the banner
        print("Fallback for end_idx")
        end_idx = start_idx + 2000 # Just a guess if we can't find it, but we should find '<!--'
        
    marquee_html = text[start_idx:end_idx]
    
    # Ensure it's the right block (just a sanity check)
    if 'AUTOMATING THE IMPOSSIBLE, DAILY' in marquee_html:
        # Delete it from its current location
        text = text[:start_idx] + text[end_idx:]
        print("Successfully removed marquee from its current location.")
        
        # 2. Find the end of the Hero Section to inject the marquee directly under it
        # The hero section starts with <section id="hero-section"
        hero_start = text.find('<section id="hero-section"')
        if hero_start != -1:
            # Find the closing tag of this section
            hero_end = text.find('</section>', hero_start)
            if hero_end != -1:
                hero_end += len('</section>')
                # Inject right after the hero section closes
                text = text[:hero_end] + "\n\n    " + marquee_html + "\n\n    " + text[hero_end:]
                
                with open('c:/Elevix Digital/index.html', 'w', encoding='utf-8') as f2:
                    f2.write(text)
                
                print("Successfully injected marquee right after the Hero Section.")
            else:
                print("Could not find the end of the Hero Section!")
        else:
            print("Could not find the Hero Section!")
    else:
        print("The block found doesn't seem to contain the marquee text!")
else:
    print("Could not find '<!-- Top Marquee Banner -->' in index.html")
