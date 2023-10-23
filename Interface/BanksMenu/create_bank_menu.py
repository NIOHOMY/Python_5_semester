from Controllers.BankController import BankController
from Models.Bank import Bank
def create_bank_menu(controller):
    name = input("Введите название банка: ")
    bank = controller.create_bank(name)
    
    if bank:
        print(f"Банк '{bank.name}' успешно создан.")
        return controller.get_bank_id(bank)
    else:
        print("Ошибка при создании банка.")
        return None