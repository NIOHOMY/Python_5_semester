from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, bank):
        self.balance = 0
        self.bank = bank

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def transfer_money(self, receiver_bank, receiver, amount):
        pass

    def get_bank(self):
        return self.bank

    def get_balance(self):
        return self.balance