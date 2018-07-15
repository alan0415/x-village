import random

from copy import deepcopy

class Matrix:

    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.wrong_count = 0 #問題: 為何不能在其他方法直接寫 self.wromg_count += 1，而一定要先寫宣告
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
        #用 deepcopy 先備份 A matrix，再將運算結果存成self.matrix，最後再將備份存入A matrix
        self.trans_matrix = deepcopy(self.matrix) #將self.matrix 備份成 self.trans_matrix
        added_matrix = list()
        added_matrix = m
        for i in range(0, self.rows):
            if len(self.matrix) != len(added_matrix):
                print('Matrix size should in the same size!! ')
                self.wrong_count += 1
                break
            else:
                for j in range(0, self.cols):
                    if len(self.matrix[i]) != len(added_matrix):
                        print('Matrix size should in the same size!! ')
                        self.wrong_count += 1
                        break# 確定break跳出的迴圈是否正確 !!!!!!
                    else: 
                        self.matrix[i][j] = self.matrix[i][j] + added_matrix[i][j]
        return self.matrix
    def sub(self, m):
        """return a new Matrix object after substraction"""
        added_matrix = list()
        added_matrix = m
        if (self.wrong_count == 1):
            print('Matrix size should in the same size!! ')
        else:
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    self.matrix[i][j] = self.trans_matrix[i][j] - added_matrix[i][j] 
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
                print(self.matrix[i][j],end = ' ')
                j += 1
            i += 1
            print(' ')

A_row = int(input("Enter A matrix's rows: "))
A_cols = int(input("Enter A matrix's cols: "))
A_matrix = Matrix(A_row,A_cols)
A_matrix.display()

B_row = int(input("Enter B matrix's rows: "))
B_cols = int(input("Enter B matrix's cols: "))
B_matrix = Matrix(B_row,B_cols)
B_matrix.display()
print('======== A + B ========')
A_matrix.add(B_matrix.matrix)
A_matrix.display()
print('======== A - B ========')
A_matrix.sub(B_matrix.matrix)
A_matrix.display()
