import re

with open('c:/Elevix Digital/services sub folder/web-development.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<!-- Premium Generated Image Architecture Map -->'
end_marker = '<!-- THE ANIMATED TERMINAL CODE BLOCK (Moved DOWN safely) -->'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    transparent_image_block = """<!-- Premium Generated Image Architecture Map (Transparent Style) -->
                <div class="relative w-full max-w-[400px] group perspective-[1000px] z-10 mx-auto lg:ml-auto mt-16 animate-[float_6s_ease-in-out_infinite]">
                    <!-- Glowing aura behind the image -->
                    <div class="absolute inset-0 bg-kinetic-red/10 blur-[80px] group-hover:bg-kinetic-red/30 transition-colors duration-1000 animate-[pulse_4s_infinite]"></div>
                    
                    <!-- Levitating Image Wrapper (NO BACKGROUND, PURE TRANSPARENT) -->
                    <div class="relative w-full overflow-visible transform transition-transform duration-[800ms] hover:scale-[1.03] hover:rotate-y-[-5deg]">
                        
                        <!-- THE TRANSPARENT IMAGE (mix-blend-screen removes the black background) -->
                        <img src="../transparent_web_diagram.png" alt="Premium Web Architecture Diagram" class="w-full h-auto object-cover relative z-0 opacity-90 group-hover:opacity-100 transition-all duration-700 mix-blend-screen" style="filter: drop-shadow(0 0 20px rgba(232,40,43,0.3));" />
                        
                    </div>
                    
                    <!-- Floating decorative particles -->
                    <div class="absolute -top-6 -right-6 w-3 h-3 bg-kinetic-red rounded-full shadow-[0_0_15px_rgba(232,40,43,1)] animate-[float_4s_ease-in-out_infinite_reverse]"></div>
                    <div class="absolute -bottom-4 -left-4 w-2 h-2 bg-white rounded-full shadow-[0_0_10px_rgba(255,255,255,1)] animate-[float_5s_ease-in-out_infinite]"></div>
                </div>

                """
    
    text = text[:start_idx] + transparent_image_block + text[end_idx:]

with open('c:/Elevix Digital/services sub folder/web-development.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Injected transparent floating image with screen blend mode!")
