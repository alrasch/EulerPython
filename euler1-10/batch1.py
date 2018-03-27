import importlib
from resources.exceptions.answerexception import AnswerException
from helpers.printer.printer import Printer

class Batch1:
    def assertEqual(self, value, expectation):
        if value != expectation:
            raise AnswerException("Got output " + str(value) + " but expected " + str(expectation) + ".")
        return True

    def runTests(self):
        testable_class_enumeration = range(1, 11)
        successes = 0
        failures = 0

        for i in testable_class_enumeration:
            module = importlib.import_module("euler" + str(i))
            mod_class = getattr(module, "Euler" + str(i))

            try:
                if self.assertEqual(mod_class.solve(self), mod_class.getSolution(self)):
                    Printer.printSuccess("Euler" + str(i) + " success!")
                successes += 1
            except AnswerException as error:
                Printer.printFailure("Euler" + str(i) + " failure!")
                Printer.printNeutral(error)
                failures += 1

        if successes == len(testable_class_enumeration):
            Printer.printSuccess("All tests passed!")

b1 = Batch1()
b1.runTests()
