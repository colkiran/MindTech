import time
def timeCalc(fnc):
    def helper(cntr):
        print("Executing the function.....")
        st = time.perf_counter()
        fnc(cntr)
        et = time.perf_counter()
        print("Completed the execution......")
        print(f"The total time taken is {round(et - st, 2)}")

    return helper

@timeCalc
def fun(x):
    lst = []
    for i in range(0, x):
        for j in range(1, i + 1):
            lst.append(j ** 2)


fun(6500)
