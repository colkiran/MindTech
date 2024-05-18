

class Animal:
    def __init__(self):
        print('Animal Ctor.....')
        self.a = 10

    def eat(self):
        print("Animals eat......")


    def fun(self):
        print("Fun method of class Animal.....")

class Person:

    def __init__(self):
        print("Person Ctor.......")
        self.p = 20
           
    def talk(self):
        print("Person talks......")

    def fun(self):
        print("Fun method of class Person.....")

class Girl(Animal, Person):

    def __init__(self):
        super().__init__()      # Animal is the parent class
        Person.__init__(self)
        print("Girl Ctor......")
        self.g = 30


tina = Girl()
tina.talk()
tina.eat()

print("-" * 60)
tina.fun()

print(tina.__dict__)