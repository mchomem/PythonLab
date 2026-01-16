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
            print('1.'.rjust(3,' '), 'Print function demonstration.')
            print('2.'.rjust(3,' '), 'Types and variables demonstration.')
            print('3.'.rjust(3,' '), 'Arithmetic operations demonstration.')
            print('4.'.rjust(3,' '), 'String (text) manipulation demonstration.')
            print('5.'.rjust(3,' '), 'Lists demonstration.')
            print('6.'.rjust(3,' '), 'Conditional statements demonstration.')
            print('7.'.rjust(3,' '), 'Loops demonstration.')
            print('8.'.rjust(3,' '), 'Try/except/else/finally demonstration.')
            print('9.'.rjust(3,' '), 'I/O - Write a text file on D: disk demonstration. (only Windows)')
            print('10.'.rjust(3,' '), 'I/O - Read a text file from D: disk demonstration. (only Windows)')
            print('11.'.rjust(3,' '), 'Read a Excel file demonstration. (only Windows)')
            print('0.'.rjust(3,' '), 'Exit.')

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
