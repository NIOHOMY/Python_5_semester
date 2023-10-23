import unittest
from Models.Bank import Bank
from Models.Client import Client
from Models.Persons.LegalPerson import  LegalPerson
from Models.Persons.PhysicalPerson import PhysicalPerson
from Models.Account import Account

"""
Для класса Client:

    Тест test_add_account проверяет, что метод add_account добавляет счет в массив bank_accounts.
    Тест test_delete_account проверяет, что метод delete_account удаляет счет из массива bank_accounts, соответствующий указанному банку.
    Тест test_get_bank_account проверяет, что метод get_bank_account возвращает правильный счет из массива bank_accounts для указанного банка.

Для класса LegalPerson (наследуется от Client):

    Тест test_add_account проверяет, что метод add_account добавляет счет в массив bank_accounts для юридического лица.
    Тест test_delete_account проверяет, что метод delete_account удаляет счет из массива bank_accounts для юридического лица, соответствующий указанному банку.
    Тест test_get_bank_account проверяет, что метод get_bank_account возвращает правильный счет из массива bank_accounts для указанного банка для юридического лица.

Для класса PhysicalPerson (наследуется от Client):

    Тест test_add_account проверяет, что метод add_account добавляет счет в массив bank_accounts для физического лица.
    Тест test_delete_account проверяет, что метод delete_account удаляет счет из массива bank_accounts для физического лица, соответствующий указанному банку.
    Тест test_get_bank_account проверяет, что метод get_bank_account возвращает правильный счет из массива bank_accounts для указанного банка для физического лица.

"""

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client("John Doe")
        self.bank1 = Bank("Bank 1")
        self.bank2 = Bank("Bank 2")
        self.account1 = Account(self.bank1)
        self.account2 = Account(self.bank2)
    
    def test_add_account(self):
        self.client.add_account(self.account1)
        self.assertEqual(len(self.client.bank_accounts), 1)
        
        self.client.add_account(self.account2)
        self.assertEqual(len(self.client.bank_accounts), 2)
        
    def test_delete_account(self):
        self.client.add_account(self.account1)
        self.client.add_account(self.account2)
        
        self.client.delete_account(self.bank1)
        self.assertEqual(len(self.client.bank_accounts), 1)
        
        self.client.delete_account(self.bank2)
        self.assertEqual(len(self.client.bank_accounts), 0)
        
    def test_get_bank_account(self):
        self.client.add_account(self.account1)
        self.client.add_account(self.account2)
        
        self.assertEqual(self.client.get_bank_account(self.bank1), self.account1)
        self.assertEqual(self.client.get_bank_account(self.bank2), self.account2)
        self.assertIsNone(self.client.get_bank_account(Bank("Bank 3")))
        

class TestLegalPerson(unittest.TestCase):
    def setUp(self):
        self.client = LegalPerson("Jane Smith")
        self.bank = Bank("Bank 1")
        self.account = Account(self.bank)
    
    def test_add_account(self):
        self.client.add_account(self.account)
        self.assertEqual(len(self.client.bank_accounts), 1)
        
    def test_delete_account(self):
        self.client.add_account(self.account)
        self.client.delete_account(self.bank)
        self.assertEqual(len(self.client.bank_accounts), 0)
        
    def test_get_bank_account(self):
        self.client.add_account(self.account)
        self.assertEqual(self.client.get_bank_account(self.bank), self.account)
        self.assertIsNone(self.client.get_bank_account(Bank("Bank 2")))
        

class TestPhysicalPerson(unittest.TestCase):
    def setUp(self):
        self.client = PhysicalPerson("Alice Johnson")
        self.bank = Bank("Bank 1")
        self.account = Account(self.bank)
    
    def test_add_account(self):
        self.client.add_account(self.account)
        self.assertEqual(len(self.client.bank_accounts), 1)
        
    def test_delete_account(self):
        self.client.add_account(self.account)
        self.client.delete_account(self.bank)
        self.assertEqual(len(self.client.bank_accounts), 0)
        
    def test_get_bank_account(self):
        self.client.add_account(self.account)
        self.assertEqual(self.client.get_bank_account(self.bank), self.account)
        self.assertIsNone(self.client.get_bank_account(Bank("Bank 2")))

if __name__ == "__main__":
    unittest.main()
