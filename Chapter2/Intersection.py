import unittest
from common.LinkedList import *

def Intersection(head1, head2):
    len1 = LinkedListNode.ListLen(head1)
    len2 = LinkedListNode.ListLen(head2)
    if len1 > len2:
        for i in range(len1-len2):
            head1 = head1.next
    if len2 > len1:
        for i in range(len2-len1):
            head2 = head2.next
    while head1:
        if head1 is head2:
            return head1
        head1 = head1.next
        head2 = head2.next
    return None

class TestIntersection(unittest.TestCase):
    def driver(self, inArr1, inArr2, inArr3):
        head1 = LinkedListNode.MakeLinkedList(inArr1)
        head2 = LinkedListNode.MakeLinkedList(inArr2)
        head3 = LinkedListNode.MakeLinkedList(inArr3)
        tail = head1
        while tail and tail.next:
            tail = tail.next
        tail.next = head3
        tail = head2
        while tail and tail.next:
            tail = tail.next
        tail.next = head3
        inter = Intersection(head1, head2)
        self.assertEqual(inter, head3)
    def test_Intersection(self):
        self.driver([1,2,3],[4,5,6,7],[8,9])
        self.driver([1],[4,5,6,7],[8,9])
        self.driver([1,2,3],[4,5,6,7],[9])
        self.driver([1,2,3],[4,5,6,7],[])

if __name__ == "__main__":
    unittest.main()
