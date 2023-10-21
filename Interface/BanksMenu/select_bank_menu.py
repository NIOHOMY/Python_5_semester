from ..Tools.print_banks import print_banks
from Controllers.BankController import BankController
from Models.Bank import Bank
from .SelectedBankMenu.bank_menu_selected_bank import bank_menu_selected_bank

def select_bank_menu(controller):
    if(print_banks(controller)):
        bank_id = input("Выберите ID банка: ")
        bank = controller.select_bank(int(bank_id))
    
        if bank:
            bank_menu_selected_bank(controller, bank)
        else:
            print("Неверный ID банка.")