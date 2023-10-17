from ..BanksMenu.create_bank_menu import create_bank_menu
from ..BanksMenu.delete_bank_menu import delete_bank_menu
from ..BanksMenu.select_bank_menu import select_bank_menu
from Controllers.BankController import BankController

def bank_menu(controller):
    while True:
        print("--- Меню работы с Банком ---")
        print("1: Создать банк")
        print("2: Удалить банк")
        print("3: Выбрать банк")
        print("0: Назад")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == "1":
            create_bank_menu(controller)
        elif choice == "2":
            delete_bank_menu(controller)
        elif choice == "3":
            select_bank_menu(controller)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")