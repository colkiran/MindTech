
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized.......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")


ply1 = Player("Sachin", 32)
ply1.get_details()

print("-" * 60)
ply2 = Player("Rahul", 29)
ply2.get_details()
ply2.runs = 85

print(f"ply2 :{ply2.runs}")
# print(f"ply1 :{ply1.runs}")
