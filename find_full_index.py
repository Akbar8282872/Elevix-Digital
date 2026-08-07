import json
import os
import re

log_path = r"C:\Users\Akbar Ali\.gemini\antigravity-ide\brain\51382114-2c62-4178-a177-034903f04bbb\.system_generated\logs\transcript_full.jsonl"
out_dir = r"c:\Elevix Digital\recovered_index"

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

def extract():
    with open(log_path, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f):
            try:
                entry = json.loads(line)
                created_at = entry.get('created_at', f"line_{idx}")
                safe_time = created_at.replace(':', '-')
                
                # Check USER_INPUT metadata
                if entry.get('type') == 'USER_INPUT':
                    content = entry.get('content', '')
                    if 'index.html' in content:
                        # Extract the content between ```html or similar if it's there
                        if '```html' in content:
                            parts = content.split('```html')
                            for i, part in enumerate(parts[1:]):
                                code = part.split('```')[0]
                                if len(code) > 5000:
                                    with open(os.path.join(out_dir, f"user_input_{safe_time}_{i}.html"), 'w', encoding='utf-8') as out_f:
                                        out_f.write(code)
                                        
                # Check Tool Responses (view_file)
                if entry.get('type') == 'TOOL_RESPONSE':
                    if entry.get('tool_name') == 'default_api:view_file':
                        output = entry.get('content', '')
                        if 'index.html' in output and len(output) > 5000:
                            # Clean up the line numbers added by view_file
                            lines = output.split('\n')
                            clean_lines = []
                            for l in lines:
                                m = re.match(r'^\d+:\s(.*)', l)
                                if m:
                                    clean_lines.append(m.group(1))
                            
                            with open(os.path.join(out_dir, f"view_file_{safe_time}.html"), 'w', encoding='utf-8') as out_f:
                                out_f.write('\n'.join(clean_lines))
                                
            except Exception as e:
                pass
                
    print(f"Extraction complete. Check {out_dir}")

if __name__ == "__main__":
    extract()
