from ...ClientsMenu.SelectedClientMenu.deposit_money_menu import deposit_money_menu
from ...ClientsMenu.SelectedClientMenu.withdraw_money_menu import withdraw_money_menu
from ...ClientsMenu.SelectedClientMenu.transfer_money_menu import transfer_money_menu
from Controllers.BankController import BankController
from Models.Client import Client

def client_menu_selected_client(controller, client,client_id):
    while True:
        print(f"--- Меню выбранного Клиента '{client.name}' ---")
        print("1: Положить деньги на счет")
        print("2: Снять деньги со счета")
        print("3: Сделать перевод на другой счет")
        print("0: Назад")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == "1":
            deposit_money_menu(controller, client)
        elif choice == "2":
            withdraw_money_menu(controller, client)
        elif choice == "3":
            transfer_money_menu(controller, client,int(client_id))
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")