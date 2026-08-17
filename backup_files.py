import shutil
import os

files_to_backup = [
    'our-story.html',
    'services.html',
    'case-studies.html',
    'blog.html',
    'careers.html'
]

for file in files_to_backup:
    src = f'c:/Elevix Digital/{file}'
    dst = f'c:/Elevix Digital/{file.replace(".html", "_original.html")}'
    if os.path.exists(src):
        shutil.copy(src, dst)
        print(f'Backed up {file} to {dst}')
    else:
        print(f'Warning: {file} not found!')
