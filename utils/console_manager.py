import os


class ConsoleManager:
    """Class to manage console input and output"""

    @staticmethod
    def display_menu(menu):
        """Display menu options"""
        for index, option in enumerate(menu, 1):
            print(f"{index}. {option}")

        choice = ConsoleManager.get_input("Enter your choice: ")
        return int(choice)

    @staticmethod
    def get_input(message=""):
        return input(message)

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[H\033[J", end="")
