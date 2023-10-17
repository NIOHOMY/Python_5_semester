from ...Tools.print_banks_clients import print_banks_clients
from Models.Client import Client
from Models.Bank import Bank
from Controllers.BankController import BankController

def delete_client_menu(controller, bank):
    print_banks_clients(controller, bank)
    client_id = input("Выберите ID клиента для удаления: ")
    client = controller.select_client(int(client_id))
    if client and bank.remove_client(client):
        print(f"Клиент '{client.name}' успешно удален из банка '{bank.name}'.")
    else:
        print("Ошибка при удалении клиента.")