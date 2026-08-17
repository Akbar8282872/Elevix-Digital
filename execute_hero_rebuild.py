import re

with open('c:/Elevix Digital/services sub folder/web-development.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the Hero structure
old_hero_start = '<!-- 2. Hero Content -->\n        <div class="max-w-7xl mx-auto w-full grid grid-cols-1 lg:grid-cols-2 gap-16 relative z-10 mt-8">'
end_marker = '</div>\n            </div>\n        </div>\n    </main>'

start_idx = text.find('<!-- 2. Hero Content -->')
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_hero = """<!-- 2. Hero Content -->
        <div class="max-w-7xl mx-auto w-full relative z-10 mt-8">
            
            <!-- Breadcrumbs -->
            <div class="flex items-center gap-4 text-on-secondary-container text-sm font-mono tracking-widest mb-16 uppercase relative z-20">
                <a href="../index.html" class="hover:text-white transition-colors cursor-pointer">Home</a>
                <span class="text-white/30">/</span>
                <a href="../services.html" class="hover:text-white transition-colors cursor-pointer">Services</a>
                <span class="text-white/30">/</span>
                <span class="text-white font-bold">Web Development</span>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">
            
            <!-- Left Side: Typography -->
            <div class="w-full flex flex-col gap-6 justify-start mt-4">

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

            <!-- Right Side: Combined Flowchart + Terminal -->
            <div class="w-full relative flex justify-end items-start mt-0 lg:mt-0 pr-8">
                
                <!-- Custom HTML Flowchart Map -->
                <div class="relative w-full max-w-[360px] group perspective-[1000px] z-10 mx-auto lg:ml-auto mt-16 animate-[float_6s_ease-in-out_infinite]">
                    <!-- Glowing aura behind the flowchart -->
                    <div class="absolute inset-0 bg-kinetic-red/10 blur-[60px] group-hover:bg-kinetic-red/30 transition-colors duration-1000 animate-[pulse_4s_infinite]"></div>

                    <!-- Red connecting line going down center -->
                    <div class="absolute left-1/2 -translate-x-1/2 top-4 bottom-4 w-[2px] bg-gradient-to-b from-kinetic-red via-kinetic-red/50 to-transparent z-0"></div>

                    <!-- 5 Blocks Container -->
                    <div class="relative z-10 flex flex-col gap-6 w-full">
                        
                        <!-- Block 1: Navbar -->
                        <div class="flex items-center justify-center bg-[#0A0A0A]/90 backdrop-blur-xl border border-white/10 rounded-xl py-3 px-6 shadow-lg shadow-kinetic-red/5 w-3/4 mx-auto hover:border-kinetic-red/50 hover:scale-105 transition-all duration-300">
                            <span class="font-mono text-[10px] text-white/80 uppercase tracking-widest font-bold">Navbar Component</span>
                        </div>
                        
                        <!-- Block 2: Hero -->
                        <div class="flex items-center justify-center bg-[#0A0A0A]/90 backdrop-blur-xl border border-kinetic-red/40 rounded-xl py-4 px-6 shadow-[0_0_20px_rgba(232,40,43,0.3)] w-[90%] mx-auto hover:border-kinetic-red hover:shadow-[0_0_30px_rgba(232,40,43,0.5)] hover:scale-105 transition-all duration-300 relative">
                            <!-- Glowing dot -->
                            <div class="absolute -left-2 top-1/2 -translate-y-1/2 w-4 h-4 bg-kinetic-red rounded-full shadow-[0_0_10px_rgba(232,40,43,1)] animate-pulse"></div>
                            <div class="absolute -right-2 top-1/2 -translate-y-1/2 w-4 h-4 bg-kinetic-red rounded-full shadow-[0_0_10px_rgba(232,40,43,1)] animate-pulse"></div>
                            <span class="font-mono text-[12px] text-white uppercase tracking-[0.2em] font-black text-kinetic-red drop-shadow-[0_0_8px_rgba(232,40,43,0.5)]">Hero Block</span>
                        </div>

                        <!-- Block 3: Features -->
                        <div class="flex items-center justify-center bg-[#0A0A0A]/90 backdrop-blur-xl border border-white/10 rounded-xl py-3 px-6 shadow-lg shadow-kinetic-red/5 w-full hover:border-kinetic-red/50 hover:scale-105 transition-all duration-300">
                            <span class="font-mono text-[10px] text-white/80 uppercase tracking-widest font-bold">Features Grid</span>
                        </div>

                        <!-- Block 4: CTA -->
                        <div class="flex items-center justify-center bg-[#0A0A0A]/90 backdrop-blur-xl border border-white/10 rounded-xl py-3 px-6 shadow-lg shadow-kinetic-red/5 w-3/4 mx-auto hover:border-kinetic-red/50 hover:scale-105 transition-all duration-300">
                            <span class="font-mono text-[10px] text-white/80 uppercase tracking-widest font-bold">Conversion CTA</span>
                        </div>

                        <!-- Block 5: Footer -->
                        <div class="flex items-center justify-center bg-[#0A0A0A]/90 backdrop-blur-xl border border-white/10 rounded-xl py-3 px-6 shadow-lg shadow-kinetic-red/5 w-2/3 mx-auto hover:border-kinetic-red/50 hover:scale-105 transition-all duration-300">
                            <span class="font-mono text-[10px] text-white/50 uppercase tracking-widest font-bold">Global Footer</span>
                        </div>
                    </div>
                </div>

                <!-- THE ANIMATED TERMINAL CODE BLOCK (Moved DOWN safely) -->
                <div class="absolute top-0 -right-4 z-30 w-[300px] perspective-[1200px] animate-[float_7s_ease-in-out_infinite_reverse] hidden md:block">
                    <div class="relative bg-[#0A0A0A]/85 backdrop-blur-xl border border-white/10 rounded-xl shadow-[0_30px_60px_rgba(0,0,0,0.8)] flex flex-col overflow-hidden transform rotate-y-[-10deg] rotate-x-[5deg] hover:rotate-y-[0deg] hover:rotate-x-[0deg] transition-transform duration-[800ms] hover:border-kinetic-red/40 group">
                        
                        <!-- Terminal Header -->
                        <div class="h-8 border-b border-white/10 flex items-center px-3 justify-between bg-white/5">
                            <div class="flex gap-1.5">
                                <div class="w-2 h-2 rounded-full bg-[#FF5F56]"></div>
                                <div class="w-2 h-2 rounded-full bg-[#FFBD2E]"></div>
                                <div class="w-2 h-2 rounded-full bg-[#27C93F]"></div>
                            </div>
                            <span class="text-[8px] font-mono tracking-widest text-white/40 uppercase">Elevix_Scale.js</span>
                        </div>

                        <!-- Typing Code Block -->
                        <div class="p-4 flex-1 font-mono text-[10px] leading-[1.6]">
                            <div class="text-white/40 mb-2">// Flowchart connected...</div>
                            <div class="text-[#E8282B] font-bold">import <span class="text-white">Elevix</span> from <span class="text-[#A3A3A3]">'@ai'</span>;</div>
                            <div class="text-white mt-2">
                                <span class="text-[#E8282B]">const</span> <span class="text-white">app</span> = <span class="text-[#E8282B]">await</span> Elevix.<span class="text-[#A3A3A3]">build</span>({
                                    <div class="pl-4 border-l border-white/10 ml-1 my-1">
                                        stack: <span class="text-[#E8282B]">'Next.js'</span>,<br>
                                        perf: <span class="text-[#E8282B]">99.9</span>
                                    </div>
                                });
                            </div>
                            <div class="mt-3 flex items-center gap-1.5">
                                <span class="text-kinetic-red font-bold">></span>
                                <!-- GSAP Typewriter target -->
                                <span id="typewriter-target" class="text-white font-bold tracking-wider"></span><span class="animate-pulse bg-white w-1.5 h-3 inline-block ml-0.5"></span>
                            </div>
                        </div>
                        <!-- Scanline inside terminal -->
                        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-kinetic-red/10 to-transparent h-[200%] animate-[scan_3s_linear_infinite] pointer-events-none"></div>
                    </div>
                </div>
                
                <script>
                    document.addEventListener('DOMContentLoaded', () => {
                        // Ensure GSAP TextPlugin is available
                        if(window.gsap && window.gsap.plugins && window.gsap.plugins.TextPlugin) {
                            setTimeout(() => {
                                gsap.to('#typewriter-target', {
                                    duration: 2.0,
                                    text: "SYSTEM LIVE.",
                                    ease: "none"
                                });
                            }, 1000);
                        } else {
                            // Fallback if plugin isn't loaded
                            var el = document.getElementById('typewriter-target');
                            if(el) el.innerText = "SYSTEM LIVE.";
                        }
                    });
                </script>
"""
    
    text = text[:start_idx] + new_hero + text[end_idx:]
    with open('c:/Elevix Digital/services sub folder/web-development.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully rebuilt the hero with custom HTML flowchart and safe code block placement.")
else:
    print("Could not find start/end markers.")
