from Models.Bank import Bank
from Controllers.BankController import BankController

def print_banks(controller):
    banks = controller.banks
    if banks:
        for index, bank in enumerate(banks):
            print(f"ID: {index}, Имя: {bank.name}")
        return True
    else:
        print("Список банков пуст.")
        return False