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
        
        if (
            isinstance(sender, Client) and
            isinstance(receiver, Client) and
            sender_account and receiver_account and  # Проверяем, что у отправителя и получателя есть счета в соответствующих банках
            sender_account.balance >= amount and
            (
                (
                    isinstance(sender, LegalPerson) and (sender != receiver) and (self != receiver_bank)
                ) or
                (
                    sender != receiver and self == receiver_bank
                ) or
                (
                    sender == receiver and self != receiver_bank
                )
            )
        ):
            sender_account.withdraw(amount)
            receiver_bank.receive_transfer(amount)
            self.collect_transfer_fee(self.calculate_transfer_fee(amount))
            self.own_funds -= amount
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
