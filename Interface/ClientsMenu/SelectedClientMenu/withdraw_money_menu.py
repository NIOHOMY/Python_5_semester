from Controllers.BankController import BankController
from Models.Client import Client

def withdraw_money_menu(controller, client):
    amount = float(input("Введите сумму в рублях: "))
    if client.account.withdraw(amount):
        print(f"Сумма {amount} успешно списана со счета клиента '{client.name}'.")
    else:
        print("Недостаточно средств на счете.")