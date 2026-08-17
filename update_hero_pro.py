import re

with open('c:/Elevix Digital/services sub folder/web-development.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the entire Hero section again
start_marker = '<!-- 2. Hero Content -->'
end_marker = '</main>'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_hero = """<!-- 2. Hero Content -->
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-16 relative z-10 w-full mt-12 pb-24">
            
            <!-- Left Side: Typography & New Text/Buttons -->
            <div class="w-full md:w-[50%] flex flex-col gap-6 justify-start z-20">
                
                <!-- Breadcrumbs EXACTLY like services.html -->
                <div class="flex items-center gap-4 text-on-secondary-container text-sm font-mono tracking-widest mb-2 uppercase">
                    <a href="../index.html" class="hover:text-white transition-colors cursor-pointer">Home</a>
                    <span class="text-white/30">/</span>
                    <a href="../services.html" class="hover:text-white transition-colors cursor-pointer">Services</a>
                    <span class="text-white/30">/</span>
                    <span class="text-white drop-shadow-[0_0_10px_rgba(255,255,255,0.5)]">Web Development</span>
                </div>

                <!-- Main Headline -->
                <h1 class="font-display font-black text-white text-[56px] md:text-[60px] leading-[1.05] tracking-tight mt-4 max-w-xl relative z-10">
                    The website development company<br>
                    engineered to scale,<br>
                    <span class="text-kinetic-red drop-shadow-[0_0_20px_rgba(232,40,43,0.3)]">Elevix Digital.</span>
                </h1>

                <!-- NEW PARAGRAPH FROM SCREENSHOT -->
                <p class="text-white/60 font-display text-[15px] leading-[1.8] mt-4 max-w-xl">
                    Web development Kerala — a Kochi-based website development company shipping Next.js, WordPress, Shopify, and custom web development. Engineered for Core Web Vitals, SEO, and conversion from day one. No plugin bloat, no template churn, no rip-and-replace at scale. Every build ships to a Lighthouse 90+ performance budget.
                </p>

                <!-- NEW BUTTONS FROM SCREENSHOT -->
                <div class="flex items-center gap-8 mt-6">
                    <button class="bg-[#E8282B] text-white px-8 py-3.5 rounded-[100px] text-[15px] font-bold hover:bg-[#ff3333] transition-all shadow-[0_0_20px_rgba(232,40,43,0.4)] hover:shadow-[0_0_30px_rgba(232,40,43,0.6)] flex items-center gap-2 group">
                        Book a Strategy Call
                        <svg class="transform group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                    </button>
                    <a href="../case-studies.html" class="text-white/50 hover:text-white transition-colors text-[14px] font-medium flex items-center gap-2 group">
                        See case studies
                        <svg class="transform group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                    </a>
                </div>
            </div>

            <!-- Right Side: Best Professional 3D Animation & Down Code Block -->
            <div class="w-full md:w-[50%] relative flex flex-col items-center justify-center gap-8 mt-12 md:mt-0 perspective-[2000px] z-10">
                
                <!-- BACKGROUND GLOW -->
                <div class="absolute inset-0 bg-kinetic-red/10 blur-[150px] z-0 animate-[pulse_6s_infinite] pointer-events-none"></div>

                <!-- ELITE 3D GLASS UI STACK (Professional Web Architecture Diagram) -->
                <div class="relative w-[320px] h-[320px] sm:w-[400px] sm:h-[400px] z-10 mx-auto" style="transform-style: preserve-3d; transform: rotateX(60deg) rotateZ(-45deg);">
                    
                    <!-- CSS to drive the continuous rotation of the stack -->
                    <style>
                        @keyframes spin-stack {
                            0% { transform: rotateX(60deg) rotateZ(0deg); }
                            100% { transform: rotateX(60deg) rotateZ(360deg); }
                        }
                        .animate-spin-stack {
                            animation: spin-stack 30s linear infinite;
                            transform-style: preserve-3d;
                        }
                        .glass-panel-3d {
                            background: rgba(255,255,255,0.03);
                            backdrop-filter: blur(8px);
                            -webkit-backdrop-filter: blur(8px);
                            border: 1px solid rgba(255,255,255,0.1);
                        }
                        .glass-panel-red {
                            background: rgba(232,40,43,0.05);
                            backdrop-filter: blur(12px);
                            -webkit-backdrop-filter: blur(12px);
                            border: 1px solid rgba(232,40,43,0.3);
                        }
                    </style>
                    
                    <div class="absolute inset-0 animate-spin-stack w-full h-full">
                        
                        <!-- Top Layer: UI / Frontend -->
                        <div class="absolute inset-0 w-full h-full glass-panel-3d rounded-2xl shadow-[0_20px_50px_rgba(0,0,0,0.5)] overflow-hidden" style="transform: translateZ(140px);">
                            <!-- Mock UI Header -->
                            <div class="w-full h-10 border-b border-white/10 flex items-center px-4 gap-2 bg-white/5">
                                <div class="w-2.5 h-2.5 rounded-full bg-[#FF5F56]"></div>
                                <div class="w-2.5 h-2.5 rounded-full bg-[#FFBD2E]"></div>
                                <div class="w-2.5 h-2.5 rounded-full bg-[#27C93F]"></div>
                                <div class="ml-auto flex gap-2">
                                    <div class="w-8 h-1.5 rounded-full bg-white/20"></div>
                                    <div class="w-8 h-1.5 rounded-full bg-white/20"></div>
                                </div>
                            </div>
                            <!-- Mock Content -->
                            <div class="p-6 flex flex-col gap-4">
                                <div class="w-3/4 h-4 rounded bg-white/20"></div>
                                <div class="w-1/2 h-3 rounded bg-white/10"></div>
                                <div class="grid grid-cols-2 gap-4 mt-4">
                                    <div class="h-24 rounded-lg bg-white/5 border border-white/10 relative overflow-hidden">
                                        <div class="absolute inset-0 bg-gradient-to-tr from-kinetic-red/20 to-transparent"></div>
                                    </div>
                                    <div class="h-24 rounded-lg bg-white/5 border border-white/10 relative overflow-hidden">
                                        <div class="absolute inset-0 bg-gradient-to-bl from-white/10 to-transparent"></div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Middle Layer: Logic / API Core -->
                        <div class="absolute inset-8 w-[calc(100%-4rem)] h-[calc(100%-4rem)] glass-panel-red rounded-full shadow-[0_0_60px_rgba(232,40,43,0.3)] flex items-center justify-center" style="transform: translateZ(70px);">
                            <div class="w-full h-full rounded-full border border-kinetic-red/30 border-dashed animate-[spin_10s_linear_infinite] flex items-center justify-center">
                                <div class="w-24 h-24 rounded-full bg-kinetic-red/20 flex items-center justify-center animate-pulse shadow-[0_0_30px_rgba(232,40,43,0.8)]">
                                    <div class="w-8 h-8 bg-kinetic-red rounded-full"></div>
                                </div>
                            </div>
                        </div>

                        <!-- Bottom Layer: Database / Infrastructure -->
                        <div class="absolute inset-0 w-full h-full bg-[#0A0A0A]/80 border border-white/5 backdrop-blur-3xl rounded-2xl shadow-[0_40px_100px_rgba(0,0,0,0.9)] p-8 grid grid-cols-4 grid-rows-4 gap-3" style="transform: translateZ(0px);">
                            <div class="bg-white/5 rounded-md animate-pulse"></div>
                            <div class="bg-white/5 rounded-md animate-pulse" style="animation-delay: 0.1s"></div>
                            <div class="bg-kinetic-red/30 rounded-md shadow-[0_0_15px_rgba(232,40,43,0.5)]"></div>
                            <div class="bg-white/5 rounded-md animate-pulse" style="animation-delay: 0.3s"></div>
                            
                            <div class="bg-white/5 rounded-md animate-pulse" style="animation-delay: 0.4s"></div>
                            <div class="bg-kinetic-red/30 rounded-md shadow-[0_0_15px_rgba(232,40,43,0.5)]"></div>
                            <div class="bg-white/5 rounded-md animate-pulse" style="animation-delay: 0.6s"></div>
                            <div class="bg-white/5 rounded-md animate-pulse" style="animation-delay: 0.7s"></div>

                            <div class="bg-kinetic-red/30 rounded-md shadow-[0_0_15px_rgba(232,40,43,0.5)]"></div>
                            <div class="bg-white/5 rounded-md animate-pulse" style="animation-delay: 0.9s"></div>
                            <div class="bg-white/5 rounded-md animate-pulse" style="animation-delay: 1.0s"></div>
                            <div class="bg-white/5 rounded-md animate-pulse" style="animation-delay: 1.1s"></div>
                            
                            <div class="bg-white/5 rounded-md animate-pulse" style="animation-delay: 1.2s"></div>
                            <div class="bg-white/5 rounded-md animate-pulse" style="animation-delay: 1.3s"></div>
                            <div class="bg-kinetic-red/30 rounded-md shadow-[0_0_15px_rgba(232,40,43,0.5)]"></div>
                            <div class="bg-white/5 rounded-md animate-pulse" style="animation-delay: 1.5s"></div>
                        </div>

                        <!-- Data Link Beams (Vertical connections) -->
                        <div class="absolute left-1/4 top-1/4 w-[2px] h-[140px] bg-gradient-to-b from-white to-kinetic-red/10 shadow-[0_0_15px_rgba(255,255,255,1)]" style="transform: translateZ(0px) rotateX(-90deg); transform-origin: bottom;"></div>
                        <div class="absolute right-1/4 bottom-1/4 w-[2px] h-[140px] bg-gradient-to-b from-kinetic-red to-kinetic-red/10 shadow-[0_0_20px_rgba(232,40,43,1)]" style="transform: translateZ(0px) rotateX(-90deg); transform-origin: bottom;"></div>

                    </div>
                </div>

                <!-- 2. THE ANIMATED TERMINAL CODE BLOCK (MOVED DOWN) -->
                <div class="relative w-full max-w-[360px] bg-[#0A0A0A]/95 backdrop-blur-2xl border border-white/10 rounded-xl shadow-[0_30px_60px_rgba(0,0,0,0.9)] overflow-hidden transform hover:scale-[1.02] hover:border-kinetic-red/40 transition-all duration-500 z-30 mx-auto -mt-20 lg:-mt-10 lg:ml-auto">
                    <div class="h-8 border-b border-white/10 flex items-center px-4 justify-between bg-white/5">
                        <div class="flex gap-1.5">
                            <div class="w-2.5 h-2.5 rounded-full bg-[#FF5F56]"></div>
                            <div class="w-2.5 h-2.5 rounded-full bg-[#FFBD2E]"></div>
                            <div class="w-2.5 h-2.5 rounded-full bg-[#27C93F]"></div>
                        </div>
                        <span class="text-[9px] font-mono tracking-widest text-white/40 uppercase">Architecture.js</span>
                    </div>
                    <div class="p-5 font-mono text-[11px] leading-[1.8] text-white/70">
                        <span class="text-[#E8282B] font-bold">import</span> { Scale } <span class="text-[#E8282B] font-bold">from</span> <span class="text-[#A3A3A3]">'@elevix/core'</span>;<br><br>
                        <span class="text-[#E8282B] font-bold">const</span> app = <span class="text-[#E8282B] font-bold">await</span> Scale.<span class="text-white">init</span>({<br>
                        &nbsp;&nbsp;engine: <span class="text-[#A3A3A3]">'Next.js'</span>,<br>
                        &nbsp;&nbsp;budget: <span class="text-[#A3A3A3]">'Lighthouse 90+'</span>,<br>
                        &nbsp;&nbsp;status: <span class="text-[#A3A3A3]">'Online'</span><br>
                        });<br><br>
                        <span class="text-kinetic-red font-bold">></span> <span id="typewriter-target" class="text-white font-bold tracking-widest"></span><span class="animate-pulse bg-white w-1.5 h-3 inline-block ml-0.5 align-middle"></span>
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
    
    text = text[:start_idx] + new_hero + "\n    " + text[end_idx:]
    
    with open('c:/Elevix Digital/services sub folder/web-development.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Injected ultra-premium 3D layout, moved code block down, and added left side screenshot text.")
else:
    print("Could not find markers.")
