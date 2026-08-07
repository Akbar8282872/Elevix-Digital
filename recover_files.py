import json
import os
import re

log_path = r"C:\Users\Akbar Ali\.gemini\antigravity-ide\brain\51382114-2c62-4178-a177-034903f04bbb\.system_generated\logs\transcript_full.jsonl"
out_dir = r"c:\Elevix Digital\recovered_backups"

def extract_backups():
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    print("Parsing transcript...")
    
    file_versions = {}
    
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                entry = json.loads(line)
                created_at = entry.get('created_at', '')
                
                # We need to find when the agent replaced the whole file or chunks.
                # Actually, the agent uses `multi_replace_file_content` to edit. 
                # If we don't have a FULL file dump, we can't reconstruct easily.
                # Did I ever use `write_to_file` on index.html?
                if entry.get('type') == 'PLANNER_RESPONSE' and 'tool_calls' in entry:
                    for call in entry['tool_calls']:
                        if call.get('name') == 'write_to_file':
                            args = call.get('args', {})
                            target = args.get('TargetFile', '')
                            if 'index.html' in target.lower():
                                content = args.get('CodeContent', '')
                                safe_time = created_at.replace(':', '-')
                                with open(os.path.join(out_dir, f"index_{safe_time}.html"), 'w', encoding='utf-8') as out_f:
                                    out_f.write(content)
                                print(f"Recovered index.html full write from {created_at}")

                # What about view_file? If the agent read the whole file in chunks?
                if entry.get('type') == 'TOOL_RESPONSE':
                    tool_name = entry.get('tool_name', '')
                    if tool_name == 'default_api:view_file':
                        output = entry.get('content', '')
                        if 'index.html' in output.lower():
                            # Extract lines from output
                            safe_time = created_at.replace(':', '-')
                            with open(os.path.join(out_dir, f"index_view_{safe_time}.txt"), 'w', encoding='utf-8') as out_f:
                                out_f.write(output)

            except Exception as e:
                pass
                
    print("Done checking transcript.")

if __name__ == "__main__":
    extract_backups()
