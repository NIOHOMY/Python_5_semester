import traceback
from Models.Client import Client
from Models.Bank import Bank
from Controllers.BankController import BankController

def choose_account(client):
    """
    Функция выводит список счетов клиента в разных банках и позволяет выбрать нужный счет.
    :param client: объект класса Client
    :return: объект класса Account или None, если счет не найден
    """
    try:
        account_map = {}  # Отображение для хранения связи между id и объектами аккаунтов
        print("Список ваших счетов:")
        for index, account in enumerate(client.bank_accounts):
            account_map[index + 1] = account  # Добавляем элемент в отображение
            print(f"{index + 1}) Банк: {account.get_bank().name}")
    
        if len(account_map) == 0:
            print("У вас нет открытых счетов.")
            return None
    
        while True:
            choice = input("Выберите номер счета: ")
            try:
                account = account_map[int(choice)]
                return account
            except (ValueError, KeyError):
                print("Ошибка: введите корректный номер.")
        
    except Exception as e:
            traceback.print_exc()
            return None
