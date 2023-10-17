from ..Tools.print_banks import print_banks
from Controllers.BankController import BankController
from Models.Bank import Bank

def delete_bank_menu(controller):
    print_banks(controller)
    bank_id = input("Выберите ID банка для удаления: ")
    bank = controller.select_bank(int(bank_id))
    if bank and controller.delete_bank(bank):
        print(f"Банк '{bank.name}' успешно удален.")
    else:
        print("Ошибка при удалении банка.")