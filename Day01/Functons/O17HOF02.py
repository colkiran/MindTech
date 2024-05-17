
def callme():
    print('Apples from ooty......')

def fun(fnc):
    print("hello")
    fnc()
    print ('Hi')
    print("-" * 60)

    def defineMe():
        print("Oranges from kanpur......")

    return defineMe

def funCallBack(fnc):
    print("Mera Baharath Mahan")
    fnc()
    print("India is Great")

funCallBack(fun(callme))
