from Controllers.BankController import BankController
from Interface.BanksMenu.bank_menu import bank_menu
from Interface.ClientsMenu.client_menu import client_menu
    
def main():
    controller = BankController()
    
    while True:
        print("--- Меню ---")
        print("1: Работа с Банком")
        print("2: Работа с Клиентами")
        print("0: Выход")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == "1":
            bank_menu(controller)
        elif choice == "2":
            client_menu(controller)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")
            

if __name__ == "__main__":
    main()
