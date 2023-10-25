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
            client.add_account(Account(self))
            self.clients.append(client)
            return True
        else:
            return False

    def remove_client(self, client):
        if client in self.clients:
            client.delete_account(self)
            self.clients.remove(client)

    def transfer_money(self, sender, receiver_bank, receiver, amount):
        sender_account = sender.get_bank_account(self)
        receiver_account = receiver.get_bank_account(receiver_bank)
        fee = self.calculate_transfer_fee(amount)
        if (
            sender_account and receiver_account and  # Проверяем, что у отправителя и получателя есть счета в соответствующих банках
            sender_account.balance >= amount+fee and
            (
                (
                    isinstance(sender, LegalPerson) and (sender != receiver)
                ) or
                (
                    isinstance(sender, LegalPerson) and (sender == receiver) and (self != receiver_bank)
                ) or
                (
                   isinstance(sender, PhysicalPerson) and (sender != receiver) and (self == receiver_bank)
                )
                
            )
        ):
            
            sender_account.withdraw(amount+fee)
            self.collect_transfer_fee(fee)
            receiver_account.deposit(amount)
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
    def get_funds(self):
        return self.own_funds
    def get_name(self):
        return self.name
