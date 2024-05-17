
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

emp1 = Employee("Peter", 45)
print(str(emp1))
print(emp1)         # implicitly call __str__

