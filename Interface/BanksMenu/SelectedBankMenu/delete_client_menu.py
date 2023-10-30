import traceback
from ...Tools.print_banks_clients import print_banks_clients
from Interface.Tools.input_integer_non_negative_numbers import input_integer_non_negative_numbers

def delete_client_menu(controller, bank):
    try:
        if print_banks_clients(controller, bank):
            client_id = input_integer_non_negative_numbers("Выберите ID клиента для удаления: ")
            if client_id is not None:
                client = controller.select_client(client_id)
    
                if client:
                    if bank.remove_client(client):
                        print(f"Клиент '{client.name}' успешно удален из банка '{bank.name}'.")
                    else:
                        print("Ошибка при удалении клиента.")
                else:
                    print("Клиент не найден.")
            else:
                print("Неверный ID клиента.")
            
    except Exception as e:
            traceback.print_exc()
            return False
    