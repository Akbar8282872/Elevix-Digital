import glob

# Target string to remove
target = "border-top:2px solid #E8282B; "

for file_path in glob.glob('c:/Elevix Digital/*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target in content:
        new_content = content.replace(target, "")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed red line from {file_path}")

print("Done removing red line from mega menu.")
