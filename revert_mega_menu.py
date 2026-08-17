import glob
import re

# We will read index.html to extract the exact 6 service blocks we currently have.
with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all 6 mega-cols
mega_cols = re.findall(r'(<div class="mega-col">.*?</ul></div>)', content, re.DOTALL)

if len(mega_cols) != 6:
    print(f"Error: Found {len(mega_cols)} mega-cols instead of 6.")
    exit(1)

# The HTML to revert to
old_grid = f"""<div style="display:grid; grid-template-columns:repeat(2, 1fr); gap: 40px 60px;">
                <!-- Left 50% -->
                <div style="display: flex; flex-direction: column; gap: 40px;">
                    {mega_cols[0]}
                    {mega_cols[1]}
                    {mega_cols[2]}
                </div>
                <!-- Right 50% -->
                <div style="display: flex; flex-direction: column; gap: 40px;">
                    {mega_cols[3]}
                    {mega_cols[4]}
                    {mega_cols[5]}
                </div>
            </div>"""

for file_path in glob.glob('c:/Elevix Digital/*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # We replace the 3-column grid back to the 2-column flex setup
    # Look for the exact 3-column block we just inserted.
    match = re.search(r'(<div style="display:grid; grid-template-columns:repeat\(3, 1fr\); gap: 40px 60px;">.*?</div>\s*</div>\s*</div>)', file_content, re.DOTALL)
    
    if match:
        # Wait, the </div> counting might be tricky. Let's just match everything between the <div grid> and the end of the last mega-col
        # Actually it's better to just grab the whole grid container:
        match_grid = re.search(r'(<div style="display:grid; grid-template-columns:repeat\(3, 1fr\); gap: 40px 60px;">\s*<div class="mega-col">.*?</script>)', file_content, re.DOTALL)
        if match_grid:
            # We want to keep everything AFTER the 6th mega_col.
            # But the easiest way is to just rebuild the whole services-mega-panel inner content.
            pass

for file_path in glob.glob('c:/Elevix Digital/*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
        
    # Let's target the exact string block that currently exists.
    # The 3-column wrapper we injected was `<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap: 40px 60px;">`
    # and it ended with 6 mega-cols and a closing `</div>`.
    
    # We'll use a more robust regex that finds the 3-column grid opening, all its content, until the closing div.
    match = re.search(r'(<div style="display:grid; grid-template-columns:repeat\(3, 1fr\); gap: 40px 60px;">\s*<div class="mega-col">.*?</ul></div>\s*</div>)', file_content, re.DOTALL)
    
    if match:
        new_file_content = file_content.replace(match.group(1), old_grid)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_file_content)
        print(f"Reverted {file_path}")
    else:
        print(f"Pattern not found in {file_path}")

print("Done reverting mega menu layout.")
