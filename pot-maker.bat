py step1.py
xgettext -d JMdict_es --its="rules.its" --no-wrap "JMdict_e.xml"
py "diff finder.py"
py step2.py