from Models.Client import Client
from Models.Account import Account
from Models.Persons.LegalPerson import LegalPerson
from Models.Persons.PhysicalPerson import PhysicalPerson

class Bank:
    def __init__(self, name):
        self.name = name
        self.own_funds = 0
        self.clients = []

    def add_client(self, client):
        if client not in self.clients:
            self.clients.append(client)
            return True
        else:
            return False

    def remove_client(self, client):
        if client in self.clients:
            self.clients.remove(client)

    def transfer_money(self, sender, receiver_bank, receiver, amount):
        if (sender != receiver and
            isinstance(sender, Client) and
            isinstance(receiver, Client) and
            sender.account.balance >= amount and
            (isinstance(sender, LegalPerson) or self == receiver_bank)):
        
            sender.account.withdraw(amount)
            receiver_bank.receive_transfer(amount)
            receiver.account.deposit(amount)
            return True
        else:
            return False


    def calculate_transfer_fee(self, amount):
        return 0.01 * amount

    def collect_transfer_fee(self, fee):
        self.own_funds += fee

    def receive_transfer(self, amount):
        self.own_funds += amount
        
    def get_clients(self):
        return self.clients.copy()