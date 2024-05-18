
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'ReactJs']

    def __str__(self):
        return f"Name is {self.name} and Salary is {self.salary}"

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)      # self.tech.__iter__()


emp1 = Employee("Kenedy", 45000)
print(emp1)

print("-" * 60)
print(len(emp1))

print("-" * 60)
# list comprehension - iterating through a collection using lambda syntax
print([emp for emp in emp1])
