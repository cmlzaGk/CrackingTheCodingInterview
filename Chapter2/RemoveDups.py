import unittest
from common.LinkedList import *

# RemoveDups does not change the head
def RemoveDups(head):
    lookupDict = {}
    prev = None
    while head != None:
        if head.data in lookupDict:
            prev.next = head.next
        else:
            lookupDict[head.data] = None
            prev = head
        head = head.next

class TestRemoveDups(unittest.TestCase):
    def driver(self, inArr, expected):
        head = LinkedListNode.MakeLinkedList(inArr)
        RemoveDups(head)
        result = LinkedListNode.List(head)
        self.assertEqual(result, expected)
    def test_RemoveDups(self):
        self.driver([1,2,3,4,3,5], [1,2,3,4,5])
        self.driver([1,1,1], [1])

if __name__ == "__main__":
    unittest.main()
