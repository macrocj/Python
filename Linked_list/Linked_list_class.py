#Author: JC
#Date: 8/14/2018
#Version: 1.0

class ListNode:
    def __init__(self, data = 0):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = ListNode()
    def append(self, data):
        new_node = ListNode(data)
        cur = self.head
        while cur.next!= None:
            cur = cur.next
        cur.next = new_node
    def display(self):
        elems = []
        cur_node =self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    # Insert a new_node after node
    def insert_after(self,node, new_node):
        new_node.next = node.next
        node.next = new_node

    def search_list(self,L,key):
        while L and L.data != key:
            L = L.next
        # if key was not present in the list, L will have become null.
        return L

    # Delete the node past this one. Assume node is not a tail.
    def delete_after(self, node):
        node.next = node.next.next




