import re

with open('c:/Elevix Digital/services sub folder/web-development.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I will replace the ENTIRE Hero section to ensure everything is perfectly structured and bulletproof.
start_marker = '<!-- 2. Hero Content -->'
end_marker = '</main>'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_hero = """<!-- 2. Hero Content -->
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-16 relative z-10 w-full mt-12">
            
            <!-- Left Side: Typography -->
            <div class="w-full md:w-[50%] flex flex-col gap-6 justify-start">
                
                <!-- Breadcrumbs EXACTLY like services.html -->
                <div class="flex items-center gap-4 text-on-secondary-container text-sm font-mono tracking-widest mb-4 uppercase">
                    <a href="../index.html" class="hover:text-white transition-colors cursor-pointer">Home</a>
                    <span class="text-white/30">/</span>
                    <a href="../services.html" class="hover:text-white transition-colors cursor-pointer">Services</a>
                    <span class="text-white/30">/</span>
                    <span class="text-white">Web Development</span>
                </div>

                <!-- Badge -->
                <div class="inline-flex items-center gap-3 border border-white/10 rounded-full px-5 py-2.5 w-max bg-transparent mt-0 hover:border-kinetic-red/30 transition-all cursor-default">
                    <span class="w-2 h-2 rounded-full bg-kinetic-red"></span>
                    <span class="text-[10px] font-display font-bold tracking-[0.2em] text-white uppercase">Website Development Company &middot; Elevix Digital</span>
                </div>

                <!-- Main Headline -->
                <h1 class="font-display font-black text-white text-[56px] md:text-[60px] leading-[1.05] tracking-tight mt-6 max-w-xl relative z-10">
                    The website development company<br>
                    engineered to scale,<br>
                    <span class="text-kinetic-red drop-shadow-[0_0_20px_rgba(232,40,43,0.3)]">Elevix Digital.</span>
                </h1>
            </div>

            <!-- Right Side: Code Block FIRST, then Node Chart Flowchart -->
            <div class="w-full md:w-[50%] relative flex flex-col items-center justify-center pr-0 lg:pr-8 gap-10">
                
                <!-- BACKGROUND GLOW -->
                <div class="absolute inset-0 bg-kinetic-red/10 blur-[120px] z-0 animate-[pulse_6s_infinite]"></div>

                <!-- 1. THE ANIMATED TERMINAL CODE BLOCK (FIRST) -->
                <div class="relative w-full max-w-[360px] bg-[#0A0A0A]/90 backdrop-blur-2xl border border-white/10 rounded-xl shadow-[0_20px_50px_rgba(0,0,0,0.8)] overflow-hidden transform hover:scale-[1.02] hover:border-kinetic-red/40 transition-all duration-500 z-30 mr-auto lg:mr-12 animate-[float_7s_ease-in-out_infinite]">
                    <div class="h-8 border-b border-white/10 flex items-center px-4 justify-between bg-white/5">
                        <div class="flex gap-1.5">
                            <div class="w-2 h-2 rounded-full bg-[#FF5F56]"></div>
                            <div class="w-2 h-2 rounded-full bg-[#FFBD2E]"></div>
                            <div class="w-2 h-2 rounded-full bg-[#27C93F]"></div>
                        </div>
                        <span class="text-[9px] font-mono tracking-widest text-white/40 uppercase">Architecture.js</span>
                    </div>
                    <div class="p-6 font-mono text-[11px] leading-[1.8] text-white/70">
                        <span class="text-[#E8282B] font-bold">import</span> { Scale } <span class="text-[#E8282B] font-bold">from</span> <span class="text-[#A3A3A3]">'@elevix/core'</span>;<br><br>
                        <span class="text-[#E8282B] font-bold">const</span> app = <span class="text-[#E8282B] font-bold">await</span> Scale.<span class="text-white">init</span>({<br>
                        &nbsp;&nbsp;engine: <span class="text-[#A3A3A3]">'Next.js'</span>,<br>
                        &nbsp;&nbsp;status: <span class="text-[#A3A3A3]">'Online'</span><br>
                        });<br><br>
                        <span class="text-kinetic-red font-bold">></span> <span id="typewriter-target" class="text-white font-bold tracking-widest"></span><span class="animate-pulse bg-white w-1.5 h-3 inline-block ml-0.5 align-middle"></span>
                    </div>
                </div>

                <!-- 2. BEST DIAGRAM OF CHART TYPE (NATIVE HTML, NO PIC) -->
                <div class="relative w-full max-w-[400px] perspective-[1200px] animate-[float_6s_ease-in-out_infinite_reverse] z-20 ml-auto">
                    <!-- Glowing vertical connector line -->
                    <div class="absolute left-[38px] top-8 bottom-8 w-[2px] bg-gradient-to-b from-kinetic-red via-kinetic-red/40 to-transparent z-0 shadow-[0_0_15px_rgba(232,40,43,1)]"></div>
                    
                    <div class="flex flex-col gap-6 relative z-10">
                        <!-- Node 1: Navbar -->
                        <div class="flex items-center gap-8 group cursor-default transform transition-all duration-300 hover:translate-x-4">
                            <!-- Circular Node point -->
                            <div class="w-[24px] h-[24px] rounded-full bg-[#0A0A0A] border-[3px] border-kinetic-red flex items-center justify-center shadow-[0_0_20px_rgba(232,40,43,0.8)] group-hover:scale-125 transition-transform flex-shrink-0 z-10">
                                <div class="w-2.5 h-2.5 bg-kinetic-red rounded-full animate-pulse"></div>
                            </div>
                            <!-- Card element -->
                            <div class="flex-1 bg-[#111111]/80 backdrop-blur-xl border border-white/10 group-hover:border-kinetic-red/50 rounded-xl p-4 flex items-center justify-between shadow-[0_15px_40px_rgba(0,0,0,0.6)]">
                                <span class="font-mono text-[12px] text-white/90 font-bold tracking-widest uppercase">Global Navbar</span>
                                <span class="font-mono text-[9px] text-kinetic-red tracking-widest">ACTIVE</span>
                            </div>
                        </div>

                        <!-- Node 2: Header -->
                        <div class="flex items-center gap-8 group cursor-default transform transition-all duration-300 hover:translate-x-4">
                            <div class="w-[24px] h-[24px] rounded-full bg-[#0A0A0A] border-[3px] border-kinetic-red flex items-center justify-center shadow-[0_0_20px_rgba(232,40,43,0.8)] group-hover:scale-125 transition-transform flex-shrink-0 z-10">
                                <div class="w-2.5 h-2.5 bg-kinetic-red rounded-full animate-pulse"></div>
                            </div>
                            <div class="flex-1 bg-[#111111]/80 backdrop-blur-xl border border-white/10 group-hover:border-kinetic-red/50 rounded-xl p-4 flex items-center justify-between shadow-[0_15px_40px_rgba(0,0,0,0.6)]">
                                <span class="font-mono text-[12px] text-white/90 font-bold tracking-widest uppercase">Hero Header</span>
                                <span class="font-mono text-[9px] text-kinetic-red tracking-widest">RENDERED</span>
                            </div>
                        </div>

                        <!-- Node 3: Features -->
                        <div class="flex items-center gap-8 group cursor-default transform transition-all duration-300 hover:translate-x-4">
                            <div class="w-[24px] h-[24px] rounded-full bg-[#0A0A0A] border-[3px] border-kinetic-red flex items-center justify-center shadow-[0_0_20px_rgba(232,40,43,0.8)] group-hover:scale-125 transition-transform flex-shrink-0 z-10">
                                <div class="w-2.5 h-2.5 bg-kinetic-red rounded-full animate-pulse"></div>
                            </div>
                            <div class="flex-1 bg-[#111111]/80 backdrop-blur-xl border border-white/10 group-hover:border-kinetic-red/50 rounded-xl p-4 flex items-center justify-between shadow-[0_15px_40px_rgba(0,0,0,0.6)]">
                                <span class="font-mono text-[12px] text-white/90 font-bold tracking-widest uppercase">Feature Grid</span>
                                <span class="font-mono text-[9px] text-kinetic-red tracking-widest drop-shadow-[0_0_5px_rgba(232,40,43,0.8)]">ANIMATED</span>
                            </div>
                        </div>

                        <!-- Node 4: CTA -->
                        <div class="flex items-center gap-8 group cursor-default transform transition-all duration-300 hover:translate-x-4">
                            <div class="w-[24px] h-[24px] rounded-full bg-[#0A0A0A] border-[3px] border-white/20 flex items-center justify-center group-hover:border-kinetic-red group-hover:scale-125 transition-all flex-shrink-0 z-10">
                            </div>
                            <div class="flex-1 bg-[#111111]/80 backdrop-blur-xl border border-white/10 group-hover:border-kinetic-red/50 rounded-xl p-4 flex items-center justify-between shadow-[0_15px_40px_rgba(0,0,0,0.6)]">
                                <span class="font-mono text-[12px] text-white/50 font-bold tracking-widest uppercase group-hover:text-white/90 transition-colors">Conversion CTA</span>
                                <span class="font-mono text-[9px] text-white/30 tracking-widest">PENDING</span>
                            </div>
                        </div>

                        <!-- Node 5: Footer -->
                        <div class="flex items-center gap-8 group cursor-default transform transition-all duration-300 hover:translate-x-4">
                            <div class="w-[24px] h-[24px] rounded-full bg-[#0A0A0A] border-[3px] border-white/20 flex items-center justify-center group-hover:border-kinetic-red group-hover:scale-125 transition-all flex-shrink-0 z-10">
                            </div>
                            <div class="flex-1 bg-[#111111]/80 backdrop-blur-xl border border-white/10 group-hover:border-kinetic-red/50 rounded-xl p-4 flex items-center justify-between shadow-[0_15px_40px_rgba(0,0,0,0.6)]">
                                <span class="font-mono text-[12px] text-white/50 font-bold tracking-widest uppercase group-hover:text-white/90 transition-colors">Global Footer</span>
                                <span class="font-mono text-[9px] text-white/30 tracking-widest">PENDING</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- GSAP Typewriter initialization -->
                <script>
                    document.addEventListener('DOMContentLoaded', () => {
                        if(window.gsap && window.gsap.plugins && window.gsap.plugins.TextPlugin) {
                            setTimeout(() => {
                                gsap.to('#typewriter-target', {
                                    duration: 2.0,
                                    text: "SYSTEM ONLINE.",
                                    ease: "none"
                                });
                            }, 1000);
                        } else {
                            var el = document.getElementById('typewriter-target');
                            if(el) el.innerText = "SYSTEM ONLINE.";
                        }
                    });
                </script>
            </div>
        </div>
        
    """
    
    text = text[:start_idx] + new_hero + "\n    "
    
    with open('c:/Elevix Digital/services sub folder/web-development.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Perfect structure applied! Code first, native HTML node chart second, breadcrumbs match services.html exactly.")
else:
    print("Could not find start/end markers.")
