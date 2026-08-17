import re

with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open('c:/Elevix Digital/backup_marquee.html', 'r', encoding='utf-8') as f:
    marquee_content = f.read()

# 1. New Hero Inner Content (from the first successful step)
new_hero_inner = '''        <div class="relative z-10 w-full max-w-7xl mx-auto px-6 md:px-12 lg:px-24 flex flex-col md:flex-row items-center justify-between min-h-[70vh] pt-12 md:pt-0">
            
            <!-- Left Content -->
            <div class="w-full md:w-1/2 flex flex-col items-start pr-0 md:pr-12 fade-up">
                <!-- Pill -->
                <div class="flex items-center gap-2 px-4 py-1.5 rounded-full border border-white/10 bg-[#111] mb-8">
                    <span class="w-2 h-2 rounded-full bg-kinetic-red animate-pulse"></span>
                    <span class="font-mono text-white text-[10px] md:text-[11px] font-bold tracking-[0.2em] uppercase">WE'RE HIRING ALWAYS</span>
                </div>
                
                <!-- Heading -->
                <h1 class="font-display text-[55px] sm:text-[60px] md:text-[75px] font-bold tracking-tight leading-[1.05] text-white mb-6">
                    Build systems, not hustle.
                </h1>
                
                <!-- Paragraph -->
                <p class="font-display text-[15px] md:text-[17px] text-[#a1a1aa] leading-relaxed mb-10 max-w-xl">
                    Elevix hires exceptional people first and writes the job description second. Every role on this page is permanently open &mdash; we interview every month and the founder picks the best in the room, even when no seat is formally vacant. If you build with taste and own your craft, the door is open.
                </p>
                
                <!-- Buttons -->
                <div class="flex flex-col sm:flex-row items-start sm:items-center gap-6">
                    <a href="#roles" class="bg-kinetic-red text-white px-8 py-3.5 rounded-[30px] text-[15px] font-bold hover:bg-[#ff3333] transition-all flex items-center gap-2">
                        Send a general application <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                    </a>
                    <a href="#roles" class="text-on-secondary-container hover:text-white transition-colors text-[14px] font-medium flex items-center gap-2">
                        See open roles <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                    </a>
                </div>
            </div>
            
            <!-- Right Content (Stats Card) -->
            <div class="w-full md:w-[450px] mt-16 md:mt-0 fade-up" style="transition-delay: 200ms;">
                <div class="bg-[#111]/80 backdrop-blur-xl border border-white/5 rounded-[12px] p-8 hover:border-white/10 transition-colors">
                    
                    <!-- Row 1 -->
                    <div class="flex items-center justify-between py-4 border-b border-white/5">
                        <div class="flex items-center gap-3">
                            <div class="w-6 h-[1px] bg-kinetic-red"></div>
                            <span class="font-mono text-[10px] text-[#a1a1aa] tracking-[0.2em] uppercase font-bold">CAREERS</span>
                        </div>
                        <div class="flex items-center gap-2 font-mono text-[10px] text-kinetic-red tracking-[0.2em] uppercase font-bold">
                            <span class="w-1.5 h-1.5 rounded-full bg-kinetic-red animate-pulse"></span> LIVE
                        </div>
                    </div>
                    
                    <!-- Row 2 -->
                    <div class="flex items-center justify-between py-4 border-b border-white/5 font-mono text-[10px] tracking-[0.2em] uppercase font-bold">
                        <span class="text-[#a1a1aa]">OPEN ROLES</span>
                        <span class="text-kinetic-red">13</span>
                    </div>
                    
                    <!-- Row 3 -->
                    <div class="flex items-center justify-between py-4 border-b border-white/5 font-mono text-[10px] tracking-[0.2em] uppercase font-bold">
                        <span class="text-[#a1a1aa]">TEAM</span>
                        <span class="text-white">8</span>
                    </div>
                    
                    <!-- Row 4 -->
                    <div class="flex items-center justify-between py-4 border-b border-white/5 font-mono text-[10px] tracking-[0.2em] uppercase font-bold">
                        <span class="text-[#a1a1aa]">HQ</span>
                        <span class="text-white">PAKISTAN LAHORE</span>
                    </div>
                    
                    <!-- Row 5 -->
                    <div class="flex items-center justify-between py-4 border-b border-white/5 font-mono text-[10px] tracking-[0.2em] uppercase font-bold">
                        <span class="text-[#a1a1aa]">WORK MODE</span>
                        <span class="text-white">IN-PERSON</span>
                    </div>
                    
                    <!-- Row 6 -->
                    <div class="flex items-center justify-between py-4 border-b border-white/5 font-mono text-[10px] tracking-[0.2em] uppercase font-bold">
                        <span class="text-[#a1a1aa]">INTERVIEW CADENCE</span>
                        <span class="text-white">MONTHLY</span>
                    </div>
                    
                    <!-- Row 7 -->
                    <a href="#contact" class="flex items-center justify-between pt-6 mt-2 font-mono text-[10px] tracking-[0.2em] uppercase text-white hover:text-kinetic-red transition-colors group font-bold">
                        <span class="tracking-[0.2em]">BOOK A 30-MIN AUDIT</span>
                        <span class="group-hover:translate-x-1 transition-transform">&rarr;</span>
                    </a>
                    
                </div>
            </div>
        </div>
    </section>'''

# 2. Reconstruct the broken area
# Find the start of the broken inner content
start_idx = text.find('<!-- Left Content -->')
# Wait, let's find the start of the `<div class="relative z-10` which was mutated to `mt-32...`
div_start = text.find('<div class="relative z-10 w-full max-w-7xl mx-auto px-6 md:px-12 lg:px-24 flex flex-col md:flex-row items-center justify-between mt-32')
if div_start != -1:
    start_idx = div_start
else:
    # If not found, just cut from <!-- Left Content --> and we'll prepend the div opening manually
    new_hero_inner = new_hero_inner[new_hero_inner.find('<!-- Left Content -->'):]

end_idx = text.find('<!-- Results / Case Studies Section -->')

if start_idx != -1 and end_idx != -1:
    # We replace from start_idx to end_idx with new_hero_inner + marquee_content
    restored_text = text[:start_idx] + new_hero_inner + '\n\n' + marquee_content + '\n\n' + text[end_idx:]
    with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
        f.write(restored_text)
    print('Careers page restored perfectly!')
else:
    print('Failed to find indices for restoration.')
