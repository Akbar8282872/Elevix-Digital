import re

# 1. Prepare the exact background from services.html
with open('c:/Elevix Digital/services.html', 'r', encoding='utf-8') as f:
    services_text = f.read()

bg_start = services_text.find('<!-- Animated Background Mesh/Orb')
bg_end = services_text.find('</div>\n        </div>', bg_start)
if bg_end != -1:
    bg_content = services_text[bg_start:bg_end + 14]
else:
    # fallback if needed
    bg_content = '''<!-- Animated Background Mesh/Orb -->
        <div class="absolute inset-0 z-0 pointer-events-none">
            <!-- Pulsing Red Core -->
            <div class="absolute top-[10%] left-[20%] w-[600px] h-[600px] bg-kinetic-red rounded-full mix-blend-screen filter blur-[150px] opacity-20 animate-[pulse_4s_ease-in-out_infinite]"></div>
            <!-- Rotating Dark Core -->
            <div class="absolute bottom-[0%] right-[10%] w-[500px] h-[500px] bg-[#500000] rounded-full mix-blend-screen filter blur-[120px] opacity-30 animate-[spin_10s_linear_infinite]"></div>
            <!-- Grid overlay -->
            <div class="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)]" style="background-size: 50px 50px;"></div>
            <!-- Scanline -->
            <div class="absolute inset-0 bg-gradient-to-b from-transparent via-white/5 to-transparent h-[200%] animate-[scan_6s_linear_infinite]"></div>
        </div>'''

# 2. Prepare the new Why Us section
why_us_html = '''
    <!-- Why Us Section -->
    <section class="relative bg-[#050505] border-t border-white/5 py-24 px-6 md:px-12 lg:px-24 overflow-hidden">
        <div class="absolute right-0 top-0 w-[500px] h-[500px] bg-kinetic-red/5 blur-[120px] rounded-full pointer-events-none"></div>
        <div class="max-w-7xl mx-auto relative z-10">
            <!-- Section Header -->
            <div class="flex items-center gap-3 mb-6">
                <span class="w-8 h-[1px] bg-kinetic-red"></span>
                <span class="font-mono text-[10px] md:text-[12px] text-kinetic-red tracking-[0.2em] uppercase font-bold">// 01. WHY US</span>
            </div>
            
            <h2 class="font-display text-[40px] md:text-[56px] lg:text-[72px] font-bold text-white uppercase leading-[1.1] tracking-[-0.02em] mb-20 max-w-4xl">
                Why engineers, designers, and ops leads stay.
            </h2>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Card 1 -->
                <div class="bg-[#0e0e0e] border border-white/5 rounded-2xl p-8 md:p-10 hover:border-kinetic-red/30 transition-colors duration-300">
                    <span class="font-mono text-[10px] md:text-[12px] text-kinetic-red tracking-[0.2em] uppercase font-bold block mb-8">// 01</span>
                    <h3 class="font-display text-[24px] md:text-[28px] font-bold text-white mb-4">Culture before skill</h3>
                    <p class="text-[#a1a1aa] text-[15px] md:text-[16px] leading-relaxed">
                        We hire the human first. Skill we can level up in a quarter &mdash; integrity, curiosity, and ownership we can't teach. The room matters more than the r&eacute;sum&eacute;.
                    </p>
                </div>

                <!-- Card 2 -->
                <div class="bg-[#0e0e0e] border border-white/5 rounded-2xl p-8 md:p-10 hover:border-kinetic-red/30 transition-colors duration-300">
                    <span class="font-mono text-[10px] md:text-[12px] text-kinetic-red tracking-[0.2em] uppercase font-bold block mb-8">// 02</span>
                    <h3 class="font-display text-[24px] md:text-[28px] font-bold text-white mb-4">Systems over hustle</h3>
                    <p class="text-[#a1a1aa] text-[15px] md:text-[16px] leading-relaxed">
                        We don't reward late nights. We reward engineers, designers, and operators who build the checklist that makes the late night unnecessary next sprint.
                    </p>
                </div>

                <!-- Card 3 -->
                <div class="bg-[#0e0e0e] border border-white/5 rounded-2xl p-8 md:p-10 hover:border-kinetic-red/30 transition-colors duration-300">
                    <span class="font-mono text-[10px] md:text-[12px] text-kinetic-red tracking-[0.2em] uppercase font-bold block mb-8">// 03</span>
                    <h3 class="font-display text-[24px] md:text-[28px] font-bold text-white mb-4">Radical ownership</h3>
                    <p class="text-[#a1a1aa] text-[15px] md:text-[16px] leading-relaxed">
                        Every teammate owns a craft end-to-end and ships directly to the client &mdash; no agency layers, no hand-offs, no hiding behind a project manager.
                    </p>
                </div>
            </div>
        </div>
    </section>
'''

with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 3. Replace background in hero section
# We need to find the hero section and replace everything inside it up to <div class="relative z-10 text-center">
# Note: The hero section is: <section id="hero-section" class="...bg-[#0a0a0a] z-10">
hero_start = text.find('<section id="hero-section"')
if hero_start != -1:
    content_start = text.find('<div class="relative z-10', hero_start)
    if content_start != -1:
        # We replace the area between hero_start closing bracket and content_start
        hero_tag_end = text.find('>', hero_start) + 1
        old_bg = text[hero_tag_end:content_start]
        text = text[:hero_tag_end] + "\n        " + bg_content + "\n        " + text[content_start:]

# 4. Remove "Join Our Elite Team" if they didn't want it, and replace with a generic text
# But wait, what if they don't want me to change the text? They just said "elite heading these r not my topic... chk ur memory add by real hero pg of career". 
# I will change it to the overarching theme of Elevix from design.md.
text = re.sub(r'Join Our Elite Team', r'High-Velocity Engineering', text, flags=re.IGNORECASE)

# 5. Insert Why Us section above the Roles grid
# The Roles grid starts with `<section id="roles"` or `<section class="... pt-32 pb-24"` containing "13 roles, always open."
roles_idx = text.find('13 roles, always open.')
if roles_idx != -1:
    roles_section_start = text.rfind('<section', 0, roles_idx)
    if roles_section_start != -1:
        text = text[:roles_section_start] + why_us_html + "\n    " + text[roles_section_start:]

with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done inserting new career sections.")
