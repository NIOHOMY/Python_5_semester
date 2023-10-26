from ..Tools.print_clients import print_clients
from Controllers.BankController import BankController
from Models.Client import Client
from Interface.Tools.input_integer_non_negative_numbers import input_integer_non_negative_numbers

def delete_client_menu(controller):

    try :
        if(print_clients(controller)):
            client_id = input_integer_non_negative_numbers("Выберите ID клиента для удаления: ")
    
            if client_id is not None:
                client = controller.select_client(client_id)
    
                if client:
                    if controller.delete_client(client):
                        print(f"Клиент '{client.name}' успешно удален.")
                    else:
                        print("Ошибка при удалении клиента.")
                else:
                    print("Клиент не найден.")
            else:
                print("Неверный ID клиента.")
    except Exception:
        print("Некорректный ID клиента.")
        return None
    
