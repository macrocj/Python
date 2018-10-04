#Author: JC
#Date: 9/28/2018
#Version: 1.0


class LinkedList:
    def __init__(self):
        self.head = None

    class ListNode:
        def __init__(self, data, next):
            self.data = data
            self.next = next

    def append(self,data):
        new_node = self.ListNode(data, self.head)
        self.head = new_node

    def printll(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def print_helper(self, node, name):
        if node is None:
            print(name + " is None")
        else:  print(name + " value is ",node.data)

    def reverse_linklist(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            self.print_helper(cur.next, "Before: cur.next.data")
            cur.next = prev
            self.print_helper(cur.next,"After: cur.next.data")
            prev = cur
            cur = next
        self.head = prev

l = LinkedList()
for i in range(1,6):
    l.append(i)
l.printll()
print('\n')
l.reverse_linklist()
l.printll()