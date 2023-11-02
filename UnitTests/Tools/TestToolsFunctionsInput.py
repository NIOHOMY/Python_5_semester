from io import StringIO
import unittest
from unittest.mock import patch, MagicMock, Mock, call
import builtins
from Interface.Tools.input_integer_non_negative_numbers import input_integer_non_negative_numbers
from Interface.Tools.input_float_non_negative_numbers import input_float_non_negative_numbers

"""

"""
        
class TestToolsFunctionsInput(unittest.TestCase):

    def setUp(self):
          """
          """
        
    def test_input_float_negative_numbers(self):
        # Тестирование некорректного ввода отрицательного числа
        with unittest.mock.patch('builtins.input', return_value='-5'):
            result = input_float_non_negative_numbers()
            self.assertIsNone(result)

    def test_input_float_non_numeric_characters(self):
        # Тестирование некорректного ввода буквенных символов
        with unittest.mock.patch('builtins.input', return_value='abc'):
            result = input_float_non_negative_numbers()
            self.assertIsNone(result)

    def test_input_float_positive_number(self):
        # Тестирование корректного ввода положительного числа
        with unittest.mock.patch('builtins.input', return_value='3.14'):
            result = input_float_non_negative_numbers()
            self.assertEqual(result, 3.14)

    def test_input_float_zero(self):
        # Тестирование корректного ввода нуля
        with unittest.mock.patch('builtins.input', return_value='0'):
            result = input_float_non_negative_numbers()
            self.assertEqual(result, 0)

    def test_input_integer_negative_numbers(self):
        # Тестирование некорректного ввода отрицательного числа
        with unittest.mock.patch('builtins.input', return_value='-5'):
            result = input_integer_non_negative_numbers()
            self.assertIsNone(result)

    def test_input_integer_non_numeric_characters(self):
        # Тестирование некорректного ввода буквенных символов
        with unittest.mock.patch('builtins.input', return_value='abc'):
            result = input_integer_non_negative_numbers()
            self.assertIsNone(result)

    def test_input_integer_positive_number(self):
        # Тестирование корректного ввода положительного числа
        with unittest.mock.patch('builtins.input', return_value='42'):
            result = input_integer_non_negative_numbers()
            self.assertEqual(result, 42)

    def test_input_integer_zero(self):
        # Тестирование корректного ввода нуля
        with unittest.mock.patch('builtins.input', return_value='0'):
            result = input_integer_non_negative_numbers()
            self.assertEqual(result, 0)



if __name__ == '__main__':
    unittest.main()
