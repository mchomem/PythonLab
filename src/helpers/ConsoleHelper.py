import os

class ConsoleHelper:
    """
        Helper class for console operations.

        Methods;
        - clear(): Clears the console screen.
    """
    
    @staticmethod
    def clear():
        """
            Clears the console screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def pause():
        """
            Pauses the console until the user presses Enter.
        """
        input('\nPress Enter to continue...')