<<<<<<< HEAD
import re
with open('JMdict_e.xml', encoding='utf-8') as file:
    filedata = file.read()
    
g_type = r'(?<=gloss)(\sg_.+?)(?=>)' # gloss attributes
sense = '<sense>'
inf1 = '<s_inf>'
inf2 = '</s_inf>'
dial = r'(<dial>.{5,6}</dial>\n)' # leftover dialect tags
tags = r'(?<=<sense>\n)(.+?)(?=<gloss>)|<gloss>' # everything between sense and gloss
gloss2 = '</gloss>'
restr = r'(<re_restr>.+?</re_restr>)' # leftover reading tags
keb = r'(?<=<\/keb>)(.+?)(?=<\/k_ele>\n<r_ele>)' # reduce to 1 kanji
reb = r'(?<=<\/reb>)(.+?)(?=<\/r_ele>\n<sense>)' # reduce to 1 reading
id1 = '<ent_seq>'
id2 = '</ent_seq>'
id3 = r'\n<(k|r)_ele>\n<(k|r)eb>'
collapse1 = '</keb>\\n</k_ele>'
collapse2 = '</reb>\\n</r_ele>\\n<sense>\\n'


# delete gloss attributes
filedata = re.sub(g_type, '', filedata, flags=0)

# merge info into gloss
filedata = re.sub(inf1, '<gloss>(', filedata, flags=0)
filedata = re.sub(inf2, ')</gloss>', filedata, flags=0)
filedata = re.sub(dial, '', filedata, flags=0)

# add nl after <sense>
filedata = re.sub(sense, '<sense>\\n', filedata, flags=re.S)

# delete everything between sense and gloss
filedata = re.sub(tags, '', filedata, flags=re.S)

# delete </gloss>
filedata = re.sub(gloss2, '\\\\n', filedata, flags=re.S)

# one kanji+reading
filedata = re.sub(keb, '\\n', filedata, flags=re.S)
filedata = re.sub(reb, '\\n', filedata, flags=re.S)

# collapse id+term+sense
filedata = re.sub(id1, '<sense>\\n[', filedata, flags=re.S)
filedata = re.sub(id2, '] ', filedata, flags=re.S)
filedata = re.sub(id3, '', filedata, flags=re.S)
filedata = re.sub(collapse1, '\\t', filedata, flags=re.S)
filedata = re.sub(collapse2, '\\\\n\n', filedata, flags=re.S)

# check that everything went well
#print(filedata)

with open('JMdict_e.xml', 'w', encoding='utf-8') as file:
    file.write(filedata)

=======
import re
with open('JMdict_e.xml', encoding='utf-8') as file:
    filedata = file.read()
    
g_type = r'(?<=gloss)(\sg_.+?)(?=>)' # gloss attributes
sense = '<sense>'
inf1 = '<s_inf>'
inf2 = '</s_inf>'
dial = r'(<dial>.{5,6}</dial>\n)' # leftover dialect tags
tags = r'(?<=<sense>\n)(.+?)(?=<gloss>)|<gloss>' # everything between sense and gloss
gloss2 = '</gloss>'
restr = r'(<re_restr>.+?</re_restr>)' # leftover reading tags
keb = r'(?<=<\/keb>)(.+?)(?=<\/k_ele>\n<r_ele>)' # reduce to 1 kanji
reb = r'(?<=<\/reb>)(.+?)(?=<\/r_ele>\n<sense>)' # reduce to 1 reading
id1 = '<ent_seq>'
id2 = '</ent_seq>'
id3 = r'\n<(k|r)_ele>\n<(k|r)eb>'
collapse1 = '</keb>\\n</k_ele>'
collapse2 = '</reb>\\n</r_ele>\\n<sense>\\n'


# delete gloss attributes
filedata = re.sub(g_type, '', filedata, flags=0)

# merge info into gloss
filedata = re.sub(inf1, '<gloss>(', filedata, flags=0)
filedata = re.sub(inf2, ')</gloss>', filedata, flags=0)
filedata = re.sub(dial, '', filedata, flags=0)

# add nl after <sense>
filedata = re.sub(sense, '<sense>\\n', filedata, flags=re.S)

# delete everything between sense and gloss
filedata = re.sub(tags, '', filedata, flags=re.S)

# delete </gloss>
filedata = re.sub(gloss2, '\\\\n', filedata, flags=re.S)

# one kanji+reading
filedata = re.sub(keb, '\\n', filedata, flags=re.S)
filedata = re.sub(reb, '\\n', filedata, flags=re.S)

# collapse id+term+sense
filedata = re.sub(id1, '<sense>\\n[', filedata, flags=re.S)
filedata = re.sub(id2, '] ', filedata, flags=re.S)
filedata = re.sub(id3, '', filedata, flags=re.S)
filedata = re.sub(collapse1, '\\t', filedata, flags=re.S)
filedata = re.sub(collapse2, '\\\\n\n', filedata, flags=re.S)

# check that everything went well
#print(filedata)

with open('JMdict_e.xml', 'w', encoding='utf-8') as file:
    file.write(filedata)

>>>>>>> 847af32 (initial commit)
file.close()