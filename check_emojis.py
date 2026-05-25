import re
import json

file_path = r'c:\Users\DIGITAL META\Downloads\reviews-FINAL.html'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    emojis = set(re.findall(r'[^\w\s,\.\-;:!\?\'\"<>\/\\=\+\(\)\[\]\{\}#&@\$\*%\^\|`~_]+', content))
    clean_emojis = [e for e in emojis if not e.isascii()]
    
    with open('emojis.json', 'w', encoding='utf-8') as f:
        json.dump(clean_emojis, f, ensure_ascii=False, indent=2)
except Exception as e:
    with open('emojis.json', 'w') as f:
        f.write(str(e))
