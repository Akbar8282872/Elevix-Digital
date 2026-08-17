import re

# 1. Extract Background from services.html
with open('c:/Elevix Digital/services.html', 'r', encoding='utf-8') as f:
    services_html = f.read()

bg_start = services_html.find('<div class="absolute inset-0 z-0 pointer-events-none">')
bg_end = services_html.find('</div>', services_html.find('animate-[scan_6s_linear_infinite]"></div>') + 10) + 6

# Fallback robust extraction
if bg_start == -1:
    print("Background not found!")
    exit(1)
background_html = services_html[bg_start:bg_end]

# 2. Prepare the new Hero HTML
new_hero = f"""
    <main class="relative min-h-screen pt-40 pb-24 px-6 overflow-hidden flex items-center bg-[#0a0a0a]">
        <!-- 1. Extracted Animated Background -->
        {background_html}

        <!-- 2. Hero Content -->
        <div class="max-w-7xl mx-auto w-full grid grid-cols-1 lg:grid-cols-2 gap-16 relative z-10 mt-8">
            
            <!-- Left Side: Typography -->
            <div class="w-full flex flex-col gap-6 justify-center">
                
                <!-- Breadcrumbs -->
                <div class="flex items-center gap-2 text-[11px] font-mono text-on-secondary-container tracking-widest uppercase">
                    <a href="../index.html" class="hover:text-white transition-colors cursor-pointer">Home</a>
                    <span class="opacity-50">/</span>
                    <a href="../services.html" class="hover:text-white transition-colors cursor-pointer">Services</a>
                    <span class="opacity-50">/</span>
                    <span class="text-white font-semibold">Web Development</span>
                </div>

                <!-- Badge -->
                <div class="inline-flex items-center gap-3 border border-white/10 rounded-full px-5 py-2.5 w-max bg-white/5 backdrop-blur-sm mt-4 hover:border-kinetic-red/30 transition-all cursor-default">
                    <span class="w-2 h-2 rounded-full bg-kinetic-red animate-pulse shadow-[0_0_10px_rgba(232,40,43,0.8)]"></span>
                    <span class="text-[9.5px] font-mono font-bold tracking-[0.2em] text-white uppercase">Website Development Company &middot; Elevix Digital</span>
                </div>

                <!-- Main Headline -->
                <h1 class="font-display font-black text-white text-[56px] md:text-[64px] lg:text-[72px] leading-[1.05] tracking-tight mt-6">
                    The web<br>
                    development<br>
                    company<br>
                    engineered to scale,<br>
                    <span class="text-kinetic-red drop-shadow-[0_0_20px_rgba(232,40,43,0.3)]">Elevix Digital.</span>
                </h1>
            </div>

            <!-- Right Side: Web Dev Map / Card -->
            <div class="w-full relative flex justify-end items-center mt-12 lg:mt-0">
                
                <!-- Code Snippet (Floating Behind) -->
                <div class="hidden md:block absolute -left-8 -top-8 opacity-40 font-mono text-[11px] text-white/50 bg-[#0A0A0A] p-6 rounded-xl border border-white/10 shadow-2xl transform -rotate-6 z-0 hover:-rotate-2 transition-transform duration-500">
<pre class="leading-loose">
export default function Page() {{
  return (
    &lt;main className="hero"&gt;
      &lt;Nav /&gt;
      &lt;Hero title="Elevix" /&gt;
      &lt;Footer /&gt;
    &lt;/main&gt;
  )
}}
</pre>
                </div>

                <!-- Main Capabilities Card -->
                <div class="relative z-10 w-full max-w-[420px] bg-[#0A0A0A]/90 backdrop-blur-2xl border border-white/10 rounded-[24px] p-8 lg:p-10 shadow-[0_30px_60px_rgba(0,0,0,0.9)] hover:border-kinetic-red/30 hover:shadow-[0_30px_80px_rgba(232,40,43,0.15)] transition-all duration-700 group">
                    
                    <!-- Header -->
                    <div class="flex justify-between items-center mb-8 border-b border-white/10 pb-5">
                        <div class="flex items-center gap-3">
                            <div class="w-8 h-[1px] bg-kinetic-red"></div>
                            <span class="text-[9px] font-mono tracking-[0.25em] text-white/50 uppercase">Capabilities</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <span class="w-1.5 h-1.5 rounded-full bg-kinetic-red animate-[pulse_1.5s_infinite]"></span>
                            <span class="text-[9px] font-mono tracking-widest text-kinetic-red uppercase font-bold">Live</span>
                        </div>
                    </div>

                    <!-- List Items -->
                    <div class="flex flex-col gap-7">
                        
                        <div class="flex justify-between items-center border-b border-white/5 pb-4">
                            <span class="text-[10px] font-mono tracking-widest text-white/40 uppercase transition-colors hover:text-white">Websites</span>
                            <span class="text-[10px] font-mono tracking-widest text-white font-semibold hover:text-kinetic-red transition-colors">30+ Shipped</span>
                        </div>
                        
                        <div class="flex justify-between items-center border-b border-white/5 pb-4">
                            <span class="text-[10px] font-mono tracking-widest text-white/40 uppercase transition-colors hover:text-white">Lighthouse</span>
                            <span class="text-[10px] font-mono tracking-widest text-white font-semibold hover:text-kinetic-red transition-colors">90+ Avg</span>
                        </div>
                        
                        <div class="flex justify-between items-center border-b border-white/5 pb-4">
                            <span class="text-[10px] font-mono tracking-widest text-white/40 uppercase transition-colors hover:text-white">Stack</span>
                            <span class="text-[10px] font-mono tracking-widest text-kinetic-red font-semibold drop-shadow-[0_0_8px_rgba(232,40,43,0.5)]">Next.js · WP · Shopify</span>
                        </div>
                        
                        <div class="flex justify-between items-center border-b border-white/5 pb-4">
                            <span class="text-[10px] font-mono tracking-widest text-white/40 uppercase transition-colors hover:text-white">Region</span>
                            <span class="text-[10px] font-mono tracking-widest text-white font-semibold hover:text-kinetic-red transition-colors">Lahore · Pakistan</span>
                        </div>
                        
                        <div class="flex justify-between items-center pt-2 relative overflow-hidden rounded-lg">
                            <div class="absolute right-[-20px] top-1/2 -translate-y-1/2 w-32 h-12 bg-kinetic-red/30 blur-[25px] rounded-full group-hover:bg-kinetic-red/50 transition-all duration-700"></div>
                            <span class="text-[10px] font-mono tracking-widest text-white/40 uppercase transition-colors hover:text-white relative z-10">Status</span>
                            <span class="text-[10.5px] font-mono tracking-[0.2em] text-white font-bold relative z-10" style="text-shadow: 0 0 10px rgba(232,40,43,0.6);">ACCEPTING CLIENTS</span>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </main>
"""

# 3. Inject it into web-development.html
target_file = 'c:/Elevix Digital/services sub folder/web-development.html'
with open(target_file, 'r', encoding='utf-8') as f:
    target_html = f.read()

# The placeholder in web-development.html is:
# <main class="min-h-screen pt-32 pb-24 px-6 bg-[#0a0a0a] flex items-center justify-center">
#     <!-- Main content will go here later -->
#     <h1 class="text-white font-display text-4xl">Service Content Coming Soon</h1>
# </main>

main_start = target_html.find('<main')
main_end = target_html.find('</main>') + 7

if main_start != -1 and main_end != -1:
    updated_html = target_html[:main_start] + new_hero + target_html[main_end:]
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(updated_html)
    print("Successfully built and injected the Web Development Hero Section!")
else:
    print("Could not find the <main> tag in web-development.html!")

