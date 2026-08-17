import glob
import re

for file_path in glob.glob('c:/Elevix Digital/*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Tighten the CSS rules for mega-col elements
    content = content.replace('margin-bottom: 12px; } /* for mega-col-num */', '') # Just in case
    content = re.sub(r'(\.mega-col-num\s*{.*?margin-bottom:\s*)12px(;)', r'\1 4px\2', content)
    content = re.sub(r'(\.mega-col-title\s*{.*?margin:\s*0\s*0\s*)16px(\s*0;\s*padding-bottom:\s*)14px(;)', r'\1 8px\2 8px\3', content)
    content = re.sub(r'(\.mega-col-list\s*{.*?gap:\s*)10px(;)', r'\1 6px\2', content)
    
    # 2. Tighten the wrapper gap and padding
    content = content.replace('gap: 40px 60px; padding: 24px 48px 48px 48px;', 'gap: 15px 40px; padding: 16px 32px 24px 32px;')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Tightened mega menu in {file_path}")

print("Done making mega menu fit on one screen without scrolling.")
