import glob

old_grid = """<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap: 40px 60px;">
                    <!-- COLUMN 1 -->
                    <div style="display: flex; flex-direction: column; gap: 40px;">
                        <div class="mega-col"><h3 class="mega-col-title">SEO Services</h3><p class="mega-col-desc">Strategy, audits, technical, AEO, GEO, links &mdash; the full ranking stack.</p><ul class="mega-col-list"><li><a href="#" class="mega-col-item">SEO Strategy &amp; Roadmap</a></li><li><a href="#" class="mega-col-item">SEO Audit &amp; Growth Plan</a></li><li><a href="#" class="mega-col-item">Local SEO (GBP/GMB)</a></li><li><a href="#" class="mega-col-item">Technical SEO</a></li><li><a href="#" class="mega-col-item">E-commerce SEO</a></li><li><a href="#" class="mega-col-item">AI Search Optimization</a></li><li><a href="#" class="mega-col-item">Link Building &amp; Authority</a></li></ul></div>
                        <div class="mega-col"><h3 class="mega-col-title">Design &amp; Creatives</h3><p class="mega-col-desc">Branding, graphic, motion, AI video, packaging.</p><ul class="mega-col-list"><li><a href="#" class="mega-col-item">Branding &amp; Identity</a></li><li><a href="#" class="mega-col-item">Graphic Design</a></li><li><a href="#" class="mega-col-item">Motion Graphics</a></li><li><a href="#" class="mega-col-item">AI Video Production</a></li><li><a href="#" class="mega-col-item">Print &amp; Packaging</a></li></ul></div>
                    </div>
                    <!-- COLUMN 2 -->
                    <div style="display: flex; flex-direction: column; gap: 40px;">
                        <div class="mega-col"><h3 class="mega-col-title">Digital Marketing <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline; margin-left:4px; opacity:0.7;"><path d="M7 17L17 7M17 7H7M17 7V17"/></svg></h3><p class="mega-col-desc">Performance, social, email, CRO, influencer, funnels, content.</p><ul class="mega-col-list"><li><a href="#" class="mega-col-item">Performance Marketing</a></li><li><a href="#" class="mega-col-item">Social Media Management</a></li><li><a href="#" class="mega-col-item">Email Marketing</a></li><li><a href="#" class="mega-col-item">Conversion Rate Optimization</a></li><li><a href="#" class="mega-col-item">Influencer Marketing</a></li><li><a href="#" class="mega-col-item">Marketing Funnels</a></li><li><a href="#" class="mega-col-item">Content Marketing</a></li></ul></div>
                        <div class="mega-col"><h3 class="mega-col-title">AI Automation</h3><p class="mega-col-desc">Voice agents, WhatsApp, chatbots, CRM, n8n workflows, strategy.</p><ul class="mega-col-list"><li><a href="#" class="mega-col-item">AI Voice Agents</a></li><li><a href="#" class="mega-col-item">WhatsApp Automation</a></li><li><a href="#" class="mega-col-item">AI Website Chatbots</a></li><li><a href="#" class="mega-col-item">CRM &amp; Lead Automation</a></li><li><a href="#" class="mega-col-item">Custom n8n Workflows</a></li></ul></div>
                    </div>
                    <!-- COLUMN 3 -->
                    <div style="display: flex; flex-direction: column; gap: 40px;">
                        <div class="mega-col"><h3 class="mega-col-title">Web Development</h3><p class="mega-col-desc">Next.js, WordPress, e-commerce, landing pages, maintenance.</p><ul class="mega-col-list"><li><a href="#" class="mega-col-item">Custom Web Development</a></li><li><a href="#" class="mega-col-item">WordPress Websites</a></li><li><a href="#" class="mega-col-item">E-commerce Websites</a></li><li><a href="#" class="mega-col-item">Landing Pages</a></li><li><a href="#" class="mega-col-item">Maintenance &amp; Support</a></li></ul></div>
                        <div class="mega-col"><h3 class="mega-col-title">App Development</h3><p class="mega-col-desc">Native iOS & Android apps, React Native cross-platform builds.</p><ul class="mega-col-list"><li><a href="#" class="mega-col-item">Native iOS & Android</a></li><li><a href="#" class="mega-col-item">React Native Apps</a></li><li><a href="#" class="mega-col-item">Flutter Development</a></li><li><a href="#" class="mega-col-item">UI/UX App Design</a></li><li><a href="#" class="mega-col-item">Scalable Architecture</a></li></ul></div>
                    </div>
                </div>"""

