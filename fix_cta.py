import re

with open(r'c:\Elevix Digital\services.html', 'r', encoding='utf-8') as f:
    html = f.read()

cta_replacement = """    <!-- Bottom CTA / Booking Section (exact match with Screenshot 3) -->
    <section class="py-32 px-6 bg-[#050505] relative overflow-hidden border-t border-white/5 min-h-[80vh] flex flex-col justify-center">
        <!-- Background elements -->
        <div class="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)]" style="background-size: 50px 50px; opacity: 0.3;"></div>
        <div class="absolute bottom-[-10%] right-[-10%] w-[800px] h-[500px] bg-kinetic-red rounded-full filter blur-[200px] opacity-15 pointer-events-none"></div>
        
        <!-- Top corners info -->
        <div class="absolute top-10 w-full left-0 px-10 flex justify-between items-center text-[10px] font-mono tracking-[0.2em] uppercase font-bold text-on-secondary-container z-20">
            <div class="flex items-center gap-3">
                <span class="w-1.5 h-1.5 bg-kinetic-red rounded-sm"></span>
                <span>ACCEPTING CLIENTS • 2026</span>
            </div>
            <div>
                LAHORE, PAKISTAN
            </div>
        </div>

        <div class="max-w-[1400px] w-full mx-auto relative z-10 flex flex-col mt-20">
            <h2 id="banner-glitch" class="font-display font-black text-[60px] md:text-[100px] lg:text-[160px] text-white leading-[0.85] uppercase tracking-tighter text-left w-full glitch-text" data-text="READY TO AUTOMATE THE IMPOSSIBLE?">
                READY TO<br/>
                AUTOMATE<br/>
                <span class="text-kinetic-red drop-shadow-[0_0_30px_rgba(232,40,43,0.6)]">THE IMPOSSIBLE?</span>
            </h2>
        </div>
    </section>"""

# We'll use regex to replace the old section with the new section
pattern = r'    <!-- Bottom CTA / Booking Section \(exact match with Our Story structure\) -->.*?    </section>'
html = re.sub(pattern, cta_replacement, html, flags=re.DOTALL)

with open(r'c:\Elevix Digital\services.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated CTA in services.html successfully')
