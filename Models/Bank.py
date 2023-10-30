import traceback
from Models.Accounts.BankAccount import BankAccount
from Models.Accounts.ClientAccount import ClientAccount

class Bank:
    def __init__(self, name):
        self.name = name
        self.own_funds = BankAccount(self)
        self.clients = []

    def add_client(self, client):
        if client not in self.clients:
            client.add_account(ClientAccount(self))
            self.clients.append(client)
            return True
        else:
            return False

    def remove_client(self, client):
        if client in self.clients:
            client.delete_account(self)
            self.clients.remove(client)

    def calculate_transfer_fee(self, amount):
        return 0.01 * amount

    def collect_transfer_fee(self, fee):
        self.own_funds.deposit(fee)

    def get_clients(self):
        return self.clients.copy()
    def get_funds(self):
        return self.own_funds.get_balance()
    def get_bank_account(self):
        return self.own_funds
    def get_name(self):
        return self.name
