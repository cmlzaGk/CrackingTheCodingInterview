from common.Tree import *
import unittest

# returns subTreeContainsA, subTreeContainsB, CommonAnncestor
def _FirstCommonAncestor(node, a, b):
    if not node:
        return False, False, None
    if a == node:
        return True, False, None
    if b == node:
        return False, True, None
    la, lb, ancestor = _FirstCommonAncestor(node.left, a, b)
    if ancestor:
        return True, True, ancestor
    ra, rb, ancestor = _FirstCommonAncestor(node.left, a, b)
    if ancestor:
        return True, True, ancestor
    if (la or lb) and (ra or rb):
        return True, True, node
    return (la or lb), (ra or rb), None

def FirstCommonAncestor(node, a, b):
    _,_, ancestor = _FirstCommonAncestor(node, a, b)
    return ancestor

class TestFirstCommonAncestor(unittest.TestCase):
    def driver(self, root, a, b, expected):
        self.assertEqual(FirstCommonAncestor(root, a, b), expected)

    def test_FirstCommonAncestor(self):
        preArr = [5, 4, 3, None, None, 5, None, None, \
                     8, 7, None, None, 13, None, None]
        root = Node.PreOrderArrayToTree(preArr)
        self.driver(root, root.left.left, root.left.right, root.left)

if __name__ == "__main__":
    unittest.main()
