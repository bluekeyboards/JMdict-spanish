python step1.py
xgettext -d JMdict_es --its="rules.its" --no-wrap "JMdict_e.xml"
python "diff finder.py"
python step2.py