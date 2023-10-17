
"""
отдельная функция показывает список элементов массива и id (аргументы - массив) (id - переменная индекс массива)
(использовать для (список клиентов, выбор по id) и (список банков, выбор по id))
Меню:

1: работа с Банком
    1: создать банк
        (название)
    2: удалить банк
        (список банков, выбор по id) 
        (удалить из массива банков)
    3: выбрать банк
        (список банков, выбор по id)
            Меню выбранного Банка:
                1: зарегестрировать клиента
                    (список клиентов, выбор по id) 
                    (добавить выбранного клиента в выбранный банк банк)
                2: удалить клиента
                    (список клиентов, выбор по id) 
                    (удалить выбранного клиента из выбранного банка)
        
2: работа с Клиентами
    1: создать клиента
        (название и тип (физическое или юридическое лицо))
        (добавить в массив клиентов)
    2: удалить клиента
        (список клиентов, выбор по id) 
        (удалить выбранного из массива клиентов)
    3: выбрать клиента
        (список клиентов, выбор по id)
            Меню выбранного Клиента:
                1: положить деньги на счет
                    (указать сумму в рублях)
                2: снять деньги со счета
                    (указать сумму в рублях)
                3: сделать перевод суммы денег на другой счет
                    (список клиентов, выбор по id)
                        (указать сумму в рублях)
                        проверка что если банки клиентов разные и текущий клиент не юридическое лицо, не проводить операцию
                        
"""


class Bank:
    def __init__(self, name):
        self.name = name
        self.own_funds = 0
        self.clients = []

    def add_client(self, client):
        if client not in self.clients:
            self.clients.append(client)
            return True
        else:
            return False

    def remove_client(self, client):
        self.clients.remove(client)

    def transfer_money(self, sender, receiver_bank, receiver, amount):
        if sender != receiver and isinstance(sender, Client) and isinstance(receiver, Client) and sender.account.balance >= amount:
            sender.account.withdraw(amount)
            receiver_bank.receive_transfer(amount)
            receiver.account.deposit(amount)
            return True
        else:
            return False

    def calculate_transfer_fee(self, amount):
        return 0.01 * amount

    def collect_transfer_fee(self, fee):
        self.own_funds += fee

    def receive_transfer(self, amount):
        self.own_funds += amount

class Client:
    def __init__(self, name, account):
        self.name = name
        self.account = account

class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

class PhysicalPerson(Client):
    def __init__(self, name):
        account = Account()
        super().__init__(name, account)

class LegalPerson(Client):
    def __init__(self, name):
        account = Account()
        super().__init__(name, account)

class BankController:
    def __init__(self):
        self.banks = []
        self.clients = []

    def create_bank(self, name):
        bank = Bank(name)
        self.banks.append(bank)
        return bank

    def delete_bank(self, bank):
        if bank in self.banks:
            self.banks.remove(bank)
            return True
        else:
            return False

    def select_bank(self, bank_id):
        if bank_id >= 0 and bank_id < len(self.banks):
            bank = self.banks[bank_id]
            return bank
        else:
            return None

    def create_client(self, name, client_type):
        if client_type == 1:
            client = PhysicalPerson(name)
        elif client_type == 2:
            client = LegalPerson(name)
        else:
            return None
        
        self.clients.append(client)
        return client

    def delete_client(self, client):
        if client in self.clients:
            self.clients.remove(client)
            return True
        else:
            return False

    def select_client(self, client_id):
        if client_id >= 0 and client_id < len(self.clients):
            client = self.clients[client_id]
            return client
        else:
            return None
        
    def deposit_money(self, client_id, amount):
        client = self.select_client(client_id)
        if client:
            client.account.deposit(amount)
            return True
        else:
            return False
        
    def withdraw_money(self, client_id, amount):
        client = self.select_client(client_id)
        if client:
            client.account.withdraw(amount)
            return True
        else:
            return False
        
    def transfer_money(self, sender_id, sender_bank_id, receiver_id, amount , receiver_bank_id=None):
        sender_bank = self.select_bank(sender_bank_id)
        sender = self.select_client(sender_id)
        
        if not receiver_bank_id:
            receiver_bank_id = sender_bank_id

        if sender_bank and sender:
            if receiver_bank_id:  
                receiver_bank = self.select_bank(receiver_bank_id)
                receiver = self.select_client(receiver_id)
                if receiver_bank and receiver:
                    return sender_bank.transfer_money(sender, receiver_bank, receiver, amount)
            else:  
                receiver = self.select_client(receiver_id)
                if receiver:
                    return sender_bank.transfer_money(sender, sender_bank, receiver, amount)
            
        return False
        
        

