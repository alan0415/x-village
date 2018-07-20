import random

from copy import deepcopy

class Matrix():
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
            self.orig_matrix = deepcopy(self.matrix)
        
        def add(self, m):
            """return a new Matrix object after summation"""
            added_matrix = list()
            added_matrix = m.extent()
            for i in range(0, self.cols):
                for j in range(0, self.rows): 
                    self.matrix[i][j] = self.orig_matrix[i][j] + added_matrix[i][j]
            return Matrix2(self.matrix)
        def sub(self, m):
            """return a new Matrix object after substraction"""
            added_matrix = list()
            added_matrix = m.extent()
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    try:
                        self.matrix[i][j] = self.orig_matrix[i][j] - added_matrix[i][j]
                    except IndexError:
                        print("wrong type")
                        return 
            return Matrix2(self.matrix)
        def mul(self, m):
            """return a new Matrix object after multiplication"""
            added_matrix = list()
            added_matrix = m.extent()
            res = [[0] * len(added_matrix[0]) for i in range(self.rows)]
            for i in range(self.rows):#self.rows 直的
                for j in range(len(added_matrix[0])):#len(m[0]) 橫的
                    for k in range(len(added_matrix)):
                        res[i][j] += self.orig_matrix[i][k] * added_matrix[k][j]
            self.matrix = list()
            self.matrix = res
            self.cols = len(added_matrix[0])
            return Matrix2(self.matrix)
        def transpose(self):
            """return a new Matrix object after transpose"""
            res = [[0] * self.rows for i in range(self.cols)]
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    res[j][i] = self.matrix[i][j]
            self.matrix = list()
            self.matrix = res
            return Matrix2(self.matrix)
    
        def display(self):
            """Display the content in the matrix"""
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    print(self.matrix[i][j],end = ' ')
                    j += 1
                i += 1
                print(' ')
        def extent(self):#接入<matrix>轉成list
            return self.matrix
class Matrix2(Matrix):
    def __init__(self,m):
        self.rows = len(m)
        self.cols = len(m[0])
        self.matrix = m
A_row = int(input("Enter A matrix's rows: "))
A_cols = int(input("Enter A matrix's cols: "))
A_matrix = Matrix(A_row,A_cols)
print('A matrix: ')
A_matrix.display()

B_row = int(input("Enter B matrix's rows: "))
B_cols = int(input("Enter B matrix's cols: "))
B_matrix = Matrix(B_row,B_cols)
print('B matrix: ')
B_matrix.display()
print('======== A + B ========')
c = A_matrix.add(B_matrix)
c.display()
print('======== A - B ========')
e = A_matrix.sub(B_matrix)
e.display()
print('======== A * B ========')
d = A_matrix.mul(B_matrix)
d.display()
print('=======================')
f = A_matrix.transpose()
f.display()