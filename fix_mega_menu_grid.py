import glob
import os

new_menu = """            <div style="display:grid; grid-template-columns:repeat(2, 1fr); gap: 40px 60px;">
                <!-- Left 50% -->
                <div style="display: flex; flex-direction: column; gap: 40px;">
                    <div class="mega-col"><div class="mega-col-num">01 / 06</div><h3 class="mega-col-title">WEB DEVELOPMENT</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> NEXT.JS DEVELOPMENT</li><li class="mega-col-item"><span class="mega-dash"></span> WORDPRESS WEBSITES</li><li class="mega-col-item"><span class="mega-dash"></span> E-COMMERCE WEBSITES</li><li class="mega-col-item"><span class="mega-dash"></span> LANDING PAGES</li><li class="mega-col-item"><span class="mega-dash"></span> MAINTENANCE &amp; SUPPORT</li></ul></div>
                    <div class="mega-col"><div class="mega-col-num">02 / 06</div><h3 class="mega-col-title">APP DEVELOPMENT</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> NATIVE IOS &amp; ANDROID</li><li class="mega-col-item"><span class="mega-dash"></span> REACT NATIVE APPS</li><li class="mega-col-item"><span class="mega-dash"></span> FLUTTER DEVELOPMENT</li><li class="mega-col-item"><span class="mega-dash"></span> UI/UX APP DESIGN</li><li class="mega-col-item"><span class="mega-dash"></span> SCALABLE ARCHITECTURE</li></ul></div>
                    <div class="mega-col"><div class="mega-col-num">03 / 06</div><h3 class="mega-col-title">AI AUTOMATION</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> AI VOICE AGENTS</li><li class="mega-col-item"><span class="mega-dash"></span> WHATSAPP AUTOMATION</li><li class="mega-col-item"><span class="mega-dash"></span> AI WEBSITE CHATBOTS</li><li class="mega-col-item"><span class="mega-dash"></span> CRM &amp; LEAD AUTOMATION</li><li class="mega-col-item"><span class="mega-dash"></span> CUSTOM N8N WORKFLOWS</li></ul></div>
                </div>
                <!-- Right 50% -->
                <div style="display: flex; flex-direction: column; gap: 40px;">
                    <div class="mega-col"><div class="mega-col-num">04 / 06</div><h3 class="mega-col-title">DESIGN &amp; CREATIVES</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> BRANDING &amp; IDENTITY</li><li class="mega-col-item"><span class="mega-dash"></span> GRAPHIC DESIGN</li><li class="mega-col-item"><span class="mega-dash"></span> MOTION GRAPHICS</li><li class="mega-col-item"><span class="mega-dash"></span> AI VIDEO PRODUCTION</li><li class="mega-col-item"><span class="mega-dash"></span> PRINT &amp; PACKAGING</li></ul></div>
                    <div class="mega-col"><div class="mega-col-num">05 / 06</div><h3 class="mega-col-title">SEO SERVICES</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> SEO STRATEGY &amp; ROADMAP</li><li class="mega-col-item"><span class="mega-dash"></span> SEO AUDIT &amp; GROWTH PLAN</li><li class="mega-col-item"><span class="mega-dash"></span> LOCAL SEO</li><li class="mega-col-item"><span class="mega-dash"></span> TECHNICAL SEO</li><li class="mega-col-item"><span class="mega-dash"></span> AI SEARCH OPTIMIZATION</li></ul></div>
                    <div class="mega-col"><div class="mega-col-num">06 / 06</div><h3 class="mega-col-title">DIGITAL MARKETING</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> PERFORMANCE MARKETING</li><li class="mega-col-item"><span class="mega-dash"></span> SOCIAL MEDIA MANAGEMENT</li><li class="mega-col-item"><span class="mega-dash"></span> EMAIL MARKETING</li><li class="mega-col-item"><span class="mega-dash"></span> CONVERSION RATE OPTIMIZATION</li><li class="mega-col-item"><span class="mega-dash"></span> MARKETING FUNNELS</li></ul></div>
                </div>
            </div>"""

for f in glob.glob('c:/Elevix Digital/*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    start_idx = -1
    end_idx = -1
    for i, line in enumerate(lines):
        if '<div style="display:grid; grid-template-columns:repeat(3,1fr);">' in line:
            start_idx = i
        if start_idx != -1 and '</div>' in line and i > start_idx + 6:
            # wait, it's safer to just replace lines start_idx to start_idx + 7
            end_idx = start_idx + 7
            break
            
    if start_idx != -1:
        new_lines = lines[:start_idx] + [new_menu + '\n'] + lines[end_idx+1:]
        with open(f, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)
        print(f"Updated {f}")
    else:
        print(f"Not found in {f}")
