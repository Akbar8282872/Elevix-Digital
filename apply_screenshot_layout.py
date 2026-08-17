import re

with open('c:/Elevix Digital/services sub folder/web-development.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix Breadcrumbs exactly like the screenshot
start_marker_bread = '<!-- Breadcrumbs -->'
end_marker_bread = '<div class="grid grid-cols-1 lg:grid-cols-2 gap-16">'

start_idx_b = text.find(start_marker_bread)
end_idx_b = text.find(end_marker_bread)

if start_idx_b != -1 and end_idx_b != -1:
    new_breadcrumbs = """<!-- Breadcrumbs -->
            <div class="flex items-center gap-2 text-white/50 text-[14px] font-display mb-16 relative z-50">
                <a href="../index.html" class="hover:text-white transition-colors cursor-pointer">Home</a>
                <span class="text-white/30 text-[12px]">/</span>
                <a href="../services.html" class="hover:text-white transition-colors cursor-pointer">Services</a>
                <span class="text-white/30 text-[12px]">/</span>
                <span class="text-white font-semibold">Web Development</span>
            </div>

            """
    text = text[:start_idx_b] + new_breadcrumbs + text[end_idx_b:]

# 2. Fix the Right Side to match the ultra-premium screenshot style
start_marker_right = '<!-- Right Side: Combined Flowchart + Terminal -->'
end_marker_right = '<script>\n                    document.addEventListener(\'DOMContentLoaded\''

start_idx_r = text.find(start_marker_right)
end_idx_r = text.find(end_marker_right)

if start_idx_r != -1 and end_idx_r != -1:
    new_right_side = """<!-- Right Side: Combined Flowchart + Terminal -->
            <div class="w-full relative flex justify-end items-center mt-12 lg:mt-0 pr-4 lg:pr-8 h-[500px]">
                
                <!-- BACKGROUND GLOW -->
                <div class="absolute inset-0 bg-kinetic-red/10 blur-[100px] z-0 animate-[pulse_6s_infinite]"></div>

                <!-- THE ANIMATED TERMINAL CODE BLOCK (Positioned top-left of the cluster) -->
                <div class="absolute top-0 right-[20%] z-20 w-[320px] transform hover:scale-[1.02] transition-transform duration-500 hidden md:block group">
                    <div class="relative bg-[#0F0F0F]/90 backdrop-blur-md border border-white/5 rounded-xl shadow-[0_20px_40px_rgba(0,0,0,0.8)] flex flex-col overflow-hidden">
                        <!-- Code text -->
                        <div class="p-6 font-mono text-[11px] leading-[1.8]">
                            <div class="text-white/80">export default function Page() {</div>
                            <div class="text-white/80 pl-4">return (</div>
                            <div class="text-white/60 pl-8"><main className="hero"></div>
                            
                            <div class="pl-12 text-kinetic-red drop-shadow-[0_0_5px_rgba(232,40,43,0.5)]"><Nav /></div>
                            <div class="pl-12 text-white/90"><Hero title...</div>
                            <div class="pl-12 text-[#A3A3A3]"><Features /></div>
                            <div class="pl-12 text-white/90"><Footer /></div>

                            <div class="text-white/60 pl-8"></main></div>
                            <div class="text-white/80 pl-4">)</div>
                            <div class="text-white/80">}</div>
                            
                            <!-- Blinking cursor -->
                            <div class="mt-2 w-2 h-4 bg-kinetic-red animate-pulse"></div>
                        </div>
                    </div>
                </div>

                <!-- ULTRA-PREMIUM GLASS FLOWCHART (Positioned bottom-right, overlapping) -->
                <div class="absolute top-[30%] right-0 z-30 w-[380px] perspective-[1000px] animate-[float_8s_ease-in-out_infinite_reverse]">
                    <div class="relative bg-[#111111]/80 backdrop-blur-2xl border border-white/10 rounded-2xl p-8 shadow-[0_30px_60px_rgba(0,0,0,0.9)] transform rotate-y-[-5deg] rotate-x-[2deg] hover:rotate-y-[0deg] hover:rotate-x-[0deg] transition-all duration-[600ms] hover:border-kinetic-red/30">
                        
                        <!-- Header -->
                        <div class="flex items-center justify-between mb-8">
                            <div class="flex items-center gap-3">
                                <div class="w-8 h-[1px] bg-kinetic-red/50"></div>
                                <span class="font-mono text-[10px] text-white/50 tracking-[0.2em] uppercase">Architecture</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <div class="w-2 h-2 rounded-full bg-kinetic-red animate-pulse shadow-[0_0_8px_rgba(232,40,43,1)]"></div>
                                <span class="font-mono text-[10px] text-kinetic-red tracking-widest">LIVE</span>
                            </div>
                        </div>

                        <!-- Rows -->
                        <div class="flex flex-col gap-5">
                            <!-- Row 1 -->
                            <div class="flex items-center justify-between border-b border-white/5 pb-4 group/row cursor-default">
                                <span class="font-mono text-[11px] text-white/60 tracking-widest uppercase group-hover/row:text-white transition-colors">1. Navbar</span>
                                <span class="font-mono text-[11px] text-white tracking-widest group-hover/row:text-kinetic-red transition-colors text-right">GLOBAL COMPONENT</span>
                            </div>
                            <!-- Row 2 -->
                            <div class="flex items-center justify-between border-b border-white/5 pb-4 group/row cursor-default">
                                <span class="font-mono text-[11px] text-white/60 tracking-widest uppercase group-hover/row:text-white transition-colors">2. Hero</span>
                                <span class="font-mono text-[11px] text-white tracking-widest group-hover/row:text-kinetic-red transition-colors text-right">CONVERSION OPTIMIZED</span>
                            </div>
                            <!-- Row 3 -->
                            <div class="flex items-center justify-between border-b border-white/5 pb-4 group/row cursor-default">
                                <span class="font-mono text-[11px] text-white/60 tracking-widest uppercase group-hover/row:text-white transition-colors">3. Features</span>
                                <span class="font-mono text-[11px] text-kinetic-red tracking-widest text-right drop-shadow-[0_0_5px_rgba(232,40,43,0.5)]">UI / UX ANIMATED</span>
                            </div>
                            <!-- Row 4 -->
                            <div class="flex items-center justify-between border-b border-white/5 pb-4 group/row cursor-default">
                                <span class="font-mono text-[11px] text-white/60 tracking-widest uppercase group-hover/row:text-white transition-colors">4. CTA Block</span>
                                <span class="font-mono text-[11px] text-white tracking-widest group-hover/row:text-kinetic-red transition-colors text-right">MAGNETIC HOVER</span>
                            </div>
                            <!-- Row 5 -->
                            <div class="flex items-center justify-between group/row cursor-default">
                                <span class="font-mono text-[11px] text-white/60 tracking-widest uppercase group-hover/row:text-white transition-colors">5. Footer</span>
                                <span class="font-mono text-[11px] text-white tracking-widest group-hover/row:text-kinetic-red transition-colors text-right">MEGA MENU LINKS</span>
                            </div>
                        </div>

                        <!-- Subtle red glow at bottom of card -->
                        <div class="absolute bottom-0 left-0 right-0 h-1/3 bg-gradient-to-t from-kinetic-red/5 to-transparent rounded-b-2xl pointer-events-none"></div>
                    </div>
                </div>

                """
    
    text = text[:start_idx_r] + new_right_side + text[end_idx_r:]

with open('c:/Elevix Digital/services sub folder/web-development.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied exact screenshot layout style and fixed breadcrumb typography!")
