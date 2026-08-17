import re

# 1. Get CTA Banner from our-story.html
with open('c:/Elevix Digital/our-story.html', 'r', encoding='utf-8') as f:
    story_content = f.read()

cta_start = story_content.find("<!-- Huge CTA Banner -->")
footer_start = story_content.find("<!-- Footer -->", cta_start)

if cta_start == -1 or footer_start == -1:
    print("Could not find CTA Banner in our-story.html")
    exit(1)

cta_section = story_content[cta_start:footer_start].strip()


# 2. Define the new sections
hr_desk_section = """    <!-- HR Desk Section -->
    <section class="py-12 px-6 bg-[#050505] relative border-t border-white/5">
        <div class="max-w-7xl mx-auto">
            <div class="bg-[#0e0e0e] border border-white/5 rounded-xl p-8 md:p-12 flex flex-col md:flex-row items-start md:items-center justify-between gap-8 hover:border-white/10 transition-colors">
                <div class="flex-1">
                    <div class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] font-bold uppercase mb-4 flex items-center gap-4">
                        <div class="w-6 h-[1px] bg-kinetic-red"></div> HR DESK
                    </div>
                    <h2 class="font-display font-bold text-[28px] md:text-[32px] text-white leading-tight mb-4">
                        Questions about a role? Reach HR directly.
                    </h2>
                    <p class="font-display text-[15px] text-[#888] leading-[1.6] max-w-xl">
                        A dedicated line for candidates &mdash; so hiring conversations don't compete with sales calls. <strong class="text-white">+92 300 000</strong>
                    </p>
                </div>
                <div class="flex flex-col sm:flex-row items-center gap-4 w-full md:w-auto">
                    <a href="#" class="w-full sm:w-auto px-6 py-3 rounded-full border border-[#0F3F2C] bg-[#0F3F2C]/30 text-[#4ade80] font-display font-bold text-[14px] flex items-center justify-center gap-3 hover:bg-[#0F3F2C]/50 transition-colors">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                        WhatsApp HR &nearr;
                    </a>
                    <a href="#" class="w-full sm:w-auto px-6 py-3 rounded-full border border-white/10 text-white font-display font-bold text-[14px] flex items-center justify-center gap-3 hover:bg-white/5 transition-colors">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                        Call HR
                    </a>
                </div>
            </div>
        </div>
    </section>
"""

