import re

def main():
    # 1. Update the 'Blogs' link to 'blog.html' across all pages
    files_to_update = ['index.html', 'our-story.html', 'services.html', 'case-studies.html']
    nav_html = None
    head_html = None
    
    for filename in files_to_update:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix Blogs link
            content = content.replace(
                '<a href="#" class="text-on-secondary-container text-[14px] font-medium hover:text-white transition-colors">Blogs</a>',
                '<a href="blog.html" class="text-on-secondary-container text-[14px] font-medium hover:text-white transition-colors">Blogs</a>'
            )
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
                
            # Grab head and nav from index.html for blog.html
            if filename == 'index.html':
                head_match = re.search(r'(<head>.*?</head>)', content, re.DOTALL)
                if head_match:
                    head_html = head_match.group(1)
                    
                nav_match = re.search(r'(<nav.*?</nav>)', content, re.DOTALL)
                if nav_match:
                    nav_html = nav_match.group(1)
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    # 2. Build blog.html
    blog_content = f"""<!DOCTYPE html>
<html lang="en">
{head_html}
<body class="font-display bg-deep-obsidian">

    {nav_html}

    <!-- Hero Section -->
    <section class="relative min-h-[90vh] pt-32 pb-16 px-6 overflow-hidden flex items-center bg-[#0a0a0a]">
        <!-- Animated Background Mesh/Orb (exactly like Our Story / Services) -->
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

        <div class="max-w-7xl mx-auto flex flex-col lg:flex-row justify-between items-center gap-16 relative z-10 w-full mt-20 lg:mt-12">
            
            <!-- Left Side -->
            <div class="w-full lg:w-[55%]">
                <div class="flex items-center gap-4 text-on-secondary-container text-[14px] font-mono tracking-widest mb-12">
                    <a href="index.html" class="hover:text-white transition-colors">Home</a>
                    <span class="text-white/30">/</span>
                    <span class="text-white">Blog</span>
                </div>
                
                <div class="flex items-center gap-3 mb-8 px-4 py-2 border border-white/10 rounded-full w-max bg-[#0A0A0A]/50 backdrop-blur-sm">
                    <span class="w-2 h-2 rounded-full bg-kinetic-red"></span>
                    <span class="font-mono text-[10px] text-white uppercase tracking-[0.2em] font-bold">THE ELEVIX BRIEF</span>
                </div>
                
                <h1 class="font-display font-bold text-[60px] md:text-[80px] lg:text-[100px] leading-[0.9] tracking-tighter text-white mb-8">
                    Playbooks from the build.
                </h1>
                
                <p class="font-display text-[16px] md:text-[18px] text-on-secondary-container leading-[1.6] mb-12 max-w-lg">
                    Long-form field notes on AI automation, growth marketing, and the systems we actually ship — not content for content's sake.
                </p>
                
                <div class="flex flex-wrap items-center gap-8">
                    <a href="#contact" class="inline-flex items-center gap-2 bg-kinetic-red text-white px-8 py-4 rounded-[30px] font-display font-bold text-[16px] hover:bg-[#ff3333] transition-all shadow-[0_0_20px_rgba(232,40,43,0.3)] hover:shadow-[0_0_35px_rgba(232,40,43,0.6)]">
                        Book a Strategy Call ↗
                    </a>
                    <a href="case-studies.html" class="text-on-secondary-container font-display font-bold text-[16px] hover:text-white transition-colors flex items-center gap-2">
                        See case studies ↗
                    </a>
                </div>
            </div>

            <!-- Right Side (Specs Card) -->
            <div class="w-full lg:w-[45%]">
                <div class="bg-[#0f0f0f]/80 backdrop-blur-xl border border-white/5 rounded-2xl p-8 md:p-10 relative overflow-hidden">
                    <!-- Red subtle gradient from right side -->
                    <div class="absolute top-0 right-0 bottom-0 w-[200px] bg-gradient-to-l from-kinetic-red/10 to-transparent pointer-events-none rounded-r-2xl"></div>

                    <!-- Header -->
                    <div class="flex justify-between items-center mb-10 relative z-10">
                        <span class="font-mono text-[10px] text-neutral-500 tracking-[0.2em] uppercase flex items-center gap-4">
                            <span class="w-8 h-[1px] bg-kinetic-red/50"></span> SPECS
                        </span>
                        <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] uppercase flex items-center gap-2">
                            <span class="w-2 h-2 rounded-full bg-kinetic-red animate-pulse"></span> LIVE
                        </span>
                    </div>

                    <!-- Rows -->
                    <div class="space-y-6 relative z-10">
                        <div class="flex justify-between items-center border-b border-white/5 pb-6">
                            <span class="font-mono text-[10px] text-neutral-500 tracking-[0.2em] uppercase">FORMAT</span>
                            <span class="font-mono text-[12px] text-white tracking-[0.1em] font-bold uppercase text-right">LONG-FORM</span>
                        </div>
                        <div class="flex justify-between items-center border-b border-white/5 pb-6">
                            <span class="font-mono text-[10px] text-neutral-500 tracking-[0.2em] uppercase">CADENCE</span>
                            <span class="font-mono text-[12px] text-white tracking-[0.1em] font-bold uppercase text-right">2x MONTHLY</span>
                        </div>
                        <div class="flex justify-between items-center border-b border-white/5 pb-6">
                            <span class="font-mono text-[10px] text-neutral-500 tracking-[0.2em] uppercase">TOPICS</span>
                            <span class="font-mono text-[12px] text-white tracking-[0.1em] font-bold uppercase text-right">AI • GROWTH • SYSTEMS</span>
                        </div>
                        <div class="flex justify-between items-center border-b border-white/5 pb-6">
                            <span class="font-mono text-[10px] text-neutral-500 tracking-[0.2em] uppercase">AUTHORS</span>
                            <span class="font-mono text-[12px] text-white tracking-[0.1em] font-bold uppercase text-right">ELEVIX TEAM <span class="text-neutral-500 block md:inline">(LAHORE, PAK)</span></span>
                        </div>
                        <div class="flex justify-between items-center border-b border-white/5 pb-6">
                            <span class="font-mono text-[10px] text-neutral-500 tracking-[0.2em] uppercase">STATUS</span>
                            <span class="font-mono text-[12px] text-kinetic-red tracking-[0.1em] font-bold uppercase text-right">PUBLISHING</span>
                        </div>
                    </div>

                    <!-- Footer Link -->
                    <a href="#contact" class="flex justify-between items-center mt-8 font-mono text-[10px] text-white tracking-[0.2em] uppercase font-bold hover:text-kinetic-red transition-colors relative z-10 w-full group">
                        BOOK A 30-MIN AUDIT 
                        <span class="group-hover:translate-x-1 transition-transform">→</span>
                    </a>
                </div>
            </div>

        </div>
    </section>
</body>
</html>
"""

    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(blog_content)
        
    print("blog.html has been fully built and nav links are updated.")

if __name__ == '__main__':
    main()
