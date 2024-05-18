
import re

st = "This is a sAmple text on an amPle string"

# res = re.search(r'\bample', st, re.I)
res = re.search(r'\Bample', st, re.I)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found......")