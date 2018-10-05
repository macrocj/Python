#Author: JC
#Date: 10/3/2018
#Version: 1.0

class LinkedList:
    def __init__(self):
        self.head = None

    class ListNode:
        def __init__(self, data, next):
            self.data= data
            self.next = next

    def append(self,data):
        new_node = self.ListNode(data,None)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def printll(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def list_pivoting(self,x):
        cur = self.head
        less_head = less_iter = self.ListNode(0, None)
        equal_head = equal_iter = self.ListNode(0,None)
        greater_head = greater_iter = self.ListNode(0,None)

        # Populate the three list:
        while cur:
            if cur.data < x:
                less_iter.next = cur
                less_iter = less_iter.next
            elif cur.data == x:
                equal_iter.next = cur
                equal_iter = equal_iter.next
            elif cur.data > x:
                greater_iter.next = cur
                greater_iter = greater_iter.next
            cur = cur.next

        # Combine three list together
        greater_iter.next = None
        equal_iter.next = greater_head.next
        less_iter.next = equal_head.next
        self.head = less_head.next



l = LinkedList()

for i in (1,12,6,5,7,3,8,2,24):
    l.append(i)
l.list_pivoting(7)
l.printll()
