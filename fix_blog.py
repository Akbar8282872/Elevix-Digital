import re

# 1. Generate Proof, not promises section
proof_html = '''
<!-- PROOF SECTION -->
<section class="py-24 px-6 bg-[#050505] border-t border-white/5 relative z-10 overflow-hidden">
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,rgba(232,40,43,0.03)_0%,transparent_70%)] pointer-events-none"></div>
    <div class="max-w-7xl mx-auto w-full relative z-10">
        <div class="mb-16">
            <div class="flex items-center gap-2 inline-block py-1 px-3 border border-white/10 rounded-full bg-white/5 mb-6 w-max">
                <div class="w-2 h-2 rounded-full bg-kinetic-red"></div>
                <span class="font-mono text-stark-white text-[10px] font-bold tracking-[0.2em] uppercase">
                    Proof, not promises
                </span>
            </div>
            <h2 class="font-display text-4xl md:text-5xl lg:text-6xl font-black text-white tracking-tighter leading-[1.1] max-w-3xl">
                Results that speak for themselves.
            </h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            
            <div class="bg-[#111]/80 backdrop-blur-xl border border-white/10 rounded-2xl p-8 hover:border-kinetic-red/30 transition-colors duration-500 group relative overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-br from-kinetic-red/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="mb-8 flex justify-between items-start relative z-10">
                    <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] uppercase font-bold">SOFTWARE COMPANIES</span>
                </div>
                <div class="mb-8 relative z-10">
                    <div class="font-display text-5xl font-black text-white mb-2 tracking-tighter">63 Lakh<span class="text-kinetic-red text-3xl">PKR</span></div>
                    <div class="text-on-secondary-container font-mono text-xs uppercase tracking-wider">Generated in 1 Year</div>
                </div>
                <p class="text-sm text-neutral-400 font-display leading-relaxed relative z-10">
                    Scaled their pipeline and automated their backend infrastructure, resulting in massive yearly growth in the Pakistani tech sector.
                </p>
            </div>

            <div class="bg-[#111]/80 backdrop-blur-xl border border-white/10 rounded-2xl p-8 hover:border-kinetic-red/30 transition-colors duration-500 group relative overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-br from-kinetic-red/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="mb-8 flex justify-between items-start relative z-10">
                    <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] uppercase font-bold">ECOMMERCE AUTOMATION</span>
                </div>
                <div class="mb-8 relative z-10">
                    <div class="font-display text-5xl font-black text-white mb-2 tracking-tighter">300<span class="text-kinetic-red text-3xl">%</span></div>
                    <div class="text-on-secondary-container font-mono text-xs uppercase tracking-wider">Increase in efficiency</div>
                </div>
                <p class="text-sm text-neutral-400 font-display leading-relaxed relative z-10">
                    Replaced manual data entry with custom AI workflows, freeing up 40+ hours a week for the operations team.
                </p>
            </div>

            <div class="bg-[#111]/80 backdrop-blur-xl border border-white/10 rounded-2xl p-8 hover:border-kinetic-red/30 transition-colors duration-500 group relative overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-br from-kinetic-red/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="mb-8 flex justify-between items-start relative z-10">
                    <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] uppercase font-bold">B2B LEAD GEN</span>
                </div>
                <div class="mb-8 relative z-10">
                    <div class="font-display text-5xl font-black text-white mb-2 tracking-tighter">45<span class="text-kinetic-red text-3xl">+</span></div>
                    <div class="text-on-secondary-container font-mono text-xs uppercase tracking-wider">Qualified appointments</div>
                </div>
                <p class="text-sm text-neutral-400 font-display leading-relaxed relative z-10">
                    Built a hyper-personalized outreach system that booked more sales calls in 30 days than the previous two quarters combined.
                </p>
            </div>

        </div>
    </div>
</section>
'''

# 2. Extract CTA from our-story.html
with open('c:/Elevix Digital/our-story.html', 'r', encoding='utf-8') as f:
    story_text = f.read()
story_sections = list(re.finditer(r'<section[^>]*>(.*?)</section>', story_text, re.DOTALL | re.IGNORECASE))
cta_html = story_sections[-1].group(0)

# 3. Extract Banner and Footer from index.html
with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    index_text = f.read()
index_sections = list(re.finditer(r'<section[^>]*>(.*?)</section>', index_text, re.DOTALL | re.IGNORECASE))
banner_html = index_sections[-2].group(0)

footer_idx = index_text.find('<footer')
footer_end = index_text.find('</footer>', footer_idx) + 9
footer_html = index_text[footer_idx:footer_end]

# 4. Inject into blog.html
with open('c:/Elevix Digital/blog.html', 'r', encoding='utf-8') as f:
    blog_text = f.read()

chat_btn_idx = blog_text.find('<!-- Floating Chat Button -->')
if chat_btn_idx == -1:
    chat_btn_idx = blog_text.find('</body>')

injection = f'\n{proof_html}\n{cta_html}\n{banner_html}\n{footer_html}\n\n    '
new_blog_text = blog_text[:chat_btn_idx] + injection + blog_text[chat_btn_idx:]

with open('c:/Elevix Digital/blog.html', 'w', encoding='utf-8') as f:
    f.write(new_blog_text)

print('Success! Added Proof, CTA, Banner, and Footer to blog.html')
