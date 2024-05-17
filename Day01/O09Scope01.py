
glbX = 100

def fun(y):             # y is a local variable
    global  glbX       # do not assign any value to glbX
    print(f"y :{y}")
    glbX = 250
    print(f"inside :{glbX}")



print(f"Before :{glbX}")

fun(10)

print(f"After :{glbX}")
