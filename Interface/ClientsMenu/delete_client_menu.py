from ..Tools.print_clients import print_clients
from Controllers.BankController import BankController
from Models.Client import Client

def delete_client_menu(controller):
    print_clients(controller)
    client_id = input("Выберите ID клиента для удаления: ")
    client = controller.select_client(int(client_id))
    if client and controller.delete_client(client):
        print(f"Клиент '{client.name}' успешно удален.")
    else:
        print("Ошибка при удалении клиента.")