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

    def swap_node(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        cur_1 = self.head
        # search the node, stop the loop until find it
        while cur_1 and cur_1.data != key_1:
            prev_1 = cur_1  # once find the node data, set prev and skip cur to next node
            cur_1 = cur_1.next

        prev_2 = None
        cur_2 = self.head
        while cur_2 and cur_2.data != key_2:
            prev_2 = cur_2
            cur_2 = cur_2.next

        if not cur_1 or not cur_2:
            return
        if prev_1:  # if prev is not none
            prev_1.next = cur_2
        else:
            self.head = cur_2
        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1

        cur_1.next, cur_2.next = cur_2.next, cur_1.next

    def delete_node(self, key):
        cur_node = self.head
        # if head is the one you want to delete, set head to next node
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node= None
            return

        # if head node is not the one you want to delete
        prev = None
        # find the one you want to delete
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        # check if the one you want to delete is not in the linklist
        if cur_node is None:
            return
        # set the node to point to c skip the B and set B to none
        prev.next = cur_node.next
        cur_node = None

    def delete_node_location(self,location):
        cur_node = self.head
        if cur_node and location == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 1
        while cur_node and location != location:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return # the position is great than the location provided
       # set the pointer to next node, and delete the node you set
        prev.next = cur_node.next
        cur_node = None
l1 = linked_list()
l1.append('a')
l1.append('b')
l1.append('c')
l1.append('d')

#l1.swap_node('b','c')
l1.delete_node('b')
l1.print_list()