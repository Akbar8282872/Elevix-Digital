import json

with open(r'C:\Users\Akbar Ali\.gemini\antigravity-ide\brain\a5218241-057a-43da-83d5-b761b7950147\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if '"type":"USER_INPUT"' in line:
            data = json.loads(line)
            content = data.get('content', '')
            if 'career' in content.lower():
                print('--- USER SAID ---')
                print(content[:1000])
