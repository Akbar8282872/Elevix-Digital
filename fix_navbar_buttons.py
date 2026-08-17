import os
import re

html_files = [f for f in os.listdir('c:/Elevix Digital') if f.endswith('.html')]

for filename in html_files:
    filepath = os.path.join('c:/Elevix Digital', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to make sure the Services button in the navbar goes to services.html on click.
    # The button looks like: <button id="services-trigger-btn">
    # Or maybe it has classes.
    
    # Let's replace it:
    if 'id="services-trigger-btn"' in content:
        # check if it already has onclick
        if 'onclick="window.location.href=\'services.html\'"' not in content:
            # We replace <button id="services-trigger-btn"> with <button id="services-trigger-btn" onclick="window.location.href='services.html'">
            new_content = re.sub(
                r'<button([^>]*)id="services-trigger-btn"([^>]*)>',
                r'<button\1id="services-trigger-btn"\2 onclick="window.location.href=\'services.html\'">',
                content
            )
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {filename}")

print("Done fixing buttons.")
