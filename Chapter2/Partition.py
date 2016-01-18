from common.LinkedList import *
import unittest

def Partition(head, x):
    rPointer = None
    current = head
    while current != None:
        if current.data < x:
            if rPointer != None:
                rPointer.data, current.data = current.data, rPointer.data
                rPointer = rPointer.next
        else:
            if rPointer == None:
                rPointer = current
        current=current.next
    return head

def Partition2(head, x):
    currentHead = head
    previous = None
    current = head
    originalTail = LinkedListNode.Tail(head)
    currentTail = originalTail
    crossedOriginalTail = False

    while current and not crossedOriginalTail :
        if current == originalTail:
            crossedOriginalTail = True
        if current.data < x:
            previous = current
            current = current.next
        elif previous == None:
            #The below order is very important to take care of scenarios
            #where there is only one element.
            currentTail.next = current
            currentHead = current.next
            currentTail = current
            current.next = None
            current = currentHead
        else:
            previous.next = current.next
            currentTail.next = current
            currentTail = current
            current.next = None
            current = previous.next
    return currentHead

class TestPartition(unittest.TestCase):
    def driver(self, inArr, x):
        for fn in [Partition, Partition2]:
            head = LinkedListNode.MakeLinkedList(inArr)
            head = fn(head, x)
            inLeftPartition = True
            result = LinkedListNode.List(head)
            for r in result:
                if r < x:
                    self.assertEqual(inLeftPartition, True)
                else:
                    inLeftParition = False
            self.assertEqual(sorted(result), sorted(inArr))

    def test_Partition(self):
        self.driver([3, 5, 8, 7, 10, 2, 1], 5)
        self.driver([3, 5, 8, 7, 10, 2, 1], 3)
        self.driver([3, 5, 8, 7, 10, 2, 1], 0)
        self.driver([1], 5)
        self.driver([1], 0)

if __name__ == "__main__":
    unittest.main()

