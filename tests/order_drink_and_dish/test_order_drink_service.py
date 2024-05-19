import unittest
from unittest.mock import patch, MagicMock
from services.order_drink_service import OrderDrinkService


class TestOrderDrinkService(unittest.TestCase):

    @patch('services.order_drink_service.OrderDrinkRepositoryManager')
    def test_get_order_drink(self, MockOrderDrinkRepositoryManager):
        mock_repo_instance = MockOrderDrinkRepositoryManager.return_value.__enter__.return_value
        mock_repo_instance.get_order_drink.return_value = "order_drink"

        result = OrderDrinkService.get_order_drink(1, 1)
        self.assertEqual(result, "order_drink")
        mock_repo_instance.get_order_drink.assert_called_once_with(1, 1)

    @patch('services.order_drink_service.OrderDrinkRepositoryManager')
    def test_get_order_drinks(self, MockOrderDrinkRepositoryManager):
        mock_repo_instance = MockOrderDrinkRepositoryManager.return_value.__enter__.return_value
        mock_repo_instance.get_order_drinks.return_value = ["order_drink1", "order_drink2"]

        result = OrderDrinkService.get_order_drinks(1)
        self.assertEqual(result, ["order_drink1", "order_drink2"])
        mock_repo_instance.get_order_drinks.assert_called_once_with(1)

    @patch('services.order_drink_service.OrderDrinkRepositoryManager')
    def test_get_order_drink_quantity(self, MockOrderDrinkRepositoryManager):
        mock_repo_instance = MockOrderDrinkRepositoryManager.return_value.__enter__.return_value
        mock_repo_instance.get_order_drink_quantity.return_value = 5

        result = OrderDrinkService.get_order_drink_quantity(1, 1)
        self.assertEqual(result, 5)
        mock_repo_instance.get_order_drink_quantity.assert_called_once_with(1, 1)

    @patch('services.order_drink_service.OrderDrinkRepositoryManager')
    def test_create_order_drink(self, MockOrderDrinkRepositoryManager):
        mock_repo_instance = MockOrderDrinkRepositoryManager.return_value.__enter__.return_value
        mock_repo_instance.create_order_drink.return_value = "created_order_drink"

        result = OrderDrinkService.create_order_drink(1, 1, 2)
        self.assertEqual(result, "created_order_drink")
        mock_repo_instance.create_order_drink.assert_called_once_with(1, 1, 2)

    @patch('services.order_drink_service.OrderDrinkRepositoryManager')
    def test_update_order_drink(self, MockOrderDrinkRepositoryManager):
        mock_repo_instance = MockOrderDrinkRepositoryManager.return_value.__enter__.return_value
        mock_repo_instance.update_order_drink.return_value = "updated_order_drink"

        result = OrderDrinkService.update_order_drink(1, 1, 3)
        self.assertEqual(result, "updated_order_drink")
        mock_repo_instance.update_order_drink.assert_called_once_with(1, 1, 3)

    @patch('services.order_drink_service.OrderDrinkRepositoryManager')
    def test_delete_order_drink(self, MockOrderDrinkRepositoryManager):
        mock_repo_instance = MockOrderDrinkRepositoryManager.return_value.__enter__.return_value
        mock_repo_instance.delete_order_drink_id.return_value = "deleted_order_drink"

        result = OrderDrinkService.delete_order_drink(1)
        self.assertEqual(result, "deleted_order_drink")
        mock_repo_instance.delete_order_drink_id.assert_called_once_with(1)

    @patch('services.order_drink_service.OrderDrinkRepositoryManager')
    def test_delete_order_drinks(self, MockOrderDrinkRepositoryManager):
        mock_repo_instance = MockOrderDrinkRepositoryManager.return_value.__enter__.return_value
        mock_repo_instance.delete_order_drinks.return_value = "deleted_order_drinks"

        result = OrderDrinkService.delete_order_drinks(1)
        self.assertEqual(result, "deleted_order_drinks")
        mock_repo_instance.delete_order_drinks.assert_called_once_with(1)


if __name__ == '__main__':
    unittest.main()
