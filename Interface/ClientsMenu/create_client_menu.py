from Controllers.BankController import BankController
from Models.Client import Client

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