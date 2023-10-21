class Account:
    def __init__(self, bank):
        self.balance = 0
        self.bank = bank

    def deposit(self, amount):
        self.balance += amount
        self.bank.receive_transfer(amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.bank.receive_transfer(-amount)
            return True
        else:
            return False
        
    def get_bank(self):
        return self.bank