'''
Author: ''
Created on '10/4/2018'
Version: 1.0
'''
from builtins import range


class LinkedList:
    def __init__(self):
        self.head = None

    class ListNode:
        def __init__(self, data, next):
            self.data = data
            self.next = next

    def append(self,data):
        new_node = self.ListNode(data,None)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def append2(self,data):
        new_node = self.ListNode(data,self.head)
        self.head = new_node

    def printll(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def print_linked_list_in_reverse(self):
        cur = self.head
        nodes = []
        while cur:
            nodes.append(cur.data)
            cur = cur.next
        while nodes:
            print(nodes.pop())

l = LinkedList()
for i in range(1,6):
    l.append(i)
l.printll()
print('\n')
l.print_linked_list_in_reverse()
