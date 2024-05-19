import unittest
from unittest.mock import patch, MagicMock
from services.order_dish_service import OrderDishService


class TestOrderDishService(unittest.TestCase):

    @patch('services.order_dish_service.OrderDishRepositoryManager')
    def test_get_order_dish(self, MockOrderDishRepositoryManager):
        mock_repo_instance = MockOrderDishRepositoryManager.return_value.__enter__.return_value
        mock_repo_instance.get_order_dish.return_value = "order_dish"

        result = OrderDishService.get_order_dish(1, 1)
        self.assertEqual(result, "order_dish")
        mock_repo_instance.get_order_dish.assert_called_once_with(1, 1)

    @patch('services.order_dish_service.OrderDishRepositoryManager')
    def test_get_order_dishes(self, MockOrderDishRepositoryManager):
        mock_repo_instance = MockOrderDishRepositoryManager.return_value.__enter__.return_value
        mock_repo_instance.get_order_dishes.return_value = ["order_dish1", "order_dish2"]

        result = OrderDishService.get_order_dishes(1)
        self.assertEqual(result, ["order_dish1", "order_dish2"])
        mock_repo_instance.get_order_dishes.assert_called_once_with(1)

    @patch('services.order_dish_service.OrderDishRepositoryManager')
    def test_create_order_dish(self, MockOrderDishRepositoryManager):
        mock_repo_instance = MockOrderDishRepositoryManager.return_value.__enter__.return_value
        mock_repo_instance.create_order_dish.return_value = "created_order_dish"

        result = OrderDishService.create_order_dish(1, 1, 2)
        self.assertEqual(result, "created_order_dish")
        mock_repo_instance.create_order_dish.assert_called_once_with(1, 1, 2)

    @patch('services.order_dish_service.OrderDishRepositoryManager')
    def test_update_order_dish(self, MockOrderDishRepositoryManager):
        mock_repo_instance = MockOrderDishRepositoryManager.return_value.__enter__.return_value
        mock_repo_instance.update_order_dish.return_value = "updated_order_dish"

        result = OrderDishService.update_order_dish(1, 1, 3)
        self.assertEqual(result, "updated_order_dish")
        mock_repo_instance.update_order_dish.assert_called_once_with(1, 1, 3)

    @patch('services.order_dish_service.OrderDishRepositoryManager')
    def test_delete_order_dish(self, MockOrderDishRepositoryManager):
        mock_repo_instance = MockOrderDishRepositoryManager.return_value.__enter__.return_value
        mock_repo_instance.delete_order_dish_id.return_value = "deleted_order_dish"

        result = OrderDishService.delete_order_dish(1)
        self.assertEqual(result, "deleted_order_dish")
        mock_repo_instance.delete_order_dish_id.assert_called_once_with(1)


if __name__ == '__main__':
    unittest.main()
