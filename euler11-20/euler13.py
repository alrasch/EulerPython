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

            if total[i] >= 10:
                tens = int(((total[i] - (total[i] % 10)) / 10) % 10)
                total[i-1] += tens
                total[i] -= tens * 10

            if total[i] >= 100:
                hundreds = int((total[i] - (total[i] % 100)) / 100)
                total[i - 2] += hundreds
                total[i] -= hundreds * 100

        total_string = ""
        for i in total:
            total_string += str(i)

        return int(total_string[:10])

Euler13().solve()
