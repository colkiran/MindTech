
marks = {'maths': 85, 'phy': 78, 'che': 86}
def fun(mrqs):
    print(f"marks :{mrqs}")
    mrqs['Eng'] = 80
    mrqs['Kan'] = 75
    print(f"Inside :{mrqs}")


print(f"Before :{marks}")

fun(marks)

print(f"After :{marks}")