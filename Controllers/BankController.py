from Models.Client import Client
from Models.Account import Account
from Models.Bank import Bank
from Models.Persons.LegalPerson import LegalPerson
from Models.Persons.PhysicalPerson import PhysicalPerson

class BankController:
    def __init__(self):
        self.banks = []
        self.clients = []

    def create_bank(self, name):
        if name != None and name != "":
            bank = Bank(name)
            self.banks.append(bank)
            return bank
        else:
            return None

    def delete_bank(self, bank):
        if bank in self.banks:
            self.banks.remove(bank)
            return True
        else:
            return False

    def select_bank(self, bank_id):
        if bank_id >= 0 and bank_id < len(self.banks):
            bank = self.banks[bank_id]
            return bank
        else:
            return None

    def create_client(self, name, client_type):
        if name != None and name != "":
            if client_type == 1:
                client = PhysicalPerson(name)
            elif client_type == 2:
                client = LegalPerson(name)
            else:
                return None
        else:
            return None
        
        self.clients.append(client)
        return client

    def delete_client(self, client):
        if client in self.clients:
            self.clients.remove(client)
            return True
        else:
            return False

    def select_client(self, client_id):
        if client_id >= 0 and client_id < len(self.clients):
            client = self.clients[client_id]
            return client
        else:
            return None
        
    def deposit_money(self, account, amount):
        if account and amount>=0:
            account.deposit(amount)
            return True
        else:
            return False
        
    def withdraw_money(self, account, amount):
        if account and amount>=0:
            return account.withdraw(amount)
        else:
            return False
        
    def transfer_money(self, sender_id, sender_bank_id, receiver_id, amount, receiver_bank_id=None):
        sender_bank = self.select_bank(sender_bank_id)
        sender = self.select_client(sender_id)
        
        if not sender_bank or not sender:
            return False
            
        if not receiver_bank_id:
            receiver_bank_id = sender_bank_id
        
        receiver_bank = self.select_bank(receiver_bank_id)
        receiver = self.select_client(receiver_id)
        
        if receiver_bank and receiver:
            return sender_bank.transfer_money(sender, receiver_bank, receiver, amount)
            
        return False
    def get_bank_id(self, bank):
        for idx, b in enumerate(self.banks):
            if b == bank:
                return idx
        return None
    def get_client_id(self, client):
        for idx, c in enumerate(self.clients):
            if c == client:
                return idx
        return None
    def get_bank_by_id(self, bank_id):
        if bank_id < 0 or bank_id >= len(self.banks):
            return None
        return self.banks[bank_id]


