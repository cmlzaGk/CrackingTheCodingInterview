import common.LinkedList
import common.Tree
import unittest

from collections import defaultdict


def InOrder(node, mappings, depth):
    if not node:
        return
    if node.left:
        InOrder(node.left, mappings, depth+1)
    mappings[depth].Append(node.data)
    if node.right:
        InOrder(node.right, mappings, depth+1)

def ListOfDepths(node):
    mappings = defaultdict(common.LinkedList.LinkedList)
    InOrder(node, mappings, 0)
    return dict(mappings)

def _MapLinkedListToAList(linkedList):
    return common.LinkedList.LinkedListNode.List(linkedList.head)

class TestListOfDepths(unittest.TestCase):
    def driver(self, preArr, expected):
        mappings = ListOfDepths(common.Tree.Node.PreOrderArrayToTree(preArr))
        for depthLevel in mappings:
            self.assertEqual(expected, list(map(\
                _MapLinkedListToAList, mappings.values())))
    def test_ListOfDepths(self):
        self.driver([1, 2, 3, 4, None, None, None,\
                    5, None, None, 7, None, None],\
                    [[1],[2,7],[3,5],[4]])
        self.driver([1, None, None],\
                    [[1]])

if __name__ == "__main__":
    unittest.main()