new_grid = """<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap: 40px 60px;">
                    <!-- COLUMN 1 -->
                    <div style="display: flex; flex-direction: column; gap: 40px;">
                        <div class="mega-col"><h3 class="mega-col-title">Web Development</h3><ul class="mega-col-list"><li><a href="#" class="mega-col-item">Next.js Development</a></li><li><a href="#" class="mega-col-item">WordPress Websites</a></li><li><a href="#" class="mega-col-item">E-commerce Websites</a></li><li><a href="#" class="mega-col-item">Landing Pages</a></li><li><a href="#" class="mega-col-item">Maintenance &amp; Support</a></li></ul></div>
                        <div class="mega-col"><h3 class="mega-col-title">Design &amp; Creatives</h3><ul class="mega-col-list"><li><a href="#" class="mega-col-item">Branding &amp; Identity</a></li><li><a href="#" class="mega-col-item">Graphic Design</a></li><li><a href="#" class="mega-col-item">Motion Graphics</a></li><li><a href="#" class="mega-col-item">AI Video Production</a></li><li><a href="#" class="mega-col-item">Print &amp; Packaging</a></li></ul></div>
                    </div>
                    <!-- COLUMN 2 -->
                    <div style="display: flex; flex-direction: column; gap: 40px;">
                        <div class="mega-col"><h3 class="mega-col-title">App Development</h3><ul class="mega-col-list"><li><a href="#" class="mega-col-item">Native iOS &amp; Android</a></li><li><a href="#" class="mega-col-item">React Native Apps</a></li><li><a href="#" class="mega-col-item">Flutter Development</a></li><li><a href="#" class="mega-col-item">UI/UX App Design</a></li><li><a href="#" class="mega-col-item">Scalable Architecture</a></li></ul></div>
                        <div class="mega-col"><h3 class="mega-col-title">SEO Services</h3><ul class="mega-col-list"><li><a href="#" class="mega-col-item">SEO Strategy &amp; Roadmap</a></li><li><a href="#" class="mega-col-item">SEO Audit &amp; Growth Plan</a></li><li><a href="#" class="mega-col-item">Local SEO</a></li><li><a href="#" class="mega-col-item">Technical SEO</a></li><li><a href="#" class="mega-col-item">AI Search Optimization</a></li></ul></div>
                    </div>
                    <!-- COLUMN 3 -->
                    <div style="display: flex; flex-direction: column; gap: 40px;">
                        <div class="mega-col"><h3 class="mega-col-title">AI Automation</h3><ul class="mega-col-list"><li><a href="#" class="mega-col-item">AI Voice Agents</a></li><li><a href="#" class="mega-col-item">WhatsApp Automation</a></li><li><a href="#" class="mega-col-item">AI Website Chatbots</a></li><li><a href="#" class="mega-col-item">CRM &amp; Lead Automation</a></li><li><a href="#" class="mega-col-item">Custom n8n Workflows</a></li></ul></div>
                        <div class="mega-col"><h3 class="mega-col-title">Digital Marketing</h3><ul class="mega-col-list"><li><a href="#" class="mega-col-item">Performance Marketing</a></li><li><a href="#" class="mega-col-item">Social Media Management</a></li><li><a href="#" class="mega-col-item">Email Marketing</a></li><li><a href="#" class="mega-col-item">Conversion Rate Optimization</a></li><li><a href="#" class="mega-col-item">Marketing Funnels</a></li></ul></div>
                    </div>
                </div>"""

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_grid in content:
        content = content.replace(old_grid, new_grid)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
