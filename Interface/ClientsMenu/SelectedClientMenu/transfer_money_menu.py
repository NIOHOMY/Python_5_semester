from Controllers.BankController import BankController
from Models.Client import Client
from Models.Bank import Bank
from ...Tools.print_banks_by_indices import print_banks_by_indices
from ...Tools.print_clients import print_clients

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
            sender_bank_id = None

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
                receiver_bank_id = None

            if sender_bank_id and receiver_bank_id is not None:
                amount = float(input("Введите сумму в рублях: "))
                if controller.transfer_money(int(sender_id), int(sender_bank_id), int(receiver_id), amount, int(receiver_bank_id)):
                    print(f"Сумма {amount} успешно переведена с клиента '{sender.name}' банка '{controller.get_bank_by_id(int(sender_bank_id)).get_name()}' на клиента '{receiver.name}' банка '{controller.get_bank_by_id(int(receiver_bank_id)).get_name()}'.")
                    print(f"Коммиссия составила {controller.get_bank_by_id(int(sender_bank_id)).calculate_transfer_fee(amount)} рублей.")
                else:
                    print("Ошибка при переводе средств.")
            else:
                print("Получатель не зарегистрирован ни в одном банке.")
        else:
            print("Отправитель не зарегистрирован ни в одном банке.")
    else:
        print("Неверный ID получателя.")