import common.Tree
import unittest

def _CheckBalanced(node):
    if not node:
        return True, 0
    leftCheck, leftHeight = _CheckBalanced(node.left)
    rightCheck, rightHeight = _CheckBalanced(node.right)
    currentHeight = max(leftHeight, rightHeight) + 1
    if abs(leftHeight - rightHeight) >= 2:
        return False, currentHeight
    return (rightCheck and leftCheck), currentHeight

def CheckBalanced(node):
    isBalanced, _ = _CheckBalanced(node)
    return isBalanced

class TestCheckBalanced(unittest.TestCase):
    def driver(self, preArr, expected):
        node = common.Tree.Node.PreOrderArrayToTree(preArr)
        self.assertEqual(expected, CheckBalanced(node))
    def test_CheckBalanced(self):
        self.driver([1, 2, 3, 4, 5, None, None, None, None, \
                     6, None, 7, None, None, 8, 9, None, 11,\
                     None, None, 10, None, None], \
                     False)
        self.driver([1, 2, 3, 4, 5, None, None, None, \
                     13, None, None, \
                     6, None, 7, None, None, 8, 9, None, 11,\
                     None, None, 10, None, None], \
                     True)
        self.driver([1, None, None],\
                    True)

if __name__ == "__main__":
    unittest.main()
