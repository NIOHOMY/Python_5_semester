import unittest
from unittest.mock import patch
from mock import Mock
from Models.Accounts.BankAccount import BankAccount
from Models.Accounts.ClientAccount import ClientAccount
from Models.Bank import Bank
from Models.Client import Client
from Models.Persons.LegalPerson import  LegalPerson
from Models.Persons.PhysicalPerson import PhysicalPerson

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.bank_account = BankAccount(Mock())

    def test_deposit_with_positive_amount_should_increase_balance(self):
        self.bank_account.deposit(100)
        self.assertEqual(self.bank_account.get_balance(), 100)

    def test_deposit_with_negative_amount_should_not_change_balance(self):
        self.bank_account.deposit(-100)
        self.assertEqual(self.bank_account.get_balance(), 0)

    def test_withdraw_with_sufficient_balance_and_positive_amount_should_decrease_balance(self):
        self.bank_account.deposit(200)
        self.bank_account.withdraw(100)
        self.assertEqual(self.bank_account.get_balance(), 100)

    def test_withdraw_with_insufficient_balance_should_not_change_balance(self):
        self.bank_account.deposit(50)
        self.bank_account.withdraw(100)
        self.assertEqual(self.bank_account.get_balance(), 50)

class TestClientAccount(unittest.TestCase):
    def setUp(self):
        self.bank = Mock()
        self.bank_account = Mock()
        self.bank.get_bank_account.return_value = self.bank_account
        self.client_account = ClientAccount(self.bank)

    def test_deposit_with_positive_amount_should_increase_client_balance_and_bank_balance(self):
        result = self.client_account.deposit(100)
        self.assertEqual(self.client_account.get_balance(), 100)
        self.bank_account.deposit.assert_called_with(100)
        self.bank.get_bank_account.assert_called_once()
        self.assertEqual(result, True)

    def test_deposit_with_negative_amount_should_not_change_balances(self):
        result = self.client_account.deposit(-100)
        self.assertEqual(self.client_account.get_balance(), 0)
        self.bank.get_bank_account.assert_not_called()
        self.assertEqual(result, False)

    def test_withdraw_with_sufficient_balance_and_positive_amount_should_decrease_client_balance_and_bank_balance(self):
        self.client_account.deposit(200)
        result = self.client_account.withdraw(100)
        self.assertEqual(self.client_account.get_balance(), 100)
        self.bank_account.withdraw.assert_called_with(100)
        self.assertEqual(result, True)

    def test_withdraw_with_insufficient_balance_should_not_change_balances(self):
        self.client_account.deposit(50)
        result = self.client_account.withdraw(100)
        self.assertEqual(self.client_account.get_balance(), 50)
        self.assertEqual(result, False)

    #@patch('Models.Accounts.BankAccount')
    def test_transfer_money_with_valid_parameters_should_withdraw_from_sender_and_deposit_to_receiver(self):
        sender_bank = Mock()
        sender = PhysicalPerson("c1") 
        receiver = PhysicalPerson("c2")
        sender_account = ClientAccount(sender_bank)
        receiver_account = ClientAccount(sender_bank)
        
        sender_bank.calculate_transfer_fee.return_value = 1
        sender_account.deposit(200)
        result = sender_account.transfer_money(sender, receiver_account, receiver, 100)
        
        self.assertEqual(sender_account.get_balance(), 100-1)
        sender_bank.collect_transfer_fee.assert_called_with(1)
        self.assertEqual(receiver_account.get_balance(), 100)
        self.assertEqual(result, True)

    def test_transfer_money_with_invalid_parameters_should_not_change_balances(self):
        sender_bank = Mock()
        sender = PhysicalPerson("c1") 
        receiver = PhysicalPerson("c2")
        sender_account = ClientAccount(sender_bank)
        receiver_account = ClientAccount(sender_bank)
        
        sender_bank.calculate_transfer_fee.return_value = 1
        sender_account.deposit(50)
        result = sender_account.transfer_money(sender, receiver_account, receiver, 100)
        
        self.assertEqual(sender_account.get_balance(), 50)
        
        self.assertEqual(receiver_account.get_balance(), 0) 
        self.assertEqual(result, False)
        

    def test_transfer_money_with_invalid_parameters_should_not_make_transfer(self):
        sender_bank = Mock()
        sender = PhysicalPerson("c1") 
        receiver = PhysicalPerson("c2")
        sender_account = ClientAccount(sender_bank)
        receiver_account = None
        
        sender_bank.calculate_transfer_fee.return_value = 1
        sender_account.deposit(500)
        result = sender_account.transfer_money(sender, receiver_account, receiver, 100)
        
        self.assertEqual(sender_account.get_balance(), 500)
        self.assertEqual(result, False)
        

    def test_transfer_money_with_valid_parameters_should_withdraw_from_legalsender_and_deposit_to_another_bank_receiver(self):
        sender_bank = Mock()
        receiver_bank = Mock()
        sender = LegalPerson("c1") 
        receiver = PhysicalPerson("c2")
        sender_account = ClientAccount(sender_bank)
        receiver_account = ClientAccount(receiver_bank)
        
        sender_bank.calculate_transfer_fee.return_value = 1
        sender_account.deposit(200)
        result = sender_account.transfer_money(sender, receiver_account, receiver, 100)
        
        self.assertEqual(sender_account.get_balance(), 100-1)
        sender_bank.collect_transfer_fee.assert_called_with(1)
        self.assertEqual(receiver_account.get_balance(), 100)
        self.assertEqual(result, True)
        
    def test_transfer_money_with_valid_parameters_should_withdraw_from_legalsender_and_deposit_to_sender_another_bank(self):
        sender_bank = Mock()
        sender_bank2 = Mock()
        sender = LegalPerson("c1")
        sender_account = ClientAccount(sender_bank)
        sender_account2 = ClientAccount(sender_bank2)
        
        sender_bank.calculate_transfer_fee.return_value = 1
        sender_account.deposit(200)
        result = sender_account.transfer_money(sender, sender_account2, sender, 100)
        
        self.assertEqual(sender_account.get_balance(), 100-1)
        sender_bank.collect_transfer_fee.assert_called_with(1)
        self.assertEqual(sender_account2.get_balance(), 100)
        self.assertEqual(result, True)

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("Test Bank")

    def test_add_client_should_add_client_to_bank(self):
        client = Mock()
        self.bank.add_client(client)
        self.assertIn(client, self.bank.get_clients())

    """
    def test_add_client_should_add_client_account_to_client(self):
        client = Mock()
        self.bank.add_client(client)
        client.add_account.assert_called_with(Mock(self.bank))
    """
    def test_add_client_should_add_client_account_to_client(self):
        client = Mock()
        self.bank.add_client(client)
        client.add_account.assert_called_once()

    def test_add_client_should_not_add_duplicate_client(self):
        client = Mock()
        self.bank.add_client(client)
        result = self.bank.add_client(client)
        self.assertFalse(result)

    def test_remove_client_should_remove_client_from_bank(self):
        client = Mock()
        self.bank.add_client(client)
        self.bank.remove_client(client)
        self.assertNotIn(client, self.bank.get_clients())

    def test_remove_client_should_delete_client_account_from_client(self):
        client = Mock()
        self.bank.add_client(client)
        self.bank.remove_client(client)
        client.delete_account.assert_called_with(self.bank)
        
    def test_remove_client_shouldnt_remove_client_from_bank(self):
        client = Mock()
        self.bank.remove_client(client)
        self.assertNotIn(client, self.bank.get_clients())

    def test_calculate_transfer_fee_should_return_correct_fee(self):
        fee = self.bank.calculate_transfer_fee(100)
        self.assertEqual(fee, 1.0)

    def test_collect_transfer_fee_should_increase_bank_funds(self):
        self.bank.collect_transfer_fee(10)
        self.assertEqual(self.bank.get_funds(), 10)

    def test_get_bank_account_should_return_own_funds_account(self):
        bank_account = self.bank.get_bank_account()
        self.assertEqual(bank_account, self.bank.own_funds)

    def test_get_name_should_return_bank_name(self):
        name = self.bank.get_name()
        self.assertEqual(name, "Test Bank")


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client('John')

    def test_add_account(self):
        bank = Mock()
        account = Mock()
        self.client.add_account(account)
        self.assertIn(account, self.client.bank_accounts)

    def test_delete_account(self):
        self.account1 = Mock()
        self.account2 = Mock()
        self.client.add_account(self.account1)
        self.client.add_account(self.account2)
        bank = Mock()
        self.account2.get_bank.return_value = bank

        result = self.client.delete_account(bank)

        self.assertNotIn(self.account2, self.client.bank_accounts)
        self.assertIn(self.account1, self.client.bank_accounts)
        self.assertEqual(result, True)

    def test_get_bank_account_existing(self):
        self.account1 = Mock()
        self.account2 = Mock()
        self.client.add_account(self.account1)
        self.client.add_account(self.account2)
        bank = Mock()
        self.account2.get_bank.return_value = bank

        result = self.client.get_bank_account(bank)

        self.assertEqual(result, self.account2)

    def test_get_bank_account_non_existing(self):
        bank = Mock()
        result = self.client.get_bank_account(bank)
        self.assertIsNone(result)

class TestLegalPerson(unittest.TestCase):
    def setUp(self):
        self.person = LegalPerson('John')

    def test_inheritance(self):
        self.assertIsInstance(self.person, Client)

class TestPhysicalPerson(unittest.TestCase):
    def setUp(self):
        self.person = PhysicalPerson('John')

    def test_inheritance(self):
        self.assertIsInstance(self.person, Client)


if __name__ == "__main__":
    unittest.main()
