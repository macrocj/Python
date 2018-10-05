#Author: JC
#Date: 10/4/2018
#Version: 1.0

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

    def print_helper(self, node, name):
        if node is None:
            print(name + " is None")
        else:  print(name + " value is ",node.data)

    def add_two_numbers(self,L1,L2):
        place_iter = dummy_head = self.ListNode(0,None)
        L1 = L1.head
        L2 = L2.head
        carry = 0
        while L1 or L2 or carry:
            val = carry + (L1.data if L1 else 0) + (L2.data if L2 else 0)
            L1 = L1.next if L1 else None
            L2 = L2.next if L2 else None
            place_iter.next = self.ListNode(val % 10, None)
            carry, place_iter = val // 10, place_iter.next
            #print(L1.data, L2.data, val, carry, place_iter.data)
            self.print_helper(place_iter,"Place_iter")
        self.head = dummy_head.next


l1 = LinkedList()
for i in (3,1,4):
    l1.append(i)
l2 = LinkedList()
for i in (7,0,9):
    l2.append(i)
l1.printll()
l2.printll()
print("\n")

l = LinkedList()
l.add_two_numbers(l1,l2)
l.printll()
