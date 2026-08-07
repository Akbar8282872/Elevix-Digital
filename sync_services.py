import re

# Read index.html to extract the exact services section
with open(r'c:\Elevix Digital\index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

services_match = re.search(r'    <!-- Services Section.*?    </section>', index_html, re.DOTALL)
if not services_match:
    print("Could not find services section in index.html")
    exit(1)
    
exact_homepage_services = services_match.group(0)

# Clean up fade-up classes to guarantee visibility
exact_homepage_services = exact_homepage_services.replace('fade-up', '')

# Read services.html
with open(r'c:\Elevix Digital\services.html', 'r', encoding='utf-8') as f:
    services_html = f.read()

# Replace the existing services section in services.html
services_pattern = r'    <!-- 6-Pillar Services Grid.*?    </section>'
services_html = re.sub(services_pattern, exact_homepage_services, services_html, flags=re.DOTALL)

with open(r'c:\Elevix Digital\services.html', 'w', encoding='utf-8') as f:
    f.write(services_html)

print("Successfully synced services grid from index.html to services.html")
