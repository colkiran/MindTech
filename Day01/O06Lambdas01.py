
def add(x, y):
    return x + y

print(add(10, 20))

a = add
res = a(100, 200)
print(f"res :{res}")

print("-" * 60)

x = lambda a, b: a + b
print(x(10, 20))

print("-" * 60)
# map

l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = list(map(lambda x: x ** 2, l1))
print(f"res :{res}")

print("-" * 60)
# conversions - currency (rs - dollars, dollar - pounds)
#             - Weight (pounds - kgs)

months = ['nov', 'jul', 'dec', 'aug', 'sep', 'mar', 'may', 'oct', 'feb', 'jun', 'jan', 'apr']

print(f"months :{months}")

# sort these months according to calendar dates

print("-" * 60)

from calendar import month_abbr
print(f"month_abbr :{list(month_abbr)}")

print("-" * 60)

res = sorted(months, key = list(map(lambda mth: mth.lower(), list(month_abbr))).index)

print(f"sorted months :{res}")

