from utils.console_manager import ConsoleManager


class InteractiveMenuHandler:
    def __init__(self, options, previous_menus=None):
        """
        Initialize the menu handler with a list of options.
        Each option should be a tuple (description, function_to_execute).
        `previous_menus` is a stack to keep track of menu navigation history.
        """
        self.options = options

    def display_menu(self):
        for index, (description, _) in enumerate(self.options, start=1):
            ConsoleManager.display_message(f"{index}. {description}")

    def handle_input(self, choice):
        if 1 <= choice <= len(self.options):
            _, action = self.options[choice - 1]
            if action:
                result = action()
                return result
        else:
            ConsoleManager.display_message("Niepoprawny wybór, proszę spróbować ponownie.")

    def run(self):
        while True:
            self.display_menu()
            user_input = ConsoleManager.get_input("Twój wybór: ")
            if user_input.lower() == 'exit':
                break
            try:
                choice = int(user_input)
                result = self.handle_input(choice)
                if result == "back":
                    break
            except ValueError:
                ConsoleManager.display_message("Prosze wybrac poprawna opcje lub wpisz 'exit' aby wyjsc.")
