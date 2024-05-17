
class Player:

    def __init__(self):         # constructor
        self.name = "Sachin"
        self.age = 32

    def get_details(self):
        print(f"Name is :{self.name}\nAge is {self.age}")

    def __del__(self):
        print("Destructor called......")


ply1 = Player()         # call the constructor
ply1.get_details()
print("-" * 60)

del ply1                # call the destructor

print("-" * 60)
ply2 = Player()
ply2.name = "Rahul"
ply2.age = 29
ply2.get_details()
print("-" * 60)


