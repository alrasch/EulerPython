import importlib
import time

from resources.exceptions.answerexception import AnswerException
from helpers.printer.printer import Printer

class TestSolutions:
    def assertEqual(self, value, expectation):
        if value != expectation:
            raise AnswerException("Got output " + str(value) + " but expected " + str(expectation) + ".")
        return True

    def runTests(self):
        testable_class_enumeration = [x for x in range(1, 17) if x not in []]
        successes = 0
        failures = 0

        for i in testable_class_enumeration:
            try:
                module = importlib.import_module("euler" + str(i))
                mod_class = getattr(module, "Euler" + str(i))
                start_time = time.time()
                success = self.assertEqual(mod_class.solve(self), mod_class.getSolution(self))
                end_time = time.time()
                time_delta = end_time - start_time

                if success: Printer.printSuccess("Euler" + str(i) + " succeeded in " + str(time_delta))

                successes += 1
            except AnswerException as error:
                Printer.printFailure("Euler" + str(i) + " failure!")
                Printer.printNeutral(error)
                failures += 1

        if successes == len(testable_class_enumeration):
            Printer.printSuccess("All tests passed!")

tester = TestSolutions()
tester.runTests()
