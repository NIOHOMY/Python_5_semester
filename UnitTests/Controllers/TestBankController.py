import unittest
from Controllers.BankController import BankController
from Models.Client import Client
from Models.Account import Account
from Models.Bank import Bank
from Models.Persons.LegalPerson import LegalPerson
from Models.Persons.PhysicalPerson import PhysicalPerson


class TestBankController(unittest.TestCase):

    def setUp(self):
        self.controller = BankController()

    def test_create_bank(self):
        bank_name = "Test Bank"
        bank = self.controller.create_bank(bank_name)
        self.assertIn(bank, self.controller.banks)
        self.assertEqual(bank.name, bank_name)
        
    def test_create_bank_invalid(self):
        bank_name = None
        result = self.controller.create_bank(bank_name)
        self.assertIsNone(result)
        self.assertNotIn(None, self.controller.banks)

    def test_delete_bank(self):
        bank_name = "Test Bank"
        bank = self.controller.create_bank(bank_name)
        result = self.controller.delete_bank(bank)
        self.assertTrue(result)
        self.assertNotIn(bank, self.controller.banks)

    def test_delete_bank_non_existing(self):
        bank = Bank('ABC Bank')
        result = self.controller.delete_bank(bank)
        self.assertFalse(result)
        self.assertNotIn(bank, self.controller.banks)
        

    def test_select_bank(self):
        bank_name = "Test Bank"
        bank = self.controller.create_bank(bank_name)
        selected_bank = self.controller.select_bank(0)
        self.assertEqual(selected_bank, bank)
        
    def test_select_bank_invalid(self):
        bank_id = 100
        result = self.controller.select_bank(bank_id)
        self.assertIsNone(result)

    def test_create_client_physical_person(self):
        client_name = "John Doe"
        client_type = 1
        client = self.controller.create_client(client_name, client_type)
        self.assertIn(client, self.controller.clients)
        self.assertEqual(client.name, client_name)
        
    def test_create_client_legal_person(self):
        client_name = "John Doe"
        client_type = 2
        client = self.controller.create_client(client_name, client_type)
        self.assertIn(client, self.controller.clients)
        self.assertEqual(client.name, client_name)
        
    def test_create_client_invalid(self):
        name = None
        client_type = 3
        result = self.controller.create_client(name, client_type)
        self.assertIsNone(result)
        self.assertNotIn(None, self.controller.clients)

    def test_delete_client_existing(self):
        client_name = "John Doe"
        client_type = 1
        client = self.controller.create_client(client_name, client_type)
        result = self.controller.delete_client(client)
        self.assertTrue(result)
        self.assertNotIn(client, self.controller.clients)
        
    def test_delete_client_non_existing(self):
        client_name = "John Doe"
        client = PhysicalPerson(client_name)
        result = self.controller.delete_client(client)
        self.assertFalse(result)
        self.assertNotIn(client, self.controller.clients)

    def test_select_client_valid(self):
        client_name = "John Doe"
        client_type = 1
        client = self.controller.create_client(client_name, client_type)
        selected_client = self.controller.select_client(0)
        self.assertEqual(selected_client, client)
        
    def test_select_client_invalid(self):
        client_id = 100
        result = self.controller.select_client(client_id)
        self.assertIsNone(result)

    def test_deposit_money_valid(self):
        bank = self.controller.create_bank("test_bank_name")
        client_name = "John Doe"
        client_type = 1
        client = self.controller.create_client(client_name, client_type)
        amount = 1000
        bank.add_client(client)
        account = client.get_bank_account(bank)
        result = self.controller.deposit_money(account, amount)
        self.assertTrue(result)
        self.assertEqual(client.get_bank_account(bank).get_balance(), amount)
        
    def test_deposit_money_invalid(self):
        client_name = "John Doe"
        client = PhysicalPerson(client_name)
        bank = Bank('ABC Bank')
        bank.add_client(client)
        account = client.get_bank_account(bank)
        amount = -100
        result = self.controller.deposit_money(account, amount)
        self.assertFalse(result)
        self.assertEqual(account.get_balance(), 0)

    def test_withdraw_money_valid(self):
        bank = self.controller.create_bank("test_bank_name")
        client_name = "John Doe"
        client_type = 1
        client = self.controller.create_client(client_name, client_type)
        initial_balance = 1000
        amount_to_withdraw = 500
        bank.add_client(client)
        account = client.get_bank_account(bank)
        account.deposit(initial_balance)
        result = self.controller.withdraw_money(account, amount_to_withdraw)
        self.assertTrue(result)
        self.assertEqual(account.get_balance(), initial_balance - amount_to_withdraw)
        
    def test_withdraw_money_invalid(self):
        client_name = "John Doe"
        client = PhysicalPerson(client_name)
        bank = Bank('ABC Bank')
        bank.add_client(client)
        account = client.get_bank_account(bank)
        account.deposit(100)
        amount = -500
        result = self.controller.withdraw_money(account, amount)
        self.assertFalse(result)
        self.assertEqual(account.get_balance(), 100)

    def test_transfer_money_same_bank_for_PhysicalPerson(self):
        sender_bank_name = "Test Bank 1"
        receiver_bank_name = "Test Bank 2"

        sender_bank = self.controller.create_bank(sender_bank_name)
        receiver_bank = self.controller.create_bank(receiver_bank_name)

        sender_name = "John Doe"
        client1 = self.controller.create_client(sender_name, 1)
        sender_bank.add_client(client1)
        sender_account = client1.get_bank_account(sender_bank)
        sender_amount = 1000
        sender_account.deposit(sender_amount)

        receiver_name = "Jane Smith"
        client2 = self.controller.create_client(receiver_name, 1)
        receiver_bank.add_client(client2)

        amount_to_transfer = 500

        # Проверяем, что нельзя перевести деньги от клиента, не зарегистрированного в банке отправителя
        result = self.controller.transfer_money(self.controller.get_client_id(client1), self.controller.get_bank_id(receiver_bank), self.controller.get_client_id(client2), amount_to_transfer, self.controller.get_bank_id(receiver_bank))
        self.assertFalse(result)

        # Проверяем, что нельзя перевести деньги клиенту, не зарегистрированному в банке получателя
        result = self.controller.transfer_money(self.controller.get_client_id(client1), self.controller.get_bank_id(sender_bank), self.controller.get_client_id(client2), amount_to_transfer, self.controller.get_bank_id(sender_bank))
        self.assertFalse(result)
        
        # Проверяем, что нельзя успешно перевести деньги между физическими клиентами в разных банках
        result = self.controller.transfer_money(self.controller.get_client_id(client1), self.controller.get_bank_id(sender_bank), self.controller.get_client_id(client2), amount_to_transfer, self.controller.get_bank_id(receiver_bank))
        self.assertFalse(result)

        sender_bank.add_client(client2)
        receiver_account = client2.get_bank_account(sender_bank)
        # Проверяем, что можно успешно перевести деньги между клиентами в одном банке
        result = self.controller.transfer_money(self.controller.get_client_id(client1), self.controller.get_bank_id(sender_bank), self.controller.get_client_id(client2), amount_to_transfer, self.controller.get_bank_id(sender_bank))
        self.assertTrue(result)
        self.assertEqual(sender_account.get_balance(), sender_amount - amount_to_transfer - (sender_bank.calculate_transfer_fee(amount_to_transfer)))
        self.assertEqual(receiver_account.get_balance(), amount_to_transfer)
        
    def test_transfer_money_same_bank_for_LegalPerson(self):
        sender_bank_name = "Test Bank 1"
        receiver_bank_name = "Test Bank 2"

        sender_bank = self.controller.create_bank(sender_bank_name)
        receiver_bank = self.controller.create_bank(receiver_bank_name)

        sender_name = "John Doe"
        client1 = self.controller.create_client(sender_name, 2)
        sender_bank.add_client(client1)
        sender_account = client1.get_bank_account(sender_bank)
        sender_amount = 10000
        sender_account.deposit(sender_amount)

        receiver_name = "Jane Smith"
        client2 = self.controller.create_client(receiver_name, 1)
        receiver_bank.add_client(client2)

        amount_to_transfer = 500

        # Проверяем, что нельзя перевести деньги от клиента, не зарегистрированного в банке отправителя
        result = self.controller.transfer_money(self.controller.get_client_id(client1), self.controller.get_bank_id(receiver_bank), self.controller.get_client_id(client2), amount_to_transfer, self.controller.get_bank_id(receiver_bank))
        self.assertFalse(result)

        # Проверяем, что нельзя перевести деньги клиенту, не зарегистрированному в банке получателя
        result = self.controller.transfer_money(self.controller.get_client_id(client1), self.controller.get_bank_id(sender_bank), self.controller.get_client_id(client2), amount_to_transfer, self.controller.get_bank_id(sender_bank))
        self.assertFalse(result)
        
        receiver_account = client2.get_bank_account(receiver_bank)
        # Проверяем, что можно успешно перевести деньги между юридическими клиентами в разных банках
        result = self.controller.transfer_money(self.controller.get_client_id(client1), self.controller.get_bank_id(sender_bank), self.controller.get_client_id(client2), amount_to_transfer, self.controller.get_bank_id(receiver_bank))
        self.assertTrue(result)
        self.assertEqual(sender_account.get_balance(), sender_amount - amount_to_transfer - (sender_bank.calculate_transfer_fee(amount_to_transfer)))
        self.assertEqual(receiver_account.get_balance(), amount_to_transfer)

        sender_amount = sender_amount - amount_to_transfer - (sender_bank.calculate_transfer_fee(amount_to_transfer))
        sender_bank.add_client(client2)
        receiver_account = client2.get_bank_account(sender_bank)
        # Проверяем, что можно успешно перевести деньги между клиентами в одном банке
        result = self.controller.transfer_money(self.controller.get_client_id(client1), self.controller.get_bank_id(sender_bank), self.controller.get_client_id(client2), amount_to_transfer, self.controller.get_bank_id(sender_bank))
        self.assertTrue(result)
        self.assertEqual(sender_account.get_balance(), sender_amount - amount_to_transfer - (sender_bank.calculate_transfer_fee(amount_to_transfer)))
        self.assertEqual(receiver_account.get_balance(), amount_to_transfer)
  
        

if __name__ == '__main__':
    unittest.main()
    