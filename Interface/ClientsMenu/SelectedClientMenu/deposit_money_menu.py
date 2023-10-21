from Controllers.BankController import BankController
from Models.Client import Client
from ...Tools.choose_account import choose_account

def deposit_money_menu(controller, client):
    amount = float(input("Введите сумму в рублях: "))
    account = choose_account(client)
    if account:
        account.deposit(amount)
        print(f"Сумма {amount} успешно зачислена на счет клиента '{client.name}'.")
    else:
        print("Отсутствуют аккаунты.")    