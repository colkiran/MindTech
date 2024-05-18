
from abc import ABC, abstractmethod


class Employee(ABC):
    def doJob(self):
        pass


class Manager(Employee):

    def doJob(self):
        print("Manger's job........")


class Developer(Employee):

    def doJob(self):
        print("Developer's job........")


def BankJob(emp):
    print("Bank job started.......")
    emp.doJob()
    print("Bank job ended........")
    print("-" * 60)

Mike = Manager()
Dave = Developer()


BankJob(Mike)           # manager's job
BankJob(Dave)           # developer's job