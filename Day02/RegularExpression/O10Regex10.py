
import re

st = "this  *#$)&@#   is a sample string"

# res = re.search(r'\w+', st)
res = re.search(r'\W+', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found......")