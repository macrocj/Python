#Author: JC
#Date: 8/14/2018
#Version: 1.0

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)

        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def merge_2_sorted_linkedlist(self, l2):
        p = self.head # linked list 1
        q = l2.head  # linked list 2
        s = None # new empty linked list
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head
#############################################################

    def merge_sorted_linkedlists(self, L2):
        # Create a placeholder for the result
        dummy_head = tail = ListNode(0)
        L1 = self.head
        L2 = L2.head

        while L1 and L2:
            if L1.data < L2.data:
                tail.next, L1 = L1, L1.next
            else:
                tail.next, L2 = L2, L2.next
            if L1.next is not None: tail = tail.next
            print(L1.data, L2.data)
            #if L2.next is not None: tail = tail.next

        # Appends the remaining nodes of L1 or L2
        tail.next = L1 or L2
        return dummy_head.next
#####################################################################
l1 = linked_list()
l2 = linked_list()
l1.append(1)
l1.append(4)
l1.append(7)
l1.append(9)

l2.append(2)
l2.append(6)
l2.append(8)
l2.append(10)


l1.merge_2_sorted_linkedlist(l2)
#l1.print_list()
l1.merge_sorted_linkedlists(l2)
l1.print_list()
#l1.merge_sorted_linkedlists(l1,l2)
#print(merge_two_sorted_lists(l1,l2))
