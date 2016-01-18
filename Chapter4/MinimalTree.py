from common.Tree import Node
import math
import unittest


def MinimalTree(inArr, start, end):
    if start > end:
        return None
    if start == end:
        return Node(inArr[start])
    midPoint = int((start+end)/2)
    midNode = Node(inArr[midPoint])
    midNode.left = MinimalTree(inArr, start, midPoint-1)
    midNode.right = MinimalTree(inArr, midPoint+1, end)
    return midNode

class TestMinimalTree(unittest.TestCase):
    def driver(self, inArr):
        node = MinimalTree(inArr, 0, len(inArr)-1)
        resultArr = []
        Node.InOrderArray(node, resultArr)
        # we don't need to additional check if the list is sorted
        # as the assumption is that inArr is sorted
        self.assertEqual(inArr, resultArr)
        minimalLen = math.ceil(math.log2(len(inArr) + 1))
        self.assertEqual(minimalLen, Node.Depth(node))
    def test_TestMinimalTree(self):
        self.driver([1, 2, 3, 4, 5, 6])
        self.driver([1, 2, 3, 4, 5])
        self.driver([1, 2, 3, 4])
        self.driver([1, 2, 3])
        self.driver([2 , 3])
        self.driver([2])

if __name__ == "__main__":
    unittest.main()
