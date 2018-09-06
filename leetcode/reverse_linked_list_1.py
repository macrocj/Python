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

    def printll(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def print_helper(self, node, name):
        if node is None:
            print(name + ":None")
        else:
            print(name + ":" + node.data)
    def reversell(self):
        prev = None
        cur = self.head
        ############################
        #   reverse the link list
        #   from 1 -> 2 -> 3 -> 4
        #   to   1 <- 2 <- 3 <- 4
        ###########################
        while cur:
            next = cur.next #set temp var to store the next value
            cur.next = prev  #set the point back to previous one, first round set to None
            prev = cur  # store the previous value to current one
            cur = next  # iter to next value for looping
        self.head = prev  # set the head value to 4

mylist = linklist()
mylist.append("1")
mylist.append("2")
mylist.append("3")
mylist.append("4")
mylist.printll()
print("\n")
mylist.reversell()
mylist.printll()