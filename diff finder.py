from contextlib import redirect_stdout
import re

l = open('differences.txt', 'w', encoding='utf-8')

with open('JMdict_es.po', encoding='utf-8') as f:
    seen = set()
    dupes = set()
    for line in f:
        if not line.strip(): continue
        line_lower = line.lower()
        if line_lower in seen:
            dupes.add(line)
        else:
            seen.add(line_lower)
            
print(dupes, file=l)

f.close()
#print(line+'\n', file=l)
