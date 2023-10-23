from ..Tools.print_clients import print_clients
from Controllers.BankController import BankController
from Models.Client import Client

def delete_client_menu(controller):
    print_clients(controller)
    _client_id = input("Выберите ID клиента для удаления: ")
    
    # Добавьте цикл для повторного запрашивания ID, если пользователь ввел некорректное значение.
    try :
        client_id = int(_client_id)
        client = controller.select_client(client_id)
    
        if client:
            if controller.delete_client(client):
                print(f"Клиент '{client.name}' успешно удален.")
            else:
                print("Ошибка при удалении клиента.")
        else:
            print("Неверный ID клиента.")
    except Exception:
        print("Некорректный ID клиента.")
        return None
    
