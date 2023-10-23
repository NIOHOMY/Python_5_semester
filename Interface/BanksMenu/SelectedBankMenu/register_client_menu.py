from ...Tools.print_clients import print_clients
from Models.Client import Client
from Models.Bank import Bank
from Controllers.BankController import BankController

def register_client_menu(controller, bank):
    print_clients(controller)
    _client_id = input("Выберите ID клиента для регистрации: ")
    try :
        client_id = int(_client_id)
        client = controller.select_client(client_id)
    
        if client:
            if bank.add_client(client):
                print(f"Клиент '{client.name}' успешно зарегистрирован в банке '{bank.name}'.")
            else:
                print("Ошибка при регистрации клиента.")
        else:
            print("Неверный ID клиента.")
    except Exception:
        print("Некорректный ID клиента.")
        return None