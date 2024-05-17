
# variable length arguments

#  *var can accept more than one value and store it in a tuple
# *args
def calcProd(*numbers):
    print(f"numbers :{numbers}")
    print(*numbers)
    k = 1
    for number in numbers:
        k *= number
    return k

res = calcProd(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)

# **kwargs
def extractDet(**details):
    print(details)
    print(type(details))
    # items is a combination of KEY and VALUES function
    print("-" * 60)
    for k, v in details.items():
        print(k, "=>", v)

extractDet(name="Rahul", age=32, runs=85, oppn="Aus")

