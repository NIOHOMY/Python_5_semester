from Models.Account import Account

class Client:
    def __init__(self, name):
        self.name = name
        self.bank_accounts = []  # Массив для хранения счетов клиента в разных банках

    def add_account(self, account):
        self.bank_accounts.append(account)
        
    def delete_account(self, bank):
        for account in self.bank_account:
            if account.get_bank() == bank:
                self.bank_accounts.remove(account)
        
    def get_bank_account(self,bank):
        for account in self.bank_accounts:
            if account.get_bank() == bank:
                return account
            
         