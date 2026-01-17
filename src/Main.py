from Menu import Menu      # Import Menu class

class Main:                # Class definition
    
    @staticmethod          # Static method decorator
    def run():             # Method definition
        Menu.show()

if __name__ == '__main__': # Entry point check
    Main.run()
