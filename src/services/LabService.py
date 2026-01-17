from helpers.ConsoleHelper import ConsoleHelper
from colorama import Fore, Style, init
from pathlib import Path
import subprocess
import sys
import pandas as pd

class LabService:
    init(autoreset=True)

    @staticmethod
    def run_print_demo():
        ConsoleHelper.clear()
        
        print(f'{Fore.CYAN}1. Print function demonstration.\n')

        print('Hello World with Python ...')
        
        ConsoleHelper.pause()

    @staticmethod
    def run_types_and_variables_demo():
        ConsoleHelper.clear()
        
        print(f'{Fore.CYAN}2. Types and variables demonstration.\n')

        type_integer = 42
        type_float = 3.14
        type_string = "Hello, Python!"
        type_boolean = True

        print(f'Type: {type(type_integer)}\t - Value: {type_integer}')
        print(f'Type: {type(type_float)}\t - Value: {type_float}')
        print(f'Type: {type(type_string)}\t - Value: {type_string}')
        print(f'Type: {type(type_boolean)}\t - Value: {type_boolean}')

        ConsoleHelper.pause()

    @staticmethod
    def run_arithmetic_operations_demo():
        ConsoleHelper.clear()
        
        print(f'{Fore.CYAN}3. Arithmetic operations demonstration.\n')

        spacing = 20
        a = 10
        b = 3

        print('Operation'.ljust(spacing, ' ')        , 'Expression'.ljust(spacing, ' ')            , 'Result'.ljust(spacing, ' '))
        print(''.ljust(60, '='))
        print('Addition'.ljust(spacing, ' ')         , 'a + b = '.ljust(spacing, ' ')              , a + b)
        print('Subtraction'.ljust(spacing, ' ')      , 'a - b = '.ljust(spacing, ' ')              , a - b)
        print('Multiplication'.ljust(spacing, ' ')   , 'a * b = '.ljust(spacing, ' ')              , a * b)
        print('Division'.ljust(spacing, ' ')         , 'a / b = '.ljust(spacing, ' ')              , a / b)
        print('Integer Division'.ljust(spacing, ' ') , 'a // b = '.ljust(spacing, ' ')             , a // b)
        print('Modulus'.ljust(spacing, ' ')          , 'a % b = '.ljust(spacing, ' ')              , a % b)
        print('Exponentiation'.ljust(spacing, ' ')   , 'a ** b = '.ljust(spacing, ' ')             , a ** b)
        print('Expression'.ljust(spacing, ' ')       , '(a + b) * (a - b) = '.ljust(spacing, ' ') , (a + b) * (a - b))
        print(''.ljust(60, '-'))

        ConsoleHelper.pause()

    @staticmethod
    def run_text_manipulation_demo():
        ConsoleHelper.clear()
        
        print(f'{Fore.CYAN}4. String (text) manipulation demonstration.\n')

        greeting = "Hello"
        name = "World"
        fullGreeting = greeting + ", " + name + "!"                # string concatenation
        print(fullGreeting)                                        # print the full greeting
        print(fullGreeting.upper())                                # to upper case
        print(fullGreeting.lower())                                # to lower case
        print(fullGreeting.replace("World", "Python"))             # string replacement
        print(fullGreeting.split(", "))                            # string splitting
        print(len(fullGreeting))                                   # Calculate the string length
        print(fullGreeting[0])                                     # Accessing first character by index
        print(fullGreeting[0:5])                                   # Slicing example
        print(fullGreeting[:5])                                    # Reading from start to index 5
        print(fullGreeting[5:])                                    # Reading from index 5 to end
        print(fullGreeting.index("W"))                             # Finding index of substring
        print(fullGreeting.startswith("Hello"))                    # Check start
        print(fullGreeting.endswith("!"))                          # Check end
        print(fullGreeting.count("o"))                             # Count occurrences
        print(fullGreeting.find("Python"))                         # Find substring
        print(fullGreeting.isalpha())                              # Check if all characters are alphabetic
        print(fullGreeting.isdigit())                              # Check if all characters are digits
        print(fullGreeting.strip("!"))                             # Strip characters from both ends
        print(fullGreeting.center(30))                             # Center the string within a width
        print(fullGreeting.format())                               # Format the string (no placeholders here)
        print('\'Test your skill in python\'')                     # escape quote characters example
        print(f'This is a formatted string: {fullGreeting}')       # similar to string interpolation on c#.net
        print(r'This raw example\n string')                        # raw string example (similar to string verbatim on c#.net)
        print('''\
                Usage: thingy [OPTIONS]
                    -h                        Display this usage message
                    -H hostname               Hostname to connect to
            ''')                                                   # multi-line string example (similar to string verbatim on c#.net)
        
        brokedTest = ('Any text'
                      ' continues here')
        print(brokedTest)                                          # demonstrates string concatenation across lines

        ConsoleHelper.pause()

    @staticmethod
    def run_lists_demo():
        ConsoleHelper.clear()
        
        print(f'{Fore.CYAN}5. Lists demonstration.\n')

        values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print('Values List:', values)
        print('First Value:', values[0])
        print('Last Value:', values[-1])
        print('Sliced Values (2-5):', values[2:6])  # slicing from index 2 to 5

        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        combinedList = list1 + list2
        print('Combined List:', combinedList)

        myList = [10, 20, 30]
        myList.append(40)  # Add an element to the end
        print('Appended List:', myList)

        myList.remove(20)  # Remove an element
        print('After Removal:', myList)
        print('List Length:', len(myList))  # Get length of the list

        myList.clear()  # Remove all elements
        print('After Clear:', myList)

        nestedList = [[1, 2], [3, 4], [5, 6], [0, 2], [0, 4], [0, 6]]
        print('Nested List:', nestedList)
        print(nestedList[0][0])  # Accessing first element of the first nested list

        # TODO: review this code.
        fruits = ['Apple', 'Banana', 'Cherry']
        print('Initial list:', fruits)

        fruits.append('Date')
        print('After appending Date:', fruits)

        fruits.insert(1, 'Blueberry')
        print('After inserting Blueberry at index 1:', fruits)

        fruits.remove('Banana')
        print('After removing Banana:', fruits)

        popped_fruit = fruits.pop()
        print('After popping last fruit ({}):'.format(popped_fruit), fruits)

        fruits.sort()
        print('After sorting the list:', fruits)

        fruits.reverse()
        print('After reversing the list:', fruits)

        print('List length:', len(fruits))

        for index, fruit in enumerate(fruits):
            print('Index {}: {}'.format(index, fruit))

        ConsoleHelper.pause()

    @staticmethod
    def run_conditional_statements_demo():
        ConsoleHelper.clear()
        
        print(f'{Fore.CYAN}6. Conditional statements demonstration.\n')

        # if/else statement demo
        isActive = True

        if isActive:
            print('The variable isActive is True')
        else:
            print('The variable isActive is False')
        
        # match statement demo (similar to switch case in c#.net)
        value = 1

        match value:
            case 1:
                print("Value is 1")
            case 2:
                print("Value is 2")
            case _:  # as default in c#.net
                print("Value is something else")

        ConsoleHelper.pause()

    @staticmethod
    def run_loops_demo():
        ConsoleHelper.clear()
        
        print(f'{Fore.CYAN}7. Loops demonstration.\n')

        # "while" loop example
        count = 0
        while count < 5:
            print('Count is:', count)
            count += 1

        # Fibonacci sequence example
        a, b = 0, 1
        print('\nFibonacci sequence:')
        while a < 10:
            print(a, end=',')
            a, b = b, a + b
        print()  # new line

        # "foreach" loop example
        words = ['apple', 'banana', 'cherry']
        print('\nWords and their lengths:')
        for word in words:
            print(word, len(word))

        print('\nRange example:')
        for i in range(10):
            print(i, end=' ')
        print()  # new line

        ConsoleHelper.pause()

    @staticmethod
    def run_try_except_demo():
        ConsoleHelper.clear()
        
        print(f'{Fore.CYAN}8. Try/except/else/finally demonstration.\n')

        try:
            numerator = int(input('Enter the numerator (integer): '))
            denominator = int(input('Enter the denominator (integer): '))
            result = numerator / denominator
        except ValueError:
            print(f'{Fore.RED}Error: Please enter valid integers.{Style.RESET_ALL}')
        except ZeroDivisionError:
            print(f'{Fore.RED}Error: Division by zero is not allowed.{Style.RESET_ALL}')
        else:
            print(f'{Fore.GREEN}The result of {numerator} divided by {denominator} is {result}{Style.RESET_ALL}')
        finally:
            print('Execution of try/except block is complete.')

        ConsoleHelper.pause()

    @staticmethod
    def run_file_write_demo():
        ConsoleHelper.clear()
        
        print(f'{Fore.CYAN}9. I/O - Write a text file on D: disk demonstration. (only Windows)\n')

        base_path = Path(__file__).resolve()
        text_file_path = base_path.parents[2] / "data" / "sample_text_file.txt"

        print('Enter the text to write to the file (end with Ctrl+Z on a new line and press Enter):\n')
        user_text = sys.stdin.read() # Users can input multiple lines, ending with Ctrl+Z (Windows) or Ctrl+D (Unix)

        try:
            with open(text_file_path, 'w', encoding='utf-8') as file:
                file.write(user_text)

            print(f'File written successfully to {text_file_path}, and opening the folder with Windows Explorer...')

            subprocess.run(['explorer', '/select,', str(text_file_path)])
        except Exception as e:
            print(Fore.RED + 'An error occurred while writing the file:' + Style.RESET_ALL, e)

        ConsoleHelper.pause()

    @staticmethod
    def run_file_read_demo():
        ConsoleHelper.clear()
        
        print(f'{Fore.CYAN}10. I/O - Read a text file from D: disk demonstration. (only Windows)\n')

        base_path = Path(__file__).resolve()
        text_file_path = base_path.parents[2] / "data" / "sample_text_file.txt"

        try:
            with open(text_file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                print('File Content:\n')
                print(content)
        except Exception as e:
            print(f'{Fore.RED}An error occurred while reading the file:{Style.RESET_ALL} {e}')

        ConsoleHelper.pause()

    @staticmethod
    def run_excel_read_demo():
        ConsoleHelper.clear()
        
        print(f'{Fore.CYAN}11. Read a Excel file demonstration. (only Windows)\n')        

        print('Report about global sales by country\n')

        # Current file path (LabService.py)
        base_path = Path(__file__).resolve()

        # Path to the Excel file
        excel_path = base_path.parents[2] / "data" / "global_sales_by_country.xlsx"

        try:
            df = pd.read_excel(excel_path)

            # Define the spacing for each column
            col_width = 20
            
            # Show the headers of the columns
            header = 'Row'.ljust(col_width)
            for col in df.columns:
                header += str(col).ljust(col_width)
            
            print(f'{Fore.CYAN}{header}')
            print('=' * (col_width * (len(df.columns) + 1)))
            
            # Iterate over rows
            for i, row in df.iterrows():
                line = f'{Fore.CYAN}{str(i + 1).ljust(col_width)}{Fore.RESET}'
                
                # Iterate over all columns and concatenate side by side
                for col in df.columns:
                    line += str(row[col]).ljust(col_width)
                print(line)

            print('-' * (col_width * (len(df.columns) + 1)))

        except Exception as e:
            print(f'{Fore.RED}An error occurred while reading the Excel file:{Style.RESET_ALL} {e}')

        ConsoleHelper.pause()
