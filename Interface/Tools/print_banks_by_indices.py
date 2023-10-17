from Models.Bank import Bank
from Controllers.BankController import BankController

def print_banks_by_indices(controller, indices):
    banks = controller.banks
    for index in indices:
        bank = banks[index]
        print(f"ID: {index}, Имя: {bank.name}")