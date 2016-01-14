import unittest

def RotateLayer(matrix, N, layerIndex):
    nPrime = N - 1
    layerEnd = nPrime - layerIndex
    for i in range(layerIndex, layerEnd):
        matrix[layerIndex][nPrime - i], \
        matrix[nPrime - i][nPrime - layerIndex], \
        matrix[nPrime - layerIndex][i], \
        matrix[i][layerIndex] \
            = matrix[i][layerIndex],\
            matrix[layerIndex][nPrime - i], \
            matrix[nPrime - i][nPrime - layerIndex], \
            matrix[nPrime - layerIndex][i]
    return


def RotateMatrix(matrix):
    N = len(matrix[0])
    layerEnd = int((N-1)/2)
    for i in range(layerEnd + 1):
        RotateLayer(matrix, N, i)


def PrintMatrix(matrix):
    N = len(matrix[0])
    for i in range(N):
        for j in range(N):
            print("{0} ".format(matrix[i][j]), end = "")
        print()

class TestRotateMatrix(unittest.TestCase):
    def driver(self, matrix, expected):
        RotateMatrix(matrix)
        self.assertEqual(matrix, expected)
    def test_Rotation4(self):
        matrix = [ \
            ['a', 'b', 'c', 'd'], \
            ['e', 'f', 'g', 'h'], \
            ['i', 'j', 'k', 'l'], \
            ['m', 'n', 'o', 'p'] \
            ]
        expected = [ \
            ['m', 'i', 'e', 'a'], \
            ['n', 'j', 'f', 'b'], \
            ['o', 'k', 'g', 'c'], \
            ['p', 'l', 'h', 'd'] \
            ]
        self.driver(matrix, expected)
    def test_Rotation5(self):
        matrix = [ \
            ['a', 'b', 'c', 'd', 'e'], \
            ['f', 'g', 'h', 'i', 'j'], \
            ['k', 'l', 'm', 'n', 'o'], \
            ['p', 'q', 'r', 's', 't'], \
            ['u', 'v', 'w', 'x', 'y'] \
            ]
        expected = [ \
            ['u', 'p', 'k', 'f', 'a'], \
            ['v', 'q', 'l', 'g', 'b'], \
            ['w', 'r', 'm', 'h', 'c'], \
            ['x', 's', 'n', 'i', 'd'], \
            ['y', 't', 'o', 'j', 'e'] \
            ]
        self.driver(matrix, expected)

if __name__ == "__main__":
    unittest.main()

