from Controllers.BankController import BankController
from Models.Client import Client
from ...Tools.choose_account import choose_account

def withdraw_money_menu(controller, client):
    amount = float(input("Введите сумму в рублях: "))
    account = choose_account(client)
    if account.withdraw(amount):
        print(f"Сумма {amount} успешно списана со счета клиента '{client.name}'.")
    else:
        print("Недостаточно средств на счете или отсутствуют аккаунты.")