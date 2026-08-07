import os

def main():
    # Read index.html
    with open('c:\\Elevix Digital\\index.html', 'r', encoding='utf-8') as f:
        index_html = f.read()

    # Find the newly added case-studies-section
    start_marker = '<section id="case-studies-section" class="relative pt-32'
    end_marker = '    <!-- // D. Audit Offer & Value Prop Section -->'
    
    start_idx = index_html.find(start_marker)
    
    if start_idx == -1:
        print("Could not find case-studies-section in index.html")
        # Maybe it's still named something else? Let's check for "Results we can ship on a screenshot."
        start_idx = index_html.find('Results we can ship<br />on a screenshot.')
        if start_idx != -1:
            # backtrack to the nearest <section> or <header>
            section_start = index_html.rfind('<section', 0, start_idx)
            header_start = index_html.rfind('<header', 0, start_idx)
            start_idx = max(section_start, header_start)
    
    # Let's find the end of the contact section
    contact_start = index_html.find('<section id="contact"', start_idx)
    contact_end = index_html.find('</section>', contact_start) + len('</section>')
    
    case_studies_content = index_html[start_idx:contact_end]
    
    # Remove it from index.html
    new_index_html = index_html[:start_idx] + index_html[contact_end:]
    
    # Let's also make sure the old #results section is fully gone from index.html
    # It was a <section id="results" ... >
    # Actually wait, in my previous script, I completely replaced the old #results section with the case studies content!
    # So if I remove case_studies_content, both are gone! Which matches "delete it from my homepage".
    
    # Fix the links in index.html to point back to "case-studies.html"
    new_index_html = new_index_html.replace('href="#case-studies-section"', 'href="case-studies.html"')
    
    with open('c:\\Elevix Digital\\index.html', 'w', encoding='utf-8') as f:
        f.write(new_index_html)
        
    # Now create case-studies.html based on our-story.html
    with open('c:\\Elevix Digital\\our-story.html', 'r', encoding='utf-8') as f:
        our_story_html = f.read()
        
    # Replace the main content of our-story.html with case_studies_content
    # The main content in our-story starts with <!-- HERO SECTION --> and ends with the </section> before the <footer>
    story_start = our_story_html.find('<!-- HERO SECTION -->')
    footer_start = our_story_html.find('<footer class="')
    if footer_start == -1:
        footer_start = our_story_html.rfind('<footer')
        
    new_case_studies = our_story_html[:story_start] + case_studies_content + "\n\n" + our_story_html[footer_start:]
    
    # Fix the background of the case studies hero. In our-story, the background is in the hero section.
    # We should make sure the case studies hero doesn't have duplicate background.
    # Actually, the user liked the background we had. I'll just change <section id="case-studies-section" class="relative pt-32...> 
    # to <header class="relative pt-40...> to restore its top padding since it's now at the top of a page.
    new_case_studies = new_case_studies.replace('<section id="case-studies-section" class="relative pt-32', '<header class="relative pt-40 lg:pt-48')
    new_case_studies = new_case_studies.replace('</section>\n    <!-- // 02 . THE WORK (Case Studies Grid) -->', '</header>\n    <!-- // 02 . THE WORK (Case Studies Grid) -->')
    
    with open('c:\\Elevix Digital\\case-studies.html', 'w', encoding='utf-8') as f:
        f.write(new_case_studies)
        
    print("Extracted Case Studies content, saved to case-studies.html, and removed from index.html.")
    
if __name__ == "__main__":
    main()
