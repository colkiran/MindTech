
def fun(*x):
    print(f"function fun {x}")

fun()
fun(10)
fun(10, 20)
fun(10, 20, 30)

print("-" * 60)

def sum(x, y):
    return x + y

def diff(x, y):
    return x - y


def outerFun(fnc):
    log = "logging into the service....."
    def innerFun(*args):
        print(log)
        print(fnc(*args))       # call back
        print("-" * 60)

    return innerFun

sumlogger = outerFun(sum)
sumlogger(10, 20)

print("-" * 60)

difflogger = outerFun(diff)
difflogger(30, 6)
