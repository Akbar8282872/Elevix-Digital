import re

with open(r'c:\Elevix Digital\services.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace card outer container
html = re.sub(r'group rounded-\[20px\] p-\[1px\] bg-gradient-to-b from-white/10 to-transparent hover:from-kinetic-red/60 hover:to-kinetic-red/5', r'group rounded-[20px] border border-[#2b2a2a] bg-[#050505] hover:border-kinetic-red/50', html)

# Replace card inner container
html = re.sub(r'class="p-10 rounded-\[20px\] bg-\[#0A0A0A\] h-full', r'class="p-10 rounded-[20px] h-full', html)

# Replace background numbers
html = re.sub(r'font-display text-\[140px\] font-bold text-white/5', r'font-mono text-[140px] font-bold text-[#e8282b]/10', html)
html = re.sub(r'group-hover:text-kinetic-red/10', r'group-hover:text-[#e8282b]/20', html)

# Add marquee before location map
marqueeHtml = """    </section>

    <!-- Top Marquee Banner -->
    <div class="w-full bg-kinetic-red py-4 overflow-hidden flex relative z-20 shadow-[0_0_20px_rgba(232,40,43,0.3)] my-16">
        <div class="animate-marquee flex whitespace-nowrap items-center font-display font-black text-[28px] md:text-[40px] uppercase tracking-tighter text-white w-max">
            <!-- Set 1 -->
            <span class="mx-6">AUTOMATING THE IMPOSSIBLE, DAILY</span> <span class="mx-6 text-black/50">•</span>
            <span class="mx-6">AUTOMATING THE IMPOSSIBLE, DAILY</span> <span class="mx-6 text-black/50">•</span>
            <span class="mx-6">AUTOMATING THE IMPOSSIBLE, DAILY</span> <span class="mx-6 text-black/50">•</span>
            <span class="mx-6">AUTOMATING THE IMPOSSIBLE, DAILY</span> <span class="mx-6 text-black/50">•</span>
            <span class="mx-6">AUTOMATING THE IMPOSSIBLE, DAILY</span> <span class="mx-6 text-black/50">•</span>
            <!-- Set 2 -->
            <span class="mx-6">AUTOMATING THE IMPOSSIBLE, DAILY</span> <span class="mx-6 text-black/50">•</span>
            <span class="mx-6">AUTOMATING THE IMPOSSIBLE, DAILY</span> <span class="mx-6 text-black/50">•</span>
            <span class="mx-6">AUTOMATING THE IMPOSSIBLE, DAILY</span> <span class="mx-6 text-black/50">•</span>
            <span class="mx-6">AUTOMATING THE IMPOSSIBLE, DAILY</span> <span class="mx-6 text-black/50">•</span>
            <span class="mx-6">AUTOMATING THE IMPOSSIBLE, DAILY</span> <span class="mx-6 text-black/50">•</span>
        </div>
    </div>
"""

html = re.sub(r'    </section>\s+<!-- Address & Global Reach Map Section \(identical to homepage layout\) -->', marqueeHtml + '\n    <!-- Address & Global Reach Map Section (identical to homepage layout) -->', html)

with open(r'c:\Elevix Digital\services.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Modified services.html successfully')
