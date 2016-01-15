import unittest
from common.LinkedList import *

def PalindromeIterative(head):
    listLen = LinkedListNode.ListLen(head)
    numNodesToPush = int(listLen/2)
    stackHead = None
    for i in range(numNodesToPush):
        stackHead = LinkedListNode(head.data, stackHead)
        head = head.next
    if listLen % 2 == 1:
        head = head.next
    while head:
        if head.data != stackHead.data:
            return False
        stackHead = stackHead.next
        head=head.next
    return True

def PalindromeRecursive(head):
    listLen = LinkedListNode.ListLen(head)
    tmpHead = head
    for i in range(int(listLen/2)):
        tmpHead = tmpHead.next
    if listLen %2 == 1:
        tmpHead=tmpHead.next
    t,ignore = PalindromeRecursiveDriver(tmpHead, head)
    return t

def PalindromeRecursiveDriver(tailHead, head):
    if tailHead == None:
        return True, head
    result, cmpHead = PalindromeRecursiveDriver(tailHead.next, head)
    if result == False or cmpHead.data != tailHead.data:
        return False, cmpHead.next
    return True, cmpHead.next

class TestPalindrome(unittest.TestCase):
    def driver(self, testStr, expected):
        head = LinkedListNode.MakeLinkedList(list(testStr))
        self.assertEqual(PalindromeIterative(head), expected)
        self.assertEqual(PalindromeRecursive(head), expected)
    def test_Palindrome(self):
        self.driver("abc", False)
        self.driver("abcba", True)
        self.driver("abba", True)
        self.driver("aa", True)
        self.driver("ab", False)
        self.driver("a", True)
if __name__ == "__main__":
    unittest.main()
