import traceback
from Interface.Tools.input_integer_non_negative_numbers import input_integer_non_negative_numbers

def create_client_menu(controller):
    try:
        name = input("Введите имя клиента: ")
        if name != None and name != "":
            print("Тип клиента:")
            print("1: Физическое лицо")
            print("2: Юридическое лицо")
            client_type = input_integer_non_negative_numbers("Выберите тип клиента: ")

            if client_type in [1, 2]:
                client = controller.create_client(name, client_type)
        
                if client:
                    print(f"Клиент '{client.name}' успешно создан.")
                else:
                    print("Ошибка при создании клиента.")
            else:
                print("Неверный тип клиента.")
        else:
            print("Ошибка при создании клиента.")
    except Exception as e:
            traceback.print_exc()
            return None