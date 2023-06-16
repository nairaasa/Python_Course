import re

"[^a-zA-Z\d\s]"
txt = " alice15@gmail.com "
pattern = "[^a-zA-Z\d\s]"

print(re.findall(pattern, txt))