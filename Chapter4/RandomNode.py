from common.Tree import *
from random import randint
import unittest

class SNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.size = 1
    def insert(self, insertData):
        self.size += 1
        if self.data >= insertData:
            if self.left:
                self.left.insert(insertData)
            else:
                self.left = SNode(insertData)
        else:
            if self.right:
                self.right.insert(insertData)
            else:
                self.right = SNode(insertData)
    # 0 <= k < self.size
    def _FindRandom(self, k):
        leftSize = self.left.size if self.left else 0
        if k < leftSize:
            return self.left._FindRandom(k)
        if k == leftSize:
            return self
        return self.right._FindRandom(k-leftSize-1)

    def FindRandom(self):
        return self._FindRandom(randint(0,self.size-1))

class TestRandomNode(unittest.TestCase):
    # A farcical test
    def driver(self, inArr):
        root = None
        for x in inArr:
            if root:
                root.insert(x)
            else:
                root = SNode(x)
        for i in range(100):
            self.assertIsNotNone(root.FindRandom())

    def test_RandomNode(self):
        self.driver([4,5,2,3,6,10,2,8])

if __name__ == "__main__":
    unittest.main()
