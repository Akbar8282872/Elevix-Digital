import re

with open('c:/Elevix Digital/services sub folder/web-development.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<!-- 2. BEST DIAGRAM OF CHART TYPE (NATIVE HTML, NO PIC) -->'
end_marker = '<!-- GSAP Typewriter initialization -->'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_image_code = """<!-- 2. BEST DIAGRAM OF CHART TYPE (AI IMAGE) -->
                <div class="relative w-full max-w-[450px] perspective-[1200px] animate-[float_6s_ease-in-out_infinite_reverse] z-20 ml-auto mt-4">
                    <img src="../hud_diagram.png" alt="Web Architecture Diagram" class="w-full h-auto object-contain mix-blend-screen drop-shadow-[0_0_25px_rgba(232,40,43,0.4)] opacity-90 transform hover:scale-105 transition-transform duration-700">
                </div>

                """
    
    text = text[:start_idx] + new_image_code + text[end_idx:]
    
    with open('c:/Elevix Digital/services sub folder/web-development.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Replaced HTML diagram with AI Image!")
else:
    print("Could not find markers.")
