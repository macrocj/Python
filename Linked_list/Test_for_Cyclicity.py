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
    def cyclelinklist(self):
        last = Node(8)
        head = Node(7, last)
        head = Node(6, head)
        head = Node(5, head)
        head = Node(4, head)
        head = Node(3, head)
        head = Node(2, head)
        head = Node(1, head)
        last.next = head
        return head
    def has_cycle(self):
        def cycle_len(end):
            start, step = end, 0
            while True:
                step += 1
                start = start.next
                if start is end:
                    return step

        fast = slow = self.head
        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                # Finds the start of the cycle.
                cycle_len_advanced_iter = self.head
                for _ in range(cycle_len(slow)):
                    cycle_len_advanced_iter = cycle_len_advanced_iter.next

                it = self.head
                # Both iterators advance in tandem.
                while it is not cycle_len_advanced_iter:
                    it = it.next
                    cycle_len_advanced_iter = cycle_len_advanced_iter.next
                return it # iter is the start of cycle.
        return None # No cycle.

    def cycle_method_2(self,head):
        dm = ListNode(0)
        while head:
            if head == dm: return True
            temp = head
            head = head.next
            temp.next = dm
        return False
    def cycle_medhod_3(self,head):
        fast = slow = head
        while fast and slow:
            try:
                fast = fast.next.next
                slow = slow.next
            except:
                return False
            if fast == slow:
                return True
        return False


mylist = Linklist()
head = mylist.cyclelinklist()
mylist.printll()
mylist.has_cycle()
print(mylist.cycle_medhod_3(head))
print(mylist.cycle_method_2(head))