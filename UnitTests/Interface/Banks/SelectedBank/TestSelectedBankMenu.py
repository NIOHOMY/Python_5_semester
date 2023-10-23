import unittest
from unittest.mock import patch
from io import StringIO
from Controllers.BankController import BankController
from Models.Bank import Bank
from Models.Client import Client
from Models.Account import Account

from Interface.BanksMenu.SelectedBankMenu.bank_menu_selected_bank  import bank_menu_selected_bank
from Interface.BanksMenu.SelectedBankMenu.delete_client_menu  import delete_client_menu
from Interface.BanksMenu.SelectedBankMenu.register_client_menu  import register_client_menu
from Interface.Tools.print_banks_clients  import print_banks_clients
from Interface.Tools.print_clients  import print_clients

"""

test_bank_menu_selected_bank_register_client: Этот тест проверяет, что при выборе пункта "Зарегистрировать клиента" из главного меню банка, 
выводится соответствующий текст на экране.

test_bank_menu_selected_bank_delete_client: Этот тест проверяет, что при выборе пункта "Удалить клиента" из главного меню банка, 
выводится соответствующий текст на экране.

test_bank_menu_selected_bank_exit: Этот тест проверяет, что при выборе пункта "Назад" из главного меню банка, не выводится текст,
связанный с другими пунктами меню.

test_delete_client_menu_invalid_id: Этот тест проверяет, что при попытке удалить несуществующего клиента, выводится соответствующий текст на экране.

test_register_client_menu_invalid_id: Этот тест проверяет, что при попытке зарегистрировать клиента с неверным ID, 
выводится соответствующий текст на экране.

"""

class TestSelectedBankMenu(unittest.TestCase):
    def setUp(self):
        # Создание контроллера и банка для тестов
        self.controller = BankController()
        self.bank = Bank("b1")

    def tearDown(self):
        del self.controller
        del self.bank

    @patch('builtins.input', side_effect=['1', '0'])
    def test_bank_menu_selected_bank_register_client(self, mocked_input):
        # Проверка функции bank_menu_selected_bank с выбором пункта "Зарегистрировать клиента"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            bank_menu_selected_bank(self.controller, self.bank)
            self.assertIn("Выберите пункт меню:", fake_output.getvalue())
            self.assertIn("Зарегистрировать клиента", fake_output.getvalue())

    @patch('builtins.input', side_effect=['2', '0'])
    def test_bank_menu_selected_bank_delete_client(self, mocked_input):
        # Проверка функции bank_menu_selected_bank с выбором пункта "Удалить клиента"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            bank_menu_selected_bank(self.controller, self.bank)
            self.assertIn("Выберите пункт меню:", fake_output.getvalue())
            self.assertIn("Удалить клиента", fake_output.getvalue())

    @patch('builtins.input', side_effect=['0'])
    def test_bank_menu_selected_bank_exit(self, mocked_input):
        # Проверка функции bank_menu_selected_bank с выбором пункта "Назад"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            bank_menu_selected_bank(self.controller, self.bank)
            self.assertIn("--- Меню выбранного Банка 'b1' ---", fake_output.getvalue())

    def test_delete_client_menu_invalid_id(self):
        # Проверка функции delete_client_menu с неверным ID клиента
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', return_value=None):
                delete_client_menu(self.controller, self.bank)
                self.assertIn("Некорректный ID клиента.", fake_output.getvalue())

    def test_register_client_menu_invalid_id(self):
        # Проверка функции register_client_menu с неверным ID клиента
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', return_value=None):
                register_client_menu(self.controller, self.bank)
                self.assertIn("Некорректный ID клиента.", fake_output.getvalue())

if __name__ == '__main__':
    unittest.main()
