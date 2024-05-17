
gname = "Sachin"

def fun(gname):
    gname = "Mr." + gname + " Tendulkar"
    print(f"Inside {gname}")


print(f"Before :{gname}")

fun(gname)

print(f"After :{gname}")
