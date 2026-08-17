import re

# 1. Get header and navbar from index.html
with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Header goes from <!DOCTYPE html> to </nav>
nav_end = index_content.find("</nav>") + 6
header_nav = index_content[:nav_end]

# 2. Get footer from our-story.html
with open('c:/Elevix Digital/our-story.html', 'r', encoding='utf-8') as f:
    story_content = f.read()

footer_start = story_content.find("<!-- Footer -->")
body_end = story_content.find("</body>", footer_start)
footer = story_content[footer_start:body_end]

# 3. Build the Contact Hero Section
contact_hero = """

    <!-- Hero Section -->
    <section class="relative min-h-screen flex items-center pt-32 pb-20 overflow-hidden bg-[#0a0a0a] z-10">
        
        <!-- Grid/Box Container Background Styling (Matching Homepage) -->
        <div class="absolute inset-0 z-0 pointer-events-none">
            <!-- Top and Bottom Faint Boundary Lines -->
            <div class="absolute top-8 md:top-12 left-8 md:left-12 right-8 md:right-12 h-[1px] bg-kinetic-red/20"></div>
            <div class="absolute bottom-8 md:bottom-12 left-8 md:left-12 right-8 md:right-12 h-[1px] bg-kinetic-red/20"></div>
            
            <!-- Corner Angles -->
            <div class="absolute top-8 md:top-12 left-4 md:left-8 w-4 h-4 border-t-[2px] border-l-[2px] border-kinetic-red"></div>
            <div class="absolute top-8 md:top-12 right-4 md:right-8 w-4 h-4 border-t-[2px] border-r-[2px] border-kinetic-red"></div>
            <div class="absolute bottom-8 md:bottom-12 left-4 md:left-8 w-4 h-4 border-b-[2px] border-l-[2px] border-kinetic-red"></div>
            <div class="absolute bottom-8 md:bottom-12 right-4 md:right-8 w-4 h-4 border-b-[2px] border-r-[2px] border-kinetic-red"></div>
        </div>

        <div class="relative z-10 w-full max-w-7xl mx-auto px-6 md:px-12 lg:px-16 flex flex-col justify-center">
            
            <!-- Breadcrumb -->
            <div class="font-display text-[14px] font-medium text-[#666] mb-12 flex items-center gap-2">
                <a href="index.html" class="hover:text-white transition-colors">Home</a> 
                <span>/</span> 
                <span class="text-white">Contact</span>
            </div>

            <div class="flex flex-col lg:flex-row gap-16 lg:gap-24 items-center">
                <!-- Left Content -->
                <div class="flex-1 lg:w-1/2">
                    <div class="inline-flex items-center gap-3 px-4 py-1.5 rounded-full border border-white/10 bg-white/5 mb-8">
                        <div class="w-2 h-2 rounded-full bg-kinetic-red shadow-[0_0_8px_rgba(232,40,43,0.8)]"></div>
                        <span class="font-mono text-[10px] text-white/70 tracking-[0.2em] font-bold uppercase">LET'S TALK</span>
                    </div>
                    
                    <h1 class="font-display font-bold text-[55px] md:text-[70px] lg:text-[85px] text-white leading-[1.05] tracking-tight mb-8">
                        Tell us what you want to scale.
                    </h1>
                    
                    <p class="font-display text-[17px] text-[#999] leading-[1.6] max-w-xl mb-12 font-medium">
                        This isn't an automated intake form. A founder reads every inbound, replies inside 4 business hours, and either books a call &mdash; or tells you honestly we're not the right fit. No sequences, no SDR follow-ups, no noise.
                    </p>
                    
                    <div class="flex flex-wrap items-center gap-6">
                        <a href="#intake" class="bg-kinetic-red text-white px-8 py-4 rounded-full font-display font-bold text-[16px] hover:bg-[#d42023] transition-colors shadow-[0_0_30px_rgba(232,40,43,0.3)] flex items-center gap-3 group">
                            Jump to the form
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform"><path d="M7 17l9.2-9.2M17 17V7H7"/></svg>
                        </a>
                        <a href="case-studies.html" class="text-white/60 hover:text-white font-display font-medium text-[16px] flex items-center gap-2 transition-colors group">
                            See case studies
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform"><path d="M7 17l9.2-9.2M17 17V7H7"/></svg>
                        </a>
                    </div>
                </div>

                <!-- Right Content (Intake Box) -->
                <div class="flex-1 lg:w-1/2 w-full mt-12 lg:mt-0 relative" id="intake">
                    <!-- Red Circular button on bottom right matching the screenshot slightly -->
                    <div class="absolute -bottom-6 -right-6 w-16 h-16 bg-kinetic-red rounded-full flex items-center justify-center text-white shadow-[0_0_30px_rgba(232,40,43,0.4)] z-20 hover:scale-105 transition-transform cursor-pointer">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                    </div>

                    <div class="bg-[#0e0e0e] border border-white/5 rounded-2xl p-8 md:p-12 relative shadow-[0_0_50px_rgba(0,0,0,0.5)] z-10">
                        <div class="flex justify-between items-center mb-10">
                            <div class="font-mono text-[10px] text-[#666] tracking-[0.2em] font-bold uppercase flex items-center gap-4">
                                <div class="w-6 h-[1px] bg-kinetic-red"></div> INTAKE
                            </div>
                            <div class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] font-bold uppercase flex items-center gap-2">
                                <div class="w-1.5 h-1.5 rounded-full bg-kinetic-red shadow-[0_0_8px_rgba(232,40,43,0.8)]"></div> LIVE
                            </div>
                        </div>

                        <div class="space-y-6">
                            <!-- Row 1 -->
                            <div class="flex justify-between items-center border-b border-white/5 pb-6">
                                <span class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold uppercase">RESPONSE</span>
                                <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] font-bold uppercase">&lt; 4 HRS</span>
                            </div>
                            <!-- Row 2 -->
                            <div class="flex justify-between items-center border-b border-white/5 pb-6">
                                <span class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold uppercase">CHANNELS</span>
                                <span class="font-mono text-[10px] text-white tracking-[0.2em] font-bold uppercase">CALL &bull; WA &bull; EMAIL</span>
                            </div>
                            <!-- Row 3 -->
                            <div class="flex justify-between items-center border-b border-white/5 pb-6">
                                <span class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold uppercase">HQ</span>
                                <span class="font-mono text-[10px] text-white tracking-[0.2em] font-bold uppercase">GULBERG, LAHORE, PAKISTAN</span>
                            </div>
                            <!-- Row 4 -->
                            <div class="flex justify-between items-center border-b border-white/5 pb-6">
                                <span class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold uppercase">TIMEZONE</span>
                                <span class="font-mono text-[10px] text-white tracking-[0.2em] font-bold uppercase">PKT (GMT+5)</span>
                            </div>
                            <!-- Row 5 -->
                            <div class="flex justify-between items-center border-b border-white/5 pb-6">
                                <span class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold uppercase">INTAKE</span>
                                <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] font-bold uppercase">OPEN</span>
                            </div>
                        </div>

                        <a href="#" class="mt-8 font-mono text-[10px] text-[#888] hover:text-white transition-colors tracking-[0.2em] font-bold uppercase flex justify-between items-center w-full group">
                            <span>JUMP TO THE FORM</span>
                            <span class="group-hover:translate-x-1 transition-transform">&rarr;</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

"""

# 4. Assemble and write to contact.html
final_content = header_nav + contact_hero + "\n" + footer + "\n</body>\n</html>"

with open('c:/Elevix Digital/contact.html', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Successfully created contact.html!")
