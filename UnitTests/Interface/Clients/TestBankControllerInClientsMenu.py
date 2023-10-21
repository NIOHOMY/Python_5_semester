import unittest
from unittest.mock import patch, MagicMock
from Controllers.BankController import BankController
from Models.Client import Client

from ....Interface.ClientsMenu.create_client_menu import create_client_menu
from ....Interface.ClientsMenu.delete_client_menu import delete_client_menu
from ....Interface.ClientsMenu.select_client_menu import select_client_menu

"""
Метод test_create_client_menu_success проверяет случай успешного создания клиента с верными параметрами и убеждается, 
что клиент добавлен в список контроллера.

Метод test_create_client_menu_invalid_type проверяет случай, когда выбран неверный тип клиента, и убеждается, 
что выводится соответствующее сообщение об ошибке.

Метод test_create_client_menu_failure проверяет случай, когда создание клиента происходит с ошибкой, и убеждается, 
что выводится соответствующее сообщение об ошибке.

Метод test_delete_client_menu_success проверяет успешное удаление клиента из списка клиентов контроллера.

Метод test_delete_client_menu_invalid_id проверяет случай, когда введен недопустимый идентификатор клиента для удаления, 
и убеждается, что выводится соответствующее сообщение об ошибке.

Метод test_delete_client_menu_failure проверяет случай, когда удаление клиента происходит с ошибкой, и убеждается, 
что выводится соответствующее сообщение об ошибке.

Метод test_select_client_menu_success проверяет успешный выбор клиента, убеждаясь, что выбранный клиент становится текущим выбранным клиентом в контроллере.

Метод test_select_client_menu_invalid_id проверяет случай, когда введен недопустимый идентификатор клиента для выбора,
и убеждается, что выводится соответствующее сообщение об ошибке.
"""


class TestClientMenus(unittest.TestCase):

    def setUp(self):
        self.controller = BankController()

    @patch('builtins.input', side_effect=["John Doe", "1"])
    def test_create_client_menu_success(self, mock_input):
        create_client_menu(self.controller)
        self.assertEqual(len(self.controller.clients), 1)
        client = self.controller.clients[0]
        self.assertEqual(client.name, "John Doe")
        self.assertEqual(client.client_type, 1)

    @patch('builtins.input', side_effect=["John Doe", "3"])
    def test_create_client_menu_invalid_type(self, mock_input):
        with patch('builtins.print') as mock_print:
            create_client_menu(self.controller)
        self.assertEqual(mock_print.call_args[0][0], "Неверный тип клиента.")

    @patch('builtins.input', side_effect=["1"])
    def test_create_client_menu_failure(self, mock_input):
        with patch('builtins.print') as mock_print:
            create_client_menu(self.controller)
        self.assertEqual(mock_print.call_args[0][0], "Ошибка при создании клиента.")

    def test_delete_client_menu_success(self):
        client = Client("John Doe", 1)
        self.controller.clients.append(client)
        with patch('builtins.input', return_value=str(client.id)), \
                patch('builtins.print') as mock_print:
            delete_client_menu(self.controller)
        self.assertEqual(mock_print.call_args[0][0], f"Клиент '{client.name}' успешно удален.")
        self.assertEqual(len(self.controller.clients), 0)

    @patch('builtins.input', side_effect=["invalid_id"])
    def test_delete_client_menu_invalid_id(self, mock_input):
        with patch('builtins.print') as mock_print:
            delete_client_menu(self.controller)
        self.assertEqual(mock_print.call_args[0][0], "Неверный ID клиента.")

    def test_delete_client_menu_failure(self):
        with patch('builtins.print') as mock_print:
            delete_client_menu(self.controller)
        self.assertEqual(mock_print.call_args[0][0], "Ошибка при удалении клиента.")

    def test_select_client_menu_success(self):
        client = Client("John Doe", 1)
        self.controller.clients.append(client)
        with patch('builtins.input', return_value=str(client.id)), \
                patch('builtins.print'):
            select_client_menu(self.controller)
        self.assertEqual(self.controller.selected_client, client)

    @patch('builtins.input', side_effect=["invalid_id"])
    def test_select_client_menu_invalid_id(self, mock_input):
        with patch('builtins.print') as mock_print:
            select_client_menu(self.controller)
        self.assertEqual(mock_print.call_args[0][0], "Неверный ID клиента.")

if __name__ == '__main__':
    unittest.main()
