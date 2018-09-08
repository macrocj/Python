#Author: JC
#Date: 8/20/2018
#Version: 1.0

class ListNode:
    def __init__(self,data):
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

    def reverse_sublist(self,start,finish):
        dummy_head = sublist_head = ListNode(0)
        sublist_head =self.head
        for _ in range(1, start):
            sublist_head = sublist_head.next
        # Revesrse sublist
        sublist_iter = sublist_head.next
        print("sublist_iter init value is ", sublist_iter.data)
        self.print_list()
        for _ in range(finish - start):
            temp = sublist_iter.next
            print("temp value is ", temp.data)
            sublist_iter.next, temp.next, sublist_head.next = (
                temp.next, sublist_head.next, temp)
            print(sublist_iter.data, ".next point to ", temp.next.data)
            print(temp.data, ".next point to ", sublist_head.next.data)
            print(sublist_head.data,".next point to ", temp.data)
            self.print_list()
        return dummy_head.next

    def reverseBetween(self,start,finish):
        dummy = ListNode(0)
        dummy = self.head
        sublist = dummy
        for _ in range(start-1):
            sublist = sublist.next
        prev = sublist.next
        cur = prev.next
        for _ in range(finish - start):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        sublist.next.next = cur
        print(cur)
        sublist.next = prev
        print(sublist.next.data,prev.data)
        #return dummy.next
mylist = LinkedList()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)

mylist.reverse_sublist(1,4)
mylist.print_list()
#mylist.reverseBetween(3,4)
#mylist.print_list()