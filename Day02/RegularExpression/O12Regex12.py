


import re

st = "the complaint id is 32392 reistered on 10-15-2000"

# res = re.search(r"\d", st)
res = re.search(r"\D+", st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found......")