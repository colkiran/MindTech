
from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def checkBalance(self):
        pass

    def deposit(self):
        pass

class Savings(Account):

    def checkBalance(self):
        print("Balance in the account is xxxxxx.xx")

    def deposit(self):
        print("Amount deposited......")


sav1 = Savings()
sav1.deposit()
