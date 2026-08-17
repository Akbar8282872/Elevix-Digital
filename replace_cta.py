import re

with open('c:/Elevix Digital/blog.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The new CTA section
new_cta = '''
<!-- NEW CTA SECTION -->
<section class="py-24 px-6 bg-[#0a0a0a] border-t border-white/5 relative z-10 overflow-hidden">
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_left,rgba(232,40,43,0.05)_0%,transparent_50%)] pointer-events-none"></div>
    <div class="max-w-7xl mx-auto w-full relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24">
            
            <!-- Left Side -->
            <div class="flex flex-col justify-center">
                <div class="flex items-center gap-2 inline-block py-1.5 px-4 border border-white/10 rounded-full bg-white/5 mb-8 w-max">
                    <div class="w-2 h-2 rounded-full bg-kinetic-red animate-pulse"></div>
                    <span class="font-mono text-stark-white text-[10px] font-bold tracking-[0.2em] uppercase">
                        NEXT STEP
                    </span>
                </div>
                
                <h2 class="font-display font-black text-5xl md:text-6xl text-white leading-[1.1] tracking-tighter mb-6">
                    Ready to<br>automate your<br>growth?
                </h2>
                
                <p class="text-lg text-neutral-400 font-display leading-relaxed max-w-md mb-12">
                    One 30-minute audit call. Honest read on your funnel, no deck, no obligations.
                </p>
                
                <a href="#contact" class="group relative inline-flex items-center justify-center gap-4 bg-kinetic-red text-white px-8 py-5 rounded-[40px] font-display font-bold text-[15px] tracking-wide hover:bg-red-600 transition-all duration-300 w-max mb-12 shadow-[0_0_30px_rgba(232,40,43,0.3)]">
                    <span class="flex items-center justify-center w-6 h-6 border border-white/30 rounded-full group-hover:bg-white group-hover:text-kinetic-red transition-colors">
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17l9.2-9.2M17 17V7H7"/></svg>
                    </span>
                    Book a Strategy Call
                </a>
                
                <div class="flex flex-wrap items-center gap-4 text-neutral-500 font-mono text-[9px] uppercase tracking-[0.2em] font-bold mb-8">
                    <span>30 MIN</span>
                    <span class="w-1 h-1 rounded-full bg-kinetic-red"></span>
                    <span>FREE AUDIT</span>
                    <span class="w-1 h-1 rounded-full bg-kinetic-red"></span>
                    <span>NO DECK</span>
                    <span class="w-1 h-1 rounded-full bg-kinetic-red"></span>
                    <span>NO OBLIGATION</span>
                </div>
                
                <a href="#whatsapp" class="flex items-center gap-3 text-neutral-400 hover:text-white transition-colors font-display text-[15px]">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="kinetic-red" stroke-width="2" class="text-kinetic-red"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                    Or send us a WhatsApp <span class="text-xs">↗</span>
                </a>
            </div>
            
            <!-- Right Side -->
            <div class="flex flex-col justify-center border-l border-white/5 pl-0 lg:pl-16 pt-12 lg:pt-0">
                <h3 class="font-mono text-[10px] text-kinetic-red uppercase tracking-[0.3em] font-bold mb-12">
                    // WHAT YOU WALK AWAY WITH
                </h3>
                
                <div class="flex flex-col gap-10">
                    <!-- Item 1 -->
                    <div class="flex items-start gap-6 group">
                        <div class="flex items-center justify-center min-w-[32px] w-[32px] h-[32px] rounded-full border border-kinetic-red/30 bg-kinetic-red/10 text-kinetic-red mt-1">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div>
                            <div class="font-mono text-[10px] text-neutral-600 mb-2 font-bold tracking-widest">0 1</div>
                            <h4 class="font-display text-white text-[17px] leading-[1.4] font-medium group-hover:text-kinetic-red transition-colors duration-300">A map of every manual task worth automating</h4>
                        </div>
                    </div>
                    
                    <!-- Item 2 -->
                    <div class="flex items-start gap-6 group">
                        <div class="flex items-center justify-center min-w-[32px] w-[32px] h-[32px] rounded-full border border-kinetic-red/30 bg-kinetic-red/10 text-kinetic-red mt-1">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div>
                            <div class="font-mono text-[10px] text-neutral-600 mb-2 font-bold tracking-widest">0 2</div>
                            <h4 class="font-display text-white text-[17px] leading-[1.4] font-medium group-hover:text-kinetic-red transition-colors duration-300">Ballpark ROI on your top 3 automation opportunities</h4>
                        </div>
                    </div>
                    
                    <!-- Item 3 -->
                    <div class="flex items-start gap-6 group">
                        <div class="flex items-center justify-center min-w-[32px] w-[32px] h-[32px] rounded-full border border-kinetic-red/30 bg-kinetic-red/10 text-kinetic-red mt-1">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div>
                            <div class="font-mono text-[10px] text-neutral-600 mb-2 font-bold tracking-widest">0 3</div>
                            <h4 class="font-display text-white text-[17px] leading-[1.4] font-medium group-hover:text-kinetic-red transition-colors duration-300">Honest read on whether we are a fit — or who is</h4>
                        </div>
                    </div>
                </div>
                
                <div class="mt-16 pt-8 border-t border-white/5 flex items-center gap-3">
                    <div class="w-2 h-2 rounded-full bg-kinetic-red animate-pulse"></div>
                    <span class="font-mono text-[9px] text-neutral-500 uppercase tracking-[0.2em] font-bold">USUALLY RESPONDS WITHIN 24 HOURS</span>
                </div>
            </div>
            
        </div>
    </div>
</section>
'''

sections = list(re.finditer(r'<section[^>]*>(.*?)</section>', text, re.DOTALL | re.IGNORECASE))
# The section to replace is the one with 'READY TO AUTOMATE'
replace_start = -1
replace_end = -1
for s in sections:
    if 'READY TO AUTOMATE' in s.group(0).upper():
        replace_start = s.start()
        replace_end = s.end()
        break

if replace_start != -1:
    new_text = text[:replace_start] + new_cta + text[replace_end:]
    with open('c:/Elevix Digital/blog.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully replaced the 'Ready to automate the impossible' banner.")
else:
    print("Could not find the target banner.")
