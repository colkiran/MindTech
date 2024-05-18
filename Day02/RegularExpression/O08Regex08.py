
import re

st = "boat"

res = re.search(r"b(oa|ai)t", st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found......")