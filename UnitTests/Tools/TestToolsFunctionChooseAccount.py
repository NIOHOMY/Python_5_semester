from io import StringIO
import unittest
from unittest.mock import patch, Mock
from Interface.Tools.choose_account import choose_account
from Interface.Tools.input_integer_non_negative_numbers import input_integer_non_negative_numbers

"""
with mock.patch('Interface.Tools.input_integer_non_negative_numbers.input_integer_non_negative_numbers', side_effect=[None, 0]):
            selected_account = choose_account(client)
            
with mock.patch('Interface.Tools.input_integer_non_negative_numbers.input_integer_non_negative_numbers', return_value=0):
            selected_account = choose_account(client)            
"""

"""

"""
class TestToolsFunctionChooseAccount(unittest.TestCase):

    def setUp(self):
        """
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
        """
        
    @patch('builtins.input', return_value='0')
    @patch('sys.stdout', new_callable=StringIO) 
    def test_choose_account_valid_input(self, mock_stdout, mock_input):
        client = Mock()
        account = Mock()
        account.get_bank.return_value.name = "Bank A"
        client.bank_accounts = [account]
        input_integer_non_negative_numbers.return_value = 0

        selected_account = choose_account(client)

        self.assertEqual(selected_account, account)
        self.assertEqual(mock_stdout.getvalue().strip(), "Список ваших счетов:\n0. Банк: Bank A")

    @patch('builtins.input', side_effect=['invalid', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_choose_account_invalid_and_valid_input_letter(self, mock_stdout, mock_input):
        client = Mock()
        account = Mock()
        account.get_bank.return_value.name = "Bank A"
        client.bank_accounts = [account]
        input_integer_non_negative_numbers.return_value = Mock(side_effect=[None, 0])

        selected_account = choose_account(client)

        self.assertEqual(selected_account, account)
        self.assertEqual(mock_stdout.getvalue().strip(), "Список ваших счетов:\n0. Банк: Bank A\nОшибка: введите корректный номер.")
        
    @patch('builtins.input', side_effect=['9', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_choose_account_invalid_and_valid_input_greater_lengths_array(self, mock_stdout, mock_input):
        client = Mock()
        account = Mock()
        account.get_bank.return_value.name = "Bank A"
        client.bank_accounts = [account]
        input_integer_non_negative_numbers.return_value = Mock(side_effect=[9, 0])

        selected_account = choose_account(client)

        self.assertEqual(selected_account, account)
        self.assertEqual(mock_stdout.getvalue().strip(), "Список ваших счетов:\n0. Банк: Bank A\nОшибка: введите корректный номер.")
        
    @patch('builtins.input', side_effect=["-1", '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_choose_account_invalid_and_valid_input_less_lengths_array(self, mock_stdout, mock_input):
        client = Mock()
        account = Mock()
        account.get_bank.return_value.name = "Bank A"
        client.bank_accounts = [account]
        input_integer_non_negative_numbers.return_value = Mock(side_effect=[None, 0])

        selected_account = choose_account(client)

        self.assertEqual(selected_account, account)
        self.assertEqual(mock_stdout.getvalue().strip(), "Список ваших счетов:\n0. Банк: Bank A\nОшибка: введите корректный номер.")
       

    @patch('builtins.input', return_value='0')
    @patch('sys.stdout', new_callable=StringIO)
    def test_choose_account_no_accounts(self, mock_stdout, mock_input):
        client = Mock()
        client.bank_accounts = []
        input_integer_non_negative_numbers.return_value = 0

        selected_account = choose_account(client)

        self.assertIsNone(selected_account)
        self.assertEqual(mock_stdout.getvalue().strip(), "Список ваших счетов:\nУ вас нет открытых счетов.")

    """
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
        
    """
    
if __name__ == '__main__':
    unittest.main()