import unittest
from common.LinkedList import *

def SumLists(head1, head2):
    resultHead = None
    carryOver = 0
    current = None
    while head1 != None or head2 != None:
        resultData = carryOver
        if head1 != None:
            resultData += head1.data
        if head2 != None:
            resultData += head2.data
        if resultHead == None:
            resultHead = LinkedListNode(resultData % 10)
            current = resultHead
        else:
            current.next = LinkedListNode(resultData % 10)
            current = current.next
        carryOver = int(resultData / 10)
        if head1 != None:
            head1 = head1.next
        if head2 != None:
            head2 = head2.next
    if carryOver != 0:
        current.next = LinkedListNode(carryOver)
    return resultHead

# FollowUp
# invariance is that the lenght of both the lists is same
def SumListsForwardOrderDriver(head1, head2):
    if head1 == None:
        return None, 0
    nextNode, carryOver = SumListsForwardOrderDriver(head1.next, head2.next)
    resultData = head1.data + head2.data + carryOver
    newNode = LinkedListNode(resultData % 10)
    newNode.next = nextNode
    return newNode, int(resultData/10)

def PadLinkList(head, padLen):
    newHead = head
    for i in range(padLen):
        newHead = LinkedListNode(0, newHead)
    return newHead

def SumListsForwardOrder(head1, head2):
    len1 = LinkedListNode.ListLen(head1)
    len2 = LinkedListNode.ListLen(head2)
    if len1 > len2:
        head2 = PadLinkList(head2, len1-len2)
    if len2 > len1:
        head1 = PadLinkList(head1, len2-len1)
    resultHead, carryOver = SumListsForwardOrderDriver(head1, head2)
    if carryOver != 0:
        return LinkedListNode(carryOver, resultHead)
    return resultHead

class TestSumLists(unittest.TestCase):

    @staticmethod
    def ReverseArrayToInteger(inArr):
        inArrayCopy = inArr.copy()
        inArrayCopy.reverse()
        return int("".join(map(str, inArrayCopy)))

    @staticmethod
    def ArrayToInteger(inArr):
        return int("".join(map(str, inArr)))

    def driver(self, inArr1, inArr2):
        head1 = LinkedListNode.MakeLinkedList(inArr1)
        head2 = LinkedListNode.MakeLinkedList(inArr2)
        result = self.ReverseArrayToInteger(LinkedListNode.List(SumLists(head1, head2)))
        expected = self.ReverseArrayToInteger(inArr1) + self.ReverseArrayToInteger(inArr2)
        self.assertEqual(result, expected)
        result = self.ArrayToInteger(LinkedListNode.List(SumListsForwardOrder(head1, head2)))
        expected = self.ArrayToInteger(inArr1) + self.ArrayToInteger(inArr2)
        self.assertEqual(result, expected)

    def test_TestSumLists(self):
        self.driver([6,7,9], [9,8,5])
        self.driver([6,7,9], [1,8,5])
        self.driver([7,9], [1,8,5])
        self.driver([6,7,9], [8,5])
        self.driver([6,7,9], [5])
        self.driver([9], [9,8,5])

if __name__ == "__main__":
    unittest.main()
