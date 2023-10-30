import traceback
from ...Tools.choose_account import choose_account
from Interface.Tools.input_float_non_negative_numbers import input_float_non_negative_numbers

def deposit_money_menu(controller, client):
    try:
        amount = (input_float_non_negative_numbers("Введите сумму в рублях: "))
        if amount is not None:
            account = choose_account(client)

            if account:
                account.deposit(amount)
                print(f"Сумма {amount} успешно зачислена на счет клиента '{client.name}'.")
            else:
                print("Отсутствуют аккаунты клиента.")
        else:
            print("Некорректная сумма.")
        
    except Exception as e:
            traceback.print_exc()
            return None
    