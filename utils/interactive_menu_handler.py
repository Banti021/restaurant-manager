from utils.console_manager import ConsoleManager


class InteractiveMenuHandler:
    def __init__(self, options):
        """
        Initialize the menu handler with a list of options.
        Each option should be a tuple (description, function_to_execute).
        """
        self.options = options

    def display_menu(self):
        ConsoleManager.display_message("\nProsze wybrac jedna z opcji (wpisz 'exit' aby wyjsc)")
        for index, (description, _) in enumerate(self.options, start=1):
            ConsoleManager.display_message(f"{index}. {description}")

    def handle_input(self, choice):
        if 1 <= choice <= len(self.options):
            _, action = self.options[choice - 1]
            if action is not None:
                action()
        else:
            ConsoleManager.display_message("Niepoprawny wybór, proszę spróbować ponownie.")

    def run(self):
        while True:
            self.display_menu()
            user_input = ConsoleManager.get_input("Twój wybór: ")
            if user_input.lower() == 'exit':
                break  # Exiting the loop if the user types 'exit'
            try:
                choice = int(user_input)
                self.handle_input(choice)
            except ValueError:
                ConsoleManager.display_message("Prosze wybrac poprawna opcje lub wpisz 'exit' aby wyjsc.")

