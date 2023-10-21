import unittest
from Controllers.BankController import BankController
from ...Models.Client import Client
from Models.Account import Account
from Models.Bank import Bank
from Models.Persons.LegalPerson import LegalPerson
from Models.Persons.PhysicalPerson import PhysicalPerson


"""
Первый тест test_create_bank проверяет, что при создании банка через метод create_bank он корректно добавляется в список banks, 
его имя соответствует заданному и возвращается созданный объект Bank.

Второй тест test_delete_bank проверяет, что при удалении банка через метод delete_bank он корректно удаляется из списка banks, 
а в случае удаления несуществующего банка метод возвращает False.

Третий тест test_select_bank проверяет, что при выборе банка по ID через метод select_bank, он возвращается корректно для существующего банка, 
а для несуществующего возвращается None.

Четвертый тест test_create_client проверяет, что при создании клиента через метод create_client он корректно добавляется в список clients, 
его имя соответствует заданному и возвращается созданный объект Client. Также тест проверяет на создание клиента с некорректным типом, 
в таком случае метод должен возвращать None.

Пятый тест test_delete_client проверяет, что при удалении клиента через метод delete_client он корректно удаляется из списка clients, 
а в случае удаления несуществующего клиента метод возвращает False.

Шестой тест test_select_client проверяет, что при выборе клиента по ID через метод select_client, он возвращается корректно для существующего клиента, 
а для несуществующего возвращается None.

Седьмой тест test_deposit_money проверяет, что при внесении денег на счет клиента через метод deposit_money баланс счета изменяется корректно и 
метод возвращает True. В случае попытки внесения денег на несуществующий счет метод должен возвращать False.

Восьмой тест test_withdraw_money проверяет, что при снятии денег со счета клиента через метод withdraw_money баланс счета изменяется корректно и 
метод возвращает True. В случае попытки снятия денег со несуществующего счета метод должен возвращать False.

Девятый тест test_transfer_money проверяет, что при переводе денег между счетами клиентов через метод transfer_money балансы счетов изменяются корректно. 
Тест проверяет три сценария: перевод между счетами в рамках одного банка, между счетами в разных банках и перевод к несуществующему клиенту или банку, 
в таких случаях метод должен возвращать False.
"""

class TestBankController(unittest.TestCase):
    
    def setUp(self):
        self.bank_controller = BankController()
        
    def test_create_bank(self):
        bank_name = "ABC Bank"
        bank = self.bank_controller.create_bank(bank_name)
        banks = self.bank_controller.banks
        
        self.assertEqual(len(banks), 1)
        self.assertIn(bank, banks)
        self.assertEqual(bank.name, bank_name)
        
    def test_delete_bank(self):
        bank_name = "ABC Bank"
        bank = self.bank_controller.create_bank(bank_name)
        banks = self.bank_controller.banks
        
        result = self.bank_controller.delete_bank(bank)
        
        self.assertTrue(result)
        self.assertNotIn(bank, banks)
        
        # Deleting non-existent bank should return False
        result = self.bank_controller.delete_bank(bank)
        self.assertFalse(result)
        
    def test_select_bank(self):
        bank_name = "ABC Bank"
        bank = self.bank_controller.create_bank(bank_name)
        
        selected_bank = self.bank_controller.select_bank(0)
        self.assertEqual(selected_bank, bank)
        
        selected_bank = self.bank_controller.select_bank(1)
        self.assertIsNone(selected_bank)
        
    def test_create_client(self):
        client_name = "John Doe"
        client_type = 1 # PhysicalPerson
        client = self.bank_controller.create_client(client_name, client_type)
        clients = self.bank_controller.clients
        
        self.assertEqual(len(clients), 1)
        self.assertIn(client, clients)
        self.assertEqual(client.name, client_name)
        
        # Creating invalid client type should return None
        client_type = 3
        client = self.bank_controller.create_client(client_name, client_type)
        self.assertIsNone(client)
        
    def test_delete_client(self):
        client_name = "John Doe"
        client_type = 1 # PhysicalPerson
        client = self.bank_controller.create_client(client_name, client_type)
        clients = self.bank_controller.clients
        
        result = self.bank_controller.delete_client(client)
        
        self.assertTrue(result)
        self.assertNotIn(client, clients)
        
        # Deleting non-existent client should return False
        result = self.bank_controller.delete_client(client)
        self.assertFalse(result)
        
    def test_select_client(self):
        client_name = "John Doe"
        client_type = 1 # PhysicalPerson
        client = self.bank_controller.create_client(client_name, client_type)
        
        selected_client = self.bank_controller.select_client(0)
        self.assertEqual(selected_client, client)
        
        selected_client = self.bank_controller.select_client(1)
        self.assertIsNone(selected_client)
        
    def test_deposit_money(self):
        client_name = "John Doe"
        client_type = 1 # PhysicalPerson
        client = self.bank_controller.create_client(client_name, client_type)
        account = client.account
        initial_balance = account.balance
        
        deposit_amount = 100
        result = self.bank_controller.deposit_money(0, deposit_amount)
        
        new_balance = account.balance
        self.assertTrue(result)
        self.assertEqual(new_balance, initial_balance + deposit_amount)
        
        # Depositing into non-existent client should return False
        result = self.bank_controller.deposit_money(1, deposit_amount)
        self.assertFalse(result)
        
    def test_withdraw_money(self):
        client_name = "John Doe"
        client_type = 1 # PhysicalPerson
        client = self.bank_controller.create_client(client_name, client_type)
        account = client.account
        
        withdraw_amount = 50
        result = self.bank_controller.withdraw_money(0, withdraw_amount)
        
        new_balance = account.balance
        self.assertTrue(result)
        self.assertEqual(new_balance, 50)
        
        # Withdrawing from non-existent client should return False
        result = self.bank_controller.withdraw_money(1, withdraw_amount)
        self.assertFalse(result)
        
    def test_transfer_money(self):
        sender_bank_name = "ABC Bank"
        sender_bank = self.bank_controller.create_bank(sender_bank_name)
        sender_name = "John Doe"
        sender_type = 1 # PhysicalPerson
        sender = self.bank_controller.create_client(sender_name, sender_type)
        sender.account.deposit(100) # initial balance
        receiver_bank_name = "XYZ Bank"
        receiver_bank = self.bank_controller.create_bank(receiver_bank_name)
        receiver_name = "Jane Doe"
        receiver_type = 1 # PhysicalPerson
        receiver = self.bank_controller.create_client(receiver_name, receiver_type)
        
        # Case 1: Same bank transfer
        result = self.bank_controller.transfer_money(0, 0, 1, 50)
        self.assertTrue(result)
        self.assertEqual(sender.account.balance, 50)
        self.assertEqual(receiver.account.balance, 50)
        
        # Case 2: Inter-bank transfer
        result = self.bank_controller.transfer_money(0, 0, 2, 30, receiver_bank_id=1)
        self.assertTrue(result)
        self.assertEqual(sender.account.balance, 20)
        self.assertEqual(receiver.account.balance, 80)
        
        # Case 3: Invalid sender bank or client
        result = self.bank_controller.transfer_money(1, 0, 1, 50)
        self.assertFalse(result)
        
        # Case 4: Invalid receiver bank or client
        result = self.bank_controller.transfer_money(0, 0, 3, 50)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
