from services.dish_service import DishService



def test_create_dish():
    dish = DishService.create_dish("Spaghetti", 10.50, False)


if __name__ == "__main__":
    test_create_dish()
