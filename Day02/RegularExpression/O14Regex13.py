

import re

st = "the quick brown fox jumps over the laz dog"

res = re.search(r"dog\Z", st)
# res = re.search(r'\Athe', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found......")