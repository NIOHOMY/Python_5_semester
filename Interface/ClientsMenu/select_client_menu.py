from ..Tools.print_clients import print_clients
from Controllers.BankController import BankController
from Models.Client import Client
from ..ClientsMenu.SelectedClientMenu.client_menu_selected_client import client_menu_selected_client

def select_client_menu(controller):
    print_clients(controller)
    client_id = input("Выберите ID клиента: ")
    try:
        client = controller.select_client(int(client_id))
        if client:
            client_menu_selected_client(controller, client, int(client_id))
        else:
            print("Неверный ID клиента.")
    except ValueError:
        print("Ошибка: введите корректный ID клиента (целое число).")
