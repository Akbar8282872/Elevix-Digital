import re

def main():
    # 1. Extract nav from index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        index_html = f.read()
    
    nav_match = re.search(r'(<nav.*?</nav>)', index_html, re.DOTALL)
    if not nav_match:
        print("Nav not found in index.html")
        return
    nav_content = nav_match.group(1)

    # 2. Extract huge CTA from our-story.html
    with open('our-story.html', 'r', encoding='utf-8') as f:
        our_story_html = f.read()
    
    huge_cta_match = re.search(r'(<!-- Huge CTA Banner -->.*?</section>)', our_story_html, re.DOTALL)
    if not huge_cta_match:
        print("Huge CTA not found in our-story.html")
        return
    huge_cta_content = huge_cta_match.group(1)

    # New Receipts CTA HTML
    receipts_cta = """
    <!-- New CTA Section: Receipts -->
    <section class="py-32 px-6 bg-[#0A0A0A] relative z-10 border-t border-white/5 overflow-hidden">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row gap-20 items-center">
            
            <!-- Left Side -->
            <div class="w-full md:w-1/2">
                <div class="flex items-center gap-3 mb-8 px-4 py-2 border border-white/10 rounded-full w-max">
                    <span class="w-2 h-2 rounded-full bg-kinetic-red"></span>
                    <span class="font-mono text-[10px] text-white uppercase tracking-[0.2em] font-bold">NEXT STEP</span>
                </div>
                <h2 class="font-display font-bold text-[50px] md:text-[60px] leading-[1.1] tracking-tight text-white mb-8">
                    Want receipts like<br/>these on your<br/>account?
                </h2>
                <p class="font-display text-[16px] text-on-secondary-container leading-[1.6] mb-12 max-w-md">
                    Book a 30-minute audit call. We'll pull your current numbers, show you where the leaks are, and tell you honestly whether we can move them.
                </p>
                <a href="#contact" class="inline-flex items-center gap-4 bg-kinetic-red text-white px-8 py-5 rounded-[30px] font-display font-bold text-[16px] hover:bg-[#ff3333] transition-all shadow-[0_0_20px_rgba(232,40,43,0.3)] hover:shadow-[0_0_35px_rgba(232,40,43,0.6)] mb-12">
                    <span class="border border-white/30 rounded-full w-8 h-8 flex items-center justify-center">↗</span>
                    Book a Strategy Call
                </a>
                <div class="font-mono text-[10px] text-on-secondary-container tracking-[0.2em] uppercase font-bold flex flex-wrap gap-4">
                    <span>30 MIN</span>
                    <span class="text-kinetic-red">•</span>
                    <span>FREE AUDIT</span>
                    <span class="text-kinetic-red">•</span>
                    <span>NO DECK</span>
                    <span class="text-kinetic-red">•</span>
                    <span>NO OBLIGATION</span>
                </div>
            </div>

            <!-- Right Side -->
            <div class="w-full md:w-1/2 md:border-l border-white/5 md:pl-20">
                <div class="font-mono text-[10px] text-kinetic-red uppercase tracking-[0.2em] font-bold mb-12">
                    // WHAT YOU WALK AWAY WITH
                </div>
                
                <div class="space-y-10">
                    <!-- Item 1 -->
                    <div class="flex gap-6">
                        <div class="w-10 h-10 rounded-full border border-kinetic-red/30 flex items-center justify-center flex-shrink-0">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#E8282B" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div>
                            <div class="font-mono text-[10px] text-on-secondary-container mb-2">01</div>
                            <p class="font-display text-white text-[16px] font-medium leading-relaxed">A map of every manual task worth automating</p>
                        </div>
                    </div>
                    
                    <!-- Item 2 -->
                    <div class="flex gap-6">
                        <div class="w-10 h-10 rounded-full border border-kinetic-red/30 flex items-center justify-center flex-shrink-0">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#E8282B" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div>
                            <div class="font-mono text-[10px] text-on-secondary-container mb-2">02</div>
                            <p class="font-display text-white text-[16px] font-medium leading-relaxed">Ballpark ROI on your top 3 automation opportunities</p>
                        </div>
                    </div>

                    <!-- Item 3 -->
                    <div class="flex gap-6">
                        <div class="w-10 h-10 rounded-full border border-kinetic-red/30 flex items-center justify-center flex-shrink-0">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#E8282B" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </div>
                        <div>
                            <div class="font-mono text-[10px] text-on-secondary-container mb-2">03</div>
                            <p class="font-display text-white text-[16px] font-medium leading-relaxed">Honest read on whether we are a fit — or who is</p>
                        </div>
                    </div>
                </div>

                <div class="mt-16 pt-8 border-t border-white/5 flex items-center gap-3 font-mono text-[10px] text-on-secondary-container uppercase tracking-[0.2em] font-bold">
                    <span class="w-1.5 h-1.5 rounded-full bg-kinetic-red"></span>
                    USUALLY RESPONDS WITHIN 24 HOURS
                </div>
            </div>
        </div>
    </section>
"""

    combined_ctas = receipts_cta + "\n" + huge_cta_content + "\n\n"

    # 3. Update files
    for filename in ['services.html', 'our-story.html', 'case-studies.html']:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace nav
        content = re.sub(r'<nav.*?</nav>', nav_content, content, flags=re.DOTALL)
        
        # Specific updates for case-studies.html
        if filename == 'case-studies.html':
            # Add breadcrumb
            breadcrumb = '''
                <div class="flex items-center gap-4 text-on-secondary-container text-sm font-mono tracking-widest mb-12">
                    <a href="index.html" class="hover:text-white transition-colors">Home</a>
                    <span class="text-white/30">/</span>
                    <span class="text-white">Case Studies</span>
                </div>
            '''
            
            # Find the hero text div (starts with <div class="flex items-center gap-2 inline-block)
            hero_target = r'(<div class="lg:col-span-7">\s*)(<div class="flex items-center gap-2 inline-block)'
            content = re.sub(hero_target, r'\1' + breadcrumb + r'\n                \2', content)

            # Insert combined CTAs before footer
            # The footer starts with <footer id="footer" class="bg-[#050505]
            footer_pattern = r'(<footer id="footer" class="bg-\[#050505\])'
            # But the footer in case-studies is exactly <footer class="pt-32 bg-[#050505] relative border-t border-white/10 z-10"> (since we replaced it)
            # Let's just find the first <footer
            content = re.sub(r'(<footer\b[^>]*>)', combined_ctas + r'\1', content)
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated {filename}")

if __name__ == '__main__':
    main()
