#Author: JC
#Date: 9/28/2018
#Version: 1.0

# Remove the duplicates from sort linked list !!!!!!!
class linkedlist:

    def __init__(self):
        self.head = None

    class ListNode:
        def __init__(self,data,next):
            self.data = data
            self.next = next

    def append(self,data):
        new_node = self.ListNode(data, self.head)
        self.head = new_node

    def printll(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def print_helper(self, node, name):
        if node is None:
            print(name, ":None")
        else: print(name + ":" , node.data)

    def remove_duplicates(self):
        dummy_head = cur = self.ListNode(0,None)
        dummy_head.next = self.head
        while cur:
            # Use next_distinct to fine the next distinct value.
            next_distinct = cur.next

            while next_distinct and next_distinct.data == cur.data:
                self.print_helper(next_distinct, "next_distinct")
                next_distinct = next_distinct.next
            cur.next = next_distinct
            cur = next_distinct
            self.print_helper(cur,"cur")
        #return self.head

l = linkedlist()
l.append(1)
l.append(1)
l.append(2)
l.append(2)
l.append(3)
l.append(3)
l.append(3)
l.append(11)
#l.printll()
l.remove_duplicates()
print("\n")
l.printll()
