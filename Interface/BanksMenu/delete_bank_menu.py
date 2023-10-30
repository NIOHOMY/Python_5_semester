import traceback
from ..Tools.print_banks import print_banks
from Controllers.BankController import BankController
from Models.Bank import Bank
from Interface.Tools.input_integer_non_negative_numbers import input_integer_non_negative_numbers

def delete_bank_menu(controller):
    try:
        if(print_banks(controller)):
            bank_id = input_integer_non_negative_numbers("Выберите ID банка для удаления: ")
            if bank_id is not None:
                bank = controller.select_bank(bank_id)
                if bank:
                    if controller.delete_bank(bank):
                        print(f"Банк '{bank.name}' успешно удален.")
                    else:
                        print("Ошибка при удалении банка.")      
                else:
                    print("Банк не найден.")
            else:
                print("Неверный ID банка.")
    except Exception as e:
        traceback.print_exc()
        return None
        
