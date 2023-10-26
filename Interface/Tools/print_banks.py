import traceback
from Models.Bank import Bank
from Controllers.BankController import BankController

def print_banks(controller):
    try:
        banks = controller.banks
        if banks:
            for index, bank in enumerate(banks):
                print(f"ID: {index}, Имя: {bank.name}")
            return True
        else:
            print("Список банков пуст.")
            return False
        
    except Exception as e:
            traceback.print_exc()
            return False