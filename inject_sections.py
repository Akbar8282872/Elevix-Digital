import re
import os

with open('c:/Elevix Digital/contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_sections = """
    <!-- What Happens Next Section -->
    <section class="relative bg-deep-obsidian py-24 overflow-hidden z-10 border-t border-white/5">
        <div class="max-w-7xl mx-auto px-6 md:px-12 lg:px-16">
            <!-- Header -->
            <div class="flex items-center gap-4 mb-6">
                <div class="w-12 h-[1px] bg-kinetic-red"></div>
                <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] font-bold uppercase">// 03. WHAT HAPPENS NEXT</span>
            </div>
            
            <h2 class="font-display font-bold text-[45px] md:text-[60px] text-white leading-[1.05] tracking-tight mb-6">
                After you hit send.
            </h2>
            
            <p class="font-display text-[16px] text-[#999] leading-[1.7] max-w-2xl mb-16 font-medium">
                Four steps between your inbound and a signed plan. No black box. No "we'll be in touch" and silence.
            </p>
            
            <!-- 4 Cards Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                
                <!-- Card 1 -->
                <div class="bg-[#0a0a0a] border border-white/5 rounded-xl p-8 hover:border-kinetic-red/50 hover:-translate-y-1 hover:shadow-[0_10px_30px_rgba(232,40,43,0.1)] transition-all duration-300 group">
                    <div class="flex justify-between items-center mb-8 border-b border-white/5 pb-4">
                        <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] font-bold uppercase">// 01</span>
                        <div class="w-4 h-4 rounded-full border border-kinetic-red flex items-center justify-center">
                            <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="#E8282B" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                    </div>
                    <span class="font-mono text-[9px] text-[#666] tracking-[0.1em] font-bold uppercase mb-4 block">WITHIN MINUTES</span>
                    <h4 class="font-display font-bold text-[22px] text-white leading-tight mb-4 group-hover:text-kinetic-red transition-colors">Founder reads the inbound</h4>
                    <p class="font-display text-[14px] text-[#888] leading-relaxed">
                        Akbar or someone on the leadership bench reads it personally. No SDR, no ticket queue, no auto-router.
                    </p>
                </div>
                
                <!-- Card 2 -->
                <div class="bg-[#0a0a0a] border border-white/5 rounded-xl p-8 hover:border-kinetic-red/50 hover:-translate-y-1 hover:shadow-[0_10px_30px_rgba(232,40,43,0.1)] transition-all duration-300 group">
                    <div class="flex justify-between items-center mb-8 border-b border-white/5 pb-4">
                        <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] font-bold uppercase">// 02</span>
                        <div class="w-4 h-4 rounded-full border border-kinetic-red flex items-center justify-center">
                            <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="#E8282B" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                    </div>
                    <span class="font-mono text-[9px] text-[#666] tracking-[0.1em] font-bold uppercase mb-4 block">< 4 BUSINESS HOURS</span>
                    <h4 class="font-display font-bold text-[22px] text-white leading-tight mb-4 group-hover:text-kinetic-red transition-colors">We reply</h4>
                    <p class="font-display text-[14px] text-[#888] leading-relaxed">
                        Either a direct email with sharpened questions, or a booking link for a 30-min call. If we're not the right fit we tell you honestly.
                    </p>
                </div>
                
                <!-- Card 3 -->
                <div class="bg-[#0a0a0a] border border-white/5 rounded-xl p-8 hover:border-kinetic-red/50 hover:-translate-y-1 hover:shadow-[0_10px_30px_rgba(232,40,43,0.1)] transition-all duration-300 group">
                    <div class="flex justify-between items-center mb-8 border-b border-white/5 pb-4">
                        <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] font-bold uppercase">// 03</span>
                        <div class="w-4 h-4 rounded-full border border-kinetic-red flex items-center justify-center">
                            <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="#E8282B" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                    </div>
                    <span class="font-mono text-[9px] text-[#666] tracking-[0.1em] font-bold uppercase mb-4 block">DAY 1-3</span>
                    <h4 class="font-display font-bold text-[22px] text-white leading-tight mb-4 group-hover:text-kinetic-red transition-colors">Strategy call</h4>
                    <p class="font-display text-[14px] text-[#888] leading-relaxed">
                        Half an hour, honest. We pull context on your funnel, your numbers, your constraints. You walk out with at least one tactical unlock even if we never work together.
                    </p>
                </div>
                
                <!-- Card 4 -->
                <div class="bg-[#0a0a0a] border border-white/5 rounded-xl p-8 hover:border-kinetic-red/50 hover:-translate-y-1 hover:shadow-[0_10px_30px_rgba(232,40,43,0.1)] transition-all duration-300 group">
                    <div class="flex justify-between items-center mb-8 border-b border-white/5 pb-4">
                        <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] font-bold uppercase">// 04</span>
                        <div class="w-4 h-4 rounded-full border border-kinetic-red flex items-center justify-center">
                            <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="#E8282B" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                    </div>
                    <span class="font-mono text-[9px] text-[#666] tracking-[0.1em] font-bold uppercase mb-4 block">DAY 3-7</span>
                    <h4 class="font-display font-bold text-[22px] text-white leading-tight mb-4 group-hover:text-kinetic-red transition-colors">Plan in writing</h4>
                    <p class="font-display text-[14px] text-[#888] leading-relaxed">
                        If there's a fit, you get a scoped proposal &mdash; deliverables, timelines, pricing, and exit terms. Signed, starts the next week.
                    </p>
                </div>
                
            </div>
        </div>
    </section>

    <!-- By The Numbers Section -->
    <section class="relative bg-deep-obsidian pt-12 pb-32 overflow-hidden z-10 border-t border-white/5">
        <style>
            @keyframes marqueeLoop {
                0% { transform: translateX(0); }
                100% { transform: translateX(-50%); }
            }
            .animate-marquee {
                display: flex;
                width: max-content;
                animation: marqueeLoop 30s linear infinite;
            }
        </style>
        
        <div class="max-w-7xl mx-auto px-6 md:px-12 lg:px-16">
            <!-- Header -->
            <div class="flex items-center gap-4 mb-8">
                <div class="w-12 h-[1px] bg-kinetic-red"></div>
                <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] font-bold uppercase">// 04. BY THE NUMBERS</span>
            </div>
            
            <!-- Numbers Box -->
            <div class="bg-[#080808] border border-white/5 rounded-2xl grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 divide-y md:divide-y-0 md:divide-x divide-white/5 mb-24 shadow-[0_0_40px_rgba(0,0,0,0.4)]">
                
                <!-- Stat 1 -->
                <div class="p-10 flex flex-col justify-center">
                    <h3 class="font-display font-bold text-[50px] md:text-[60px] text-white tracking-tight mb-2">14.5x</h3>
                    <span class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold uppercase">ROAS &bull; EME EDUCATION</span>
                </div>
                
                <!-- Stat 2 -->
                <div class="p-10 flex flex-col justify-center">
                    <h3 class="font-display font-bold text-[50px] md:text-[60px] text-white tracking-tight mb-2">21x</h3>
                    <span class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold uppercase">ROAS &bull; GULBERG</span>
                </div>
                
                <!-- Stat 3 -->
                <div class="p-10 flex flex-col justify-center">
                    <h3 class="font-display font-bold text-[50px] md:text-[60px] text-white tracking-tight mb-2">150M+</h3>
                    <span class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold uppercase">ATTRIBUTED REVENUE PKR</span>
                </div>
                
                <!-- Stat 4 -->
                <div class="p-10 flex flex-col justify-center">
                    <h3 class="font-display font-bold text-[50px] md:text-[60px] text-white tracking-tight mb-2">30+</h3>
                    <span class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold uppercase">AI AGENTS IN THE STACK</span>
                </div>
                
            </div>
        </div>
        
        <!-- Scrolling Brands Marquee -->
        <div class="w-full overflow-hidden border-y border-white/5 py-10 bg-[#050505]">
            <div class="animate-marquee gap-16 md:gap-32 px-8 flex items-center">
                <!-- Group 1 -->
                <span class="font-display text-[40px] font-bold text-white/10 uppercase tracking-tighter hover:text-kinetic-red hover:opacity-100 transition-all cursor-default">NETSOL</span>
                <span class="font-display text-[40px] font-bold text-white/10 uppercase tracking-tighter hover:text-kinetic-red hover:opacity-100 transition-all cursor-default">ARBISOFT</span>
                <span class="font-display text-[40px] font-bold text-white/10 uppercase tracking-tighter hover:text-kinetic-red hover:opacity-100 transition-all cursor-default">ZAMEEN</span>
                <span class="font-display text-[40px] font-bold text-white/10 uppercase tracking-tighter hover:text-kinetic-red hover:opacity-100 transition-all cursor-default">SYSTEMS LTD</span>
                <span class="font-display text-[40px] font-bold text-white/10 uppercase tracking-tighter hover:text-kinetic-red hover:opacity-100 transition-all cursor-default">TECHLOGIX</span>
                <span class="font-display text-[40px] font-bold text-white/10 uppercase tracking-tighter hover:text-kinetic-red hover:opacity-100 transition-all cursor-default">DEVINC</span>
                
                <!-- Group 2 (Duplicate for seamless loop) -->
                <span class="font-display text-[40px] font-bold text-white/10 uppercase tracking-tighter hover:text-kinetic-red hover:opacity-100 transition-all cursor-default">NETSOL</span>
                <span class="font-display text-[40px] font-bold text-white/10 uppercase tracking-tighter hover:text-kinetic-red hover:opacity-100 transition-all cursor-default">ARBISOFT</span>
                <span class="font-display text-[40px] font-bold text-white/10 uppercase tracking-tighter hover:text-kinetic-red hover:opacity-100 transition-all cursor-default">ZAMEEN</span>
                <span class="font-display text-[40px] font-bold text-white/10 uppercase tracking-tighter hover:text-kinetic-red hover:opacity-100 transition-all cursor-default">SYSTEMS LTD</span>
                <span class="font-display text-[40px] font-bold text-white/10 uppercase tracking-tighter hover:text-kinetic-red hover:opacity-100 transition-all cursor-default">TECHLOGIX</span>
                <span class="font-display text-[40px] font-bold text-white/10 uppercase tracking-tighter hover:text-kinetic-red hover:opacity-100 transition-all cursor-default">DEVINC</span>
            </div>
        </div>
    </section>
"""

# Insert right before the footer
footer_index = content.find("<!-- Footer -->")
if footer_index != -1:
    final_content = content[:footer_index] + new_sections + "\n" + content[footer_index:]
    with open('c:/Elevix Digital/contact.html', 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Successfully injected the additional sections into contact.html!")
else:
    print("Error: Could not find <!-- Footer -->")
