import unittest
from common.LinkedList import *

class DeleteTailNotSupportedException(Exception): pass

def DeleteMiddleNode(middleNode):
    if middleNode.next == None:
        raise DeleteTailNotSupportedException
    middleNode.data = middleNode.next.data
    middleNode.next = middleNode.next.next

class TestDeleteMiddleNode(unittest.TestCase):
    def driver(self, inArr, k, expected):
        head = LinkedListNode.MakeLinkedList(inArr)
        middleNode = LinkedListNode.KthNode(head, k)
        if expected == None:
            with self.assertRaises(DeleteTailNotSupportedException):
                DeleteMiddleNode(middleNode)
            return
        DeleteMiddleNode(middleNode)
        result = LinkedListNode.List(head)
        self.assertEqual(result, expected)

    def test_DeleteMiddleNode(self):
        self.driver([1,2,3,4,5,6], 5, [1,2,3,4,6])
        self.driver([1,2,3,4,5,6], 6, None)
        self.driver([1,2,3,4,5,6], 1, [2,3,4,5,6])


if __name__ == "__main__":
    unittest.main()
