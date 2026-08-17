import re

with open('c:/Elevix Digital/contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the "Contact Us" navbar link
# We need to find the <a href="#" ...>Contact Us</a> and change it to <a href="contact.html" ...>Contact Us</a>
# Only in the nav section.
nav_contact_pattern = re.compile(r'<a href="#"([^>]*>Contact Us</a>)')
if nav_contact_pattern.search(content):
    content = nav_contact_pattern.sub(r'<a href="#" class="text-white text-[14px] font-medium transition-colors">Contact Us</a>', content)
    # Wait, the active page should have href="#" or href="contact.html", but typically it's white. 
    # Let's just do a simple replacement for the href.
    content = content.replace('<a href="#" class="text-on-secondary-container text-[14px] font-medium hover:text-white transition-colors">Contact Us</a>', '<a href="#" class="text-white text-[14px] font-bold transition-colors">Contact Us</a>')

# 2. Replace the background styling
old_bg_start = content.find("<!-- Grid/Box Container Background Styling (Matching Homepage) -->")
old_bg_end = content.find("</div>", old_bg_start) + 6

if old_bg_start != -1:
    new_bg = """<!-- Animated Background Mesh/Orb (exactly like Services) -->
        <div class="absolute inset-0 z-0 pointer-events-none">
            <!-- Pulsing Red Core -->
            <div class="absolute top-[10%] left-[20%] w-[600px] h-[600px] bg-kinetic-red rounded-full mix-blend-screen filter blur-[150px] opacity-20 animate-[pulse_4s_ease-in-out_infinite]"></div>
            <!-- Rotating Dark Core -->
            <div class="absolute bottom-[0%] right-[10%] w-[500px] h-[500px] bg-[#500000] rounded-full mix-blend-screen filter blur-[120px] opacity-30 animate-[spin_10s_linear_infinite]"></div>
            <!-- Grid overlay -->
            <div class="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)]" style="background-size: 50px 50px;"></div>
            <!-- Scanline -->
            <div class="absolute inset-0 bg-gradient-to-b from-transparent via-white/5 to-transparent h-[200%] animate-[scan_6s_linear_infinite]"></div>
        </div>"""
    
    content = content[:old_bg_start] + new_bg + content[old_bg_end:]

with open('c:/Elevix Digital/contact.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated contact.html background and navbar!")
