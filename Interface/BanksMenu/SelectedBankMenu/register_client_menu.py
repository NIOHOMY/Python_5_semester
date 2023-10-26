import traceback
from ...Tools.print_clients import print_clients
from Models.Client import Client
from Models.Bank import Bank
from Controllers.BankController import BankController
from Interface.Tools.input_integer_non_negative_numbers import input_integer_non_negative_numbers

def register_client_menu(controller, bank):
    try :
        if print_clients(controller):
            client_id = input_integer_non_negative_numbers("Выберите ID клиента для регистрации: ")
            if client_id is not None:
                client = controller.select_client(client_id)
    
                if client:
                    if bank.add_client(client):
                        print(f"Клиент '{client.name}' успешно зарегистрирован в банке '{bank.name}'.")
                    else:
                        print("Ошибка при регистрации клиента.")
                else:
                    print("Клиент не найден.")
            else:
                print("Неверный ID клиента.")
        
    except Exception as e:
            traceback.print_exc()
            return None