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
            print(Fore.YELLOW + '1.'.rjust(3,' ') + Fore.RESET, 'Print function demonstration.')
            print(Fore.YELLOW + '2.'.rjust(3,' ') + Fore.RESET, 'Types and variables demonstration.')
            print(Fore.YELLOW + '3.'.rjust(3,' ') + Fore.RESET, 'Arithmetic operations demonstration.')
            print(Fore.YELLOW + '4.'.rjust(3,' ') + Fore.RESET, 'String (text) manipulation demonstration.')
            print(Fore.YELLOW + '5.'.rjust(3,' ') + Fore.RESET, 'Lists demonstration.')
            print(Fore.YELLOW + '6.'.rjust(3,' ') + Fore.RESET, 'Conditional statements demonstration.')
            print(Fore.YELLOW + '7.'.rjust(3,' ') + Fore.RESET, 'Loops demonstration.')
            print(Fore.YELLOW + '8.'.rjust(3,' ') + Fore.RESET, 'Try/except/else/finally demonstration.')
            print(Fore.YELLOW + '9.'.rjust(3,' ') + Fore.RESET, 'I/O - Write a text file on D: disk demonstration. (only Windows)')
            print(Fore.YELLOW + '10.'.rjust(3,' ') + Fore.RESET, 'I/O - Read a text file from D: disk demonstration. (only Windows)')
            print(Fore.YELLOW + '11.'.rjust(3,' ') + Fore.RESET, 'Read a Excel file demonstration. (only Windows)')
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
    def exit():
        print('Exiting...')
        sys.exit(0)