def main():
    controller = BankController()
    
    while True:
        print("--- Меню ---")
        print("1: Работа с Банком")
        print("2: Работа с Клиентами")
        print("0: Выход")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == "1":
            bank_menu(controller)
        elif choice == "2":
            client_menu(controller)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")
            
def bank_menu(controller):
    while True:
        print("--- Меню работы с Банком ---")
        print("1: Создать банк")
        print("2: Удалить банк")
        print("3: Выбрать банк")
        print("0: Назад")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == "1":
            create_bank_menu(controller)
        elif choice == "2":
            delete_bank_menu(controller)
        elif choice == "3":
            select_bank_menu(controller)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")
            
def create_bank_menu(controller):
    name = input("Введите название банка: ")
    bank = controller.create_bank(name)
    if bank:
        print(f"Банк '{bank.name}' успешно создан.")
    else:
        print("Ошибка при создании банка.")
        
def delete_bank_menu(controller):
    print_banks(controller)
    bank_id = input("Выберите ID банка для удаления: ")
    bank = controller.select_bank(int(bank_id))
    if bank and controller.delete_bank(bank):
        print(f"Банк '{bank.name}' успешно удален.")
    else:
        print("Ошибка при удалении банка.")
        
def select_bank_menu(controller):
    print_banks(controller)
    bank_id = input("Выберите ID банка: ")
    bank = controller.select_bank(int(bank_id))
    if bank:
        bank_menu_selected_bank(controller, bank)
    else:
        print("Неверный ID банка.")
        
def bank_menu_selected_bank(controller, bank):
    while True:
        print(f"--- Меню выбранного Банка '{bank.name}' ---")
        print("1: Зарегистрировать клиента")
        print("2: Удалить клиента")
        print("0: Назад")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == "1":
            register_client_menu(controller, bank)
        elif choice == "2":
            delete_client_menu(controller, bank)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")
            
def register_client_menu(controller, bank):
    print_clients(controller)
    client_id = input("Выберите ID клиента для регистрации: ")
    client = controller.select_client(int(client_id))
    if client and bank.add_client(client):
        print(f"Клиент '{client.name}' успешно зарегистрирован в банке '{bank.name}'.")
    else:
        print("Ошибка при регистрации клиента.")
        
def delete_client_menu(controller, bank):
    print_clients(controller)
    client_id = input("Выберите ID клиента для удаления: ")
    client = controller.select_client(int(client_id))
    if client and bank.remove_client(client):
        print(f"Клиент '{client.name}' успешно удален из банка '{bank.name}'.")
    else:
        print("Ошибка при удалении клиента.")
        
def client_menu(controller):
    while True:
        print("--- Меню работы с Клиентами ---")
        print("1: Создать клиента")
        print("2: Удалить клиента")
        print("3: Выбрать клиента")
        print("0: Назад")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == "1":
            create_client_menu(controller)
        elif choice == "2":
            delete_client_menu(controller)
        elif choice == "3":
            select_client_menu(controller)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")
            
def create_client_menu(controller):
    name = input("Введите имя клиента: ")
    print("Тип клиента:")
    print("1: Физическое лицо")
    print("2: Юридическое лицо")
    client_type = input("Выберите тип клиента: ")
    client = controller.create_client(name, int(client_type))
    if client:
        print(f"Клиент '{client.name}' успешно создан.")
    else:
        print("Ошибка при создании клиента.")
        
