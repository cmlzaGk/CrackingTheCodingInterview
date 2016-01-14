import unittest
from common.LinkedList import *

def ReturnKthToLast(head, k):
    fastPointer = slowPointer = head
    for i in range(k-1):
        if fastPointer.next == None:
            return None
        fastPointer = fastPointer.next
    while fastPointer.next != None:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next
    return slowPointer

class TestReturnKthTolast(unittest.TestCase):
    def driver(self, inArr, k, expected):
        head = LinkedListNode.MakeLinkedList(inArr)
        kthElem = ReturnKthToLast(head, k)
        self.assertEqual(kthElem.data if kthElem else kthElem, expected)
    def test_ReturnKthToLast(self):
        self.driver([1,2,3,4,7,6], 5, 2)
        self.driver([1,3,3,4,7,6], 2, 7)
        self.driver([1,3,4,4,5,6], 2, 5)
        self.driver([1,3,4], 2, 3)
        self.driver([1,3,4], 5, None)

if __name__ == "__main__":
    unittest.main()
