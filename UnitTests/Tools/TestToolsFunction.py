﻿import unittest
from unittest.mock import patch, MagicMock
from Models.Bank import Bank
from Models.Client import Client
from Models.Account import Account
from Controllers.BankController import BankController
from ...Interface.Tools.choose_account import choose_account
from ...Interface.Tools.print_banks import print_banks
from ...Interface.Tools.print_banks_by_indices import print_banks_by_indices 
from ...Interface.Tools.print_banks_clients import print_banks_clients
from ...Interface.Tools.print_clients import print_clients

"""
Тест test_choose_account_valid_choice проверяет, что функция choose_account корректно выбирает счет клиента из списка, когда пользователь вводит допустимый выбор.

Тест test_choose_account_invalid_choice проверяет, что функция choose_account правильно обрабатывает недопустимый выбор от пользователя и просит повторить ввод, пока не будет указан допустимый выбор.

Тест test_choose_account_no_accounts проверяет, что функция choose_account правильно обрабатывает случай, когда у клиента нет открытых счетов. В этом случае функция должна вывести сообщение об отсутствии счетов и вернуть None.

Тесты test_print_banks и test_print_banks_empty_list проверяют, что функция print_banks правильно выводит список банков или сообщение о пустом списке банков.

Тест test_print_banks_by_indices проверяет, что функция print_banks_by_indices правильно выводит список банков на основе указанных индексов банков.

Тесты test_print_banks_clients и test_print_banks_clients_empty_list проверяют, что функция print_banks_clients правильно выводит список клиентов определенного банка или сообщение о пустом списке клиентов.

Тест test_print_clients проверяет, что функция print_clients правильно выводит список всех клиентов в системе.
"""

class TestToolsFunctions(unittest.TestCase):

    def setUp(self):
        self.bank1 = Bank("Bank 1")
        self.bank2 = Bank("Bank 2")

        self.client1 = Client("Client 1")
        self.client2 = Client("Client 2")

        self.account1_bank1 = Account(self.bank1)
        self.account2_bank1 = Account(self.bank1)
        self.account1_bank2 = Account(self.bank2)

        self.client1.add_account(self.account1_bank1)
        self.client1.add_account(self.account2_bank1)
        self.client2.add_account(self.account1_bank2)

        self.controller = BankController()
        self.controller.add_bank(self.bank1)
        self.controller.add_bank(self.bank2)
        self.controller.add_client(self.client1)
        self.controller.add_client(self.client2)

    def test_choose_account_valid_choice(self):
        with patch('builtins.input', return_value='2'):
            chosen_account = choose_account(self.client1)
            self.assertEqual(chosen_account, self.account2_bank1)

    def test_choose_account_invalid_choice(self):
        with patch('builtins.input', side_effect=['0', '3', '1']):
            chosen_account = choose_account(self.client1)
            self.assertEqual(chosen_account, self.account1_bank1)

    def test_choose_account_no_accounts(self):
        client = Client("Client 3")
        with patch('builtins.print') as mock_print:
            chosen_account = choose_account(client)
            self.assertIsNone(chosen_account)
            mock_print.assert_called_with("У вас нет открытых счетов.")

    def test_print_banks(self):
        with patch('builtins.print') as mock_print:
            print_banks(self.controller)
            mock_print.assert_has_calls([
                unittest.mock.call("ID: 0, Имя: Bank 1"),
                unittest.mock.call("ID: 1, Имя: Bank 2")
            ])

    def test_print_banks_empty_list(self):
        controller = BankController()
        with patch('builtins.print') as mock_print:
            print_banks(controller)
            mock_print.assert_called_with("Список банков пуст.")

    def test_print_banks_by_indices(self):
        indices = [0, 1]
        with patch('builtins.print') as mock_print:
            print_banks_by_indices(self.controller, indices)
            mock_print.assert_has_calls([
                unittest.mock.call("ID: 0, Имя: Bank 1"),
                unittest.mock.call("ID: 1, Имя: Bank 2")
            ])

    def test_print_banks_clients(self):
        bank = self.bank1
        with patch('builtins.print') as mock_print:
            print_banks_clients(self.controller, bank)
            mock_print.assert_has_calls([
                unittest.mock.call("ID: 0, Имя: Client 1"),
            ])

    def test_print_banks_clients_empty_list(self):
        bank = self.bank2
        with patch('builtins.print') as mock_print:
            print_banks_clients(self.controller, bank)
            mock_print.assert_called_with("Список клиентов пуст.")

    def test_print_clients(self):
        with patch('builtins.print') as mock_print:
            print_clients(self.controller)
            mock_print.assert_has_calls([
                unittest.mock.call("ID: 0, Имя: Client 1"),
                unittest.mock.call("ID: 1, Имя: Client 2")
            ])


if __name__ == '__main__':
    unittest.main()
