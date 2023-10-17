from Controllers.BankController import BankController
from Models.Client import Client

def deposit_money_menu(controller, client):
    amount = float(input("Введите сумму в рублях: "))
    client.account.deposit(amount)
    print(f"Сумма {amount} успешно зачислена на счет клиента '{client.name}'.")