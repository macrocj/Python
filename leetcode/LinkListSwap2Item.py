'''
Author: ''
Created on '9/5/2018'
Version: 1.0
'''

'''
Author: ''
Created on '9/5/2018'
Version: 1.0
'''

class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class linklist:
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

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def print_helper(self, node, name):
        if node is None:
            print(name + ":None")
        else:
            print(name + ":" + node.data)

    def swap_nodes(self, key_1, key_2):
        # check if key 1 is equal to key 2
        if key_1 == key_2:
            return
        # set the pointer 1 to provided key 1 value
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
            self.print_helper(prev_1, "PREV_1")
            self.print_helper(curr_1, "CUR_1")
            print("\n")
        # set the pointer 2 to provided key 2 vlaue
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
            self.print_helper(prev_2, "PREV_2")
            self.print_helper(curr_2, "CUR_2")
            print("\n")
        # check if curr_1 or curr2 is not None
        if not curr_1 or not curr_2:
            return
        # check if Key 1 is the head value, in other word, does key 1 has previous vlaue
        if prev_1:
            prev_1.next = curr_2  # set pointer from A to C
        else:
            self.head = curr_2  # set the key 1 value as head value
        if prev_2:
            prev_2.next = curr_1 # set the pointer from C to B
        else:
            self.head = curr_1   # set the key 2 value as head value
        # set pointer B to D, and C to B
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

mylist = linklist()
mylist.append("A")
mylist.append("B")
mylist.append("C")
mylist.append("D")
mylist.print_list()
mylist.swap_nodes("B","C")
print("\n")
mylist.print_list()