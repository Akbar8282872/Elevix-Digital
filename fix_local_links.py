import os
import glob

def fix_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    content = content.replace('services%20sub%20folder', 'services sub folder')
    content = content.replace('design%20creative.html', 'design creative.html')
    content = content.replace('SEO%20services.html', 'SEO services.html')
    
    # Check if we broke anything
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed links in {file_path}")

root_dir = r"c:\Elevix Digital"
sub_dir = r"c:\Elevix Digital\services sub folder"

for f in glob.glob(os.path.join(root_dir, "*.html")):
    fix_links(f)

for f in glob.glob(os.path.join(sub_dir, "*.html")):
    fix_links(f)

print("Done fixing links.")
