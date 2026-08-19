import re

def replace_code_block_with_image(file_path, image_name):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The code block starts right after <!-- 1. Small Code Block (Top Left) -->
    # and ends before <!-- 2. Defining 3D Web Dev Image
    
    # We want to keep the wrapper div if possible, or just replace the whole thing.
    # The wrapper is: <div class="absolute -top-16 left-4 md:left-4 w-[85%] max-w-[300px] bg-[#0A0A0A]/95 backdrop-blur-2xl border border-white/10 rounded-xl shadow-[0_20px_40px_rgba(0,0,0,0.8)] overflow-hidden z-20 transform md:rotate-y-[5deg] md:rotate-x-[2deg] hover:rotate-0 transition-transform duration-700 animate-[float_5s_ease-in-out_infinite]">
    
    # Let's just find the entire div and replace it.
    
    pattern = r'(<!-- 1\. Small Code Block \(Top Left\) -->\s*<div class="absolute -top-16 left-4.*?animate-\[float_5s_ease-in-out_infinite\]">).*?(<!-- 2\. Defining 3D)'
    
    # Replacement string: keep the wrapper, put the img inside, close the wrapper.
    replacement = r'\1\n                    <img src="' + image_name + r'" alt="Concept" class="w-full h-auto" style="filter: drop-shadow(0 0 10px rgba(232,40,43,0.3));" />\n                </div>\n\n                \2'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {file_path} with {image_name}")


replace_code_block_with_image('c:\\Elevix Digital\\services sub folder\\ai-automation.html', 'ai_dev_hud.jpg')
replace_code_block_with_image('c:\\Elevix Digital\\services sub folder\\app-development.html', 'app_dev_hud.jpg')

