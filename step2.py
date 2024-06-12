# make msgid multiline

import re
with open('JMdict_es.po', encoding='utf-8') as file:
    filedata = file.read()
    
sub1 = '\\\\n '
sub2 = '\\\\n'

filedata = re.sub(sub1, '\\\\n"\n"', filedata, flags=0)
filedata = re.sub(sub2, 'n', filedata, flags=0)

#print(filedata)

with open ('JMdict_es.po', 'w', encoding='utf-8') as file:
    file.write(filedata)
    

file.close()