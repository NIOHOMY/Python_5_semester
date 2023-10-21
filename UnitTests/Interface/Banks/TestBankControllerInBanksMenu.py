import unittest
from unittest.mock import patch, mock_input
from ....Controllers.BankController import BankController
from ....Interface.Tools.print_banks import  print_banks
from ....Interface.BanksMenu.SelectedBankMenu.bank_menu_selected_bank import bank_menu_selected_bank
from ....Interface.BanksMenu.create_bank_menu import create_bank_menu
from ....Interface.BanksMenu.delete_bank_menu import delete_bank_menu
from ....Interface.BanksMenu.select_bank_menu import select_bank_menu
from ....Interface.BanksMenu.bank_menu import bank_menu

"""
В методе test_bank_menu_create_bank проверяется, что создание банка происходит успешно и он появляется в списке банков контроллера.

В методе test_bank_menu_delete_bank проверяется, что удаление банка происходит успешно и он удаляется из списка банков контроллера.

В методе test_bank_menu_select_bank проверяется, что выбор банка происходит успешно и выбранный банк становится текущим выбранным банком в контроллере.

В методе test_create_bank_menu проверяется, что создание банка через меню происходит успешно и он появляется в списке банков контроллера.

В методе test_create_bank_menu_failure проверяются случаи, когда название банка не было предоставлено или уже существует банк с таким же названием.

В методе test_delete_bank_menu_failure проверяются случаи, когда нет ни одного банка для удаления или был предоставлен неверный идентификатор банка.

В методе test_select_bank_menu проверяется, что выбор банка через меню происходит успешно и выбранный банк становится текущим выбранным банком в контроллере.

В методе test_select_bank_menu_failure проверяются случаи, когда нет ни одного банка для выбора или был предоставлен неверный идентификатор банка.

"""


class TestBankControllerInBanksMenu(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["1", "Test Bank", "0"])
    def test_bank_menu_create_bank(self, mock_input):
        controller = BankController()
        self.assertIsNone(controller.get_bank_by_name("Test Bank"))
        bank_menu(controller)
        self.assertIsNotNone(controller.get_bank_by_name("Test Bank"))

    @patch('builtins.input', side_effect=["2", "1", "y", "0"])
    def test_bank_menu_delete_bank(self, mock_input):
        controller = BankController()
        bank = controller.create_bank("Test Bank")
        self.assertIsNotNone(controller.get_bank_by_name("Test Bank"))
        with patch('builtins.input', side_effect=[str(bank.id), "y", "0"]):
            bank_menu(controller)
        self.assertIsNone(controller.get_bank_by_id(bank.id))

    @patch('builtins.input', side_effect=["3", "1", "0"])
    def test_bank_menu_select_bank(self, mock_input):
        controller = BankController()
        bank = controller.create_bank("Test Bank")
        with patch('builtins.input', return_value=bank.id):
            bank_menu(controller)
        self.assertEqual(controller.selected_bank, bank)

    @patch('builtins.input', side_effect=["Test Bank", "0"])
    def test_create_bank_menu(self, mock_input):
        controller = BankController()
        self.assertIsNone(controller.get_bank_by_name("Test Bank"))
        create_bank_menu(controller)
        self.assertIsNotNone(controller.get_bank_by_name("Test Bank"))

    def test_create_bank_menu_failure(self):
        controller = BankController()

        # Test case when no name is provided
        with patch('builtins.input', side_effect=["", "0"]):
            create_bank_menu(controller)
        self.assertIsNone(controller.get_bank_by_name(""))

        # Test case when bank already exists with same name
        controller.create_bank("Test Bank")
        with patch('builtins.input', side_effect=["Test Bank", "0"]):
            create_bank_menu(controller)
        self.assertEqual(len(controller.banks), 1)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_delete_bank_menu_failure(self, mock_stdout):
        controller = BankController()

        # Test case when no banks exist
        with patch('builtins.input', side_effect=["1", "n", "0"]):
            delete_bank_menu(controller)
        self.assertEqual(mock_stdout.getvalue().strip(), "No banks to delete.")

        # Test case when invalid bank id is provided
        controller.create_bank("Test Bank")
        with patch('builtins.input', return_value="invalid_id"), \
                patch('builtins.print') as mock_print:
            delete_bank_menu(controller)
        self.assertIn("Invalid bank id", mock_print.call_args[0][0])

    @patch('builtins.input', side_effect=["1", "0"])
    def test_select_bank_menu(self, mock_input):
        controller = BankController()
        bank = controller.create_bank("Test Bank")
        select_bank_menu(controller)
        self.assertEqual(controller.selected_bank, bank)

    def test_select_bank_menu_failure(self):
        controller = BankController()

        # Test case when no banks exist
        with patch('builtins.input', return_value="1"), \
                patch('builtins.print') as mock_print:
            select_bank_menu(controller)
        self.assertEqual(mock_print.call_args[0][0].strip(), "No banks available.")

        # Test case when invalid bank id is provided
        controller.create_bank("Test Bank")
        with patch('builtins.input', return_value="invalid_id"), \
                patch('builtins.print') as mock_print:
            select_bank_menu(controller)
        self.assertIn("Invalid bank id", mock_print.call_args[0][0])


if __name__ == '__main__':
    unittest.main()
