import re

with open('c:/Elevix Digital/services sub folder/web-development.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Breadcrumbs
old_breadcrumbs = """                <!-- Breadcrumbs -->
                <div class="flex items-center gap-3 text-[13px] font-display text-white/50 mb-10">
                    <a href="../index.html" class="hover:text-white transition-colors cursor-pointer">Home</a>
                    <span class="opacity-30">/</span>
                    <a href="../services.html" class="hover:text-white transition-colors cursor-pointer">Services</a>
                    <span class="opacity-30">/</span>
                    <span class="text-white font-bold">Web Development</span>
                </div>"""

new_breadcrumbs = """                <!-- Breadcrumbs -->
                <div class="flex items-center gap-4 text-on-secondary-container text-[13px] md:text-sm font-mono tracking-widest mb-12 uppercase">
                    <a href="../index.html" class="hover:text-white transition-colors cursor-pointer">Home</a>
                    <span class="text-white/30">/</span>
                    <a href="../services.html" class="hover:text-white transition-colors cursor-pointer">Services</a>
                    <span class="text-white/30">/</span>
                    <span class="text-white font-bold">Web Development</span>
                </div>"""

text = text.replace(old_breadcrumbs, new_breadcrumbs)

# 2. Update Right Side to Premium Animated Flowchart Image
start_marker = '<!-- FABULOUS ANIMATED RIGHT SIDE -->'
end_marker = '</div>\n            </div>\n        </div>\n    </main>'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    premium_image_block = """<!-- Premium Animated Flowchart Image Container -->
                <div class="relative w-full max-w-[400px] group perspective-[1000px] z-10 mx-auto lg:ml-auto">
                    <!-- Glowing aura behind the image -->
                    <div class="absolute inset-0 bg-kinetic-red/30 blur-[60px] group-hover:bg-kinetic-red/50 transition-colors duration-1000 animate-[pulse_4s_infinite]"></div>
                    
                    <!-- Levitating Image Wrapper -->
                    <div class="relative w-full rounded-2xl overflow-hidden border border-white/10 bg-[#0A0A0A]/40 backdrop-blur-2xl shadow-[0_30px_60px_rgba(0,0,0,0.9)] transform transition-transform duration-[800ms] hover:scale-[1.05] hover:rotate-y-[-5deg] animate-[float_6s_ease-in-out_infinite] group-hover:border-kinetic-red/50 group-hover:shadow-[0_30px_80px_rgba(232,40,43,0.3)]">
                        <!-- Glass reflection -->
                        <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none z-10"></div>
                        
                        <!-- Shine effect on hover -->
                        <div class="absolute top-0 left-[-100%] w-[50%] h-[200%] bg-gradient-to-r from-transparent via-white/10 to-transparent transform -rotate-45 translate-y-[-20%] group-hover:animate-[shine_1.5s_ease-in-out] pointer-events-none z-20"></div>
                        
                        <!-- The Generated Flowchart Image -->
                        <img src="../web_architecture_chart.png" alt="Web Architecture Flowchart" class="w-full h-auto object-cover relative z-0 opacity-90 group-hover:opacity-100 transition-all duration-700" />
                        
                        <!-- Subtle red tint overlay -->
                        <div class="absolute inset-0 bg-kinetic-red mix-blend-overlay opacity-20 pointer-events-none z-10"></div>
                    </div>
                    
                    <!-- Floating decorative particles -->
                    <div class="absolute -top-6 -right-6 w-3 h-3 bg-kinetic-red rounded-full shadow-[0_0_15px_rgba(232,40,43,1)] animate-[float_4s_ease-in-out_infinite_reverse]"></div>
                    <div class="absolute -bottom-4 -left-4 w-2 h-2 bg-white rounded-full shadow-[0_0_10px_rgba(255,255,255,1)] animate-[float_5s_ease-in-out_infinite]"></div>
                </div>
"""
    
    text = text[:start_idx] + premium_image_block + text[end_idx:]

with open('c:/Elevix Digital/services sub folder/web-development.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Restored image with ultra-premium animations and fixed breadcrumbs!")
