

num = 10
div = 0

try:
    res = num / div
except ZeroDivisionError as z:
    print("Exception occured.....")
    print(z)
except TypeError as t:
    print("Exceotion occured.....")
    print(t)
except Exception as e:
    print("Exception class")
    print(e)
else:

    print(f"The result is :{res}")

finally:
    print("Completed the process of dividing the numbers.....")
