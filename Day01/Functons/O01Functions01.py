
def greet():
    print("Greetings Mr.Sachin, Welcome to the event.....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event......")

# name is a non default arg and city is a default argument
def greetGstCty(gname, x,  city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event....")

greet()

print("-" * 60)
greetGst("Sachin")
greetGst("Rahul")

print("-" * 60)
greetGstCty("Sunil Gavaskar", 10)
greetGstCty("Rohit Sharma", 20)
greetGstCty("Rahul Dravid", 30, "Bangalore")