import re

with open('c:/Elevix Digital/services sub folder/web-development.html', 'r', encoding='utf-8') as f:
    text = f.read()

# We need to find the start of the right side container
# The container is the <div class="w-full relative flex justify-end items-center mt-12 lg:mt-0">
start_marker = '<!-- Right Side: Web Dev Map / Card -->'
end_marker = '</div>\n            </div>\n        </div>\n    </main>'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_right_side = """<!-- Right Side: Fabulous Animated Terminal -->
            <div class="w-full relative flex justify-end items-center mt-20 lg:mt-0 pr-8">
                
                <!-- FABULOUS ANIMATED RIGHT SIDE -->
                <div class="relative z-10 w-full max-w-[440px] h-[340px] perspective-[1200px]">
                    <!-- Outer Glowing Ring (Orbital) -->
                    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[420px] h-[420px] border border-white/5 rounded-full animate-[spin_20s_linear_infinite] pointer-events-none z-0">
                        <div class="absolute -top-1.5 left-1/2 -translate-x-1/2 w-3 h-3 bg-kinetic-red rounded-full shadow-[0_0_15px_rgba(232,40,43,1)]"></div>
                        <div class="absolute bottom-10 right-4 w-2 h-2 bg-white rounded-full shadow-[0_0_15px_rgba(255,255,255,0.8)]"></div>
                    </div>

                    <!-- Inner Dashed Ring -->
                    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[340px] h-[340px] border border-dashed border-white/10 rounded-full animate-[spin_30s_linear_infinite_reverse] pointer-events-none z-0"></div>

                    <!-- Main Glass Terminal -->
                    <div class="absolute inset-0 bg-[#0A0A0A]/70 backdrop-blur-xl border border-white/10 rounded-2xl shadow-[0_30px_60px_rgba(0,0,0,0.8)] flex flex-col overflow-hidden transform rotate-y-[-15deg] rotate-x-[5deg] hover:rotate-y-[0deg] hover:rotate-x-[0deg] transition-transform duration-[800ms] hover:border-kinetic-red/40 group z-10">
                        
                        <!-- Terminal Header -->
                        <div class="h-10 border-b border-white/10 flex items-center px-4 justify-between bg-white/5">
                            <div class="flex gap-2">
                                <div class="w-2.5 h-2.5 rounded-full bg-[#FF5F56]"></div>
                                <div class="w-2.5 h-2.5 rounded-full bg-[#FFBD2E]"></div>
                                <div class="w-2.5 h-2.5 rounded-full bg-[#27C93F]"></div>
                            </div>
                            <span class="text-[9px] font-mono tracking-widest text-white/30 uppercase">Elevix_Engine.js</span>
                        </div>

                        <!-- Typing Code Block -->
                        <div class="p-6 flex-1 font-mono text-[12px] md:text-[13px] leading-[1.8]">
                            <div class="text-white/40 mb-3">// Initializing scale protocol...</div>
                            <div class="text-[#E8282B] font-bold">import <span class="text-white">Elevix</span> from <span class="text-[#A3A3A3]">'@future/web'</span>;</div>
                            <div class="text-white mt-4">
                                <span class="text-[#E8282B]">const</span> <span class="text-white">project</span> = <span class="text-[#E8282B]">await</span> Elevix.<span class="text-[#A3A3A3]">build</span>({
                                    <div class="pl-6 border-l border-white/10 ml-2 my-1">
                                        architecture: <span class="text-[#E8282B]">'Next.js + AI'</span>,<br>
                                        performance: <span class="text-[#E8282B]">99.9</span>,<br>
                                        design: <span class="text-[#E8282B]">'Bespoke'</span>
                                    </div>
                                });
                            </div>
                            <div class="mt-4 flex items-center gap-2">
                                <span class="text-kinetic-red font-bold">></span>
                                <!-- GSAP Typewriter target -->
                                <span id="typewriter-target" class="text-white font-bold tracking-wider"></span><span class="animate-pulse bg-white w-2 h-4 inline-block ml-0.5"></span>
                            </div>
                        </div>

                        <!-- Scanline inside terminal -->
                        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-kinetic-red/5 to-transparent h-[200%] animate-[scan_3s_linear_infinite] pointer-events-none"></div>
                    </div>

                    <!-- Floating Tech Badge 1 -->
                    <div class="absolute -right-6 -bottom-6 bg-[#0A0A0A]/90 backdrop-blur-xl border border-white/10 rounded-xl p-4 shadow-2xl animate-[float_6s_ease-in-out_infinite] z-20 group-hover:border-kinetic-red/30 transition-colors duration-500">
                        <div class="flex items-center gap-4">
                            <div class="w-10 h-10 rounded-lg bg-kinetic-red/10 flex items-center justify-center border border-kinetic-red/20 relative overflow-hidden">
                                <div class="absolute inset-0 bg-kinetic-red/20 animate-pulse"></div>
                                <span class="font-black text-kinetic-red relative z-10">AI</span>
                            </div>
                            <div class="flex flex-col">
                                <span class="text-[9px] font-mono tracking-widest text-white/50 uppercase">Powered by</span>
                                <span class="text-xs font-bold text-white tracking-widest uppercase">Deep Learning</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Floating Tech Badge 2 (Top Left) -->
                    <div class="absolute -left-12 -top-6 bg-[#0A0A0A]/90 backdrop-blur-xl border border-white/10 rounded-xl px-4 py-2 shadow-2xl animate-[float_7s_ease-in-out_infinite_reverse] z-20">
                        <div class="flex items-center gap-2">
                            <span class="w-1.5 h-1.5 rounded-full bg-[#27C93F] animate-pulse"></span>
                            <span class="text-[9px] font-mono tracking-widest text-white uppercase font-bold">Systems Live</span>
                        </div>
                    </div>

                </div>
                
                <script>
                    document.addEventListener('DOMContentLoaded', () => {
                        // Ensure GSAP TextPlugin is available
                        if(window.gsap && window.gsap.plugins && window.gsap.plugins.TextPlugin) {
                            setTimeout(() => {
                                gsap.to('#typewriter-target', {
                                    duration: 2.5,
                                    text: "SYSTEM ONLINE. READY TO SCALE.",
                                    ease: "none"
                                });
                            }, 1000);
                        } else {
                            // Fallback if plugin isn't loaded for some reason
                            document.getElementById('typewriter-target').innerText = "SYSTEM ONLINE. READY TO SCALE.";
                        }
                    });
                </script>
"""
    
    text = text[:start_idx] + new_right_side + text[end_idx:]
    with open('c:/Elevix Digital/services sub folder/web-development.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully injected the fabulous animated hero!")
else:
    print("Could not find the target container!")

