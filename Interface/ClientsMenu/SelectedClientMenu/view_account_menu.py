import traceback
from Interface.Tools.choose_account import choose_account

def view_account_menu(controller, client):
    try:
        account = choose_account(client);
        if account:
            print(f"У вас на счёте {account.get_balance()} рублей.")
        else:
            print("У вас нет ни одного аккаунта в банках.")
   
    except Exception as e:
            traceback.print_exc()
            return None