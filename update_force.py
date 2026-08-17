import re

with open('c:/Elevix Digital/our-story.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Heading
content = content.replace(
    "Two humans. A hundred agents. One operating system.",
    "Six humans. A hundred agents. One operating system."
)

# 2. Update // HUMANS tag
content = content.replace(
    "// HUMANS &bull; 2",
    "// HUMANS &bull; 6"
)
content = content.replace(
    "// HUMANS • 2",
    "// HUMANS • 6"
)

# 3. Update the Avatars
old_avatars = """                    <div class="flex flex-wrap gap-4 mb-20">
                        <!-- AC -->
                        <div class="w-[80px] h-[80px] rounded-full border border-kinetic-red/30 flex items-center justify-center text-white font-display font-bold text-[18px] relative group-hover:shadow-[0_0_30px_rgba(232,40,43,0.4)] transition-all duration-500 bg-black z-10 hover:scale-110 cursor-pointer">
                            <div class="absolute inset-0 rounded-full border border-kinetic-red animate-ping opacity-20"></div>
                            AC
                        </div>
                        <!-- AR -->
                        <div class="w-[80px] h-[80px] rounded-full border border-kinetic-red/30 flex items-center justify-center text-white font-display font-bold text-[18px] relative group-hover:shadow-[0_0_30px_rgba(232,40,43,0.4)] transition-all duration-500 bg-black z-10 hover:scale-110 cursor-pointer">
                            <div class="absolute inset-0 rounded-full border border-kinetic-red animate-ping opacity-20" style="animation-delay: 1s;"></div>
                            AR
                        </div>
                    </div>"""

new_avatars = """                    <div class="flex flex-wrap gap-4 mb-20 justify-center md:justify-start">
                        <!-- AC -->
                        <div class="w-[60px] h-[60px] md:w-[70px] md:h-[70px] lg:w-[80px] lg:h-[80px] rounded-full border border-kinetic-red/30 flex items-center justify-center text-white font-display font-bold text-[16px] md:text-[18px] relative group-hover:shadow-[0_0_30px_rgba(232,40,43,0.4)] transition-all duration-500 bg-black z-10 hover:-translate-y-2 cursor-pointer flex-shrink-0">
                            <div class="absolute inset-0 rounded-full border border-kinetic-red animate-ping opacity-20" style="animation-delay: 0s;"></div>
                            AC
                        </div>
                        <!-- AR -->
                        <div class="w-[60px] h-[60px] md:w-[70px] md:h-[70px] lg:w-[80px] lg:h-[80px] rounded-full border border-kinetic-red/30 flex items-center justify-center text-white font-display font-bold text-[16px] md:text-[18px] relative group-hover:shadow-[0_0_30px_rgba(232,40,43,0.4)] transition-all duration-500 bg-black z-10 hover:-translate-y-2 cursor-pointer flex-shrink-0">
                            <div class="absolute inset-0 rounded-full border border-kinetic-red animate-ping opacity-20" style="animation-delay: 0.5s;"></div>
                            AR
                        </div>
                        <!-- AH -->
                        <div class="w-[60px] h-[60px] md:w-[70px] md:h-[70px] lg:w-[80px] lg:h-[80px] rounded-full border border-kinetic-red/30 flex items-center justify-center text-white font-display font-bold text-[16px] md:text-[18px] relative group-hover:shadow-[0_0_30px_rgba(232,40,43,0.4)] transition-all duration-500 bg-black z-10 hover:-translate-y-2 cursor-pointer flex-shrink-0">
                            <div class="absolute inset-0 rounded-full border border-kinetic-red animate-ping opacity-20" style="animation-delay: 1.0s;"></div>
                            AH
                        </div>
                        <!-- AM -->
                        <div class="w-[60px] h-[60px] md:w-[70px] md:h-[70px] lg:w-[80px] lg:h-[80px] rounded-full border border-kinetic-red/30 flex items-center justify-center text-white font-display font-bold text-[16px] md:text-[18px] relative group-hover:shadow-[0_0_30px_rgba(232,40,43,0.4)] transition-all duration-500 bg-black z-10 hover:-translate-y-2 cursor-pointer flex-shrink-0">
                            <div class="absolute inset-0 rounded-full border border-kinetic-red animate-ping opacity-20" style="animation-delay: 1.5s;"></div>
                            AM
                        </div>
                        <!-- FT -->
                        <div class="w-[60px] h-[60px] md:w-[70px] md:h-[70px] lg:w-[80px] lg:h-[80px] rounded-full border border-kinetic-red/30 flex items-center justify-center text-white font-display font-bold text-[16px] md:text-[18px] relative group-hover:shadow-[0_0_30px_rgba(232,40,43,0.4)] transition-all duration-500 bg-black z-10 hover:-translate-y-2 cursor-pointer flex-shrink-0">
                            <div class="absolute inset-0 rounded-full border border-kinetic-red animate-ping opacity-20" style="animation-delay: 2.0s;"></div>
                            FT
                        </div>
                        <!-- SD -->
                        <div class="w-[60px] h-[60px] md:w-[70px] md:h-[70px] lg:w-[80px] lg:h-[80px] rounded-full border border-kinetic-red/30 flex items-center justify-center text-white font-display font-bold text-[16px] md:text-[18px] relative group-hover:shadow-[0_0_30px_rgba(232,40,43,0.4)] transition-all duration-500 bg-black z-10 hover:-translate-y-2 cursor-pointer flex-shrink-0">
                            <div class="absolute inset-0 rounded-full border border-kinetic-red animate-ping opacity-20" style="animation-delay: 2.5s;"></div>
                            SD
                        </div>
                    </div>"""

if old_avatars in content:
    content = content.replace(old_avatars, new_avatars)
else:
    print("Could not find the old avatars div to replace.")
    exit(1)

with open('c:/Elevix Digital/our-story.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated the Force Multiplier section.")
