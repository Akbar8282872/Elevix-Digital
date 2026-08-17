import json
import re

transcript_path = r'C:\Users\Akbar Ali\.gemini\antigravity-ide\brain\a5218241-057a-43da-83d5-b761b7950147\.system_generated\logs\transcript_full.jsonl'

h1s = []
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('type') in ('VIEW_FILE', 'RUN_COMMAND', 'TOOL_RESPONSE'):
                content = str(data)
                if 'services.html' in content and 'hero' in content.lower():
                    matches = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL | re.IGNORECASE)
                    for m in matches:
                        clean_text = re.sub(r'<[^>]+>', '', m).strip()
                        if clean_text not in h1s:
                            h1s.append(clean_text)
                            print(f"Step {data.get('step_index')}: {m.strip()}")
        except Exception as e:
            pass
