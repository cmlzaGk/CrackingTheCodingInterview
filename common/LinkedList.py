class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    @staticmethod
    def MakeLinkedList(inArr):
        head = curr = None
        for data in inArr:
            if head == None:
                head = LinkedListNode(data)
                curr = head
            else:
                curr.next = LinkedListNode(data)
                curr = curr.next
        return head

    @staticmethod
    def List(head):
        oList = []
        while head != None:
            oList.append(head.data)
            head = head.next
        return oList

    @staticmethod
    def KthNode(head, k):
        for i in range(k-1):
            if head != None:
                head = head.next
            else:
                break
        return head

    @staticmethod
    def ListLen(head):
        listLen = 0
        while head:
            listLen += 1
            head = head.next
        return listLen

    @staticmethod
    def Tail(head):
        tail = None
        while head:
            tail = head
            head = head.next
        return tail

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
    def Append(self, data):
        node = LinkedListNode(data)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
