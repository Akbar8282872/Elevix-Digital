import glob
import re

# We will read index.html to extract the exact 6 service blocks we already have.
with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all 6 mega-cols
mega_cols = re.findall(r'(<div class="mega-col">.*?</ul></div>)', content, re.DOTALL)

if len(mega_cols) != 6:
    print(f"Error: Found {len(mega_cols)} mega-cols instead of 6.")
    exit(1)

# Build the new inner grid HTML
new_grid = f"""<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap: 40px 60px;">
                {mega_cols[0]}
                {mega_cols[1]}
                {mega_cols[2]}
                {mega_cols[3]}
                {mega_cols[4]}
                {mega_cols[5]}
            </div>"""

# Replace in all HTML files
for file_path in glob.glob('c:/Elevix Digital/*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # We find the <div style="display:grid... > to the closing </div> that matches it.
    # The safest way is to use regex to replace the entire <div style="display:grid; grid-template-columns:repeat(2, 1fr); gap: 40px 60px;"> ... </div>
    # Let's target the exact string block that currently exists.
    
    match = re.search(r'(<div style="display:grid; grid-template-columns:repeat\(2, 1fr\); gap: 40px 60px;">.*?</div>\s*<!-- Right 50% -->.*?</div>\s*</div>)', file_content, re.DOTALL)
    
    if match:
        new_file_content = file_content.replace(match.group(1), new_grid)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_file_content)
        print(f"Updated {file_path}")
    else:
        print(f"Pattern not found in {file_path}")

print("Done updating mega menu layout.")
