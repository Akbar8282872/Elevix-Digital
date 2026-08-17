import re

with open('c:/Elevix Digital/our-story.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_grid = """            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-8 border-t border-l border-white/10 max-w-4xl mx-auto">
                <!-- Team 1 -->
                <div class="service-card p-10 border-r border-b border-white/10 flex flex-col items-start hover:bg-white/5 transition-all duration-700 hover:scale-[1.03] hover:-translate-y-3 hover:shadow-[0_20px_50px_rgba(232,40,43,0.3)] relative group cursor-pointer overflow-hidden transform-gpu">
                    <div class="absolute inset-0 bg-[radial-gradient(circle_at_var(--mouse-x)_var(--mouse-y),rgba(232,40,43,0.15)_0%,transparent_50%)] opacity-0 group-hover:opacity-100 transition-opacity duration-500 rounded-lg"></div>
                    <div class="w-12 h-12 rounded-full border-2 border-kinetic-red/50 text-kinetic-red font-mono text-[14px] font-bold flex items-center justify-center mb-8 shadow-[0_0_15px_rgba(232,40,43,0.3)]">AC</div>
                    <h3 class="font-display text-[24px] font-bold text-white mb-2 group-hover:text-kinetic-red transition-colors relative z-10">Aziz Cheema</h3>
                    <p class="font-mono text-[11px] text-on-secondary-container tracking-widest uppercase mb-6 relative z-10">Founder & CEO</p>
                    <p class="font-display text-[14px] text-white/50 leading-[1.6] relative z-10">Revenue strategy, partnerships, and the business engine behind Elevix growth.</p>
                </div>
                <!-- Team 2 -->
                <div class="service-card p-10 border-r border-b border-white/10 flex flex-col items-start hover:bg-white/5 transition-all duration-700 hover:scale-[1.03] hover:-translate-y-3 hover:shadow-[0_20px_50px_rgba(232,40,43,0.3)] relative group cursor-pointer overflow-hidden transform-gpu">
                    <div class="absolute inset-0 bg-[radial-gradient(circle_at_var(--mouse-x)_var(--mouse-y),rgba(232,40,43,0.15)_0%,transparent_50%)] opacity-0 group-hover:opacity-100 transition-opacity duration-500 rounded-lg"></div>
                    <div class="w-12 h-12 rounded-full border-2 border-kinetic-red/50 text-kinetic-red font-mono text-[14px] font-bold flex items-center justify-center mb-8 shadow-[0_0_15px_rgba(232,40,43,0.3)]">AR</div>
                    <h3 class="font-display text-[24px] font-bold text-white mb-2 group-hover:text-kinetic-red transition-colors relative z-10">Ali Raja</h3>
                    <p class="font-mono text-[11px] text-on-secondary-container tracking-widest uppercase mb-6 relative z-10">Manager & Vibe Coder</p>
                    <p class="font-display text-[14px] text-white/50 leading-[1.6] relative z-10">Operations, delivery systems, and the rhythm that keeps every client engagement on track.</p>
                </div>
            </div>"""

new_grid = """            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-7xl mx-auto">
                <!-- Team 1 -->
                <div class="bg-[#111] border border-white/5 rounded-[12px] p-6 md:p-8 flex flex-row items-start gap-6 hover:bg-[#150a0a] hover:border-kinetic-red/30 transition-all duration-300 group shadow-lg hover:-translate-y-2">
                    <div class="w-14 h-14 rounded-full border border-kinetic-red/30 text-kinetic-red font-mono text-[14px] font-bold flex items-center justify-center flex-shrink-0 group-hover:border-kinetic-red group-hover:shadow-[0_0_15px_rgba(232,40,43,0.3)] transition-all">AC</div>
                    <div class="flex flex-col">
                        <span class="font-mono text-[10px] text-white/40 tracking-[0.2em] uppercase font-bold mb-2">LEADERSHIP</span>
                        <h3 class="font-display text-[22px] font-bold text-white mb-1 group-hover:text-kinetic-red transition-colors">Aziz Cheema</h3>
                        <p class="font-display text-[14px] text-kinetic-red mb-4">Founder & CEO</p>
                        <p class="font-display text-[13px] text-white/50 leading-[1.6]">Revenue strategy, partnerships, and the business engine behind Elevix growth.</p>
                    </div>
                </div>

                <!-- Team 2 -->
                <div class="bg-[#111] border border-white/5 rounded-[12px] p-6 md:p-8 flex flex-row items-start gap-6 hover:bg-[#150a0a] hover:border-kinetic-red/30 transition-all duration-300 group shadow-lg hover:-translate-y-2">
                    <div class="w-14 h-14 rounded-full border border-kinetic-red/30 text-kinetic-red font-mono text-[14px] font-bold flex items-center justify-center flex-shrink-0 group-hover:border-kinetic-red group-hover:shadow-[0_0_15px_rgba(232,40,43,0.3)] transition-all">AR</div>
                    <div class="flex flex-col">
                        <span class="font-mono text-[10px] text-white/40 tracking-[0.2em] uppercase font-bold mb-2">OPERATIONS</span>
                        <h3 class="font-display text-[22px] font-bold text-white mb-1 group-hover:text-kinetic-red transition-colors">Ali Raja</h3>
                        <p class="font-display text-[14px] text-kinetic-red mb-4">Manager & Vibe Coder</p>
                        <p class="font-display text-[13px] text-white/50 leading-[1.6]">Operations, delivery systems, and the rhythm that keeps every client engagement on track.</p>
                    </div>
                </div>

                <!-- Team 3 -->
                <div class="bg-[#111] border border-white/5 rounded-[12px] p-6 md:p-8 flex flex-row items-start gap-6 hover:bg-[#150a0a] hover:border-kinetic-red/30 transition-all duration-300 group shadow-lg hover:-translate-y-2">
                    <div class="w-14 h-14 rounded-full border border-kinetic-red/30 text-kinetic-red font-mono text-[14px] font-bold flex items-center justify-center flex-shrink-0 group-hover:border-kinetic-red group-hover:shadow-[0_0_15px_rgba(232,40,43,0.3)] transition-all">AH</div>
                    <div class="flex flex-col">
                        <span class="font-mono text-[10px] text-white/40 tracking-[0.2em] uppercase font-bold mb-2">OPERATIONS</span>
                        <h3 class="font-display text-[22px] font-bold text-white mb-1 group-hover:text-kinetic-red transition-colors">Ahad</h3>
                        <p class="font-display text-[14px] text-kinetic-red mb-4">HR & Admin Executive</p>
                        <p class="font-display text-[13px] text-white/50 leading-[1.6]">HR, talent acquisition, and office administration &mdash; building the culture and back-office spine of the agency.</p>
                    </div>
                </div>

                <!-- Team 4 -->
                <div class="bg-[#111] border border-white/5 rounded-[12px] p-6 md:p-8 flex flex-row items-start gap-6 hover:bg-[#150a0a] hover:border-kinetic-red/30 transition-all duration-300 group shadow-lg hover:-translate-y-2">
                    <div class="w-14 h-14 rounded-full border border-kinetic-red/30 text-kinetic-red font-mono text-[14px] font-bold flex items-center justify-center flex-shrink-0 group-hover:border-kinetic-red group-hover:shadow-[0_0_15px_rgba(232,40,43,0.3)] transition-all">AM</div>
                    <div class="flex flex-col">
                        <span class="font-mono text-[10px] text-white/40 tracking-[0.2em] uppercase font-bold mb-2">GROWTH</span>
                        <h3 class="font-display text-[22px] font-bold text-white mb-1 group-hover:text-kinetic-red transition-colors">Ahmed</h3>
                        <p class="font-display text-[14px] text-kinetic-red mb-4">Marketer</p>
                        <p class="font-display text-[13px] text-white/50 leading-[1.6]">Crafting campaigns, managing ad spend, and driving targeted traffic to maximize client ROI.</p>
                    </div>
                </div>

                <!-- Team 5 -->
                <div class="bg-[#111] border border-white/5 rounded-[12px] p-6 md:p-8 flex flex-row items-start gap-6 hover:bg-[#150a0a] hover:border-kinetic-red/30 transition-all duration-300 group shadow-lg hover:-translate-y-2">
                    <div class="w-14 h-14 rounded-full border border-kinetic-red/30 text-kinetic-red font-mono text-[14px] font-bold flex items-center justify-center flex-shrink-0 group-hover:border-kinetic-red group-hover:shadow-[0_0_15px_rgba(232,40,43,0.3)] transition-all">FT</div>
                    <div class="flex flex-col">
                        <span class="font-mono text-[10px] text-white/40 tracking-[0.2em] uppercase font-bold mb-2">GROWTH</span>
                        <h3 class="font-display text-[22px] font-bold text-white mb-1 group-hover:text-kinetic-red transition-colors">Fatima</h3>
                        <p class="font-display text-[14px] text-kinetic-red mb-4">Digital Marketer</p>
                        <p class="font-display text-[13px] text-white/50 leading-[1.6]">Executing comprehensive digital strategies, social media management, and online brand growth.</p>
                    </div>
                </div>

                <!-- Team 6 -->
                <div class="bg-[#111] border border-white/5 rounded-[12px] p-6 md:p-8 flex flex-row items-start gap-6 hover:bg-[#150a0a] hover:border-kinetic-red/30 transition-all duration-300 group shadow-lg hover:-translate-y-2">
                    <div class="w-14 h-14 rounded-full border border-kinetic-red/30 text-kinetic-red font-mono text-[14px] font-bold flex items-center justify-center flex-shrink-0 group-hover:border-kinetic-red group-hover:shadow-[0_0_15px_rgba(232,40,43,0.3)] transition-all">SD</div>
                    <div class="flex flex-col">
                        <span class="font-mono text-[10px] text-white/40 tracking-[0.2em] uppercase font-bold mb-2">CREATIVE</span>
                        <h3 class="font-display text-[22px] font-bold text-white mb-1 group-hover:text-kinetic-red transition-colors">Saad</h3>
                        <p class="font-display text-[14px] text-kinetic-red mb-4">Video Editor</p>
                        <p class="font-display text-[13px] text-white/50 leading-[1.6]">Editing high-retention video content, motion graphics, and visual storytelling for client campaigns.</p>
                    </div>
                </div>
            </div>"""

if old_grid in content:
    content = content.replace(old_grid, new_grid)
    with open('c:/Elevix Digital/our-story.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced team grid!")
else:
    print("Could not find the old grid to replace. Please check the content.")
