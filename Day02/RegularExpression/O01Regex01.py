
import re
# print(dir(re))

st = "bat"
res = re.match(r'b.t', st)
# print(f"res :{res}")

if res:
    print("Match found.....")
    print(res.group(0))         # string that matched the regex
else:
    print("Match not found,......")
