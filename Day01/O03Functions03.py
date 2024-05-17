
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

# res.p = 500

print("-" * 60)

def fun():
    # this is a comment
    "This is a doc string"
    print("Hello World")


fun()
# double underscore doc  - dunder_doc
print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    fun1
    ----
    1. if both the arguments are numbers then we get the sum of the numbers as a return value
    2. if both the arguments are strings then we get the concatenated string as a return value
    3. if the arguments are of different data types then it throws an error
    """

    return x + y

print(fun1(20, 30))
print(fun1("hello", "world"))
# print(fun1("hello", 30))

help(fun1)

