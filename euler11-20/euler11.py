import helpers.math_helper as mh
from abstract.AbstractSolution import AbstractSolution

class Euler11(AbstractSolution):
    def getSolution(self):
        return 70600674

    def solve(self):
        with open("../inputs/euler11input.txt") as stream:
            input = stream.readlines()

        content = [x.strip().split() for x in input]

        running_highest = 0

        #Rows and columns
        for idx1 in range(0, 20):
            for idx2 in range(0, 17):
                row_cells = [int(content[idx1][idx2]),
                             int(content[idx1][idx2+1]),
                             int(content[idx1][idx2+2]),
                             int(content[idx1][idx2+3])]

                column_cells = [int(content[idx2][idx1]),
                                int(content[idx2+1][idx1]),
                                int(content[idx2+2][idx1]),
                                int(content[idx2+3][idx1])]

                row_product = mh.product_of_list(row_cells)
                column_product = mh.product_of_list(column_cells)

                if row_product > running_highest:
                    running_highest = row_product
                if column_product > running_highest:
                    running_highest = column_product

        #Down/right diagonal
        for idx1 in range(0, 17):
            for idx2 in range(0, 17):
                cells = [int(content[idx1][idx2]),
                         int(content[idx1+1][idx2+1]),
                         int(content[idx1+2][idx2+2]),
                         int(content[idx1+3][idx2+3])]

                product = mh.product_of_list(cells)
                if product > running_highest:
                    running_highest = product

        #Up/right diagonal
        for idx1 in range(0, 17):
            for idx2 in range(3, 20):
                cells = [int(content[idx1][idx2]),
                         int(content[idx1+1][idx2-1]),
                         int(content[idx1+2][idx2-2]),
                         int(content[idx1+3][idx2-3])]

                product = mh.product_of_list(cells)
                if product > running_highest:
                    running_highest = product

        return running_highest
