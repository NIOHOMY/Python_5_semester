class Account:
    def __init__(self, bank):
        self.balance = 0
        self.bank = bank

    def deposit(self, amount):
        if amount > 0:  # Проверяем, что сумма для депозита положительная
            self.balance += amount
            self.bank.receive_transfer(amount)
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:  # Проверяем, что запрашиваемая сумма для снятия положительная и не превышает баланс
            self.balance -= amount
            self.bank.receive_transfer(-amount)
            return True
        else:
            return False
        
    def get_bank(self):
        return self.bank
    def get_balance(self):
        return self.balance
    
