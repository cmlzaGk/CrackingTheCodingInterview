from common.LinkedList import *
import unittest
import random

def LoopDetection(head):
    fast = slow = head
    while True:
        fast = fast.next
        if not fast:
            return None
        fast = fast.next
        if not fast:
            return None
        slow = slow.next
        if fast is slow:
            break
    nodesInLoop = 0
    while True:
        slow = slow.next
        nodesInLoop += 1
        if fast == slow:
            break
    slow = fast = head
    for i in range(nodesInLoop):
        fast = fast.next
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return slow

class TestLoopDetection(unittest.TestCase):
    def driver(self, inArr, k):
        inList = LinkedListNode.MakeLinkedList(inArr)
        loopStart = None
        expectedValue = None
        if k != -1:
            expectedValue = inArr[k]
            current = inList
            for i in range(k):
                current = current.next
            loopStart = current
            while current and current.next:
                current=current.next
            current.next = loopStart
        self.assertEqual(loopStart, LoopDetection(inList))
        self.assertEqual(loopStart.data if loopStart else None, expectedValue)

    def test_LoopDetection(self):
        self.driver([1,2,3,4,5,6], 0)
        self.driver([1,2,3,4,5,6], 1)
        self.driver([1,2,3,4,5,6], 2)
        self.driver([1,2,3,4,5,6], 3)
        self.driver([1,2,3,4,5,6], 4)
        self.driver([1,2,3,4,5,6], 5)
        self.driver([1,2,3,4,5], 0)
        self.driver([1,2,3,4,5], 1)
        self.driver([1,2,3,4,5], 2)
        self.driver([1,2,3,4,5], 3)
        self.driver([1,2,3,4,5], 4)
        self.driver([1], 0)

if __name__ == "__main__":
    unittest.main()
