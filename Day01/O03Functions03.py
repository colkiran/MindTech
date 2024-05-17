
def multiplyMe(x, y):
    return x * y

a = 10
b = 20
print(f"The product of {a} and {b} is {multiplyMe(10, 20)}")

# Named Tuple
# tuple is immutable list, Named Tuple is immutable dictionary

from collections import namedtuple
def arithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    nmdTpl = namedtuple("Arithematic", "s d p q")
    arith = nmdTpl(s = sum, d = diff, p = prod, q = quot)
    return arith

res = arithmeticCalc(20, 8)
print(f"res :{res}")
print(f"Sum is  :{res.s}")
print(f"Diff is :{res.d}")
print(f"Prod is :{res.p}")
print(f"Quot is :{res.q}")

res.p = 500

