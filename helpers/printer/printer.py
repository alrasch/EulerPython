class Printer:
    @staticmethod
    def printSuccess(message):
        print('\x1b[0;33;42m' + str(message) + '\x1b[0m')

    @staticmethod
    def printFailure(message):
        print('\x1b[0;38;41m' + str(message) + '\x1b[0m')

    @staticmethod
    def printNeutral(message):
        print(message)
