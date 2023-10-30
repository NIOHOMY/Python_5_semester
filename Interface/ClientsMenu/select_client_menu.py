from ..Tools.print_clients import print_clients
from Controllers.BankController import BankController
from Models.Client import Client
from ..ClientsMenu.SelectedClientMenu.client_menu_selected_client import client_menu_selected_client
from Interface.Tools.input_integer_non_negative_numbers import input_integer_non_negative_numbers

def select_client_menu(controller):
    try:
        if(print_clients(controller)):
            client_id = input_integer_non_negative_numbers("Выберите ID клиента: ")
            if client_id is not None:
                client = controller.select_client(int(client_id))
                if client:
                    client_menu_selected_client(controller, client, int(client_id))
                else:
                    print("Клиент не найден.")
            else:
                print("Неверный ID клиента.")
    except Exception:
        print("Некорректный ID клиента.")
        return None
