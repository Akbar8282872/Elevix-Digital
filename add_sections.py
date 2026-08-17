import re

# Read our-story.html to extract the team section
with open('c:/Elevix Digital/our-story.html', 'r', encoding='utf-8') as f:
    story_content = f.read()

# Extract the team section from our-story.html
# It starts at <!-- The Team --> and ends before <!-- Force Multiplier Section --> or <!-- Huge CTA Banner -->
# I'll just use string find for robustness
start_team = story_content.find("<!-- The Team -->")
end_team = story_content.find("<!-- Force Multiplier Section -->")

if start_team == -1 or end_team == -1:
    print("Could not find The Team section boundaries in our-story.html")
    exit(1)

team_section = story_content[start_team:end_team].strip()

# Now create the "How we actually hire" section
hiring_section = """    <!-- How we actually hire -->
    <section class="py-24 px-6 bg-[#050505] border-t border-white/5 relative">
        <div class="max-w-7xl mx-auto">
            <div class="flex flex-col lg:flex-row gap-16 items-center">
                <!-- Left side -->
                <div class="flex-1 lg:w-1/2">
                    <h2 class="font-display font-bold text-[40px] md:text-[50px] text-white leading-[1.1] mb-10">
                        How we actually hire.
                    </h2>
                    <div class="font-display text-[16px] text-[#cfcfcf] leading-[1.8] space-y-6">
                        <p>Most agencies hire when a seat breaks. We hire on a <strong class="text-white font-medium">monthly interview sprint</strong> &mdash; not reactively, not in a panic, not only when a retainer forces our hand. Every month the founder opens a window, reviews every serious application, and sits with the strongest candidates in person.</p>
                        <p>The loop is short and honest: <strong class="text-white font-medium">screening call &rarr; paid working trial &rarr; founder final.</strong> No gauntlet of five-round interviews, no HR theatre, no ghosting. You either match the bar or you don't, and we tell you either way.</p>
                        <p>Even if no seat is formally vacant that week, exceptional candidates advance. We have built this team by making slots for the right people &mdash; not the other way around. If you are the best in the room, you are in.</p>
                    </div>
                </div>
                
                <!-- Right side -->
                <div class="flex-1 w-full lg:w-1/2 lg:pl-10 mt-8 lg:mt-0 relative">
                    <div class="bg-[#0A0A0A] border border-white/10 rounded-[12px] p-8 md:p-12 relative shadow-[0_0_30px_rgba(255,255,255,0.02)] group hover:border-white/20 transition-colors">
                        <div class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] font-bold uppercase mb-12 flex items-center gap-4">
                            <span>// THE LOOP</span>
                        </div>
                        
                        <div class="flex flex-col">
                            <!-- Step 1 -->
                            <div class="pb-8 border-b border-white/5">
                                <h3 class="font-display text-[22px] font-bold text-white mb-2 flex items-center gap-4">
                                    <span class="text-kinetic-red font-mono text-[20px] font-medium">01</span> Screening call
                                </h3>
                                <p class="text-[14px] text-white/40 font-display pl-[42px]">25 minutes &mdash; founder or ops lead</p>
                            </div>
                            
                            <!-- Step 2 -->
                            <div class="py-8 border-b border-white/5">
                                <h3 class="font-display text-[22px] font-bold text-white mb-2 flex items-center gap-4">
                                    <span class="text-kinetic-red font-mono text-[20px] font-medium">02</span> Paid working trial
                                </h3>
                                <p class="text-[14px] text-white/40 font-display pl-[42px]">Real task, real context, paid fairly</p>
                            </div>
                            
                            <!-- Step 3 -->
                            <div class="pt-8">
                                <h3 class="font-display text-[22px] font-bold text-white mb-2 flex items-center gap-4">
                                    <span class="text-kinetic-red font-mono text-[20px] font-medium">03</span> Founder final
                                </h3>
                                <p class="text-[14px] text-white/40 font-display pl-[42px]">Decision inside 7 days, always</p>
                            </div>
                        </div>
                        
                    </div>
                    <!-- Decorative element on bottom right outside the box slightly -->
                    <div class="absolute -bottom-4 -right-4 w-12 h-12 bg-kinetic-red rounded-full flex items-center justify-center text-white shadow-[0_0_20px_rgba(232,40,43,0.5)] z-10 hover:scale-110 transition-transform cursor-pointer">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# Read careers.html
with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    careers_content = f.read()

# Make sure we don't insert multiple times
if "How we actually hire." in careers_content:
    print("Already added to careers.html")
    exit(0)

# The place to insert is right before <!-- New Massive Grid Footer -->
footer_marker = "    <!-- New Massive Grid Footer -->"

if footer_marker not in careers_content:
    print("Could not find the footer marker in careers.html")
    exit(1)

# Construct new content
new_content = hiring_section + "\n\n    " + team_section + "\n\n" + footer_marker

careers_content = careers_content.replace(footer_marker, new_content)

with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(careers_content)

print("Successfully injected both sections into careers.html")
