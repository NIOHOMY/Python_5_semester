import traceback
from Models.Bank import Bank
from Controllers.BankController import BankController

def print_banks_by_indices(controller, indices):
    try:
        banks = controller.banks
        for index in indices:
            bank = banks[index]
            print(f"ID: {index}, Имя: {bank.name}")
        
    except Exception as e:
            traceback.print_exc()
            return None