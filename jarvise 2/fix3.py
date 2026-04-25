import re
with open('jarvis.py', 'r', encoding='utf-8') as f:
    content = f.read()

def fix_fstring(match):
    s = match.group(0)
    if '{' not in s:
        return s[1:]
    return s

content = re.sub(r'f\"[^\"]*\"', fix_fstring, content)
content = re.sub(r"f'[^']*'", fix_fstring, content)

with open('jarvis.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('Regex fixed.')
