#Author: JC
#Date: 8/20/2018
#Version: 1.0

# 1. iterate linked list, and add each node to python list
# 2. sort python list
# 3. iterate python list and add each node to new linked list

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def sort(self):
        # should check linked list size, add it later
        newlist = []
        cur = self.head
        newlist.append(cur.data)
        while cur.next != None:
            cur = cur.next
            newlist.append(cur.data)
        newlist =sorted(newlist , key = None, reverse = True)
        newll = LinkedList()
        for node in newlist:
            newll.append(node)
        return newll

mylist = LinkedList()
mylist.append(1)
mylist.append(5)
mylist.append(12)
mylist.append(8)
mylist.print_list()
mylist = mylist.sort()
print("New sorted linked list")
mylist.print_list()