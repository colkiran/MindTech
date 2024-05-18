
import re

st = "Hello World"

# res = re.match(r'^Hello', st)
# match will only match at the begning of the string
# seacrh will search for the entire string

res = re.search(r'World$', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found......")

