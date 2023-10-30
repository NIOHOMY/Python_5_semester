import unittest
from unittest.mock import patch, MagicMock
import builtins
from Models.Bank import Bank
from Models.Client import Client
from Models.Persons.LegalPerson import LegalPerson
from Models.Persons.PhysicalPerson import PhysicalPerson
from Models.Account import Account
from Controllers.BankController import BankController
from Interface.Tools.choose_account import choose_account
from Interface.Tools.print_banks import print_banks
from Interface.Tools.print_banks_by_indices import print_banks_by_indices 
from Interface.Tools.print_banks_clients import print_banks_clients
from Interface.Tools.print_clients import print_clients
from Interface.Tools.input_integer_non_negative_numbers import input_integer_non_negative_numbers
from Interface.Tools.input_float_non_negative_numbers import input_float_non_negative_numbers


class TestToolsFunctions(unittest.TestCase):

    def setUp(self):
        self.bank1 = Bank("Bank 1")
        self.bank2 = Bank("Bank 2")
        self.bank3 = Bank("Bank 2")

        self.client1 = PhysicalPerson("Client 1")
        self.client2 = PhysicalPerson("Client 2")
        
        self.client3 = LegalPerson("Client 3")
        
        self.bank1.add_client(self.client1)
        self.bank1.add_client(self.client1)
        self.bank2.add_client(self.client2)

        self.account1_bank1 = self.client1.get_bank_account(self.bank1)
        self.account2_bank1 = self.client1.get_bank_account(self.bank1)
        self.account1_bank2 = self.client2.get_bank_account(self.bank2)


        self.controller = BankController()
        self.controller.create_bank("Bank 1")
        self.controller.create_bank("Bank 2")
        self.controller.create_bank("Bank 3")
        self.controller.create_client("Client 1", 1)
        self.controller.create_client("Client 2", 1)

    def test_choose_account_valid_choice(self):
        with patch('builtins.input', side_effect=['0']):
            chosen_account = choose_account(self.client1)
            self.assertEqual(chosen_account, self.account2_bank1)

    def test_choose_account_invalid_choice(self):
        mock_print = MagicMock(name="builtins.print")
        builtins.print = mock_print
        
        with patch('builtins.input', side_effect=["-10", '0']):
            chosen_account = choose_account(self.client1)
            mock_print.assert_called_with("Ошибка: введите корректный номер.")
            self.assertEqual(chosen_account, self.account2_bank1)

    def test_choose_account_no_accounts(self):
        client = PhysicalPerson("test Client 3")
        mock_print = MagicMock(name="builtins.print")
        builtins.print = mock_print
        
        chosen_account = choose_account(client)
        self.assertIsNone(chosen_account)
        mock_print.assert_called_with("У вас нет открытых счетов.")

    def test_print_banks(self):
        mock_print = MagicMock(name="builtins.print")
        builtins.print = mock_print
        
        print_banks(self.controller)
        mock_print.assert_has_calls([
            unittest.mock.call("ID: 0, Имя: Bank 1"),
            unittest.mock.call("ID: 1, Имя: Bank 2")
        ])

    def test_print_banks_empty_list(self):
        controller = BankController()
        mock_print = MagicMock(name="builtins.print")
        builtins.print = mock_print
        
        print_banks(controller)
        mock_print.assert_called_with("Список банков пуст.")

    def test_print_banks_by_indices(self):
        indices = [0, 1]
        mock_print = MagicMock(name="builtins.print")
        builtins.print = mock_print
        
        print_banks_by_indices(self.controller, indices)
        mock_print.assert_has_calls([
            unittest.mock.call("ID: 0, Имя: Bank 1"),
            unittest.mock.call("ID: 1, Имя: Bank 2")
        ])

    def test_print_banks_clients(self):
        bank = self.bank1
        mock_print = MagicMock(name="builtins.print")
        builtins.print = mock_print
        
        print_banks_clients(self.controller, bank)
        mock_print.assert_has_calls([
            unittest.mock.call("ID: 0, Имя: Client 1"),
        ])

    def test_print_banks_clients_empty_list(self):
        bank = self.bank3
        mock_print = MagicMock(name="builtins.print")
        builtins.print = mock_print
        
        print_banks_clients(self.controller, bank)
        mock_print.assert_called_with("Список клиентов пуст.")

    def test_print_clients(self):
        mock_print = MagicMock(name="builtins.print")
        builtins.print = mock_print
        
        print_clients(self.controller)
        mock_print.assert_has_calls([
            unittest.mock.call("ID: 0, Имя: Client 1"),
            unittest.mock.call("ID: 1, Имя: Client 2")
        ])
        
    def test_input_float_negative_numbers(self):
        # Тестирование некорректного ввода отрицательного числа
        with unittest.mock.patch('builtins.input', return_value='-5'):
            result = input_float_non_negative_numbers()
            self.assertIsNone(result)

    def test_input_float_non_numeric_characters(self):
        # Тестирование некорректного ввода буквенных символов
        with unittest.mock.patch('builtins.input', return_value='abc'):
            result = input_float_non_negative_numbers()
            self.assertIsNone(result)

    def test_input_float_positive_number(self):
        # Тестирование корректного ввода положительного числа
        with unittest.mock.patch('builtins.input', return_value='3.14'):
            result = input_float_non_negative_numbers()
            self.assertEqual(result, 3.14)

    def test_input_float_zero(self):
        # Тестирование корректного ввода нуля
        with unittest.mock.patch('builtins.input', return_value='0'):
            result = input_float_non_negative_numbers()
            self.assertEqual(result, 0)

    def test_input_integer_negative_numbers(self):
        # Тестирование некорректного ввода отрицательного числа
        with unittest.mock.patch('builtins.input', return_value='-5'):
            result = input_integer_non_negative_numbers()
            self.assertIsNone(result)

    def test_input_integer_non_numeric_characters(self):
        # Тестирование некорректного ввода буквенных символов
        with unittest.mock.patch('builtins.input', return_value='abc'):
            result = input_integer_non_negative_numbers()
            self.assertIsNone(result)

    def test_input_integer_positive_number(self):
        # Тестирование корректного ввода положительного числа
        with unittest.mock.patch('builtins.input', return_value='42'):
            result = input_integer_non_negative_numbers()
            self.assertEqual(result, 42)

    def test_input_integer_zero(self):
        # Тестирование корректного ввода нуля
        with unittest.mock.patch('builtins.input', return_value='0'):
            result = input_integer_non_negative_numbers()
            self.assertEqual(result, 0)



if __name__ == '__main__':
    unittest.main()
