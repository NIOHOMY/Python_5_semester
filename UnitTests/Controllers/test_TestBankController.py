import unittest
from unittest.mock import MagicMock, Mock, call
from Controllers.BankController import BankController
from Models.Client import Client
from Models.Account import Account
from Models.Bank import Bank
from Models.Persons.LegalPerson import LegalPerson
from Models.Persons.PhysicalPerson import PhysicalPerson


class TestBankController(unittest.TestCase):

    def setUp(self):
        self.bank_controller = BankController()
        

    def test_create_bank_valid_name(self):
        name = "Bank 1"
        bank = self.bank_controller.create_bank(name)
        self.assertEqual(len(self.bank_controller.banks), 1)
        self.assertEqual(bank.name, name)
        
    def test_create_bank_invalid_name(self):
        name = None
        bank = self.bank_controller.create_bank(name)
        self.assertEqual(len(self.bank_controller.banks), 0)
        self.assertIsNone(bank)
        
    def test_create_bank_empty_name(self):
        name = ""
        bank = self.bank_controller.create_bank(name)
        self.assertEqual(len(self.bank_controller.banks), 0)
        self.assertIsNone(bank)

    def test_delete_bank_existing(self):
        bank = Mock(spec=Bank)
        self.bank_controller.banks = [bank]
        result = self.bank_controller.delete_bank(bank)
        self.assertTrue(result)
        self.assertEqual(len(self.bank_controller.banks), 0)

    def test_delete_bank_non_existing(self):
        bank = Mock(spec=Bank)
        result = self.bank_controller.delete_bank(bank)
        self.assertFalse(result)
        
    def test_select_bank_existing(self):
        bank = Mock(spec=Bank)
        self.bank_controller.banks = [bank]
        bank_id = self.bank_controller.get_bank_id(bank)
        selected_bank = self.bank_controller.select_bank(bank_id)
        self.assertEqual(selected_bank, bank)

    def test_select_bank_non_existing(self):
        bank = self.bank_controller.select_bank(0)
        self.assertIsNone(bank)
        
    def test_select_bank_invalid(self):
        bank_id = 100
        result = self.bank_controller.select_bank(bank_id)
        self.assertIsNone(result)

    def test_create_client_physical_person(self):
        name = "John Doe"
        client = self.bank_controller.create_client(name, 1)
        self.assertEqual(len(self.bank_controller.clients), 1)
        self.assertIsInstance(client, PhysicalPerson)
        self.assertEqual(client.name, name)
        
    def test_create_client_legal_person(self):
        name = "John Doe"
        client = self.bank_controller.create_client(name, 2)
        self.assertEqual(len(self.bank_controller.clients), 1)
        self.assertIsInstance(client, LegalPerson)
        self.assertEqual(client.name, name)

    def test_create_client_invalid_empty_name(self):
        name = ""
        client = self.bank_controller.create_client(name, 1)
        self.assertEqual(len(self.bank_controller.clients), 0)
        self.assertIsNone(client)
        
    def test_create_client_invalid_name_none(self):
        name = None
        client_type = 2
        result = self.bank_controller.create_client(name, client_type)
        self.assertIsNone(result)
        self.assertNotIn(None, self.bank_controller.clients)
        
    def test_create_client_invalid_type(self):
        name = "John Doe"
        client_type = 3
        result = self.bank_controller.create_client(name, client_type)
        self.assertIsNone(result)
        self.assertNotIn(None, self.bank_controller.clients)

    def test_delete_client_existing(self):
        client = Mock(spec=PhysicalPerson)
        self.bank_controller.clients = [client]
        result = self.bank_controller.delete_client(client)
        self.assertTrue(result)
        self.assertEqual(len(self.bank_controller.clients), 0)

    def test_delete_client_non_existing(self):
        client = Mock(spec=PhysicalPerson)
        result = self.bank_controller.delete_client(client)
        self.assertFalse(result)

    def test_select_client_existing(self):
        client = Mock(spec=PhysicalPerson)
        self.bank_controller.clients = [client]
        client_id = self.bank_controller.get_client_id(client)
        selected_client = self.bank_controller.select_client(client_id)
        self.assertEqual(selected_client, client)

    def test_select_client_non_existing(self):
        client = self.bank_controller.select_client(0)
        self.assertIsNone(client)
        
    def test_select_client_invalid(self):
        client_id = 100
        result = self.bank_controller.select_client(client_id)
        self.assertIsNone(result)

    def test_deposit_money_valid(self):
        account = Mock()
        amount = 100
        result = self.bank_controller.deposit_money(account, amount)
        account.deposit.assert_called_once_with(amount)
        self.assertTrue(result)

    def test_deposit_money_invalid(self):
        account = None
        amount = 100
        result = self.bank_controller.deposit_money(account, amount)
        self.assertFalse(result)

    def test_withdraw_money_valid(self):
        account = Mock()
        amount = 100
        account.withdraw.return_value = True
        result = self.bank_controller.withdraw_money(account, amount)
        account.withdraw.assert_called_once_with(amount)
        self.assertTrue(result)

    def test_withdraw_money_invalid(self):
        account = None
        amount = 100
        result = self.bank_controller.withdraw_money(account, amount)
        self.assertFalse(result)


    def test_transfer_money_valid(self):
        sender_id = 1
        sender_bank_id = 1
        receiver_id = 2
        amount = 100
        receiver_bank_id = 1
        sender_bank = Mock()
        sender = Mock()
        receiver_bank = Mock()
        receiver = Mock()
        sender_account = Mock()
        receiver_account = Mock()

        self.bank_controller.select_bank = Mock(side_effect=[sender_bank, receiver_bank])
        self.bank_controller.select_client = Mock(side_effect=[sender, receiver])
        sender.get_bank_account.return_value = sender_account
        receiver.get_bank_account.return_value = receiver_account
        sender_account.transfer_money.return_value = True

        result = self.bank_controller.transfer_money(sender_id, sender_bank_id, receiver_id, amount, receiver_bank_id)
        
        self.bank_controller.select_bank.assert_has_calls([call(sender_bank_id), call(receiver_bank_id)])
        self.bank_controller.select_client.assert_has_calls([call(sender_id), call(receiver_id)])
        sender.get_bank_account.assert_called_once_with(sender_bank)
        receiver.get_bank_account.assert_called_once_with(receiver_bank)
        sender_account.transfer_money.assert_called_once_with(sender, receiver_account, receiver, amount)
        self.assertTrue(result)

    def test_transfer_money_invalid_no_sender_bank(self):
        sender_id = 1
        sender_bank_id = 1
        receiver_id = 2
        amount = 100
        receiver_bank_id = 1
        sender_bank = None

        self.bank_controller.select_bank = Mock(side_effect=[sender_bank, sender_bank])

        result = self.bank_controller.transfer_money(sender_id, sender_bank_id, receiver_id, amount, receiver_bank_id)
        self.bank_controller.select_bank.assert_called_once_with(sender_bank_id)
        self.assertFalse(result)
        
    def test_transfer_money_invalid_no_sender(self):
        sender_id = -1
        sender_bank_id = 1
        receiver_id = 2
        amount = 100
        receiver_bank_id = 1
        sender_bank = Mock()

        self.bank_controller.select_bank = Mock(side_effect=[sender_bank, sender_bank])

        result = self.bank_controller.transfer_money(sender_id, sender_bank_id, receiver_id, amount, receiver_bank_id)
        self.bank_controller.select_bank.assert_called_once_with(sender_bank_id)
        self.assertFalse(result)
        
    def test_receiver_bank_id_is_none(self):
        sender_bank = MagicMock()
        receiver_bank = MagicMock()
        sender = MagicMock()
        receiver = MagicMock()
        sender_account = MagicMock()
        receiver_account = MagicMock()

        sender.get_bank_account.return_value = sender_account
        receiver.get_bank_account.return_value = receiver_account

        self.bank_controller.banks = [sender_bank, receiver_bank]
        self.bank_controller.clients = [sender, receiver]
        self.bank_controller.select_bank = Mock(side_effect=[sender_bank, sender_bank])
        self.bank_controller.select_client = Mock(side_effect=[sender, receiver])
        
        sender_bank_id = 123
        sender_id = 1
        receiver_id = 2
        amount = 100

        sender.get_bank_account.return_value = sender_account
        receiver.get_bank_account.return_value = receiver_account

        sender_account.transfer_money.return_value = True

        self.assertTrue(self.bank_controller.transfer_money(sender_id, sender_bank_id, receiver_id, amount))

        sender_account.transfer_money.assert_called_with(sender, receiver_account, receiver, amount)

    def test_receiver_and_receiver_bank_is_none(self):
        sender_bank = MagicMock()
        receiver_bank = MagicMock()
        sender = MagicMock()
        receiver = MagicMock()
        sender_account = MagicMock()
        receiver_account = MagicMock()

        sender.get_bank_account.return_value = sender_account
        receiver.get_bank_account.return_value = receiver_account

        self.bank_controller.banks = [sender_bank, receiver_bank]
        self.bank_controller.clients = [sender, receiver]
        self.bank_controller.select_bank = Mock(side_effect=[sender_bank, None])
        self.bank_controller.select_client = Mock(side_effect=[sender, None])
        
        sender_bank_id = 123
        sender_id = 1
        receiver_id = 2
        amount = 100

        sender.get_bank_account.return_value = sender_account
        receiver.get_bank_account.return_value = receiver_account

        sender_account.transfer_money.return_value = True

        self.assertFalse(self.bank_controller.transfer_money(sender_id, sender_bank_id, receiver_id, amount))

    def test_banks_accounts_id_is_none(self):
        sender_bank = MagicMock()
        receiver_bank = MagicMock()
        sender = MagicMock()
        receiver = MagicMock()
        sender_account = MagicMock()
        receiver_account = MagicMock()

        sender.get_bank_account.return_value = sender_account
        receiver.get_bank_account.return_value = receiver_account

        self.bank_controller.banks = [sender_bank, receiver_bank]
        self.bank_controller.clients = [sender, receiver]
        self.bank_controller.select_bank = Mock(side_effect=[sender_bank, sender_bank])
        self.bank_controller.select_client = Mock(side_effect=[sender, receiver])
        
        sender_bank_id = 123
        sender_id = 1
        receiver_id = 2
        amount = 100

        sender.get_bank_account.return_value = None
        receiver.get_bank_account.return_value = None

        sender_account.transfer_money.return_value = True

        self.assertFalse(self.bank_controller.transfer_money(sender_id, sender_bank_id, receiver_id, amount))

    
if __name__ == '__main__':
    unittest.main()
    