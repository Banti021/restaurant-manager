import unittest
from unittest.mock import patch
from models.order import Order
from utils.order_manager import OrderManager


class TestOrderManager(unittest.TestCase):
    @patch('utils.console_manager.ConsoleManager.get_input')
    def test_get_order_details(self, mock_get_input):
        mock_get_input.side_effect = ['Adam', '100', '1,2', '1,2', 'True']
        expected = ('Adam', 100.0, ['1', '2'], ['1', '2'], True)
        result = OrderManager.get_order_details()
        self.assertEqual(result, expected)

    @patch('utils.data_loader.DataLoader.load_items')
    @patch('utils.data_loader.DataLoader.save_data')
    def test_save_new_order(self, mock_save_data, mock_load_items):
        mock_load_items.return_value = []
        order = Order(1, 'Adam', 100.0, ['1', '2'], ['1', '2'], True)
        OrderManager.save_new_order(order)
        mock_save_data.assert_called_once()
        args, kwargs = mock_save_data.call_args
        self.assertEqual(args[0], 'data/orders.json')
        self.assertIn(order, args[1])

    @patch('utils.data_loader.DataLoader.load_items')
    @patch('utils.data_loader.DataLoader.save_data')
    def test_delete_order(self, mock_save_data, mock_load_items):
        mock_load_items.return_value = [Order(1, 'Adam', 100.0, ['1', '2'], ['1', '2'], True),
                                        Order(2, 'Ewa', 50.0, ['3', '4'], ['3', '4'], False)]
        OrderManager.delete_order(1)
        mock_save_data.assert_called_once()
        args, kwargs = mock_save_data.call_args
        self.assertEqual(len(args[1]), 1)
        self.assertEqual(args[1][0].id, 2)

    @patch('utils.data_loader.DataLoader.load_items')
    @patch('utils.data_loader.DataLoader.save_data')
    def test_update_order(self, mock_save_data, mock_load_items):
        mock_load_items.return_value = [Order(1, 'Adam', 100.0, ['1', '2'], ['1', '2'], True),
                                        Order(2, 'Ewa', 50.0, ['3', '4'], ['3', '4'], False)]
        new_order = Order(1, 'Adam', 200.0, ['1', '2', '3'], ['1', '2', '3'], False)
        OrderManager.update_order(1)
        mock_save_data.assert_called_once()
        args, kwargs = mock_save_data.call_args
        self.assertEqual(len(args[1]), 2)
        self.assertEqual(args[1][0].total, 200.0)
        self.assertEqual(args[1][0].dishes, ['1', '2', '3'])
        self.assertEqual(args[1][0].drinks, ['1', '2', '3'])
        self.assertEqual(args[1][0].is_closed, False)


if __name__ == '__main__':
    unittest.main()
