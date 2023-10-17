from ...Tools.print_clients import print_clients
from Models.Client import Client
from Models.Bank import Bank
from Controllers.BankController import BankController

def register_client_menu(controller, bank):
    print_clients(controller)
    client_id = input("Выберите ID клиента для регистрации: ")
    client = controller.select_client(int(client_id))
    if client and bank.add_client(client):
        print(f"Клиент '{client.name}' успешно зарегистрирован в банке '{bank.name}'.")
    else:
        print("Ошибка при регистрации клиента.")