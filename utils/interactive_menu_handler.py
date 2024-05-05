from utils.console_manager import ConsoleManager


class InteractiveMenuHandler:
    def __init__(self, options):
        """
        Initialize the menu handler with a list of options.
        Each option should be a tuple (description, function_to_execute).
        """
        self.options = options

    def display_menu(self):
        for index, (description, _) in enumerate(self.options, start=1):
            ConsoleManager.display_message(f"{index}. {description}")

    def handle_input(self, choice):
        if 1 <= choice <= len(self.options):
            _, action = self.options[choice - 1]
            action()
        else:
            ConsoleManager.display_message("Niepoprawny wybór. Spróbuj ponownie.")

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(ConsoleManager.get_input("Wybierz opcję: "))
                self.handle_input(choice)
            except ValueError:
                ConsoleManager.display_message("Wpisz poprawną wartość.")

