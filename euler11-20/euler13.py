from abstract.AbstractSolution import AbstractSolution

class Euler13(AbstractSolution):
    def getSolution(self):
        return 5537376230

    def solve(self, external_call=None):
        with open("../inputs/13.txt") as stream:
            input = stream.readlines()

        content = [x.strip() for x in input]
        length = content[0].__len__()

        total = [0] * (length+1)

        for place in range(0, length):
            place_sum = 0
            for number_string in content:
                place_sum += int(number_string[place])
            total[place] += place_sum

        total = [0, 0] + total

        for i in range(length, 0, -1):
            for exponent in range(1, 10):
                power = 10**exponent
                if total[i] >= power:
                    hundreds = int((total[i] - (total[i] % power)) / power)
                    total[i - exponent] += hundreds
                    total[i] -= hundreds * power

        total_string = ""
        for i in total:
            total_string += str(i)

        return int(total_string[:10])

Euler13().solve()
