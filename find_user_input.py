import json

transcript_path = r'C:\Users\Akbar Ali\.gemini\antigravity-ide\brain\a5218241-057a-43da-83d5-b761b7950147\.system_generated\logs\transcript_full.jsonl'

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('type') == 'USER_INPUT':
                content = data.get('content', '')
                if 'service' in content.lower() and 'hero' in content.lower():
                    print(f"User Input Step {data.get('step_index')}: {content.strip()}")
        except Exception as e:
            pass
