import sys
from helpers.ConsoleHelper import ConsoleHelper
from services.LabService import LabService
from colorama import Fore, init

class Menu:    
    init(autoreset=True)

    @staticmethod
    def show():
        while True:
            ConsoleHelper.clear()

            print(f'{Fore.CYAN}|--------------------------------|')
            print(f'{Fore.CYAN}|         Python labs            |')
            print(f'{Fore.CYAN}|--------------------------------|\n')

            print('*** Menu ***\n')
            Menu.mount_menu()
            print(Fore.YELLOW + '0.'.rjust(3,' ') + Fore.RESET, 'Exit.')

            option = input(f'\n{Fore.CYAN}Select an option: {Fore.RESET}')

            if option == "1":
                LabService.run_print_demo()
            elif option == "2":
                LabService.run_types_and_variables_demo()
            elif option == "3":
                LabService.run_arithmetic_operations_demo()
            elif option == "4":
                LabService.run_text_manipulation_demo()
            elif option == "5":
                LabService.run_lists_demo()
            elif option == "6":
                LabService.run_conditional_statements_demo()
            elif option == "7":                
                LabService.run_loops_demo()
            elif option == "8":
                LabService.run_try_except_demo()
            elif option == "9":
                LabService.run_file_write_demo()
            elif option == "10":
                LabService.run_file_read_demo()
            elif option == "11":
                LabService.run_excel_read_demo()
            elif option == "0":
                Menu.exit();
            else:
                ConsoleHelper.clear()
                print(f'{Fore.YELLOW}Invalid option. Please try again.\n')
                input('Press Enter to continue...')

    @staticmethod
    def mount_menu():
        menu_options = [
            'Print function demonstration.'
            , 'Types and variables demonstration.'
            , 'Arithmetic operations demonstration.'
            , 'String (text) manipulation demonstration.'
            , 'Lists demonstration.'
            , 'Conditional statements demonstration.'
            , 'Loops demonstration.'
            , 'Try/except/else/finally demonstration.'
            , 'I/O - Write a text file on disk demonstration. (only Windows)'
            , 'I/O - Read a text file from disk demonstration. (only Windows)'
            , 'Read a Excel file demonstration. (only Windows)'
        ];
    
        for i in range(len(menu_options)):
            print(Fore.YELLOW + f'{i + 1}.'.rjust(3,' ') + Fore.RESET, menu_options[i])

    @staticmethod
    def exit():
        print('Exiting...')
        sys.exit(0)
