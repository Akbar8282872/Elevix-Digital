import re

with open('c:/Elevix Digital/careers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add "Home / Career" breadcrumb above the Left Content Pill
breadcrumb = '''<!-- Breadcrumb -->
                <div class="font-display text-[13px] text-[#71717a] mb-12 flex items-center gap-2">
                    <a href="index.html" class="hover:text-white transition-colors">Home</a> 
                    <span class="text-white/20">/</span> 
                    <span class="text-white font-medium">Career</span>
                </div>
                
                <!-- Pill -->'''
text = text.replace('<!-- Pill -->', breadcrumb)

# 2. Push the entire hero container down slightly
text = text.replace(
    'class="relative z-10 w-full max-w-7xl mx-auto px-6 md:px-12 lg:px-24 flex flex-col md:flex-row items-center justify-between mt-8 md:mt-12 mb-24 md:mb-32"',
    'class="relative z-10 w-full max-w-7xl mx-auto px-6 md:px-12 lg:px-24 flex flex-col md:flex-row items-start justify-between mt-16 md:mt-24 mb-16 md:mb-24"'
)
# Note: changed items-center to items-start so we can independently push the right side down.

# 3. Push the right side card down slightly
text = text.replace(
    '<div class="w-full md:w-[450px] mt-16 md:mt-0 fade-up" style="transition-delay: 200ms;">',
    '<div class="w-full md:w-[450px] mt-16 md:mt-[100px] fade-up" style="transition-delay: 200ms;">'
)

# 4. Change Neogen to Elevix
text = text.replace(
    'Neogen hires exceptional people first',
    'Elevix hires exceptional people first'
)

with open('c:/Elevix Digital/careers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Final layout tweaks applied successfully.")
