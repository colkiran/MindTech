
def greet(grt):

    # simple curry
    def innerFun(gname):
        print(grt, gname)

    return innerFun

engGrt = greet("Hello")
kanGrt = greet("Namaskara")

engGrt("Sachin")
kanGrt("Rahul")

