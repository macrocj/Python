#Author: JC
#Date: 9/30/2018
#Version: 1.0

# write a program that takes as input as singly linked list
# and a nonnegative interger k, and return the list
# cyclically shifted to the right by k.

class LInkList:
    def __init__(self):
        self.head = None

    class ListNode:
        def __init__(self, data, next):
            self.data = data
            self.next = next

    def append(self,data):
        new_node = self.ListNode(data,self.head)
        self.head = new_node

    def printll(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def print_helper(self, node, name):
        if node is None:
            print(node, "is None")
        else: print(name + " is ", node.data)

    def cyclically_right_shift_list(self,k):
        #dummy_head = cur = self.ListNode(0,self.head)
        #dummy_head.next = self.head
        cur = self.head
        if not cur:
            return cur
        # computes the length of L and the tail
        tail, n = cur, 1
        while tail.next:
            n += 1
            tail = tail.next
        k %= n
        if k == 0:
            return cur
        tail.next = cur # Makes a cycle by connection the tail to the head

        steps_to_new_head, new_tail = n-k, tail # set initial new_tail to old tail

        while steps_to_new_head:
            steps_to_new_head -= 1
            new_tail = new_tail.next

        self.print_helper(new_tail, "new tail")
        new_head = new_tail.next
        self.print_helper(new_head," new head")
        self.head = new_head
        new_tail.next= None



    # has problem with linked list next()
    def cyclically_right_shift_list2(self,L,k):
        dummy_head =  self.ListNode(0,None)
        dummy_head.next = L
        if not L:
            return L
        # computes the length of L and the tail
        tail, n = L, 1
        while tail.next:
            n += 1
            tail = tail.next

        k %= n
        if k == 0:
            return L

        tail.next = L # Makes a cycle by connection the tail to the head
        steps_to_new_head, new_tail = n-k, tail
        while steps_to_new_head:
            steps_to_new_head -= 1
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next= None
        return new_head

l = LInkList()
for i in range(1,6):
    l.append(i)
l.printll()

l.cyclically_right_shift_list(3)
print('\n')
l.printll()
'''
s = LInkList()
s.cyclically_right_shift_list2(l,3)
s.printll()
'''