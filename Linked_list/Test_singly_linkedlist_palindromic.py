#Author: JC
#Date: 10/3/2018
#Version: 1.0

class LinkedList:
    def __init__(self):
        self.head = None

    class ListNode:
        def __init__(self, data, next):
            self.data = data
            self.next = next

    def append(self,data):
        new_node = self.ListNode(data, None)
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

    def print_helper(self,node,name):
        if node is None:
            print(name + "is None")
        else: print(name + "value is ", node.data)

    def reverse_linked_list(self,L):
        dummy_head = L = self.ListNode(0,None)
        cur = self.head
        L.next = cur
        prev= None
        while cur:
            next = cur.next
            cur.next = prev
            prev= cur
            cur = next
        self.head = prev

    def is_linkedlist_a_palindrome(self):
        # Fins athe second half of L
        cur = self.head
        slow = fast = cur
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        # Compares the first half and the reversed second half lists
        first_half_iter, second_half_iter = cur, self.reverse_linked_list(slow)

        while second_half_iter and first_half_iter:
            if second_half_iter != first_half_iter:
                return False
            second_half_iter, first_half_iter = second_half_iter.next, first_half_iter.next
        return True

l=LinkedList()
l.append(1)
l.append(5)
l.append(2)
l.append(5)
l.append(1)

l.printll()
print('\n')
print(l.is_linkedlist_a_palindrome())
