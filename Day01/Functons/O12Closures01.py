
def outerFun(gstname):
    gstname = "Mr." + gstname
    def innerFun():

        print(f"Greetings {gstname}")

    innerFun()

outerFun("Rahul")



