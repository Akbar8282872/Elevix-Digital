import re

with open('c:/Elevix Digital/services sub folder/web-development.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Replace H1
old_h1 = """                <!-- Main Headline -->
                <h1 class="font-display font-black text-white text-[56px] md:text-[60px] leading-[1.05] tracking-tight mt-6 max-w-xl">
                    The website development company engineered to scale, <span class="text-kinetic-red drop-shadow-[0_0_20px_rgba(232,40,43,0.3)]">Elevix Digital.</span>
                </h1>"""

new_h1 = """                <!-- Main Headline -->
                <h1 class="font-display font-black text-white text-[56px] md:text-[60px] leading-[1.05] tracking-tight mt-6 max-w-xl">
                    The website development company<br>
                    engineered to scale,<br>
                    <span class="text-kinetic-red drop-shadow-[0_0_20px_rgba(232,40,43,0.3)]">Elevix Digital.</span>
                </h1>"""

text = text.replace(old_h1, new_h1)

# 2. Replace Right Side Map with Image
right_side_start = text.find('<!-- Code Snippet (Floating Top Right, On Top) -->')
right_side_end = text.find('</div>\n            </div>\n        </div>\n    </main>')

if right_side_start != -1 and right_side_end != -1:
    new_right_side = """                <!-- 4D Web Architecture Flowchart Image -->
                <div class="relative z-10 w-full max-w-[500px] rounded-[24px] overflow-hidden shadow-[0_30px_60px_rgba(232,40,43,0.2)] border border-white/10 hover:border-kinetic-red/40 transition-all duration-700 group transform hover:-translate-y-2 hover:scale-[1.02]">
                    <div class="absolute inset-0 bg-gradient-to-t from-[#0A0A0A] via-transparent to-transparent opacity-50 z-10 pointer-events-none"></div>
                    <img src="../web_architecture_chart.png" alt="Web Development Architecture Chart" class="w-full h-auto object-cover opacity-90 group-hover:opacity-100 transition-opacity duration-700" />
                    <!-- Decorative glow behind image -->
                    <div class="absolute inset-0 bg-kinetic-red mix-blend-screen opacity-10 group-hover:opacity-20 transition-opacity duration-700 pointer-events-none z-10"></div>
                </div>
"""
    text = text[:right_side_start] + new_right_side + text[right_side_end:]

with open('c:/Elevix Digital/services sub folder/web-development.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated successfully!")
