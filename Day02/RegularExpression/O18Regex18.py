"""
three parts in the string

1 -> string that did not match the regex
2 -> string that matched the regex
3 -> string that is yet to be checked

"""
import re

st = "the quick brown fox jumps over the lazy dog b.t"

print(f"st :{st}")

res = re.search(r'b\.t', st)

print(res)

#
# res = re.search(r'fox', st)
#
# print("String that did'nt match the regex :", st[:res.start()])
# print("String that matched the regex :", res.group(0))
# print("String that is not checked :", st[res.end():])
