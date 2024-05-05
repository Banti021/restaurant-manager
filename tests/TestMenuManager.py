import unittest
from unittest.mock import patch
from models.dish import Dish
from models.drink import Drink
from utils.menu_manager import MenuManager


class TestMenuManager(unittest.TestCase):
    @patch('utils.console_manager.ConsoleManager.get_input')
    def test_get_dish_details(self, mock_get_input):
        mock_get_input.side_effect = ['Pizza', '20', 't']
        expected = ('Pizza', 20.0, True)
        result = MenuManager.get_dish_details()
        self.assertEqual(result, expected)

    @patch('utils.console_manager.ConsoleManager.get_input')
    def test_get_drink_details(self, mock_get_input):
        mock_get_input.side_effect = ['Cola', '5']
        expected = ('Cola', 5.0)
        result = MenuManager.get_drink_details()
        self.assertEqual(result, expected)

    @patch('utils.data_loader.DataLoader.load_items')
    @patch('utils.data_loader.DataLoader.save_data')
    def test_save_new_dish(self, mock_save_data, mock_load_items):
        mock_load_items.return_value = []
        dish = Dish(1, 'Pizza', 20.0, True)
        MenuManager.save_new_dish(dish)
        mock_save_data.assert_called_once()
        args, kwargs = mock_save_data.call_args
        self.assertEqual(args[0], 'data/dishes.json')
        self.assertIn(dish, args[1])

    @patch('utils.data_loader.DataLoader.load_items')
    @patch('utils.data_loader.DataLoader.save_data')
    def test_save_new_drink(self, mock_save_data, mock_load_items):
        mock_load_items.return_value = []
        drink = Drink(1, 'Cola', 5.0)
        MenuManager.save_new_drink(drink)
        mock_save_data.assert_called_once()
        args, kwargs = mock_save_data.call_args
        self.assertEqual(args[0], 'data/drinks.json')
        self.assertIn(drink, args[1])

    @patch('utils.data_loader.DataLoader.load_items')
    @patch('utils.data_loader.DataLoader.save_data')
    def test_delete_dish(self, mock_save_data, mock_load_items):
        mock_load_items.return_value = [Dish(1, 'Pizza', 20.0, True), Dish(2, 'Salad', 10.0, False)]
        MenuManager.delete_dish(1)
        mock_save_data.assert_called_once()
        args, kwargs = mock_save_data.call_args
        self.assertEqual(len(args[1]), 1)
        self.assertEqual(args[1][0].id, 2)

    @patch('utils.data_loader.DataLoader.load_items')
    @patch('utils.data_loader.DataLoader.save_data')
    def test_delete_drink(self, mock_save_data, mock_load_items):
        mock_load_items.return_value = [Drink(1, 'Cola', 5.0), Drink(2, 'Water', 2.0)]
        MenuManager.delete_drink(1)
        mock_save_data.assert_called_once()
        args, kwargs = mock_save_data.call_args
        self.assertEqual(len(args[1]), 1)
        self.assertEqual(args[1][0].id, 2)

    @patch('utils.data_loader.DataLoader.load_items')
    @patch('utils.data_loader.DataLoader.save_data')
    def test_update_dish(self, mock_save_data, mock_load_items):
        mock_load_items.return_value = [Dish(1, 'Pizza', 20.0, True), Dish(2, 'Salad', 10.0, False)]
        new_dish = Dish(1, 'Pasta', 25.0, False)
        MenuManager.update_dish(1, new_dish)
        mock_save_data.assert_called_once()
        args, kwargs = mock_save_data.call_args
        self.assertEqual(len(args[1]), 2)
        self.assertEqual(args[1][0].name, 'Pasta')
        self.assertEqual(args[1][0].price, 25.0)
        self.assertEqual(args[1][0].is_dish_of_the_day, False)

    @patch('utils.data_loader.DataLoader.load_items')
    @patch('utils.data_loader.DataLoader.save_data')
    def test_update_drink(self, mock_save_data, mock_load_items):
        mock_load_items.return_value = [Drink(1, 'Cola', 5.0), Drink(2, 'Water', 2.0)]
        new_drink = Drink(1, 'Fanta', 6.0)
        MenuManager.update_drink(1, new_drink)
        mock_save_data.assert_called_once()
        args, kwargs = mock_save_data.call_args
        self.assertEqual(len(args[1]), 2)
        self.assertEqual(args[1][0].name, 'Fanta')
        self.assertEqual(args[1][0].price, 6.0)

    @patch('utils.data_loader.DataLoader.load_items')
    def test_is_dish_of_the_day(self, mock_load_items):
        self.assertTrue(MenuManager.is_dish_of_the_day('t'))
        self.assertFalse(MenuManager.is_dish_of_the_day('n'))


if __name__ == '__main__':
    unittest.main()
