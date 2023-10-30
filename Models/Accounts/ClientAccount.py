import traceback
from Models.Account import Account
from Models.Persons.LegalPerson import LegalPerson
from Models.Persons.PhysicalPerson import PhysicalPerson

class ClientAccount(Account):

    def deposit(self, amount):
        if amount > 0:  # Проверяем, что сумма для депозита положительная
            self.balance += amount
            self.bank.get_bank_account().deposit(amount)
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:  # Проверяем, что запрашиваемая сумма для снятия положительная и не превышает баланс
            self.balance -= amount
            self.bank.get_bank_account().withdraw(amount)
            return True
        else:
            return False

    def transfer_money(self, sender, receiver_account, receiver, amount):
        try:
        
            fee = self.bank.calculate_transfer_fee(amount)
            if receiver_account != None:    # Проверяем, что у получателя есть счет в соответствующем банке
                if (
                    self.balance >= amount+fee and
                    (
                        (
                            isinstance(sender, LegalPerson) and (sender != receiver)
                        ) or
                        (
                            isinstance(sender, LegalPerson) and (sender == receiver) and (self.bank != receiver_account.get_bank())
                        ) or
                        (
                           isinstance(sender, PhysicalPerson) and (sender != receiver) and (self.bank == receiver_account.get_bank())
                        )
                
                    )
                ):
            
                    self.withdraw(amount+fee)
                    self.bank.collect_transfer_fee(fee)
                    receiver_account.deposit(amount)
                    return True
                
            return False
        except Exception as e:
                traceback.print_exc()
                return None
        
    def get_bank(self):
        return self.bank
    def get_balance(self):
        return self.balance
    
