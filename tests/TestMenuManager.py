import unittest
from unittest.mock import patch
from utils.menu_manager import MenuManager


class TestMenuManager(unittest.TestCase):
    @patch('utils.console_manager.ConsoleManager.get_input')
    def test_get_dish_details(self, mock_get_input):
        mock_get_input.side_effect = ['Pizza', '20', 't']
        expected = ('Pizza', 20.0, True)
        result = MenuManager.get_dish_details()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
