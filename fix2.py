import sys
with open('jarvis.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

pyflakes_lines = [1496, 1835, 1953, 1960, 1969, 2008]

for i in pyflakes_lines:
    idx = i - 1
    line = lines[idx]
    if '{' not in line and 'f"' in line:
        lines[idx] = line.replace('f"', '"', 1)
    elif '{' not in line and "f'" in line:
        lines[idx] = line.replace("f'", "'", 1)
    
    if 'resp =' in line:
        lines[idx] = line.replace('resp = ', '')

with open('jarvis.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Fixed pyflakes issues!')
