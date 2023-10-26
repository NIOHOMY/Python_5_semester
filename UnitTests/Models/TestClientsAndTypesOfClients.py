import unittest
from Models.Bank import Bank
from Models.Client import Client
from Models.Persons.LegalPerson import  LegalPerson
from Models.Persons.PhysicalPerson import PhysicalPerson
from Models.Account import Account

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank('ABC Bank')

    def test_add_client(self):
        client = Client('John')
        result = self.bank.add_client(client)
        self.assertTrue(result)
        self.assertIn(client, self.bank.get_clients())

    def test_add_existing_client(self):
        client = Client('John')
        self.bank.add_client(client)
        result = self.bank.add_client(client)
        self.assertFalse(result)

    def test_remove_client(self):
        client = Client('John')
        self.bank.add_client(client)
        self.bank.remove_client(client)
        self.assertNotIn(client, self.bank.get_clients())

    def test_transfer_money_valid(self):
        sender_bank = Bank('Sender Bank')
        receiver_bank = Bank('Receiver Bank')
        sender = LegalPerson('John')
        receiver = LegalPerson('Jane')
        
        sender_bank.add_client(sender)
        receiver_bank.add_client(receiver)
        sender_account = sender.get_bank_account(sender_bank)
        receiver_account = receiver.get_bank_account(receiver_bank)
        sender_account.deposit(1000)
        result = sender_bank.transfer_money(sender, receiver_bank, receiver, 500)
        self.assertTrue(result)
        self.assertEqual(sender_account.get_balance(), 500-sender_bank.calculate_transfer_fee(500))
        self.assertEqual(receiver_account.get_balance(), 500)

    def test_transfer_money_insufficient_funds(self):
        sender_bank = Bank('Sender Bank')
        receiver_bank = Bank('Receiver Bank')
        sender = LegalPerson('John')
        receiver = LegalPerson('Jane')
        sender_account = Account(sender_bank)
        receiver_account = Account(receiver_bank)
        sender.add_account(sender_account)
        receiver.add_account(receiver_account)
        sender_account.deposit(100)
        result = self.bank.transfer_money(sender, receiver_bank, receiver, 500)
        self.assertFalse(result)
        self.assertEqual(sender_account.get_balance(), 100)
        self.assertEqual(receiver_account.get_balance(), 0)

    def test_transfer_money_invalid_sender(self):
        sender_bank = Bank('Sender Bank')
        receiver_bank = Bank('Receiver Bank')
        sender = PhysicalPerson('John')
        receiver = LegalPerson('Jane')
        sender_account = Account(sender_bank)
        receiver_account = Account(receiver_bank)
        sender.add_account(sender_account)
        receiver.add_account(receiver_account)
        sender_account.deposit(1000)
        result = self.bank.transfer_money(sender, receiver_bank, receiver, 500)
        self.assertFalse(result)
        self.assertEqual(sender_account.get_balance(), 1000)
        self.assertEqual(receiver_account.get_balance(), 0)

    def test_calculate_transfer_fee(self):
        amount = 1000
        expected_fee = 0.01 * amount
        result = self.bank.calculate_transfer_fee(amount)
        self.assertEqual(result, expected_fee)

    def test_collect_transfer_fee(self):
        fee = 10
        self.bank.collect_transfer_fee(fee)
        self.assertEqual(self.bank.get_funds(), fee)

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.bank = Bank('ABC Bank')
        self.account = Account(self.bank)

    def test_deposit_valid(self):
        amount = 1000
        result = self.account.deposit(amount)
        self.assertTrue(result)
        self.assertEqual(self.account.get_balance(), amount)
        self.assertEqual(self.bank.get_funds(), amount)

    def test_deposit_invalid_amount(self):
        amount = -100
        result = self.account.deposit(amount)
        self.assertFalse(result)
        self.assertEqual(self.account.get_balance(), 0)
        self.assertEqual(self.bank.get_funds(), 0)

    def test_withdraw_valid(self):
        self.account.deposit(1000)
        amount = 500
        result = self.account.withdraw(amount)
        self.assertTrue(result)
        self.assertEqual(self.account.get_balance(), 500)
        self.assertEqual(self.bank.get_funds(), 500)

    def test_withdraw_insufficient_funds(self):
        self.account.deposit(100)
        amount = 500
        result = self.account.withdraw(amount)
        self.assertFalse(result)
        self.assertEqual(self.account.get_balance(), 100)
        self.assertEqual(self.bank.get_funds(), 100)

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client('John')
        self.bank = Bank('ABC Bank')
        self.account = Account(self.bank)

    def test_add_account(self):
        self.client.add_account(self.account)
        self.assertIn(self.account, self.client.bank_accounts)

    def test_delete_account(self):
        self.client.add_account(self.account)
        self.client.delete_account(self.bank)
        self.assertNotIn(self.account, self.client.bank_accounts)

    def test_get_bank_account_existing(self):
        self.client.add_account(self.account)
        result = self.client.get_bank_account(self.bank)
        self.assertEqual(result, self.account)

    def test_get_bank_account_non_existing(self):
        result = self.client.get_bank_account(self.bank)
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

if __name__ == '__main__':
    unittest.main()

if __name__ == "__main__":
    unittest.main()
