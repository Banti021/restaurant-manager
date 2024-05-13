from utils.console_manager import ConsoleManager


class MenuManager:
    @staticmethod
    def get_dish_details():
        name = ConsoleManager.get_input("Podaj nazwę dania: ")
        price = float(ConsoleManager.get_input("Podaj cenę dania: "))
        is_dish_of_the_day = MenuManager.is_dish_of_the_day(ConsoleManager.get_input("Czy danie dnia (t/n):"))
        return name, price, is_dish_of_the_day

    @staticmethod
    def get_drink_details():
        name = ConsoleManager.get_input("Podaj nazwę napoju: ")
        price = float(ConsoleManager.get_input("Podaj cenę napoju: "))
        is_alcoholic = ConsoleManager.get_input("Czy napój alkoholowy (t/n): ")
        alcohol_content = ConsoleManager.get_input("Podaj zawartość alkoholu w napoju (w %). Jeśli nie dotyczy, "
                                                   "wciśnij ENTER: ")
        return name, price, is_alcoholic, alcohol_content

    @staticmethod
    def is_dish_of_the_day(answer):
        if answer == 't':
            return True

        return False
