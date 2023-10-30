import traceback
from ..Tools.print_banks import print_banks
from .SelectedBankMenu.bank_menu_selected_bank import bank_menu_selected_bank
from Interface.Tools.input_integer_non_negative_numbers import input_integer_non_negative_numbers

def select_bank_menu(controller):
    try:
        if(print_banks(controller)):
            bank_id = input_integer_non_negative_numbers("Выберите ID банка: ")
            if bank_id is not None:
                bank = controller.select_bank(bank_id)
    
                if bank:
                    bank_menu_selected_bank(controller, bank)
                else:
                    print("Банк не найден.")
            else:
                print("Неверный ID банка.")
 
    except Exception as e:
        traceback.print_exc()
        return None