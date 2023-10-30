﻿import traceback
from ...Tools.print_banks_by_indices import print_banks_by_indices
from ...Tools.print_clients import print_clients
from Interface.Tools.input_float_non_negative_numbers import input_float_non_negative_numbers
from Interface.Tools.input_integer_non_negative_numbers import input_integer_non_negative_numbers

def transfer_money_menu(controller, sender, sender_id):
    try:
        print_clients(controller)
        receiver_id = input_integer_non_negative_numbers("Выберите ID получателя: ")
        if receiver_id is not None:
            receiver = controller.select_client(receiver_id)

            if receiver:
                banks_with_sender = []
                for index, bank in enumerate(controller.banks):
                    if sender in bank.clients:
                        banks_with_sender.append(index)

                if len(banks_with_sender) >= 1:
                    print("Банк отправителя:")
                    print_banks_by_indices(controller, banks_with_sender)
                    sender_bank_id = input_integer_non_negative_numbers("Выберите ID банка отправителя: ")
                else:
                    sender_bank_id = None

                if sender_bank_id is not None:
                    banks_with_receiver = []
                    for index, bank in enumerate(controller.banks):
                        if receiver in bank.clients:
                            banks_with_receiver.append(index)

                    if len(banks_with_receiver) >= 1:
                        print("Банк получателя:")
                        print_banks_by_indices(controller, banks_with_receiver)
                        receiver_bank_id = input_integer_non_negative_numbers("Выберите ID банка получателя: ")
                    else:
                        receiver_bank_id = None

                    if sender_bank_id is not None and receiver_bank_id is not None:
                        amount = input_float_non_negative_numbers("Введите сумму в рублях: ")
                        if amount is not None:
                            if controller.transfer_money(sender_id, sender_bank_id, receiver_id, amount, receiver_bank_id):
                                print(f"Сумма {amount} успешно переведена с клиента '{sender.name}' банка '{controller.get_bank_by_id(int(sender_bank_id)).get_name()}' на клиента '{receiver.name}' банка '{controller.get_bank_by_id(receiver_bank_id).get_name()}'.")
                                print(f"Коммиссия составила {controller.get_bank_by_id(sender_bank_id).calculate_transfer_fee(amount)} рублей.")
                            else:
                                print("Ошибка при переводе средств.")
                        else:
                            print("Некорректная сумма.")
                    else:
                        print("Получатель не зарегистрирован ни в одном банке.")
                else:
                    print("Отправитель не зарегистрирован ни в одном банке или некорректный ID.")
            else:
                print("Неверный ID получателя.")
        
    except Exception as e:
            traceback.print_exc()
            return None
        