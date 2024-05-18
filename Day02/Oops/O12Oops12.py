
class Employee:

    def __init__(self, name):
        self.__name = name
        self.tech = ['C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'ReactJs']

    def __str__(self):
        return self.__name + ", " + ", ".join([str(v) for v in self.tech])

emp1 = Employee("Ruben")
print(emp1)

print("-" * 60)
# print(emp1.__name)
# emp1.__name = "Kennedy"
# emp1.age = 45       # new property added  - expando
print(emp1.__dict__)
emp1._Employee__name = "Kennedy"
print(emp1)
