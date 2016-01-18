import common.Tree
import unittest

def _ValidateBST(node):
    if not node:
        return True, None, None
    lBST, lMin, lMax = _ValidateBST(node.left)
    if not lBST or ((lMax != None) and lMax > node.data):
        return False, None, None
    rBST, rMin, rMax = _ValidateBST(node.right)
    if not rBST or ((rMin != None) and rMin < node.data):
        return False, None, None
    return True, \
            lMin if lMin != None else node.data, \
            rMax if rMax != None else node.data

def ValidateBST(node):
    isBST, _, _ = _ValidateBST(node)
    return isBST

def ValidateBST2(node):
    inOrderArr = []
    common.Tree.Node.InOrderArray(node, inOrderArr)
    return sorted(inOrderArr) == inOrderArr

class TestValidateBST(unittest.TestCase):
    def driver(self, preArr, expected):
        node = common.Tree.Node.PreOrderArrayToTree(preArr)
        self.assertEqual(expected, ValidateBST(node))
        self.assertEqual(expected, ValidateBST2(node))
    def test_ValidateBST(self):
        self.driver([5, 4, 3, None, None, 5, None, None, \
                     8, 7, None, None, 13, None, None], \
                     True)
        self.driver([5, 4, 3, None, None, 6, None, None, \
                     8, 7, None, None, 13, None, None], \
                     False)
        self.driver([5, 4, 3, None, None, 5, None, None, \
                     8, 4, None, None, 13, None, None], \
                     False)

if __name__ == "__main__":
    unittest.main()
