
def outerFun():
    gst = "Sachin"
    def innerFun():
    # only local variables can be converted into nonlocal
        nonlocal gst
        gst += " Tendulkar"
        print("Hello World")
        print(f"Greetings Mr.{gst}")

    innerFun()
    print(f"Outer :{gst}")

outerFun()
