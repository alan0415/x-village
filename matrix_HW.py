import random

from copy import deepcopy

class Matrix:

    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.rows = nrows
        self.cols = ncols
        self.matrix = list()
        for i in range(0, self.rows):
            swap = list()
            for j in range(0, self.cols):
                swap.append(random.randint(0,9))
                j += 1
            self.matrix.append(swap)
            i += 1

    def add(self, m):
        """return a new Matrix object after summation"""
        # m 為傳入預比較的matrix
        pass

    def sub(self, m):
        """return a new Matrix object after substraction"""
        pass

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        pass

    def transpose(self):
        """return a new Matrix object after transpose"""
        pass
    
    def display(self):
        """Display the content in the matrix"""
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                print(self.matrix[i][j],end = '')
                j += 1
            i += 1
            print(' ')
        print('all matrix = ',self.matrix)

A_row = int(input("Enter A matrix's rows: "))
A_cols = int(input("Enter A matrix's cols: "))
A_matrix = Matrix(A_row,A_cols)
A_matrix.display()

B_row = int(input("Enter B matrix's rows: "))
B_cols = int(input("Enter B matrix's cols: "))
B_matrix = Matrix(B_row,B_cols)
B_matrix.display()