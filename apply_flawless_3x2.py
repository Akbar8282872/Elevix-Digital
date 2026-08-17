import glob
import re

clean_mega_menu_3x2 = """<div id="services-mega-panel" style="display:none; position:fixed; top:104px; left:0; right:0; z-index:9999;">
        <div style="background:rgba(8,8,8,0.98); backdrop-filter:blur(24px); -webkit-backdrop-filter:blur(24px); border-bottom:1px solid rgba(255,255,255,0.07); box-shadow:0 20px 60px rgba(0,0,0,0.85);">
            <div style="padding:12px 48px; border-bottom:1px solid rgba(255,255,255,0.06); display:flex; align-items:center; gap:12px;">
                <span style="width:6px;height:6px;border-radius:50%;background:#E8282B;display:inline-block;box-shadow:0 0 8px rgba(232,40,43,0.7);"></span>
                <span style="font-family:'Space Mono',monospace;font-size:9px;color:#E8282B;text-transform:uppercase;letter-spacing:0.28em;font-weight:700;">SERVICES / 6 PILLARS / 36 CAPABILITIES</span>
                <a href="services.html" style="margin-left:auto;font-family:'Space Mono',monospace;font-size:9px;color:rgba(255,255,255,0.35);text-transform:uppercase;letter-spacing:0.15em;text-decoration:none;transition:color 0.2s;" onmouseover="this.style.color='#E8282B'" onmouseout="this.style.color='rgba(255,255,255,0.35)'">VIEW ALL &#8599;</a>
            </div>
            <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap: 40px 60px; padding: 24px 48px 48px 48px;">
                <div class="mega-col"><div class="mega-col-num">01 / 06</div><h3 class="mega-col-title">WEB DEVELOPMENT</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> NEXT.JS DEVELOPMENT</li><li class="mega-col-item"><span class="mega-dash"></span> WORDPRESS WEBSITES</li><li class="mega-col-item"><span class="mega-dash"></span> E-COMMERCE WEBSITES</li><li class="mega-col-item"><span class="mega-dash"></span> LANDING PAGES</li><li class="mega-col-item"><span class="mega-dash"></span> MAINTENANCE &amp; SUPPORT</li></ul></div>
                <div class="mega-col"><div class="mega-col-num">02 / 06</div><h3 class="mega-col-title">APP DEVELOPMENT</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> NATIVE IOS &amp; ANDROID</li><li class="mega-col-item"><span class="mega-dash"></span> REACT NATIVE APPS</li><li class="mega-col-item"><span class="mega-dash"></span> FLUTTER DEVELOPMENT</li><li class="mega-col-item"><span class="mega-dash"></span> UI/UX APP DESIGN</li><li class="mega-col-item"><span class="mega-dash"></span> SCALABLE ARCHITECTURE</li></ul></div>
                <div class="mega-col"><div class="mega-col-num">03 / 06</div><h3 class="mega-col-title">AI AUTOMATION</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> AI VOICE AGENTS</li><li class="mega-col-item"><span class="mega-dash"></span> WHATSAPP AUTOMATION</li><li class="mega-col-item"><span class="mega-dash"></span> AI WEBSITE CHATBOTS</li><li class="mega-col-item"><span class="mega-dash"></span> CRM &amp; LEAD AUTOMATION</li><li class="mega-col-item"><span class="mega-dash"></span> CUSTOM N8N WORKFLOWS</li></ul></div>
                <div class="mega-col"><div class="mega-col-num">04 / 06</div><h3 class="mega-col-title">DESIGN &amp; CREATIVES</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> BRANDING &amp; IDENTITY</li><li class="mega-col-item"><span class="mega-dash"></span> GRAPHIC DESIGN</li><li class="mega-col-item"><span class="mega-dash"></span> MOTION GRAPHICS</li><li class="mega-col-item"><span class="mega-dash"></span> AI VIDEO PRODUCTION</li><li class="mega-col-item"><span class="mega-dash"></span> PRINT &amp; PACKAGING</li></ul></div>
                <div class="mega-col"><div class="mega-col-num">05 / 06</div><h3 class="mega-col-title">SEO SERVICES</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> SEO STRATEGY &amp; ROADMAP</li><li class="mega-col-item"><span class="mega-dash"></span> SEO AUDIT &amp; GROWTH PLAN</li><li class="mega-col-item"><span class="mega-dash"></span> LOCAL SEO</li><li class="mega-col-item"><span class="mega-dash"></span> TECHNICAL SEO</li><li class="mega-col-item"><span class="mega-dash"></span> AI SEARCH OPTIMIZATION</li></ul></div>
                <div class="mega-col"><div class="mega-col-num">06 / 06</div><h3 class="mega-col-title">DIGITAL MARKETING</h3><ul class="mega-col-list"><li class="mega-col-item"><span class="mega-dash"></span> PERFORMANCE MARKETING</li><li class="mega-col-item"><span class="mega-dash"></span> SOCIAL MEDIA MANAGEMENT</li><li class="mega-col-item"><span class="mega-dash"></span> EMAIL MARKETING</li><li class="mega-col-item"><span class="mega-dash"></span> CONVERSION RATE OPTIMIZATION</li><li class="mega-col-item"><span class="mega-dash"></span> MARKETING FUNNELS</li></ul></div>
            </div>
        </div>
    </div>
"""

for file_path in glob.glob('c:/Elevix Digital/*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # We replace from <div id="services-mega-panel" all the way down to just before <script> (function() { var trigger = document.getElementById('services-trigger-btn');
    match = re.search(r'(<div id="services-mega-panel".*?)\s*(?:<!--.*?-->)?\s*<script>\s*\(function\(\)', file_content, re.DOTALL)
    
    if match:
        new_file_content = file_content.replace(match.group(1), clean_mega_menu_3x2)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_file_content)
        print(f"Fixed {file_path}")
    else:
        print(f"Pattern not found in {file_path}")

print("Done perfectly fixing mega menu layout to 3x2.")
