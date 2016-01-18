from common.Tree import *
import unittest

# left and right cannot be None
def _Weave(prefix, left, iLeft, right, iRight):
    result = []
    if iLeft >= len(left):
        result.append([prefix] + right[iRight:])
        return result
    if iRight >= len(right):
        result.append([prefix] + left[iLeft:])
        return result
    leftResult = _Weave(left[iLeft], left, iLeft+1, right, iRight)
    rightResult = _Weave(right[iRight], left, iLeft, right, iRight+1)
    for r in leftResult:
        result.append([prefix] + r)
    for r in rightResult:
        result.append([prefix] + r)
    return result

def BSTSequence(node):
    if not node:
        return [None]
    result = []
    leftResult = BSTSequence(node.left)
    rightResult = BSTSequence(node.right)
    for l in leftResult:
        for r in rightResult:
            l = l if l is not None else []
            r = r if r is not None else []
            weaveResults = _Weave(node.data,l, 0, r, 0)
            for w in weaveResults:
                result.append(w)
    return result


class TestBSTSequence(unittest.TestCase):
    # A farcical test
    def driver(self, preArr, expected):
        root = Node.PreOrderArrayToTree(preArr)
        self.assertEqual(BSTSequence(root), expected)

    def test_TestBSTSequence(self):
        preArr = [2, 1, None, None, 3, None, None]
        expected = [[2,1,3],[2,3,1]]
        self.driver(preArr, expected)

# A random show
def DumpSequence():
    preArr = [6, 4, 3, None, None, 5, None, None, \
                 8, 7, None, None, 13, None, None]
    root = Node.PreOrderArrayToTree(preArr)
    for r in BSTSequence(root):
        print(repr(r))

if __name__ == "__main__":
    unittest.main()
