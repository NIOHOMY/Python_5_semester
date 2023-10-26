import traceback
from Models.Bank import Bank
from Models.Client import Client
from Controllers.BankController import BankController

def print_banks_clients(controller, bank):
    try:
        clients = bank.get_clients()
        if clients:
            for index, client in enumerate(clients):
                print(f"ID: {index}, Имя: {client.name}")
        else:
            print("Список клиентов пуст.")
        
    except Exception as e:
            traceback.print_exc()
            return None