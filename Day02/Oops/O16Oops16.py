
class Animal:

    def __init__(self):
        print("Animal Ctor.....")
        self.a = 1

    def eat(self):
        print("Animals eat......")


class Bird(Animal):

    def fly(self):
        print('Birds fly......')


class Fish(Animal):

    def swim(self):
        print("Fishes swim.......")

print("-" * 60)

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print(cuckoo.__dict__)

print("-" * 60)
dolphin = Fish()
dolphin.eat()
dolphin.swim()

print(dolphin.__dict__)