const fs = require('fs');

const content = fs.readFileSync('our-story.html', 'utf8');
const lines = content.split('\n');

// Find the line index for "<!-- Hero Section -->" and "<!-- Footer -->"
const startIdx = lines.findIndex(l => l.includes('<!-- Hero Section -->'));
const endIdx = lines.findIndex(l => l.includes('<!-- Footer -->'));

const newBody = `    <!-- Our Story Header -->
    <section class="relative pt-40 pb-24 px-6 overflow-hidden">
        <div class="max-w-7xl mx-auto relative z-10 text-center">
            <div class="font-mono text-kinetic-red text-[11px] font-bold uppercase tracking-[0.3em] mb-8 flex items-center justify-center gap-4">
                <span class="w-8 h-[1px] bg-kinetic-red/60"></span>
                THE STORY OF ELEVIX
                <span class="w-8 h-[1px] bg-kinetic-red/60"></span>
            </div>
            
            <h1 class="font-display text-[50px] sm:text-[70px] md:text-[90px] font-bold tracking-tighter leading-[1.0] text-white mb-8">
                Akbar Ali
            </h1>
            <p class="font-display text-on-secondary-container max-w-3xl mx-auto text-[18px] md:text-[20px] leading-[1.6]">
                We built Elevix Digital because we were tired of agencies pretending they still work the old way. We are a collective of systems engineers, marketers, and operators.
            </p>
        </div>
    </section>

    <!-- The Team -->
    <section class="py-24 px-6 bg-[#050505] border-t border-white/5 relative z-10">
        <div class="max-w-7xl mx-auto">
            <h2 class="font-display text-[40px] md:text-[50px] font-bold text-white mb-16 tracking-tight">The <span class="text-kinetic-red">Core.</span></h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Team Member 1 -->
                <div class="border border-white/10 bg-[#0A0A0A] p-8 relative group hover:border-kinetic-red/50 transition-colors">
                    <div class="w-3 h-3 border-t border-l border-kinetic-red absolute top-0 left-0"></div>
                    <div class="w-3 h-3 border-b border-r border-kinetic-red absolute bottom-0 right-0"></div>
                    <h3 class="font-display text-[24px] font-bold text-white mb-2 group-hover:text-kinetic-red transition-colors">Aziz Heema</h3>
                    <p class="font-mono text-[10px] text-on-secondary-container tracking-widest uppercase">Founder & CEO</p>
                </div>
                <!-- Team Member 2 -->
                <div class="border border-white/10 bg-[#0A0A0A] p-8 relative group hover:border-kinetic-red/50 transition-colors">
                    <div class="w-3 h-3 border-t border-l border-kinetic-red absolute top-0 left-0"></div>
                    <div class="w-3 h-3 border-b border-r border-kinetic-red absolute bottom-0 right-0"></div>
                    <h3 class="font-display text-[24px] font-bold text-white mb-2 group-hover:text-kinetic-red transition-colors">Ali Raja</h3>
                    <p class="font-mono text-[10px] text-on-secondary-container tracking-widest uppercase">Manager & Vibe Coder</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Our Values / Story -->
    <section class="py-32 px-6 bg-[#0A0A0A] relative z-10">
        <div class="max-w-7xl mx-auto">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-0 border-b border-white/10">
                <!-- Value 1 -->
                <div class="p-10 relative border-l border-r md:border-r-0 border-white/10 group">
                    <div class="w-4 h-4 border-t-2 border-l-2 border-kinetic-red absolute -top-[1px] -left-[1px]"></div>
                    <div class="w-4 h-4 border-b-2 border-r-2 border-kinetic-red absolute -bottom-[1px] -right-[1px]"></div>
                    <div class="font-mono text-kinetic-red text-[11px] font-bold tracking-[0.2em] uppercase mb-8">
                        // 04
                    </div>
                    <h3 class="font-display text-[28px] font-bold text-white mb-6">Radical Ownership</h3>
                    <p class="font-display text-on-secondary-container text-[16px] leading-[1.8]">
                        Responsibility without excuses. Client numbers miss, we own it. A deadline slips, we own it. No finger-pointing at platforms, vendors, or algorithms.
                    </p>
                </div>
                <!-- Value 2 -->
                <div class="p-10 relative border-l border-r border-white/10 group">
                    <div class="w-4 h-4 border-t-2 border-l-2 border-kinetic-red absolute -top-[1px] -left-[1px]"></div>
                    <div class="w-4 h-4 border-b-2 border-r-2 border-kinetic-red absolute -bottom-[1px] -right-[1px]"></div>
                    <div class="font-mono text-kinetic-red text-[11px] font-bold tracking-[0.2em] uppercase mb-8">
                        // 05
                    </div>
                    <h3 class="font-display text-[28px] font-bold text-white mb-6">Transparent Partnership</h3>
                    <p class="font-display text-on-secondary-container text-[16px] leading-[1.8]">
                        Honest communication on progress and ROI. If the campaign isn't working, you hear it from us before you notice it in the dashboard.
                    </p>
                </div>
                <!-- Value 3 -->
                <div class="p-10 relative border-l border-r md:border-l-0 border-white/10 group">
                    <div class="w-4 h-4 border-t-2 border-l-2 border-kinetic-red absolute -top-[1px] -left-[1px]"></div>
                    <div class="w-4 h-4 border-b-2 border-r-2 border-kinetic-red absolute -bottom-[1px] -right-[1px]"></div>
                    <div class="font-mono text-kinetic-red text-[11px] font-bold tracking-[0.2em] uppercase mb-8">
                        // 06
                    </div>
                    <h3 class="font-display text-[28px] font-bold text-white mb-6">Relentless Improvement</h3>
                    <p class="font-display text-on-secondary-container text-[16px] leading-[1.8]">
                        Compounding systems that improve monthly. Every retrospective ships at least one process upgrade into the next sprint.
                    </p>
                </div>
            </div>
        </div>
    </section>
`;

const head = lines.slice(0, startIdx).join('\\n');
const foot = lines.slice(endIdx).join('\\n');

fs.writeFileSync('our-story.html', head + '\\n' + newBody + '\\n    ' + foot);
console.log("Updated our-story.html");
