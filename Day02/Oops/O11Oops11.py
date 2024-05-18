
class Employee:

    def __init__(self, name):
        self.name = name
        self.tech = ['C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'ReactJs']

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return self.tech.__iter__()

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, idx):
        return self.tech[idx]

    def __setitem__(self, idx, val):
        self.tech[idx] = val

emp1 = Employee("Jack")

print(len(emp1))

print("-" * 60)

print([emp for emp in emp1])

print("-" * 60)

emp1.append("Python")
print(emp1.tech)

print("-" * 60)

x = emp1[1]
print(f"x :{x}")

print("-" * 60)
emp1[6] = "React_Native"
print([emp for emp in emp1])