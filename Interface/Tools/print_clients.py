from Models.Client import Client
from Controllers.BankController import BankController

def print_clients(controller):
    clients = controller.clients
    if clients:
        for index, client in enumerate(clients):
            print(f"ID: {index}, Имя: {client.name}")
    else:
        print("Список клиентов пуст.")