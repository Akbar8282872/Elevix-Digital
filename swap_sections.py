import sys

def main():
    try:
        # Read case-studies.html
        with open('c:\\Elevix Digital\\case-studies.html', 'r', encoding='utf-8') as f:
            case_studies_html = f.read()

        # Read index.html
        with open('c:\\Elevix Digital\\index.html', 'r', encoding='utf-8') as f:
            index_html = f.read()

        # Extract content from case-studies.html (everything between <!-- MAIN HERO --> and <!-- // D. Audit Offer --> or the end of the sections)
        # We want the <header> and the sections after it.
        start_marker = "    <!-- MAIN HERO (WITH ORB BG) -->"
        end_marker = "    <!-- // D. Audit Offer & Value Prop Section -->"
        
        start_idx = case_studies_html.find(start_marker)
        end_idx = case_studies_html.find(end_marker)
        
        if start_idx == -1 or end_idx == -1:
            print("Could not find markers in case-studies.html")
            return
            
        case_studies_content = case_studies_html[start_idx:end_idx]
        
        # We need to change the <header> tag to <section id="case-studies-section"> so it acts like a section in index.html
        case_studies_content = case_studies_content.replace('<header class="relative pt-40', '<section id="case-studies-section" class="relative pt-32')
        case_studies_content = case_studies_content.replace('</header>', '</section>')
        
        # Now find the old #results section in index.html to replace
        old_results_start = "    <!-- Results / Case Studies Section -->"
        old_results_end = "    <!-- Services Section with Figma-level Modern Spotlight Hover Animations -->"
        
        idx_start = index_html.find(old_results_start)
        idx_end = index_html.find(old_results_end)
        
        if idx_start == -1 or idx_end == -1:
            print("Could not find old results section in index.html")
            return
            
        new_index_html = index_html[:idx_start] + case_studies_content + index_html[idx_end:]
        
        # Write back to index.html
        with open('c:\\Elevix Digital\\index.html', 'w', encoding='utf-8') as f:
            f.write(new_index_html)
            
        print("Successfully merged case studies into index.html!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
