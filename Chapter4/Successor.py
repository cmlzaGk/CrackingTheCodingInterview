import common.Tree
import unittest

def leftMostNode(node):
    return leftMostNode(node.left) if node.left else node

def CrawlUp(node):
    if not node.parent:
        return None
    if node.parent.left == node:
        return node.parent
    return CrawlUp(node.parent)

def Successor(node):
    return leftMostNode(node.right) if node.right else CrawlUp(node)

class TestSuccessor(unittest.TestCase):
    def driver(self, root, expected):
        self.assertEqual(expected, Successor(root))
    def test_Successor(self):
        preArr = [5, 4, 3, None, None, 5, None, None, \
                     8, 7, None, None, 13, None, None]
        root = common.Tree.Node.PreOrderArrayToTree(preArr)
        self.driver(root, root.right.left)
        self.driver(root.left, root.left.right)
        self.driver(root.left.right, root)
        self.driver(root.right.right, None)

if __name__ == "__main__":
    unittest.main()
