import re

def sync_footers():
    # 1. Read footer from services.html
    with open('services.html', 'r', encoding='utf-8') as f:
        services_html = f.read()

    footer_match = re.search(r'(<footer.*?</script>\s*</body>)', services_html, re.DOTALL)
    if not footer_match:
        print("Could not find footer in services.html")
        return

    footer_content = footer_match.group(1)

    # 2. Update our-story.html
    with open('our-story.html', 'r', encoding='utf-8') as f:
        our_story = f.read()
    
    our_story_updated = re.sub(r'<footer.*?</script>\s*</body>', footer_content, our_story, flags=re.DOTALL)
    
    with open('our-story.html', 'w', encoding='utf-8') as f:
        f.write(our_story_updated)
    print("Updated our-story.html footer")

    # 3. Update case-studies.html
    with open('case-studies.html', 'r', encoding='utf-8') as f:
        case_studies = f.read()
    
    case_studies_updated = re.sub(r'<footer.*?</script>\s*</body>', footer_content, case_studies, flags=re.DOTALL)
    
    with open('case-studies.html', 'w', encoding='utf-8') as f:
        f.write(case_studies_updated)
    print("Updated case-studies.html footer")

if __name__ == "__main__":
    sync_footers()
