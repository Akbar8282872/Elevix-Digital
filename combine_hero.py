import re

with open('c:/Elevix Digital/services sub folder/web-development.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the entire right side with the combined image + floating terminal
start_marker = '<!-- Premium Animated Flowchart Image Container -->'
end_marker = '</div>\n            </div>\n        </div>\n    </main>'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    combined_block = """<!-- Premium Animated Flowchart Image Container -->
                <div class="relative w-full max-w-[420px] group perspective-[1000px] z-10 mx-auto lg:ml-auto">
                    <!-- Glowing aura behind the image -->
                    <div class="absolute inset-0 bg-kinetic-red/30 blur-[60px] group-hover:bg-kinetic-red/50 transition-colors duration-1000 animate-[pulse_4s_infinite]"></div>
                    
                    <!-- Levitating Image Wrapper -->
                    <div class="relative w-full rounded-2xl overflow-hidden border border-white/10 bg-[#0A0A0A]/40 backdrop-blur-2xl shadow-[0_30px_60px_rgba(0,0,0,0.9)] transform transition-transform duration-[800ms] hover:scale-[1.02] hover:rotate-y-[-5deg] animate-[float_6s_ease-in-out_infinite] group-hover:border-kinetic-red/50 group-hover:shadow-[0_30px_80px_rgba(232,40,43,0.3)]">
                        <!-- Glass reflection -->
                        <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none z-10"></div>
                        <div class="absolute top-0 left-[-100%] w-[50%] h-[200%] bg-gradient-to-r from-transparent via-white/10 to-transparent transform -rotate-45 translate-y-[-20%] group-hover:animate-[shine_1.5s_ease-in-out] pointer-events-none z-20"></div>
                        <img src="../web_architecture_chart.png" alt="Web Architecture Flowchart" class="w-full h-auto object-cover relative z-0 opacity-90 group-hover:opacity-100 transition-all duration-700" />
                        <div class="absolute inset-0 bg-kinetic-red mix-blend-overlay opacity-20 pointer-events-none z-10"></div>
                    </div>
                    
                    <!-- Floating decorative particles -->
                    <div class="absolute -top-6 -right-6 w-3 h-3 bg-kinetic-red rounded-full shadow-[0_0_15px_rgba(232,40,43,1)] animate-[float_4s_ease-in-out_infinite_reverse]"></div>
                    <div class="absolute -bottom-4 -left-4 w-2 h-2 bg-white rounded-full shadow-[0_0_10px_rgba(255,255,255,1)] animate-[float_5s_ease-in-out_infinite]"></div>

                    <!-- THE ANIMATED TERMINAL CODE BLOCK (Positioned top-right over the image) -->
                    <div class="absolute -top-12 -right-16 z-30 w-[260px] perspective-[1200px] animate-[float_7s_ease-in-out_infinite_reverse] hidden md:block">
                        <div class="relative bg-[#0A0A0A]/80 backdrop-blur-xl border border-white/10 rounded-xl shadow-[0_30px_60px_rgba(0,0,0,0.8)] flex flex-col overflow-hidden transform rotate-y-[-10deg] rotate-x-[5deg] hover:rotate-y-[0deg] hover:rotate-x-[0deg] transition-transform duration-[800ms] hover:border-kinetic-red/40 group">
                            
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
                                <div class="text-white/40 mb-2">// Scale protocol...</div>
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
    text = text[:start_idx] + combined_block + text[end_idx:]

with open('c:/Elevix Digital/services sub folder/web-development.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Injected the combined premium layout!")
