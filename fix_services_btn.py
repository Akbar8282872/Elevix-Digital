import re

with open('c:/Elevix Digital/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The button is: <button id="services-trigger-btn">Services <svg ...
# Let's add onclick to it
target = '<button id="services-trigger-btn">'
replacement = '<button id="services-trigger-btn" onclick="window.location.href=\'services.html\'" style="cursor: pointer;">'

if target in text:
    text = text.replace(target, replacement)
    with open('c:/Elevix Digital/index.html', 'w', encoding='utf-8') as f2:
        f2.write(text)
    print("Fixed Services button click!")
else:
    print("Could not find the Services button.")