general_app_section = """    <!-- General Application Section -->
    <section class="py-24 px-6 bg-[#050505] relative border-t border-white/5 overflow-hidden">
        <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-kinetic-red/10 blur-[150px] pointer-events-none"></div>
        <div class="absolute bottom-0 left-0 w-[500px] h-[500px] bg-kinetic-red/5 blur-[150px] pointer-events-none"></div>
        <div class="max-w-7xl mx-auto flex flex-col lg:flex-row gap-16">
            <!-- Left Side -->
            <div class="flex-1 lg:w-1/2">
                <div class="inline-flex items-center gap-3 px-4 py-1.5 rounded-full border border-white/10 bg-white/5 mb-8">
                    <div class="w-2 h-2 rounded-full bg-kinetic-red animate-pulse shadow-[0_0_8px_rgba(232,40,43,0.8)]"></div>
                    <span class="font-mono text-[10px] text-white/70 tracking-[0.2em] font-bold uppercase">NEXT STEP</span>
                </div>
                <h2 class="font-display font-bold text-[50px] md:text-[60px] lg:text-[70px] text-white leading-[1.05] mb-8 tracking-tight">
                    Not sure which<br/>role fits you?
                </h2>
                <p class="font-display text-[18px] text-[#888] leading-[1.6] mb-12 max-w-lg">
                    Send a general application and tell us what you are best at. We read every one and fold the strongest into the next monthly sprint &mdash; seat or no seat.
                </p>
                <a href="#" class="inline-flex items-center gap-4 bg-kinetic-red text-white px-8 py-5 rounded-full font-display font-bold text-[18px] hover:bg-[#d42023] transition-colors shadow-[0_0_30px_rgba(232,40,43,0.3)] group mb-10 w-full sm:w-auto justify-center">
                    <div class="w-10 h-10 rounded-full border border-white/30 flex items-center justify-center group-hover:rotate-45 transition-transform">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17l9.2-9.2M17 17V7H7"/></svg>
                    </div>
                    Send a general application
                </a>
                <div class="font-mono text-[10px] text-[#666] tracking-[0.2em] uppercase font-bold flex flex-wrap items-center gap-3 mb-10">
                    <span>MONTHLY</span>
                    <span class="w-1 h-1 rounded-full bg-kinetic-red"></span>
                    <span>PAID TRIAL</span>
                    <span class="w-1 h-1 rounded-full bg-kinetic-red"></span>
                    <span>DECISION IN 7 DAYS</span>
                    <br class="hidden md:block w-full"/>
                    <span class="w-1 h-1 rounded-full bg-kinetic-red hidden md:block"></span>
                    <span>NO GHOSTING</span>
                </div>
                <a href="#" class="inline-flex items-center gap-3 font-display text-[15px] text-kinetic-red hover:text-white transition-colors">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                    Or send us a WhatsApp &nearr;
                </a>
            </div>

            <!-- Right Side -->
            <div class="flex-1 lg:w-1/2">
                <div class="bg-transparent lg:border-l border-white/10 lg:pl-16 relative">
                    <div class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] font-bold uppercase mb-12">
                        // WHAT YOU WALK AWAY WITH
                    </div>
                    
                    <div class="space-y-12">
                        <!-- Item 1 -->
                        <div class="flex items-start gap-6">
                            <div class="w-8 h-8 rounded-full border border-kinetic-red/30 flex items-center justify-center flex-shrink-0 text-kinetic-red mt-1">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            </div>
                            <div>
                                <div class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold mb-2">01</div>
                                <p class="font-display text-[18px] text-white leading-[1.5] font-medium">A 25-minute screening call with the founder or ops lead</p>
                            </div>
                        </div>

                        <!-- Item 2 -->
                        <div class="flex items-start gap-6">
                            <div class="w-8 h-8 rounded-full border border-kinetic-red/30 flex items-center justify-center flex-shrink-0 text-kinetic-red mt-1">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            </div>
                            <div>
                                <div class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold mb-2">02</div>
                                <p class="font-display text-[18px] text-white leading-[1.5] font-medium">A paid working trial on a real Elevix task, with real context</p>
                            </div>
                        </div>

                        <!-- Item 3 -->
                        <div class="flex items-start gap-6">
                            <div class="w-8 h-8 rounded-full border border-kinetic-red/30 flex items-center justify-center flex-shrink-0 text-kinetic-red mt-1">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            </div>
                            <div>
                                <div class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold mb-2">03</div>
                                <p class="font-display text-[18px] text-white leading-[1.5] font-medium">A yes or no inside 7 days &mdash; always &mdash; even if the answer is "not this sprint"</p>
                            </div>
                        </div>
                    </div>

                    <div class="mt-16 pt-8 border-t border-white/10 flex items-center gap-3 font-mono text-[10px] text-[#666] tracking-[0.2em] uppercase font-bold">
                        <div class="w-1.5 h-1.5 rounded-full bg-kinetic-red"></div>
                        USUALLY RESPONDS WITHIN 24 HOURS
                    </div>
                </div>
                
                <!-- Circular decorative button exactly like screenshot bottom right -->
                <div class="hidden lg:flex justify-end mt-16">
                     <div class="w-16 h-16 bg-kinetic-red rounded-full flex items-center justify-center text-white shadow-[0_0_30px_rgba(232,40,43,0.4)] hover:scale-105 transition-transform cursor-pointer">
                         <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                     </div>
                </div>
            </div>
        </div>
    </section>
"""

# 3. Read careers.html
with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    careers_content = f.read()

# Make sure we don't insert multiple times
if "Questions about a role? Reach HR directly." in careers_content:
    print("Already added HR section to careers.html")
    exit(0)

# The place to insert is right before <!-- New Massive Grid Footer -->
footer_marker = "    <!-- New Massive Grid Footer -->"

if footer_marker not in careers_content:
    print("Could not find the footer marker in careers.html")
    exit(1)

# 4. Construct new content
new_content = hr_desk_section + "\n\n" + general_app_section + "\n\n" + cta_section + "\n\n" + footer_marker

careers_content = careers_content.replace(footer_marker, new_content)

# 5. Write back
with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(careers_content)

print("Successfully injected final three sections into careers.html")
