
from functools import reduce

l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = reduce(lambda x, y: x + y, l1)
print(f"res :{res}")

l2 = [8, 3, 5, 1, 7, 9, 6, 4, 10, 11, 13]
print(f"l2 :{l2}")
res = reduce(lambda x, y: x if x < y else y, l2)
print(f"res :{res}")
