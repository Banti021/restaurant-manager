import unittest
from unittest.mock import patch, MagicMock
from services.order_service import OrderService


class TestOrderService(unittest.TestCase):

    @patch('services.order_service.OrderRepositoryManager')
    def test_get_all_orders(self, MockOrderRepositoryManager):
        # Mock the repository's get_all_orders method
        mock_repo = MockOrderRepositoryManager.return_value.__enter__.return_value
        mock_repo.get_all_orders.return_value = ['order1', 'order2']

        # Call the method
        result = OrderService.get_all_orders()

        # Check that the repository's method was called
        mock_repo.get_all_orders.assert_called_once()

        # Check the result
        self.assertEqual(result, ['order1', 'order2'])

    @patch('services.order_service.OrderRepositoryManager')
    def test_get_order_by_id(self, MockOrderRepositoryManager):
        # Mock the repository's get_order_by_id method
        mock_repo = MockOrderRepositoryManager.return_value.__enter__.return_value
        mock_repo.get_order_by_id.return_value = 'order1'

        # Call the method
        result = OrderService.get_order_by_id(1)

        # Check that the repository's method was called with the correct parameter
        mock_repo.get_order_by_id.assert_called_once_with(1)

        # Check the result
        self.assertEqual(result, 'order1')

    @patch('services.order_service.OrderRepositoryManager')
    def test_get_open_orders(self, MockOrderRepositoryManager):
        # Mock the repository's get_open_orders method
        mock_repo = MockOrderRepositoryManager.return_value.__enter__.return_value
        mock_repo.get_open_orders.return_value = ['open_order1', 'open_order2']

        # Call the method
        result = OrderService.get_open_orders()

        # Check that the repository's method was called
        mock_repo.get_open_orders.assert_called_once()

        # Check the result
        self.assertEqual(result, ['open_order1', 'open_order2'])

    @patch('services.order_service.OrderRepositoryManager')
    def test_get_order_by_customer(self, MockOrderRepositoryManager):
        # Mock the repository's get_order_by_customer method
        mock_repo = MockOrderRepositoryManager.return_value.__enter__.return_value
        mock_repo.get_order_by_customer.return_value = ['order1']

        # Call the method
        result = OrderService.get_order_by_customer('customer1')

        # Check that the repository's method was called with the correct parameter
        mock_repo.get_order_by_customer.assert_called_once_with('customer1')

        # Check the result
        self.assertEqual(result, ['order1'])

    @patch('services.order_service.OrderRepositoryManager')
    def test_get_order_by_date(self, MockOrderRepositoryManager):
        # Mock the repository's get_order_by_date method
        mock_repo = MockOrderRepositoryManager.return_value.__enter__.return_value
        mock_repo.get_order_by_date.return_value = ['order1']

        # Call the method
        result = OrderService.get_order_by_date('2023-05-01')

        # Check that the repository's method was called with the correct parameter
        mock_repo.get_order_by_date.assert_called_once_with('2023-05-01')

        # Check the result
        self.assertEqual(result, ['order1'])

    @patch('services.order_service.OrderRepositoryManager')
    def test_get_order_by_date_range(self, MockOrderRepositoryManager):
        # Mock the repository's get_order_by_date_range method
        mock_repo = MockOrderRepositoryManager.return_value.__enter__.return_value
        mock_repo.get_order_by_date_range.return_value = ['order1', 'order2']

        # Call the method
        result = OrderService.get_order_by_date_range('2023-05-01', '2023-05-31', 1)

        # Check that the repository's method was called with the correct parameters
        mock_repo.get_order_by_date_range.assert_called_once_with('2023-05-01', '2023-05-31', 1)

        # Check the result
        self.assertEqual(result, ['order1', 'order2'])

    @patch('services.order_service.OrderRepositoryManager')
    def test_create_order(self, MockOrderRepositoryManager):
        # Mock the repository's create_order method
        mock_repo = MockOrderRepositoryManager.return_value.__enter__.return_value
        mock_repo.create_order.return_value = 'new_order'

        # Call the method
        result = OrderService.create_order('customer1', 100.0)

        # Check that the repository's method was called with the correct parameters
        mock_repo.create_order.assert_called_once_with('customer1', 100.0)

        # Check the result
        self.assertEqual(result, 'new_order')

    @patch('services.order_service.OrderRepositoryManager')
    def test_update_order(self, MockOrderRepositoryManager):
        # Mock the repository's update_order method
        mock_repo = MockOrderRepositoryManager.return_value.__enter__.return_value
        mock_repo.update_order.return_value = 'updated_order'

        # Call the method
        result = OrderService.update_order(1, 2)

        # Check that the repository's method was called with the correct parameters
        mock_repo.update_order.assert_called_once_with(1, 2)

        # Check the result
        self.assertEqual(result, 'updated_order')

    @patch('services.order_service.OrderRepositoryManager')
    @patch('services.order_service.OrderDishService')
    @patch('services.order_service.OrderDrinkService')
    def test_delete_order(self, MockOrderDrinkService, MockOrderDishService, MockOrderRepositoryManager):
        # Mock the repository's delete_order method
        mock_repo = MockOrderRepositoryManager.return_value.__enter__.return_value
        mock_repo.delete_order.return_value = 'deleted_order'

        # Call the method
        OrderService.delete_order(1)

        # Check that the OrderDishService's delete_order_dish method was called with the correct parameter
        MockOrderDishService.delete_order_dish.assert_called_once_with(1)

        # Check that the OrderDrinkService's delete_order_drink method was called with the correct parameter
        MockOrderDrinkService.delete_order_drink.assert_called_once_with(1)

        # Check that the repository's delete_order method was called with the correct parameter
        mock_repo.delete_order.assert_called_once_with(1)


if __name__ == '__main__':
    unittest.main()
