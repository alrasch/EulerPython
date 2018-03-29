import helpers.math_helper as mh
from abstract.AbstractSolution import AbstractSolution

class Euler11(AbstractSolution):
    def getSolution(self):
        return 70600674

    def solve(self, external_call=None):
        prepend = "../" if external_call == True else ""
        with open(prepend + "../inputs/euler11input.txt") as stream:
            input = stream.readlines()

        content = [x.strip().split() for x in input]

        running_highest = 0

        #Rows
        for idx1 in range(0, 20):
            for idx2 in range(0, 17):
                cells = [int(content[idx1][idx2]), int(content[idx1][idx2+1]), int(content[idx1][idx2+2]), int(content[idx1][idx2+3])]
                product = mh.product_of_list(cells)
                if product > running_highest:
                    running_highest = product

        #Columns
        for idx1 in range(0, 17):
            for idx2 in range(0, 20):
                cells = [int(content[idx1][idx2]), int(content[idx1+1][idx2]), int(content[idx1+2][idx2]), int(content[idx1+3][idx2])]
                product = mh.product_of_list(cells)
                if product > running_highest:
                    running_highest = product

        #Down/right diagonal
        for idx1 in range(0, 17):
            for idx2 in range(0, 17):
                cells = [int(content[idx1][idx2]), int(content[idx1+1][idx2+1]), int(content[idx1+2][idx2+2]), int(content[idx1+3][idx2+3])]
                product = mh.product_of_list(cells)
                if product > running_highest: running_highest = product

        #Up/right diagonal
        for idx1 in range(0, 17):
            for idx2 in range(3, 20):
                cells = [int(content[idx1][idx2]), int(content[idx1 + 1][idx2 - 1]), int(content[idx1 + 2][idx2 - 2]),
                 int(content[idx1 + 3][idx2 - 3])]
                product = mh.product_of_list(cells)
                if product > running_highest: running_highest = product

        return running_highest
