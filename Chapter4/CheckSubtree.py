from common.Tree import *
import unittest

def MakeStr(root):
    if not root:
        return "None"
    leftStr = MakeStr(root.left)
    rightStr = MakeStr(root.right)
    return leftStr+":"+rightStr+":"+str(root.data)

def CheckSubtree(t1, t2):
    str1 = MakeStr(t1)
    str2 = MakeStr(t2)
    return -1 != str1.find(str2)

class TestCheckSubtree(unittest.TestCase):
    def driver(self, t1Arr, t2Arr, expected):
        t1 = Node.PreOrderArrayToTree(t1Arr)
        t2 = Node.PreOrderArrayToTree(t2Arr)
        self.assertEqual(CheckSubtree(t1, t2), expected)

    def test_CheckSubtree(self):
        self.driver([1, 2, 4, 5, 6, None, None, \
                     None, None, None, 3, None, None],\
                     [4,5,6, None, None, None, None], True)
        self.driver([1, 2, 4, 5, 6, None, None, \
                     None, None, None, 3, None, None],\
                     [4,5,7, None, None, None, None], False)


if __name__ == "__main__":
    unittest.main()
