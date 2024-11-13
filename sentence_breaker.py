import re

test_file = open("test.txt", "r", encoding="utf8")
text_to_break = test_file.read()
text_to_break = re.sub(r"\(\d+([a-z]|[A-Z])?\)", "", text_to_break)
text_to_break = re.sub(r"\*", "", text_to_break)
text_to_break = re.sub(r"\n([a-z]|a[a-z])\)", "\n", text_to_break)
text_to_break = re.sub(r"\[(.)*\]", "\n", text_to_break)
text_to_break = re.sub(r"\d+(/[A-Z])*\.", "\n", text_to_break)

print(text_to_break)

sections = text_to_break.split(' § ')[1:]
