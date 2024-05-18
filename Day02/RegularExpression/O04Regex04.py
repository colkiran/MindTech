
import re

st = "bt"

res = re.search("ba?t", st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found......")