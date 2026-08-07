def main():
    # Read case-studies.html (which is currently a copy of our-story.html)
    with open('c:\\Elevix Digital\\case-studies.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Read index.html to grab the old #results section
    with open('c:\\Elevix Digital\\index.html', 'r', encoding='utf-8') as f:
        index_html = f.read()

    # Get the "The Work" grid from index.html (it's in the #results section)
    # The section starts with <section id="results"
    idx_results = index_html.find('<section id="results"')
    idx_results_end = index_html.find('</section>', idx_results) + len('</section>')
    work_grid_html = index_html[idx_results:idx_results_end]
    
    # We want to change its id to avoid conflicts if they ever co-exist, but it's a separate page so it's fine.
    work_grid_html = work_grid_html.replace('id="results"', 'id="the-work"')
    work_grid_html = work_grid_html.replace('<!-- Results / Case Studies Section -->', '<!-- The Work Section -->')
    
    hero_html = """
    <!-- MAIN HERO (WITH ORB BG) -->
    <header class="relative pt-40 pb-20 lg:pt-48 lg:pb-32 px-6 min-h-[70vh] flex items-center overflow-hidden">
        <!-- Animated Background Mesh/Orb -->
        <div class="absolute inset-0 z-0 pointer-events-none">
            <!-- Pulsing Red Core -->
            <div class="absolute top-[10%] left-[20%] w-[600px] h-[600px] bg-kinetic-red rounded-full mix-blend-screen filter blur-[150px] opacity-20 animate-[pulse_4s_ease-in-out_infinite]"></div>
            <!-- Rotating Dark Core -->
            <div class="absolute bottom-[0%] right-[10%] w-[500px] h-[500px] bg-[#500000] rounded-full mix-blend-screen filter blur-[120px] opacity-30 animate-[spin_10s_linear_infinite]"></div>
            <!-- Grid overlay -->
            <div class="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)]" style="background-size: 50px 50px;"></div>
            <!-- Scanline -->
            <div class="absolute inset-0 bg-gradient-to-b from-transparent via-white/5 to-transparent h-[200%] animate-[scan_6s_linear_infinite]"></div>
        </div>

        <div class="relative z-10 max-w-7xl mx-auto w-full grid grid-cols-1 lg:grid-cols-12 gap-12 items-center pointer-events-auto">
            
            <!-- Left Column: Hero Text -->
            <div class="lg:col-span-7">
                <div class="flex items-center gap-2 inline-block py-1 px-3 border border-white/10 rounded-full bg-white/5 mb-6 w-max">
                    <div class="w-2 h-2 rounded-full bg-kinetic-red"></div>
                    <span class="font-mono text-stark-white text-[10px] font-bold tracking-[0.2em] uppercase">
                        PROOF
                    </span>
                </div>
                <h1 class="font-display font-black text-5xl md:text-7xl lg:text-[90px] leading-[1.0] tracking-tighter text-white mb-6">
                    Results we can ship<br />on a screenshot.
                </h1>
                <p class="text-lg text-on-secondary-container font-display leading-relaxed max-w-2xl mb-10">
                    Campaigns, builds, and automation systems that moved real numbers — with the numbers still attached.
                </p>
                <div class="flex flex-wrap items-center gap-6">
                    <a href="#contact" class="px-8 py-4 bg-kinetic-red text-white font-display font-bold text-sm tracking-wide hover:bg-red-600 transition-colors rounded-[24px] flex items-center gap-2">
                        Book a Strategy Call <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17l9.2-9.2M17 17V7H7"/></svg>
                    </a>
                    <a href="#the-work" class="text-neutral-400 font-display font-medium text-sm hover:text-white transition-colors flex items-center gap-2">
                        See case studies <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17l9.2-9.2M17 17V7H7"/></svg>
                    </a>
                </div>
            </div>

            <!-- Right Column: Status Widget -->
            <div class="lg:col-span-5 relative">
                <div class="absolute inset-0 bg-kinetic-red/10 blur-[100px] rounded-full pointer-events-none"></div>
                
                <div class="relative border border-white/5 bg-[#111] p-8 rounded-[16px] shadow-2xl pointer-events-auto">
                    <!-- Rows -->
                    <div class="flex items-center justify-between py-4 border-b border-white/5">
                        <span class="font-mono text-[10px] text-neutral-500 uppercase tracking-[0.2em] flex items-center gap-4">
                            <span class="w-8 h-[1px] bg-kinetic-red/50"></span> STATE
                        </span>
                        <div class="flex items-center gap-2">
                            <div class="w-1.5 h-1.5 rounded-full bg-kinetic-red animate-pulse"></div>
                            <span class="font-mono text-[10px] text-kinetic-red uppercase tracking-[0.2em]">LIVE</span>
                        </div>
                    </div>

                    <div class="flex items-center justify-between py-4 border-b border-white/5">
                        <span class="font-mono text-[10px] text-neutral-500 uppercase tracking-[0.2em]">FEATURED</span>
                        <span class="font-mono text-sm text-white">2</span>
                    </div>

                    <div class="flex items-center justify-between py-4 border-b border-white/5">
                        <span class="font-mono text-[10px] text-neutral-500 uppercase tracking-[0.2em]">TOTAL ATTRIBUTED</span>
                        <span class="font-mono text-sm text-kinetic-red font-bold">$2M+</span>
                    </div>

                    <div class="flex items-center justify-between py-4 border-b border-white/5">
                        <span class="font-mono text-[10px] text-neutral-500 uppercase tracking-[0.2em]">PEAK ROAS</span>
                        <span class="font-mono text-sm text-white">41x</span>
                    </div>

                    <div class="flex items-center justify-between py-4 border-b border-white/5">
                        <span class="font-mono text-[10px] text-neutral-500 uppercase tracking-[0.2em]">SECTORS</span>
                        <span class="font-mono text-[10px] font-bold text-white uppercase tracking-[0.2em]">ECOMMERCE • SAAS</span>
                    </div>
                </div>
            </div>
        </div>
    </header>
    """
    
    # Portfolio Metrics Section
    metrics_html = """
    <!-- PORTFOLIO METRICS SECTION -->
    <section class="py-16 px-6 relative z-10 border-b border-white/5 bg-[#0a0a0a]">
        <div class="max-w-7xl mx-auto">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                <!-- Metric 1 -->
                <div class="p-8 border border-white/5 bg-[#111] rounded-[16px] hover:border-kinetic-red/30 transition-colors">
                    <p class="font-mono text-[10px] font-bold text-neutral-400 uppercase tracking-[0.2em]">ROAS - ECOMMERCE BRAND</p>
                    <p class="font-display text-4xl md:text-5xl font-black text-white mt-4 tracking-tighter">41x</p>
                    <div class="w-full h-1 bg-white/5 mt-6 rounded-full overflow-hidden"><div class="h-full bg-kinetic-red w-[90%]"></div></div>
                </div>
                <!-- Metric 2 -->
                <div class="p-8 border border-white/5 bg-[#111] rounded-[16px] hover:border-kinetic-red/30 transition-colors">
                    <p class="font-mono text-[10px] font-bold text-neutral-400 uppercase tracking-[0.2em]">CPA REDUCTION</p>
                    <p class="font-display text-4xl md:text-5xl font-black text-white mt-4 tracking-tighter">62%</p>
                    <div class="w-full h-1 bg-white/5 mt-6 rounded-full overflow-hidden"><div class="h-full bg-[#10b981] w-[62%]"></div></div>
                </div>
                <!-- Metric 3 -->
                <div class="p-8 border border-white/5 bg-[#111] rounded-[16px] hover:border-kinetic-red/30 transition-colors">
                    <p class="font-mono text-[10px] font-bold text-neutral-400 uppercase tracking-[0.2em]">MQL TO SQL CONVERSION</p>
                    <p class="font-display text-4xl md:text-5xl font-black text-white mt-4 tracking-tighter">+45%</p>
                    <div class="w-full h-1 bg-white/5 mt-6 rounded-full overflow-hidden"><div class="h-full bg-[#3b82f6] w-[45%]"></div></div>
                </div>
                <!-- Metric 4 -->
                <div class="p-8 border border-white/5 bg-[#111] rounded-[16px] hover:border-kinetic-red/30 transition-colors">
                    <p class="font-mono text-[10px] font-bold text-neutral-400 uppercase tracking-[0.2em]">TOTAL MANAGED SPEND</p>
                    <p class="font-display text-4xl md:text-5xl font-black text-white mt-4 tracking-tighter">$1.2M</p>
                    <div class="w-full h-1 bg-white/5 mt-6 rounded-full overflow-hidden"><div class="h-full bg-white/30 w-[100%]"></div></div>
                </div>
            </div>
        </div>
    </section>
    """
    
    # Audit Offer Section
    audit_html = """
    <!-- D. Audit Offer & Value Prop Section -->
    <section class="py-24 px-6 border-b border-white/5 bg-deep-obsidian" id="contact">
        <div class="max-w-5xl mx-auto flex flex-col md:flex-row gap-16 items-center">
            
            <div class="w-full md:w-1/2">
                <div class="flex items-center gap-2 mb-6">
                    <span class="w-2 h-2 bg-kinetic-red rounded-full animate-pulse"></span>
                    <span class="font-mono text-[10px] text-kinetic-red tracking-widest uppercase font-bold">Free Growth Audit</span>
                </div>
                
                <h2 class="font-display text-4xl md:text-5xl font-bold text-white leading-tight mb-6 tracking-tight">
                    Stop guessing.<br/>Start scaling.
                </h2>
                
                <p class="text-on-secondary-container text-lg mb-8 font-display">
                    We'll audit your current ad accounts, funnels, and automation systems. You'll get a step-by-step scaling roadmap within 48 hours.
                </p>
                
                <ul class="space-y-4 font-mono text-[13px] text-white">
                    <li class="flex items-center gap-3">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--color-kinetic-red)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        Ad Account Architecture Review
                    </li>
                    <li class="flex items-center gap-3">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--color-kinetic-red)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        Funnel Drop-off Analysis
                    </li>
                    <li class="flex items-center gap-3">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--color-kinetic-red)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        Automation Gap Identification
                    </li>
                </ul>
            </div>
            
            <div class="w-full md:w-1/2 bg-[#111] border border-white/10 rounded-2xl p-8 relative overflow-hidden group">
                <div class="absolute inset-0 bg-gradient-to-br from-kinetic-red/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
                <form class="space-y-4 relative z-10">
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label class="block font-mono text-[10px] text-neutral-500 uppercase tracking-widest mb-2">First Name</label>
                            <input type="text" class="w-full bg-[#050505] border border-white/10 rounded-lg px-4 py-3 text-white focus:border-kinetic-red focus:outline-none transition-colors" placeholder="John">
                        </div>
                        <div>
                            <label class="block font-mono text-[10px] text-neutral-500 uppercase tracking-widest mb-2">Last Name</label>
                            <input type="text" class="w-full bg-[#050505] border border-white/10 rounded-lg px-4 py-3 text-white focus:border-kinetic-red focus:outline-none transition-colors" placeholder="Doe">
                        </div>
                    </div>
                    <div>
                        <label class="block font-mono text-[10px] text-neutral-500 uppercase tracking-widest mb-2">Work Email</label>
                        <input type="email" class="w-full bg-[#050505] border border-white/10 rounded-lg px-4 py-3 text-white focus:border-kinetic-red focus:outline-none transition-colors" placeholder="john@company.com">
                    </div>
                    <div>
                        <label class="block font-mono text-[10px] text-neutral-500 uppercase tracking-widest mb-2">Website URL</label>
                        <input type="url" class="w-full bg-[#050505] border border-white/10 rounded-lg px-4 py-3 text-white focus:border-kinetic-red focus:outline-none transition-colors" placeholder="https://">
                    </div>
                    
                    <button class="w-full bg-kinetic-red text-white py-4 rounded-lg font-bold text-[14px] hover:bg-[#ff3333] transition-colors mt-4">
                        Request Free Audit
                    </button>
                    <p class="font-mono text-[9px] text-neutral-500 text-center uppercase tracking-widest mt-4">
                        NO COMMITMENT. NO SPAM.
                    </p>
                </form>
            </div>
            
        </div>
    </section>
    """
    
    # Now, find the <main> block in case-studies.html to replace
    # In our-story.html, the main sections start with <!-- Hero Section --> and end right before <footer
    start_idx = html.find('<!-- Hero Section -->')
    end_idx = html.rfind('<footer')
    
    # We will also make sure the Case Studies nav link is ACTIVE in case-studies.html
    html = html.replace('<a href="case-studies.html" class="text-on-secondary-container text-[14px] font-medium hover:text-white transition-colors">Case Studies</a>',
                        '<a href="case-studies.html" class="text-[14px] font-medium text-white transition-colors">Case Studies</a>')
    # and un-active the Our Story link
    html = html.replace('<a href="our-story.html" class="text-on-secondary-container text-[14px] font-medium text-white transition-colors">Our Story</a>',
                        '<a href="our-story.html" class="text-on-secondary-container text-[14px] font-medium hover:text-white transition-colors">Our Story</a>')

    new_html = html[:start_idx] + hero_html + "\n" + metrics_html + "\n" + work_grid_html + "\n" + audit_html + "\n\n" + html[end_idx:]
    
    with open('c:\\Elevix Digital\\case-studies.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

if __name__ == "__main__":
    main()
