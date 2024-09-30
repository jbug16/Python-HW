class Menu:
    def __init__(self):
        self._options = []

    def addOption(self, option):
        self._options.append(option)

    def getInput(self):
        while (True):
            for index, option in enumerate(self._options, start = 1):
                print(f'{index} {option}')
            
            # Try to get an int value from the user
            try:
                _input = int(input())
            # If not an int, then continue with the while loop and ask the user again
            except ValueError:
                print("Please enter a number 1 - 4.")
                continue

            # Check if the user's input is within the range 1 - 4
            if 1 <= _input <= len(self._options):
                return _input