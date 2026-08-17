import re

with open('c:/Elevix Digital/services sub folder/web-development.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure we don't duplicate it
if 'id="in-short-section"' in text:
    print("Already added.")
else:
    footer_code = """
        </section>

        <!-- IN SHORT SECTION (From Screenshot) -->
        <section id="in-short-section" class="py-24 px-6 md:px-12 max-w-5xl mx-auto border-t border-white/5 relative z-10">
            <div class="flex items-center gap-4 mb-8">
                <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] uppercase font-bold">// IN SHORT</span>
            </div>
            
            <h2 class="font-display text-[40px] md:text-[50px] font-black text-white leading-[1.1] tracking-tight mb-10 max-w-3xl">
                What does a website development company in Kochi do?
            </h2>
            
            <p class="font-display text-[15px] md:text-[16px] text-white/70 leading-[1.8] max-w-4xl mb-6">
                Neogen Media is a website development company in Kochi, Kerala that engineers sites to rank, convert, and scale. We build on Next.js, WordPress, and Shopify — 30+ websites shipped at a 90+ average Lighthouse score, with SEO and CRO baked in from the first commit rather than retrofitted. You own the code, hosting, and design files on day one.
            </p>
            <p class="font-display text-[15px] md:text-[16px] text-white/70 leading-[1.8] max-w-4xl">
                Whether it's a custom web app, a WordPress build, an e-commerce store, or a campaign landing page, performance and search visibility are engineered in, not bolted on later.
            </p>
        </section>

        <!-- CTA SECTION: Book Strategy Call -->
        <section class="relative py-32 px-6 overflow-hidden border-t border-white/5 z-10">
            <!-- Animated Web Concept Background for CTA -->
            <div class="absolute inset-0 pointer-events-none z-0">
                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-kinetic-red/10 rounded-full blur-[100px] animate-[pulse_5s_ease-in-out_infinite]"></div>
                <!-- Moving grid lines -->
                <div class="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)]" style="background-size: 60px 60px;"></div>
            </div>

            <div class="max-w-4xl mx-auto text-center relative z-10">
                <h2 class="font-display text-[40px] md:text-[60px] font-black text-white leading-tight tracking-tight mb-8">
                    Ready to engineer<br>your next <span class="text-kinetic-red drop-shadow-[0_0_15px_rgba(232,40,43,0.5)]">digital asset?</span>
                </h2>
                
                <button class="group relative inline-flex items-center justify-center px-10 py-5 font-bold text-white transition-all duration-300 bg-kinetic-red rounded-full overflow-hidden hover:scale-105 shadow-[0_0_30px_rgba(232,40,43,0.4)] hover:shadow-[0_0_50px_rgba(232,40,43,0.6)]">
                    <span class="absolute inset-0 w-full h-full bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:animate-[shine_1.5s_ease]"></span>
                    <span class="relative font-mono tracking-widest uppercase text-[12px] flex items-center gap-3">
                        Book Strategy Call 
                        <svg class="w-4 h-4 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </span>
                </button>
            </div>
        </section>
    </main>

    <!-- FOOTER RESTORED FROM SERVICES.HTML -->
    <footer class="border-t border-white/10 relative z-20 bg-[#0A0A0A]">
        <!-- Bottom Links -->
        <div class="grid grid-cols-1 md:grid-cols-3">
            <!-- COMPANY -->
            <div class="p-8 md:p-12 border-b md:border-b-0 md:border-r border-white/10 flex flex-col">
                <span class="font-mono text-[10px] text-white/40 tracking-[0.2em] font-bold uppercase mb-10 block">COMPANY</span>
                <div class="grid grid-cols-2 gap-y-8 mt-auto">
                    <a href="#" class="font-display text-[14px] font-bold text-white hover:text-kinetic-red transition-colors uppercase">OUR STORY</a>
                    <a href="#" class="font-display text-[14px] font-bold text-white hover:text-kinetic-red transition-colors uppercase">CASE STUDIES</a>
                    <a href="../careers.html" class="font-display text-[14px] font-bold text-white hover:text-kinetic-red transition-colors uppercase">CAREERS</a>
                    <a href="#" class="font-display text-[14px] font-bold text-white hover:text-kinetic-red transition-colors uppercase">CONTACT</a>
                    <a href="../blog.html" class="font-display text-[14px] font-bold text-white hover:text-kinetic-red transition-colors uppercase">BLOGS</a>
                </div>
            </div>

            <!-- LEGAL -->
            <div class="p-8 md:p-12 border-b md:border-b-0 md:border-r border-white/10 flex flex-col">
                <span class="font-mono text-[10px] text-white/40 tracking-[0.2em] font-bold uppercase mb-10 block">LEGAL</span>
                <div class="flex flex-col gap-y-8 mt-auto">
                    <a href="#" class="font-display text-[14px] font-bold text-white hover:text-kinetic-red transition-colors uppercase">PRIVACY POLICY</a>
                    <a href="#" class="font-display text-[14px] font-bold text-white hover:text-kinetic-red transition-colors uppercase">TERMS OF SERVICE</a>
                </div>
            </div>

            <!-- SOCIAL -->
            <div class="p-8 md:p-12 flex flex-col">
                <span class="font-mono text-[10px] text-white/40 tracking-[0.2em] font-bold uppercase mb-10 block">SOCIAL</span>
                <div class="flex flex-wrap gap-4 mt-auto">
                    <a href="#" class="w-10 h-10 flex items-center justify-center border border-white/10 rounded hover:border-kinetic-red hover:bg-kinetic-red hover:text-white transition-all text-white/60 font-bold uppercase text-[12px]">f</a>
                    <a href="#" class="w-10 h-10 flex items-center justify-center border border-white/10 rounded hover:border-kinetic-red hover:bg-kinetic-red hover:text-white transition-all text-white/60 font-bold uppercase text-[12px]">in</a>
                    <a href="#" class="w-10 h-10 flex items-center justify-center border border-white/10 rounded hover:border-kinetic-red hover:bg-kinetic-red hover:text-white transition-all text-white/60 font-bold uppercase text-[12px]">yt</a>
                    <a href="#" class="w-10 h-10 flex items-center justify-center border border-white/10 rounded hover:border-kinetic-red hover:bg-kinetic-red hover:text-white transition-all text-white/60 font-bold uppercase text-[12px]">x</a>
                    <a href="#" class="w-10 h-10 flex items-center justify-center border border-white/10 rounded hover:border-kinetic-red hover:bg-kinetic-red hover:text-white transition-all text-white/60 font-bold uppercase text-[12px]">be</a>
                </div>
            </div>
        </div>

        <!-- 6D Scanline Massive Footer Logotype -->
        <div class="w-full relative overflow-hidden bg-black flex flex-col items-center justify-center pt-24 pb-12">
            <!-- 6D Grid & Scanline Background -->
            <div class="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.04)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.04)_1px,transparent_1px)]" style="background-size: 50px 50px;"></div>
            <div class="absolute inset-0 bg-gradient-to-b from-transparent via-kinetic-red/10 to-transparent h-[100%] animate-[scan_4s_linear_infinite] pointer-events-none"></div>
            
            <!-- Massive Text -->
            <h1 class="relative z-10 w-full text-center px-4 font-display font-black leading-[0.8] tracking-tighter text-transparent opacity-90 transition-all duration-700 hover:opacity-100 hover:scale-105" style="-webkit-text-stroke: 2px rgba(255,255,255,0.9); font-size: clamp(4rem, 15vw, 15vw); background: linear-gradient(180deg, #ffffff 0%, #333333 100%); -webkit-background-clip: text;">
                ELEVIX<br/>DIGITAL
            </h1>
        </div>
    </footer>

    <!-- Custom Scripts -->
    <script src="../services.js"></script>
</body>
</html>
"""
    
    # Append the footer code right after the hero section div closes
    text = text + footer_code
    
    with open('c:/Elevix Digital/services sub folder/web-development.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Appended missing sections and footer successfully.")
