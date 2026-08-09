import re

def remove_location_map():
    with open('our-story.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # The section starts with: <!-- Address & Global Reach Map Section -->
    # and ends before <!-- Footer -->
    
    pattern = r'<!-- Address & Global Reach Map Section -->.*?</section>'
    
    if re.search(pattern, html, flags=re.DOTALL):
        updated_html = re.sub(pattern, '', html, count=1, flags=re.DOTALL)
        with open('our-story.html', 'w', encoding='utf-8') as f:
            f.write(updated_html)
        print("Successfully removed location map from our-story.html")
    else:
        print("Location map section not found")

if __name__ == "__main__":
    remove_location_map()
