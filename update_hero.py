import re

with open(r'c:\Elevix Digital\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Navbar Replacement
old_nav = r'    <!-- TopNavBar \(Elite Neogen Style\) -->.*?    </nav>'
new_nav = """    <!-- TopNavBar (Elite Neogen Style) -->
    <nav class="fixed top-6 left-1/2 -translate-x-1/2 w-[95%] max-w-7xl z-50 glass-nav border border-white/10 rounded-[20px] transition-all overflow-hidden shadow-[0_10_30px_rgba(0,0,0,0.5)]">
        <div class="px-8 h-20 flex justify-between items-center w-full">
            
            <!-- Premium 8D Hyper-Cube Logo -->
            <a href="index.html" class="flex items-center gap-4 group cursor-pointer">
                <div class="relative w-12 h-12 flex items-center justify-center group-hover:scale-110 transition-transform duration-700" style="perspective: 800px;">
                    <!-- Outer Infinity Rings -->
                    <div class="absolute inset-0 rounded-full border border-kinetic-red/30 border-t-kinetic-red animate-[spin_4s_linear_infinite] group-hover:shadow-[0_0_20px_rgba(232,40,43,0.5)] transition-all"></div>
                    <div class="absolute inset-[3px] rounded-full border border-white/10 border-b-white animate-[spin_3s_linear_infinite_reverse]"></div>
                    <div class="absolute inset-[6px] rounded-full border border-kinetic-red/10 border-l-kinetic-red animate-[spin_5s_linear_infinite]"></div>
                    
                    <!-- Inner 3D Diamond Core -->
                    <div class="relative w-6 h-6 animate-[spin_8s_linear_infinite]" style="transform-style: preserve-3d;">
                        <div class="absolute inset-0 bg-gradient-to-br from-kinetic-red to-[#500000] opacity-80 rounded shadow-[0_0_20px_rgba(232,40,43,0.8)]" style="transform: rotate(45deg) translateZ(-5px);"></div>
                        <div class="absolute inset-[1px] bg-[#0A0A0A] rounded border border-kinetic-red/50" style="transform: rotate(45deg) translateZ(5px);"></div>
                    </div>
                    
                    <!-- Floating 'E' -->
                    <span class="absolute z-20 font-display font-black text-white text-[22px] tracking-tighter" style="text-shadow: 0 0 15px rgba(232,40,43,1), 0 0 30px rgba(255,255,255,0.5);">E</span>
                </div>
                <div class="flex flex-col">
                    <span class="font-display font-black text-[20px] leading-none tracking-tight uppercase text-transparent bg-clip-text bg-gradient-to-b from-white to-white/60 drop-shadow-[0_0_10px_rgba(255,255,255,0.2)]">Elevix</span>
                    <span class="font-mono text-[8px] text-kinetic-red tracking-[0.4em] uppercase font-bold mt-0.5" style="text-shadow: 0 0 8px rgba(232,40,43,0.8);">Digital</span>
                </div>
            </a>

            <!-- Links -->
            <div class="hidden lg:flex items-center gap-10">
                <a href="our-story.html" class="text-on-secondary-container text-[14px] font-medium hover:text-white transition-colors">Our Story</a>
                <a href="services.html" class="text-on-secondary-container text-[14px] font-medium hover:text-white transition-colors flex items-center gap-1">Services <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg></a>
                <a href="#results" class="text-on-secondary-container text-[14px] font-medium hover:text-white transition-colors">Case Studies</a>
                <a href="#" class="text-on-secondary-container text-[14px] font-medium hover:text-white transition-colors">Blogs</a>
                <a href="#" class="text-on-secondary-container text-[14px] font-medium hover:text-white transition-colors">Careers</a>
                <a href="#" class="text-on-secondary-container text-[14px] font-medium hover:text-white transition-colors">Contact Us</a>
            </div>

            <!-- Let's Talk CTA Button -->
            <button class="bg-kinetic-red text-white px-8 py-3 rounded-full text-[14px] font-bold hover:bg-[#ff3333] transition-all shadow-[0_0_15px_rgba(232,40,43,0.3)] hover:shadow-[0_0_25px_rgba(232,40,43,0.5)]">
                Let's Talk
            </button>
        </div>
    </nav>"""
html = re.sub(old_nav, new_nav, html, flags=re.DOTALL)

# 2. Hero Background Replacement (Remove canvas)
html = html.replace('        <!-- Interactive 3D WebGL Background Canvas -->\n        <canvas id="hero-canvas" class="absolute inset-0 w-full h-full pointer-events-none z-0" style="z-index: 0; pointer-events: none;"></canvas>\n', '')

# 3. Hero Text and Corners Update
old_hero_content = r'            <!-- Top Boundary Line -->.*?</a>\n                </div>\n            </div>'
new_hero_content = """            <!-- Top Boundary Line -->
            <div class="absolute top-0 left-6 right-6 h-[1px] bg-white/5"></div>
            
            <!-- Corner Angles -->
            <div class="absolute top-0 left-6 w-4 h-4 border-t-2 border-l-2 border-kinetic-red"></div>
            <div class="absolute top-0 right-6 w-4 h-4 border-t-2 border-r-2 border-kinetic-red"></div>
            <div class="absolute bottom-0 left-6 w-4 h-4 border-b-2 border-l-2 border-kinetic-red"></div>
            <div class="absolute bottom-0 right-6 w-4 h-4 border-b-2 border-r-2 border-kinetic-red"></div>
            
            <!-- Texts inside the boundary -->
            <div class="absolute top-4 left-14 font-mono text-[10px] text-on-secondary-container tracking-[0.2em] uppercase hidden sm:block">
                // E-001.2026 / LAHORE PKT
            </div>
            <div class="absolute top-4 right-14 font-mono text-[10px] text-kinetic-red tracking-[0.2em] uppercase flex items-center gap-2 hidden sm:flex">
                <span class="w-1.5 h-1.5 rounded-full bg-kinetic-red animate-pulse"></span> ONLINE
            </div>
            <div class="absolute bottom-4 left-14 font-mono text-[10px] text-on-secondary-container tracking-[0.2em] uppercase hidden sm:block">
                // 03.YRS • AI.FIRST
            </div>
            <div class="absolute bottom-4 right-14 font-mono text-[10px] text-on-secondary-container tracking-[0.2em] uppercase hidden sm:block">
                // SCROLL &darr;
            </div>

            <!-- Center Content (Pushed up to fit Featured Case in 1 page view) -->
            <div class="flex flex-col items-center text-center -mt-12 fade-up">
                
                <div class="font-mono text-kinetic-red text-[11px] font-bold uppercase tracking-[0.3em] mb-10 flex items-center gap-6">
                    <span class="w-12 h-[1px] bg-kinetic-red/60 hidden sm:block"></span>
                    AUTOMATING THE IMPOSSIBLE, DAILY.
                    <span class="w-12 h-[1px] bg-kinetic-red/60 hidden sm:block"></span>
                </div>
                
                <h1 id="hero-h1" class="font-display text-[45px] sm:text-[55px] md:text-[65px] lg:text-[80px] font-bold tracking-tight leading-[1.05] text-white mb-8 w-full max-w-[1100px] mx-auto" style="opacity:1;">
                    Scale your Business with<br/>
                    <span class="text-kinetic-red">AI Marketing</span> &amp; Automation
                </h1>
                
                <p class="font-display text-on-secondary-container max-w-2xl mx-auto text-[17px] md:text-[19px] font-medium leading-[1.6]">
                    One partner. Full growth stack. AI automation at every layer. Systems that compound over time.
                </p>
                
            </div>

            <!-- Bottom Boundary Line -->
            <div class="absolute bottom-0 left-6 right-6 h-[1px] bg-white/5"></div>

            <!-- PERFECTLY CENTERED Bottom Center Pill pushed UPWARDS as requested -->
            <div class="absolute bottom-10 left-1/2 -translate-x-1/2 z-30 flex flex-col items-center gap-8">
                <!-- Featured Case -->
                <div class="fade-up" style="transition-delay: 200ms;">
                    <a href="#results" class="flex items-center gap-3 border border-kinetic-red/30 bg-deep-obsidian backdrop-blur-md pl-4 pr-6 py-2.5 rounded-full font-display text-[12px] text-on-secondary-container hover:border-kinetic-red hover:shadow-[0_0_20px_rgba(232,40,43,0.3)] transition-all cursor-pointer">
                        <span class="flex items-center gap-2 text-kinetic-red font-bold text-[10px] tracking-wider uppercase">
                            <span class="w-1.5 h-1.5 rounded-full bg-kinetic-red animate-pulse"></span> FEATURED CASE
                        </span>
                        <span class="w-[1px] h-3 bg-white/20 mx-1"></span>
                        <span class="text-white font-bold tracking-wide"><span class="text-white/70">PKR</span> 52 Lakh • 41× ROI</span>
                        <span class="ml-1 opacity-70">· Home Appliances</span>
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="ml-2 opacity-50"><path d="M7 17l9.2-9.2M17 17V7H7"/></svg>
                    </a>
                </div>
                
                <!-- CTA Buttons from Screenshot 3 -->
                <div class="fade-up flex flex-wrap justify-center items-center gap-4" style="transition-delay: 300ms;">
                    <a href="#results" class="bg-kinetic-red text-white px-8 py-3.5 rounded-full text-[15px] font-bold hover:bg-[#ff3333] transition-all shadow-[0_0_15px_rgba(232,40,43,0.3)] hover:shadow-[0_0_25px_rgba(232,40,43,0.5)] flex items-center gap-2">
                        Book a Strategy Call <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                    </a>
                    <a href="#portfolio" class="bg-[#050505] border border-white/20 text-white px-8 py-3.5 rounded-full text-[15px] font-bold hover:bg-white/10 transition-all flex items-center gap-2">
                        See Our Work <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                    </a>
                </div>
            </div>"""
html = re.sub(old_hero_content, new_hero_content, html, flags=re.DOTALL)

with open(r'c:\Elevix Digital\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully with hero refinements")
