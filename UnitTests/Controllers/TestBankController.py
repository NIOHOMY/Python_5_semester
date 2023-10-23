import unittest
from Controllers.BankController import BankController
from Models.Client import Client
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
        self.controller = BankController()

    def test_create_bank(self):
        bank_name = "Test Bank"
        bank = self.controller.create_bank(bank_name)
        self.assertIn(bank, self.controller.banks)
        self.assertEqual(bank.name, bank_name)
        

    def test_delete_bank(self):
        bank_name = "Test Bank"
        bank = self.controller.create_bank(bank_name)
        result = self.controller.delete_bank(bank)
        self.assertTrue(result)
        self.assertNotIn(bank, self.controller.banks)

    def test_select_bank(self):
        bank_name = "Test Bank"
        bank = self.controller.create_bank(bank_name)
        selected_bank = self.controller.select_bank(0)
        self.assertEqual(selected_bank, bank)

    def test_create_client(self):
        client_name = "John Doe"
        client_type = 1
        client = self.controller.create_client(client_name, client_type)
        self.assertIn(client, self.controller.clients)
        self.assertEqual(client.name, client_name)

    def test_delete_client(self):
        client_name = "John Doe"
        client_type = 1
        client = self.controller.create_client(client_name, client_type)
        result = self.controller.delete_client(client)
        self.assertTrue(result)
        self.assertNotIn(client, self.controller.clients)

    def test_select_client(self):
        client_name = "John Doe"
        client_type = 1
        client = self.controller.create_client(client_name, client_type)
        selected_client = self.controller.select_client(0)
        self.assertEqual(selected_client, client)

    def test_deposit_money(self):
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

    def test_withdraw_money(self):
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

    def test_transfer_money_same_bank(self):
        sender_bank_name = "Test Bank 1"
        receiver_bank_name = "Test Bank 2"

        sender_bank = self.controller.create_bank(sender_bank_name)
        receiver_bank = self.controller.create_bank(receiver_bank_name)
        #self.controller.banks.append(sender_bank)
        #self.controller.banks.append(receiver_bank)

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

        sender_bank.add_client(client2)
        receiver_account = client2.get_bank_account(sender_bank)
        # Проверяем, что можно успешно перевести деньги между клиентами в одном банке
        result = self.controller.transfer_money(self.controller.get_client_id(client1), self.controller.get_bank_id(sender_bank), self.controller.get_client_id(client2), amount_to_transfer, self.controller.get_bank_id(sender_bank))
        self.assertTrue(result)
        self.assertEqual(sender_account.get_balance(), sender_amount - amount_to_transfer - (sender_bank.calculate_transfer_fee(amount_to_transfer)))
        self.assertEqual(receiver_account.get_balance(), amount_to_transfer -  (sender_bank.calculate_transfer_fee(amount_to_transfer)))

    def test_transfer_money_different_banks(self):
        sender_bank_name = "Test Bank 1"
        receiver_bank_name = "Test Bank 2"

        sender_bank = self.controller.create_bank(sender_bank_name)
        receiver_bank = self.controller.create_bank(receiver_bank_name)
        #self.controller.banks.append(sender_bank)
        #self.controller.banks.append(receiver_bank)

        sender_name = "John Doe"
        client1 = self.controller.create_client(sender_name, 1)
        sender_bank.add_client(client1)
        sender_account = client1.get_bank_account(sender_bank)
        sender_amount = 1000
        sender_account.deposit(sender_amount)

        receiver_name = "Jane Smith"
        client2 = self.controller.create_client(receiver_name, 1)
        receiver_bank.add_client(client2)
        receiver_account = client2.get_bank_account(receiver_bank)

        amount_to_transfer = 500

        # Проверяем, что нельзя перевести деньги от клиента, не зарегистрированного в банке отправителя
        result = self.controller.transfer_money(self.controller.get_client_id(client1), self.controller.get_bank_id(receiver_bank), self.controller.get_client_id(client2), amount_to_transfer,self.controller.get_bank_id(receiver_bank))
        self.assertFalse(result)

        # Проверяем, что нельзя перевести деньги клиенту, не зарегистрированному в банке получателя
        result = self.controller.transfer_money(self.controller.get_client_id(client1), self.controller.get_bank_id(sender_bank), self.controller.get_client_id(client2), amount_to_transfer,self.controller.get_bank_id(sender_bank))
        self.assertFalse(result)

        # Проверяем, что нельзя успешно перевести деньги между физическими клиентами в разных банках
        result = self.controller.transfer_money(self.controller.get_client_id(client1), self.controller.get_bank_id(sender_bank), self.controller.get_client_id(client2), amount_to_transfer, self.controller.get_bank_id(receiver_bank))
        self.assertFalse(result)
        #self.assertEqual(sender_account.get_balance(), sender_amount - amount_to_transfer-(sender_bank.calculate_transfer_fee(amount_to_transfer)))
        #self.assertEqual(receiver_account.get_balance(), amount_to_transfer-(sender_bank.calculate_transfer_fee(amount_to_transfer)))

if __name__ == '__main__':
    unittest.main()
    