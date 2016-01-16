import unittest
from random import randint

def ZeroMatrix(matrix):
    firstRowZero = firstColumnZero = False
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            firstRowZero = True
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            firstColumnZero = True

    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1,len(matrix)):
        if matrix[i][0] == 0:
            for j in range(1,len(matrix[0])):
                matrix[i][j] = 0
    for j in range(1,len(matrix[0])):
        if matrix[0][j] == 0:
            for i in range(1,len(matrix)):
                matrix[i][j] = 0
    if firstRowZero:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0
    if firstColumnZero:
        for i in range(len(matrix)):
            matrix[i][0] = 0

def PrintMatrix(matrix):
    N = len(matrix[0])
    M = len(matrix)
    for i in range(M):
        for j in range(N):
            print("{0} ".format(matrix[i][j]), end = "")
        print()

def test(M,N):
    matrix = [[ randint(0, 5) for i in range(N)] for j in range(M)]
    PrintMatrix(matrix)
    print()
    print()
    ZeroMatrix(matrix)
    PrintMatrix(matrix)

class TestZeroMatrix(unittest.TestCase):
    def driver(self, matrix, expected):
        ZeroMatrix(matrix)
        self.assertEqual(matrix, expected)
    def test_ZeroMatrix(self):
        matrix = [ \
                    [2, 3, 0],\
                    [1, 3, 4],\
                    [1, 3, 4],\
                    [5, 1, 2]]
        expected = [ \
                    [0, 0, 0],\
                    [1, 3, 0],\
                    [1, 3, 0],\
                    [5, 1, 0]]
        self.driver(matrix, expected)
        matrix = [ \
                    [0, 3, 4],\
                    [1, 3, 4],\
                    [1, 3, 4],\
                    [5, 1, 2]]
        expected = [ \
                    [0, 0, 0],\
                    [0, 3, 4],\
                    [0, 3, 4],\
                    [0, 1, 2]]
        self.driver(matrix, expected)
        matrix = [ \
                    [2, 3, 4],\
                    [1, 3, 4],\
                    [1, 0, 4],\
                    [5, 1, 2]]
        expected = [ \
                    [2, 0, 4],\
                    [1, 0, 4],\
                    [0, 0, 0],\
                    [5, 0, 2]]
        self.driver(matrix, expected)
        matrix = [ \
                    [2, 3, 4],\
                    [1, 3, 4],\
                    [1, 3, 4],\
                    [5, 1, 2]]
        expected = [ \
                    [2, 3, 4],\
                    [1, 3, 4],\
                    [1, 3, 4],\
                    [5, 1, 2]]
        self.driver(matrix, expected)
        matrix = [ \
                    [0, 3, 4],\
                    [1, 0, 4],\
                    [1, 3, 0],\
                    [0, 1, 2]]
        expected = [ \
                    [0, 0, 0],\
                    [0, 0, 0],\
                    [0, 0, 0],\
                    [0, 0, 0]]
        self.driver(matrix, expected)

if __name__ == "__main__":
    unittest.main()
