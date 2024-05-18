
class Animal:

    def eat(self):
        print("Animals eat......")

class Bird(Animal):

    def fly(self):
        print("Birds fly.....")

class Chicken(Bird):

    def msg(self):
        print("Chicken are breeded for consumption.....")
        
    def fly(self):
        print("Chicken's seldom fly.......")



chic = Chicken()
chic.msg()
chic.fly()
chic.eat()

