
def outerFun(gstname):          # HOF - Higher order Function
    gstname = "Mr." + gstname
    def innerFun():

        print(f"Greetings {gstname}")

    return innerFun

res = outerFun("Rahul")
res()

outerFun("Sachin")()       # calls the innerfun directly
