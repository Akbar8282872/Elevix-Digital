import glob
import re

# This was the 3-column grid structure
new_grid = """<div style="display:grid; grid-template-columns:repeat(2, 1fr); gap: 40px 60px;">
                    <!-- COLUMN 1 -->
                    <div style="display: flex; flex-direction: column; gap: 40px;">
                        <div class="mega-col"><div class="mega-col-num">01 / 06</div><h3 class="mega-col-title">WEB DEVELOPMENT</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> NEXT.JS EXPERTS</li><li class="mega-col-item"><span class="mega-dash"></span> WORDPRESS SITES</li><li class="mega-col-item"><span class="mega-dash"></span> E-COMMERCE STORES</li><li class="mega-col-item"><span class="mega-dash"></span> HIGH-CONVERTING LANDING PAGES</li><li class="mega-col-item"><span class="mega-dash"></span> MAINTENANCE & SUPPORT</li></ul></div>
                        <div class="mega-col"><div class="mega-col-num">02 / 06</div><h3 class="mega-col-title">DESIGN & CREATIVES</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> BRANDING & IDENTITY</li><li class="mega-col-item"><span class="mega-dash"></span> GRAPHIC DESIGN</li><li class="mega-col-item"><span class="mega-dash"></span> MOTION GRAPHICS</li><li class="mega-col-item"><span class="mega-dash"></span> AI VIDEO PRODUCTION</li><li class="mega-col-item"><span class="mega-dash"></span> PRINT & PACKAGING</li></ul></div>
                        <div class="mega-col"><div class="mega-col-num">03 / 06</div><h3 class="mega-col-title">APP DEVELOPMENT</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> NATIVE IOS & ANDROID</li><li class="mega-col-item"><span class="mega-dash"></span> REACT NATIVE APPS</li><li class="mega-col-item"><span class="mega-dash"></span> FLUTTER DEVELOPMENT</li><li class="mega-col-item"><span class="mega-dash"></span> UI/UX APP DESIGN</li><li class="mega-col-item"><span class="mega-dash"></span> SCALABLE ARCHITECTURE</li></ul></div>
                    </div>
                    <!-- COLUMN 2 -->
                    <div style="display: flex; flex-direction: column; gap: 40px;">
                        <div class="mega-col"><div class="mega-col-num">04 / 06</div><h3 class="mega-col-title">SEO SERVICES</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> SEO STRATEGY & ROADMAP</li><li class="mega-col-item"><span class="mega-dash"></span> SEO AUDIT & GROWTH PLAN</li><li class="mega-col-item"><span class="mega-dash"></span> LOCAL SEO (GBP/GMB)</li><li class="mega-col-item"><span class="mega-dash"></span> TECHNICAL SEO</li><li class="mega-col-item"><span class="mega-dash"></span> LINK BUILDING & AUTHORITY</li></ul></div>
                        <div class="mega-col"><div class="mega-col-num">05 / 06</div><h3 class="mega-col-title">AI AUTOMATION</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> CUSTOM AI AGENTS</li><li class="mega-col-item"><span class="mega-dash"></span> WORKFLOW AUTOMATION</li><li class="mega-col-item"><span class="mega-dash"></span> CHATBOTS & VIRTUAL ASSISTANTS</li><li class="mega-col-item"><span class="mega-dash"></span> DATA EXTRACTION & ANALYSIS</li><li class="mega-col-item"><span class="mega-dash"></span> AI CRM INTEGRATION</li></ul></div>
                        <div class="mega-col"><div class="mega-col-num">06 / 06</div><h3 class="mega-col-title">DIGITAL MARKETING</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> PERFORMANCE MARKETING</li><li class="mega-col-item"><span class="mega-dash"></span> SOCIAL MEDIA MANAGEMENT</li><li class="mega-col-item"><span class="mega-dash"></span> EMAIL MARKETING</li><li class="mega-col-item"><span class="mega-dash"></span> CONVERSION RATE OPTIMIZATION</li><li class="mega-col-item"><span class="mega-dash"></span> MARKETING FUNNELS</li></ul></div>
                    </div>
                </div>"""

for f in glob.glob('c:/Elevix Digital/*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace the current grid: `<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap: 40px 60px;"> ... </div></div></div>` (which is hard to regex exactly)
    # Actually, we can just replace everything from `<div style="display:grid; grid-template-columns:repeat(3` up to the `<script>` tag.
    
    import re
    # We will use re.sub with DOTALL
    pattern = r'<div style="display:grid; grid-template-columns:repeat\(3, 1fr\).*?(?=\s*<script>)'
    
    new_content = re.sub(pattern, new_grid, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
    else:
        print(f"No match found in {f}")
