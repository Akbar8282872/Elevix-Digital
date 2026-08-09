import re

def update_case_studies():
    with open('case-studies.html', 'r', encoding='utf-8') as f:
        html = f.read()

    with open('our-story.html', 'r', encoding='utf-8') as f:
        our_story = f.read()

    # 1. Replace PORTFOLIO METRICS SECTION
    metrics_old_pattern = r'<!-- PORTFOLIO METRICS SECTION -->.*?</section>'
    metrics_new = """<!-- PORTFOLIO METRICS SECTION (SCREENSHOT 1) -->
    <section class="w-full bg-[#0a0a0a] border-t border-kinetic-red border-b border-white/5 relative z-10">
        <div class="max-w-[1400px] mx-auto">
            <!-- Top Bar -->
            <div class="flex justify-between items-center py-4 px-8 border-b border-white/5 text-[10px] font-mono tracking-[0.2em] uppercase">
                <div class="flex items-center gap-3 text-neutral-500">
                    <span class="w-2 h-2 rounded-full bg-kinetic-red shadow-[0_0_10px_rgba(232,40,43,0.8)]"></span> LIVE // PORTFOLIO METRICS
                </div>
                <div class="text-neutral-600 font-bold">
                    ELEVIX DIGITAL • 2026
                </div>
            </div>
            
            <!-- 4 Grid Columns -->
            <div class="grid grid-cols-1 md:grid-cols-4">
                <!-- Col 1 -->
                <div class="p-10 border-b md:border-b-0 md:border-r border-white/5 group hover:bg-[#111] transition-colors relative overflow-hidden">
                    <div class="absolute inset-0 bg-gradient-to-b from-kinetic-red/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="absolute top-6 left-6 w-3 h-3 border-t border-l border-kinetic-red/30 group-hover:border-kinetic-red transition-colors"></div>
                    <div class="absolute bottom-6 right-6 w-3 h-3 border-b border-r border-kinetic-red/30 group-hover:border-kinetic-red transition-colors"></div>
                    
                    <div class="flex justify-between items-center mb-6 font-mono text-[10px] tracking-[0.2em] font-bold">
                        <span class="text-kinetic-red/80">// 01</span>
                        <span class="w-6 h-[1px] bg-kinetic-red/50"></span>
                    </div>
                    <div class="font-display font-black text-[50px] lg:text-[70px] text-white leading-none tracking-tighter mb-6 group-hover:-translate-y-1 transition-transform">
                        23.75x
                    </div>
                    <div class="font-mono text-[9px] uppercase tracking-[0.2em] text-neutral-400 font-bold group-hover:text-white transition-colors">
                        ROAS • EME EDUCATION
                    </div>
                </div>

                <!-- Col 2 -->
                <div class="p-10 border-b md:border-b-0 md:border-r border-white/5 group hover:bg-[#111] transition-colors relative overflow-hidden">
                    <div class="absolute inset-0 bg-gradient-to-b from-kinetic-red/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="absolute top-6 left-6 w-3 h-3 border-t border-l border-kinetic-red/30 group-hover:border-kinetic-red transition-colors"></div>
                    <div class="absolute bottom-6 right-6 w-3 h-3 border-b border-r border-kinetic-red/30 group-hover:border-kinetic-red transition-colors"></div>
                    
                    <div class="flex justify-between items-center mb-6 font-mono text-[10px] tracking-[0.2em] font-bold">
                        <span class="text-kinetic-red/80">// 02</span>
                        <span class="w-6 h-[1px] bg-kinetic-red/50"></span>
                    </div>
                    <div class="font-display font-black text-[50px] lg:text-[70px] text-white leading-none tracking-tighter mb-6 group-hover:-translate-y-1 transition-transform">
                        41x
                    </div>
                    <div class="font-mono text-[9px] uppercase tracking-[0.2em] text-neutral-400 font-bold group-hover:text-white transition-colors">
                        ROAS • NAYATEL LAHORE
                    </div>
                </div>

                <!-- Col 3 -->
                <div class="p-10 border-b md:border-b-0 md:border-r border-white/5 group hover:bg-[#111] transition-colors relative overflow-hidden">
                    <div class="absolute inset-0 bg-gradient-to-b from-kinetic-red/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="absolute top-6 left-6 w-3 h-3 border-t border-l border-kinetic-red/30 group-hover:border-kinetic-red transition-colors"></div>
                    <div class="absolute bottom-6 right-6 w-3 h-3 border-b border-r border-kinetic-red/30 group-hover:border-kinetic-red transition-colors"></div>
                    
                    <div class="flex justify-between items-center mb-6 font-mono text-[10px] tracking-[0.2em] font-bold">
                        <span class="text-kinetic-red/80">// 03</span>
                        <span class="w-6 h-[1px] bg-kinetic-red/50"></span>
                    </div>
                    <div class="font-display font-black text-[50px] lg:text-[70px] text-white leading-none tracking-tighter mb-6 group-hover:-translate-y-1 transition-transform">
                        450L+
                    </div>
                    <div class="font-mono text-[9px] uppercase tracking-[0.2em] text-neutral-400 font-bold group-hover:text-white transition-colors">
                        ATTRIBUTED REVENUE
                    </div>
                </div>

                <!-- Col 4 -->
                <div class="p-10 group hover:bg-[#111] transition-colors relative overflow-hidden">
                    <div class="absolute inset-0 bg-gradient-to-b from-kinetic-red/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="absolute top-6 left-6 w-3 h-3 border-t border-l border-kinetic-red/30 group-hover:border-kinetic-red transition-colors"></div>
                    <div class="absolute bottom-6 right-6 w-3 h-3 border-b border-r border-kinetic-red/30 group-hover:border-kinetic-red transition-colors"></div>
                    
                    <div class="flex justify-between items-center mb-6 font-mono text-[10px] tracking-[0.2em] font-bold">
                        <span class="text-kinetic-red/80">// 04</span>
                        <span class="w-6 h-[1px] bg-kinetic-red/50"></span>
                    </div>
                    <div class="font-display font-black text-[50px] lg:text-[70px] text-white leading-none tracking-tighter mb-6 group-hover:-translate-y-1 transition-transform">
                        53K
                    </div>
                    <div class="font-mono text-[9px] uppercase tracking-[0.2em] text-neutral-400 font-bold group-hover:text-white transition-colors">
                        AD SPEND → 22L RETURN
                    </div>
                </div>
            </div>
        </div>
    </section>"""
    html = re.sub(metrics_old_pattern, metrics_new, html, count=1, flags=re.DOTALL)


    # 2. Update "#the-work" heading
    heading_old = r'<div class="mb-20 fade-up">\s*<h2 class="font-display text-\[50px\] md:text-\[80px\] font-bold leading-\[1\.0\] tracking-tight text-stark-white">\s*Results that speak<br>\s*<span class="text-surface-gray text-stroke"[^>]*>for themselves\.</span>\s*</h2>\s*</div>'
    heading_new = """<div class="mb-20 fade-up">
                <div class="flex items-center gap-4 mb-6">
                    <span class="w-8 h-[2px] bg-kinetic-red"></span>
                    <span class="font-mono text-[11px] text-kinetic-red font-bold uppercase tracking-[0.2em]">// 02. THE WORK</span>
                </div>
                <h2 class="font-display text-[50px] md:text-[80px] font-bold leading-[1.0] tracking-tight text-stark-white">
                    Selected client results.
                </h2>
            </div>"""
    html = re.sub(heading_old, heading_new, html, count=1)


    # 3. Rename Kerala to Lahore in the first card
    html = html.replace('Faber Kerala', 'Faber Lahore')
    html = html.replace('HOME APPLIANCES KERALA', 'HOME APPLIANCES LAHORE')


    # 4. Add 2 new screenshot cards after the first 2 cards
    cards_insertion_marker = r'(<div class="grid grid-cols-1 md:grid-cols-2 gap-8">.*?</div>\s*</div>)'
    
    new_cards = """
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mt-8">
                <!-- New Card 3: Nayatel Lahore (matching screenshot design) -->
                <div class="p-10 md:p-14 rounded-[2rem] border border-white/5 bg-[#111111] hover:border-kinetic-red/50 transition-all duration-500 fade-up relative overflow-hidden group flex flex-col h-full">
                    <div class="absolute inset-0 bg-gradient-to-br from-kinetic-red/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                    <div class="relative z-10 flex flex-col h-full">
                        <!-- Header -->
                        <div class="flex justify-between items-start mb-8 font-mono text-[9px] font-bold uppercase tracking-[0.2em]">
                            <span class="text-kinetic-red">IT & TELECOM , BROADBAND<br/>SERVICES</span>
                            <span class="text-neutral-500 flex items-center gap-4">
                                <span class="w-6 h-[1px] bg-neutral-700"></span> SEPT 2025 → MAR<br/>2026
                            </span>
                        </div>
                        
                        <h3 class="font-display text-3xl font-bold text-white mb-6">Nayatel Lahore</h3>
                        
                        <div class="font-display text-[70px] font-black text-kinetic-red leading-none mb-4 flex items-center gap-2 tracking-tighter">
                            41<span class="text-[50px] tracking-normal">×</span>
                        </div>
                        
                        <p class="font-display text-sm text-stark-white font-bold mb-10 pb-10 border-b border-white/10">March 2026 festive window</p>
                        
                        <p class="font-display text-on-secondary-container text-base leading-relaxed mb-12">
                            Nayatel Lahore provides premium broadband and telecom solutions. Strong corporate presence, but retail was lagging. We built the digital sales engine from scratch across three phases — March 2026 festive peak delivered <strong class="text-stark-white">52 Lakh PKR revenue</strong> at 41× ROAS.
                        </p>
                        
                        <!-- Pills -->
                        <div class="flex flex-wrap gap-3 mt-auto mb-10">
                            <span class="font-mono text-[9px] text-white/50 border border-white/10 rounded-full px-4 py-2 uppercase tracking-[0.2em]">DIGITAL MARKETING</span>
                            <span class="font-mono text-[9px] text-white/50 border border-white/10 rounded-full px-4 py-2 uppercase tracking-[0.2em]">AI AUTOMATION</span>
                            <span class="font-mono text-[9px] text-white/50 border border-white/10 rounded-full px-4 py-2 uppercase tracking-[0.2em]">DESIGN & CREATIVES</span>
                        </div>
                        
                        <a href="#" class="font-mono text-[10px] text-white font-bold uppercase tracking-[0.2em] flex justify-between items-center group/btn mt-auto">
                            READ THE FULL CASE STUDY
                            <span class="text-kinetic-red group-hover/btn:translate-x-1 group-hover/btn:-translate-y-1 transition-transform">↗</span>
                        </a>
                    </div>
                </div>

                <!-- New Card 4: EME (Electromech Enterprises) -->
                <div class="p-10 md:p-14 rounded-[2rem] border border-white/5 bg-[#111111] hover:border-kinetic-red/50 transition-all duration-500 fade-up relative overflow-hidden group flex flex-col h-full mt-8 md:mt-0">
                    <div class="absolute inset-0 bg-gradient-to-bl from-kinetic-red/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                    <div class="relative z-10 flex flex-col h-full">
                        <!-- Header -->
                        <div class="flex justify-between items-start mb-8 font-mono text-[9px] font-bold uppercase tracking-[0.2em]">
                            <span class="text-kinetic-red">EDUCATION . SAP CERTIFICATION</span>
                            <span class="text-neutral-500 flex items-center gap-4">
                                <span class="w-6 h-[1px] bg-neutral-700"></span> 2023 → 2025
                            </span>
                        </div>
                        
                        <h3 class="font-display text-3xl font-bold text-white mb-6">EME (Electromech Enterprises)</h3>
                        
                        <div class="font-display text-[70px] font-black text-kinetic-red leading-none mb-4 tracking-tighter">
                            450L<span class="text-[30px] font-bold ml-2 tracking-normal">PKR</span>
                        </div>
                        
                        <p class="font-display text-sm text-stark-white font-bold mb-10 pb-10 border-b border-white/10">Sustained across 24 months</p>
                        
                        <p class="font-display text-on-secondary-container text-base leading-relaxed mb-12">
                            EME sells premium SAP consultant-level programs (₹2L) alongside lower-tier end-user certs. We rebuilt the enrollment engine — precision Meta ads, AI lead qualification, and a webinar-first funnel. 237 leads closed on <strong class="text-stark-white">17.18L ad spend</strong>.
                        </p>
                        
                        <!-- Pills -->
                        <div class="flex flex-wrap gap-3 mt-auto mb-10">
                            <span class="font-mono text-[9px] text-white/50 border border-white/10 rounded-full px-4 py-2 uppercase tracking-[0.2em]">DIGITAL MARKETING</span>
                            <span class="font-mono text-[9px] text-white/50 border border-white/10 rounded-full px-4 py-2 uppercase tracking-[0.2em]">AI AUTOMATION</span>
                            <span class="font-mono text-[9px] text-white/50 border border-white/10 rounded-full px-4 py-2 uppercase tracking-[0.2em]">GOHIGHLEVEL</span>
                        </div>
                        
                        <a href="#" class="font-mono text-[10px] text-white font-bold uppercase tracking-[0.2em] flex justify-between items-center group/btn mt-auto">
                            READ THE FULL CASE STUDY
                            <span class="text-kinetic-red group-hover/btn:translate-x-1 group-hover/btn:-translate-y-1 transition-transform">↗</span>
                        </a>
                    </div>
                </div>
            </div>"""

    # We need to insert this right after the FIRST grid of 2 cards.
    # The regex r'(<div class="grid grid-cols-1 md:grid-cols-2 gap-8">.*?</div>\s*</div>)' 
    # matches the first grid. We'll replace it with itself + new_cards
    
    # Wait, the first grid might have more closing divs. Let's do it properly.
    # Instead of regex, let's just insert it before `</div>\s*</section>` of `#the-work`
    
    # Let's find </section> after id="the-work"
    the_work_end = html.find('</section>', html.find('id="the-work"'))
    # The container div closes right before </section>.
    container_end = html.rfind('</div>', 0, the_work_end)
    
    html = html[:container_end] + new_cards + "\n        " + html[container_end:]

    # 5. Replace footer
    # Find footer in our-story
    os_footer_match = re.search(r'(<footer class="pt-32.*?</script>\s*</body>)', our_story, re.DOTALL)
    if os_footer_match:
        os_footer = os_footer_match.group(1)
        # Fix copyright symbol
        os_footer = os_footer.replace('A,Ac 2026', '© 2026')
        
        # Replace footer in case-studies
        cs_footer_pattern = r'<footer class="pt-32.*?</script>\s*</body>'
        html = re.sub(cs_footer_pattern, os_footer, html, flags=re.DOTALL)
    
    with open('case-studies.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    update_case_studies()
