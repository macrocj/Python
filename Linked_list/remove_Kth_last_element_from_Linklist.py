#Author: JC
#Date: 9/9/2018
#Version: 1.0

#remvoe the kth last element from a linked list
# Kth last element means it count backward
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkList:
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
    def length(self,data):
        dummy = ListNode(0)
        dummy.next = data
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count
    def remove_kth_last(self,k):
        dummy_head = ListNode(0)
        dummy_head.next= self.head
        first = dummy_head.next
        print("The length of First: ", self.length(first))
        for _ in range(k):
            first = first.next
        print('the first data is ',first.data)
        second = dummy_head
        count = 0
        while first != None:
            first, second = first.next, second.next
            count += 1
            print('\n')
            print("second.next.data is ", second.next.data)
        # second points to the (k+1) th last node, deletes its successor.
        second.next = second.next.next
        return dummy_head

mylist = LinkList()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.printll()
print("\n")
mylist.remove_kth_last(3)
mylist.printll()
#print(mylist.remove_kth_last(3))


#Method 2 with recursion
import random

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    class _Node(object):
        __slots__ = ('_data', '_next')

        def __init__(self, data, next):
            self._data = data
            self._next = next

    def __iter__(self):
        """makes for nicer printing..."""
        walk = self.head
        while walk is not None:
            yield walk._data
            walk = walk._next

    def append(self, data):
        new_node = self._Node(data, self.head)
        self.head = new_node


    def get_nth_from_end(node, n):
        if node is None:
            return (0, None)
        (i, res) = get_nth_from_end(node._next, n)
        if i == n:
            res = node._data
        i += 1
        return (i, res)


l = SinglyLinkedList()
for i in range(10):
    l.append(random.randint(0, 20))

print('list contents:', list(l))
for i in range(10):
    _, val = get_nth_from_end(l.head, i)
    print('pos {} from last: {}'.format(i, val))