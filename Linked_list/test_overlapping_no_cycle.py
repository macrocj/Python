#Author: JC
#Date: 9/8/2018
#Version: 1.0


class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data
class Linklist:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    def printll(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    def overlapping_no_cycle(self,l1,l2):
        def length(L):
            L = L.head
            length = 0
            while L:
                length += 1
                L = L.next
            return length
        dummy1= ListNode(0)
        dummy2 = ListNode(0)
        dummy1.next = l1
        dummy2.next = l2
        l1_len, l2_len = length(l1),length(l2)
        if l1_len > l2_len:
            l1, l2 = l2, l1 # l2 is hte longer list

        # Advance the longer list to get equal legnth lists
        l1 = l1.head
        l2 = l2.head
        for _ in range(abs(l1_len - l2_len)):
            l2 = l2.next
            while l1 and l2 and l1 != l2:
                l1, l2 = l1.next, l2.next
            return l1

mylist = Linklist()
l1 =Linklist()
l2 = Linklist()
l1.append(11)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
#l1.printll()
l2.append(1)
l2.append(2)
l2.append(3)
l2.append(4)

print(mylist.overlapping_no_cycle(l1,l2))