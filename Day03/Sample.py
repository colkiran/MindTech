
def greet(gname):
    print(f"Greetings {gname}, Welcome to the event......")


class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

print(f"Current module name :{__name__}")

if __name__ == '__main__':

    print("-"  * 60)
    greet("Moses")

    emp1 = Employee("Smith", 35)
    emp1.get_details()
