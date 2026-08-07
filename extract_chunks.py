import json
import os

log_path = r"C:\Users\Akbar Ali\.gemini\antigravity-ide\brain\51382114-2c62-4178-a177-034903f04bbb\.system_generated\logs\transcript_full.jsonl"

def extract_chunks():
    chunks = []
    
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                entry = json.loads(line)
                
                if entry.get('type') == 'PLANNER_RESPONSE' and 'tool_calls' in entry:
                    for call in entry['tool_calls']:
                        if call.get('name') == 'multi_replace_file_content':
                            args = call.get('args', {})
                            target = args.get('TargetFile', '')
                            if 'index.html' in target.lower():
                                rep_chunks = args.get('ReplacementChunks', [])
                                if isinstance(rep_chunks, str):
                                    try:
                                        rep_chunks = json.loads(rep_chunks)
                                    except:
                                        pass
                                if isinstance(rep_chunks, list):
                                    for c in rep_chunks:
                                        content = c.get('ReplacementContent', '')
                                        # Only save significant chunks (e.g. grids or waves)
                                        if 'grid' in content or 'wave' in content.lower():
                                            chunks.append((entry['created_at'], content))
                                            
                        if call.get('name') == 'replace_file_content':
                            args = call.get('args', {})
                            target = args.get('TargetFile', '')
                            if 'index.html' in target.lower():
                                content = args.get('ReplacementContent', '')
                                if 'grid' in content or 'wave' in content.lower():
                                    chunks.append((entry['created_at'], content))
                                            
            except Exception as e:
                pass
                
    # Save the found chunks to a text file for me to read
    with open(r'c:\Elevix Digital\recovered_chunks.txt', 'w', encoding='utf-8') as out_f:
        for time, content in chunks:
            out_f.write(f"--- TIME: {time} ---\n{content}\n\n======================\n\n")

if __name__ == "__main__":
    extract_chunks()
