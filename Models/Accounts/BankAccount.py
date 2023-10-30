import traceback
from Models.Account import Account

class BankAccount(Account):
    def deposit(self, amount):
        if amount > 0:  # Проверяем, что сумма для депозита положительная
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:  # Проверяем, что запрашиваемая сумма для снятия положительная и не превышает баланс
            self.balance -= amount
            return True
        else:
            return False

    def transfer_money(self, receiver_bank, amount):
        """try:
            if (
                self.balance >= amount
            ):
                self.withdraw(amount)
                receiver_bank.get_bank_account().deposit(amount)
                return True
            else:
                return False
        except Exception as e:
            traceback.print_exc()
            return False
        """
        return False
    