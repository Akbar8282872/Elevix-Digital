import glob

old_css = """          .mega-col-item { display: inline-flex; align-items: center; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 13px; color: #d1d5db; text-decoration: none; transition: color 0.2s; font-weight: 500; cursor: pointer; }
          .mega-col-item:hover { color: #FDFDFD; }"""

new_css = """          .mega-col-item { position: relative; display: inline-flex; align-items: center; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 13px; color: #d1d5db; text-decoration: none; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); font-weight: 500; cursor: pointer; transform: translateX(0); }
          .mega-col-item:hover { color: #FDFDFD; transform: translateX(6px); }
          .mega-col-item::before { content: ''; position: absolute; left: -14px; top: 50%; transform: translateY(-50%) scale(0); width: 5px; height: 5px; border-radius: 50%; background: #E8282B; opacity: 0; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
          .mega-col-item:hover::before { opacity: 1; transform: translateY(-50%) scale(1); box-shadow: 0 0 8px rgba(232, 40, 43, 0.6); }"""

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_css in content:
        content = content.replace(old_css, new_css)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