def delete_client_menu(controller):
    print_clients(controller)
    client_id = input("Выберите ID клиента для удаления: ")
    client = controller.select_client(int(client_id))
    if client and controller.delete_client(client):
        print(f"Клиент '{client.name}' успешно удален.")
    else:
        print("Ошибка при удалении клиента.")
        
def select_client_menu(controller):
    print_clients(controller)
    client_id = input("Выберите ID клиента: ")
    client = controller.select_client(int(client_id))
    if client:
        client_menu_selected_client(controller, client,int(client_id))
    else:
        print("Неверный ID клиента.")
        
def client_menu_selected_client(controller, client,client_id):
    while True:
        print(f"--- Меню выбранного Клиента '{client.name}' ---")
        print("1: Положить деньги на счет")
        print("2: Снять деньги со счета")
        print("3: Сделать перевод на другой счет")
        print("0: Назад")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == "1":
            deposit_money_menu(controller, client)
        elif choice == "2":
            withdraw_money_menu(controller, client)
        elif choice == "3":
            transfer_money_menu(controller, client,int(client_id))
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")
            
def deposit_money_menu(controller, client):
    amount = float(input("Введите сумму в рублях: "))
    client.account.deposit(amount)
    print(f"Сумма {amount} успешно зачислена на счет клиента '{client.name}'.")
        
def withdraw_money_menu(controller, client):
    amount = float(input("Введите сумму в рублях: "))
    if client.account.withdraw(amount):
        print(f"Сумма {amount} успешно списана со счета клиента '{client.name}'.")
    else:
        print("Недостаточно средств на счете.")
            
def transfer_money_menu(controller, sender, sender_id):
    print_clients(controller)
    receiver_id = input("Выберите ID получателя: ")
    receiver = controller.select_client(int(receiver_id))
    
    if receiver:
        banks_with_sender = []
        for index, bank in enumerate(controller.banks):
            if sender in bank.clients:
                banks_with_sender.append(index)
                
        if len(banks_with_sender) >= 1:
            print("Банк отправителя:")
            print_banks_by_indices(controller, banks_with_sender)
            sender_bank_id = input("Выберите ID банка отправителя: ")
        else:
            sender_bank_id = banks_with_sender[0]
            
        if sender_bank_id:
            banks_with_receiver = []
            for index, bank in enumerate(controller.banks):
                if receiver in bank.clients:
                    banks_with_receiver.append(index)
                    
            if len(banks_with_receiver) >= 1:
                print("Банк получателя:")
                print_banks_by_indices(controller, banks_with_receiver)
                receiver_bank_id = input("Выберите ID банка получателя: ")
            else:
                receiver_bank_id = banks_with_receiver[0] if banks_with_receiver else None
                
            if sender_bank_id or receiver_bank_id is not None:
                amount = float(input("Введите сумму в рублях: "))
                if controller.transfer_money(int(sender_id), int(sender_bank_id), int(receiver_id), amount, int(receiver_bank_id)):
                    print(f"Сумма {amount} успешно переведена с клиента '{sender.name}' на клиента '{receiver.name}'.")
                else:
                    print("Ошибка при переводе средств.")
            else:
                print("Банк получателя не найден.")
        else:
            print("Банк отправителя не найден.")
    else:
        print("Неверный ID получателя.")
        
def print_banks_by_indices(controller, indices):
    banks = controller.banks
    for index in indices:
        bank = banks[index]
        print(f"ID: {index}, Имя: {bank.name}")
        
def print_banks(controller):
    banks = controller.banks
    if banks:
        for index, bank in enumerate(banks):
            print(f"ID: {index}, Имя: {bank.name}")
    else:
        print("Список банков пуст.")
        
def print_clients(controller):
    clients = controller.clients
    if clients:
        for index, client in enumerate(clients):
            print(f"ID: {index}, Имя: {client.name}")
    else:
        print("Список клиентов пуст.")

if __name__ == "__main__":
    main()
