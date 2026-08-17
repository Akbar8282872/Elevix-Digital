import glob
import re

for file_path in glob.glob('c:/Elevix Digital/*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace window.location.href=\' with window.location.href='
    new_content = content.replace("window.location.href=\\'", "window.location.href='")
    # Also replace \'" with '" at the end
    new_content = new_content.replace("\\'\"", "'\"")

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {file_path}")

print("Done fixing button syntax.")
