from ...BanksMenu.SelectedBankMenu.register_client_menu import register_client_menu
from ...BanksMenu.SelectedBankMenu.delete_client_menu import delete_client_menu
from ...BanksMenu.SelectedBankMenu.view_funds_menu import view_funds_menu
from Controllers.BankController import BankController
from Models.Bank import Bank

def bank_menu_selected_bank(controller, bank):
    while True:
        print(f"--- Меню выбранного Банка '{bank.name}' ---")
        print("1: Зарегистрировать клиента")
        print("2: Удалить клиента")
        print("3: Средства")
        print("0: Назад")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == "1":
            register_client_menu(controller, bank)
        elif choice == "2":
            delete_client_menu(controller, bank)
        elif choice == "3":
            view_funds_menu(bank)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")