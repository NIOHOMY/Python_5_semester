import unittest
from unittest.mock import mock_open, patch, call
from unittest import mock
import io
import tempfile
import os
from collections import Counter
import lab3
from io import StringIO

class TestLab3(unittest.TestCase):

    def test_read_existing_file(self):
        # Test reading a file that exists
        with patch('builtins.open', mock_open(read_data="Hello, world!")) as mock_file:
            data = lab3.read_file("test.txt")
            mock_file.assert_called_once_with("test.txt", 'r')
            self.assertEqual(data, "Hello, world!")
        print("-Test read_file passed")
        """
        with patch('builtins.open', mock_open(read_data="")) as mock_file:
            data = lab3.read_file("test.txt")
            mock_file.assert_called_once_with("test.txt", 'r')
            self.assertEqual(data, "")
        print("-Test empty file read_file passed")
        """
    def test_read_nonexistent_file(self):
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Test reading a file that does not exist
            with patch('builtins.open', side_effect=OSError):
                with self.assertRaises(Exception):
                    try:
                        lab3.read_file(os.path.join(temp_dir, "nonexistent.txt"))
                    except OSError:
                        pass
                    else:
                        self.fail("No exception raised")

        print("- Test nonexistent read_file passed")

    def test_compute_statistics_with_empty_data(self):
        # Test with empty data
        data = ""
        result = lab3.compute_statistics(data)
        expected = {"most_frequent_word": "", "word_count": 0, "character_count": 0}
        self.assertEqual(result, expected)
        print("-Test compute_statistics with empty data passed")
    
    def test_compute_statistics_with_one_word(self):
        # Test with data containing only one word
        data = "hello"
        result = lab3.compute_statistics(data)
        expected = {"most_frequent_word": "hello", "word_count": 1, "character_count": 5}
        self.assertEqual(result, expected)
        print("-Test compute_statistics with one word passed")
        
    def test_compute_statistics_with_multiple_words(self):
        # Test with data containing multiple words
        data = "world Hello hello"
        result = lab3.compute_statistics(data)
        expected = {"most_frequent_word": "hello", "word_count": 3, "character_count": 17}
        self.assertEqual(result, expected)
        print("-Test compute_statistics with multiple different words passed")
    
    def test_compute_statistics_with_preposition(self):
        # Test with data containing preposition
        data = "hello o world!"
        result = lab3.compute_statistics(data)
        expected = {"most_frequent_word": "hello", "word_count": 2, "character_count": 14}
        self.assertEqual(result, expected)
        print("-Test compute_statistics with punctuation passed")

    def test_compute_statistics_with_non_alphanumeric_characters(self):
        # Test with data containing non-alphanumeric characters
        data = "@world hello #hello"
        result = lab3.compute_statistics(data)
        expected = {"most_frequent_word": "hello", "word_count": 3, "character_count": 19}
        self.assertEqual(result, expected)
        print("-Test compute_statistics with non-alphanumeric characters passed")

    def test_compute_statistics_with_only_non_alphanumeric_characters(self):
        # Test with data containing only non-alphanumeric characters
        data = "@#&^%$"
        result = lab3.compute_statistics(data)
        expected = {"most_frequent_word": "", "word_count": 0, "character_count": 6}
        self.assertEqual(result, expected)
        print("-Test compute_statistics with only non-alphanumeric characters passed")
    
    def test_compute_statistics_with_non_ascii_characters(self):
        # Test with data containing non-ascii characters
        data = "你好,世界"
        result = lab3.compute_statistics(data)
        expected = {"most_frequent_word": "你好", "word_count": 2, "character_count": 5}
        self.assertEqual(result, expected)
        print("-Test compute_statistics with non-ascii characters passed")

    def test_main_no_filename_provided(self):
        print("Test 3 test_main:")
        
        # Test case when no filename is provided as argument
        with patch('sys.argv', ['lab3.py']), \
            patch('builtins.print') as mock_print, \
            patch('sys.exit') as mock_exit:
            lab3.main()

            mock_print.assert_called_with("Usage: python lab3.py <filename>")
            mock_exit.assert_called_with(1)
        print("- Test no argv 1 passed")
        
    def test_main_with_filename_console_output(self):
        result = {"most_frequent_word": "this", "word_count": 4, "character_count": 20}
        
        with patch('sys.argv', ['lab3.py', 'test.txt']), \
            patch('builtins.open', mock_open(read_data="this is a test file.")) as mock_open_func, \
            patch('builtins.print') as mock_print:
            mock_file = mock_open_func.return_value
            lab3.main()

            mock_print.assert_any_call("Most frequent word:", result["most_frequent_word"])
            mock_print.assert_any_call("Number of words:", result["word_count"])
            mock_print.assert_any_call("Number of characters:", result["character_count"])
            
        print("- Test console_output passed")
            
    def test_main_with_filename_file_write(self):
    
        result = {"most_frequent_word": "this", "word_count": 4, "character_count": 20}
        
        with patch('sys.argv', ['lab3.py', 'test.txt']), \
            patch('builtins.open', mock_open(read_data="this is a test file.")) as mock_open_func, \
            patch('builtins.print') as mock_print:
            mock_file = mock_open_func.return_value
            lab3.main()
            
            expected_calls = [
                call('Most frequent word: this\n'),
                call('Number of words: 4\n'),
                call('Number of characters: 20\n')
            ]
            
            mock_file.write.assert_has_calls(expected_calls)

            # Verify that only three lines were written
            mock_file.seek(0)
            assert mock_file.write.call_count == 3
            
            
        
        print("- Test file_contents passed")

if __name__ == '__main__':
    unittest.main()
