
def outerFun(greet):
    def innerFun(sep):
        def innerMostFun(gname):

            from emojis import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun

    return innerFun

kanGrt = outerFun("Namaskara")

kanGrtTgr = kanGrt("lion")

kanGrtTgr("Prabhakar")




"""
engGrt = outerFun("Hello")
kanGrt = outerFun("Namaskara")

engGrtSngArw = engGrt("------>")
kanGrtDblArw = kanGrt("======>>")

engGrtSngArw("Sachin")
kanGrtDblArw("Javagal Srinath")

"""
