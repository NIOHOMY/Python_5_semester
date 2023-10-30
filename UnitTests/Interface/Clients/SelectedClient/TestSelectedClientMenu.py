import unittest
from unittest.mock import patch
from io import StringIO
from .....Controllers.BankController import BankController
from .....Models.Bank import Bank
from .....Models.Client import Client
from .....Models.Account import Account

from .....Interface.ClientsMenu.SelectedClientMenu.deposit_money_menu  import deposit_money_menu
from .....Interface.ClientsMenu.SelectedClientMenu.withdraw_money_menu  import withdraw_money_menu
from .....Interface.ClientsMenu.SelectedClientMenu.transfer_money_menu  import transfer_money_menu
from .....Interface.ClientsMenu.SelectedClientMenu.client_menu_selected_client  import client_menu_selected_client
from .....Interface.Tools.print_banks_clients  import print_banks_clients
from .....Interface.Tools.print_clients  import print_clients
from .....Interface.Tools.print_banks_by_indices  import print_banks_by_indices
from .....Interface.Tools.choose_account  import choose_account


class TestClientMenu(unittest.TestCase):

    def setUp(self):
        self.controller = BankController()
        self.client = Client("John Doe")

    @patch('builtins.input', side_effect=['1'])
    def test_deposit_money_menu(self, mock_input):
        output = StringIO()
        with patch('sys.stdout', new=output):
            deposit_money_menu(self.controller, self.client)
        self.assertEqual(output.getvalue().strip(), "Сумма 0.0 успешно зачислена на счет клиента 'John Doe'.")

    @patch('builtins.input', side_effect=['2'])
    def test_withdraw_money_menu(self, mock_input):
        output = StringIO()
        with patch('sys.stdout', new=output):
            withdraw_money_menu(self.controller, self.client)
        self.assertEqual(output.getvalue().strip(), "Недостаточно средств на счете.")

    @patch('builtins.input', side_effect=['3'])
    def test_transfer_money_menu(self, mock_input):
        output = StringIO()
        with patch('sys.stdout', new=output):
            transfer_money_menu(self.controller, self.client, 1)
        self.assertEqual(output.getvalue().strip(), "Получатель не зарегистрирован ни в одном банке.")

    @patch('builtins.input', side_effect=['0'])
    def test_client_menu_selected_client(self, mock_input):
        with patch('sys.stdout', new=StringIO()):
            with self.assertRaises(SystemExit):
                client_menu_selected_client(self.controller, self.client, 1)

if __name__ == '__main__':
    unittest.main()
