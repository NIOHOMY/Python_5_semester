from ..ClientsMenu.create_client_menu import create_client_menu
from ..ClientsMenu.delete_client_menu import delete_client_menu
from ..ClientsMenu.select_client_menu import select_client_menu

def client_menu(controller):
    while True:
        print("--- Меню работы с Клиентами ---")
        print("1: Создать клиента")
        print("2: Удалить клиента")
        print("3: Выбрать клиента")
        print("0: Назад")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == "1":
            create_client_menu(controller)
        elif choice == "2":
            delete_client_menu(controller)
        elif choice == "3":
            select_client_menu(controller)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")