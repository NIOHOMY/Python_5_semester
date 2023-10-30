import traceback
from Interface.Tools.input_integer_non_negative_numbers import input_integer_non_negative_numbers

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
            account_map[index] = account  # Добавляем элемент в отображение
            print(f"{index}. Банк: {account.get_bank().name}")
    
        if len(account_map) == 0:
            print("У вас нет открытых счетов.")
            return None
    
        while True:
            choice = input_integer_non_negative_numbers("Выберите номер счета: ")
            if choice != None:
                account = account_map[int(choice)]
                return account
            
            print("Ошибка: введите корректный номер.")
            
        
    except Exception as e:
            traceback.print_exc()
            return None
