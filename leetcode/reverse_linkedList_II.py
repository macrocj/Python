'''
Author: ''
Created on '9/7/2018'
Version: 1.0
'''


class ListNode(object):
    def __init__(self, x):
        self.data = x
        self.next = None


class Solution(object):
    def __init__(self):
        self.head = None
    # Method 1
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        for __ in range(m - 1):
            node = node.next
        prev = node.next
        curr = prev.next
        for __ in range(n - m):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        node.next.next = curr
        node.next = prev
        return dummy.next
    # method 2: 24ms
    def reverse_sublist(self,head,m,n):
        dummy_head = sublist_head = ListNode(0)
        sublist_head.next = head

        for _ in range(1, m):
            sublist_head = sublist_head.next

        sublist_iter = sublist_head.next
        for _ in range(n - m):
            temp = sublist_iter.next
            sublist_iter.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)
        return dummy_head.next
'''
Method 3: 24ms
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy
        for i in range(m - 1):
            curr = curr.next

        last = curr.next
        for i in range(n - m):
            temp = curr.next
            curr.next = last.next
            last.next = last.next.next
            curr.next.next = temp

        return dummy.next

Method 4: 20ms
        dummy = pre = ListNode(0)
        dummy.next = head
        for _ in xrange(m-1):
            pre = pre.next
        cur = start = pre.next
        # reverse the defined part 
        node = None
        for _ in xrange(n-m+1):
            nxt = cur.next
            cur.next = node
            node = cur
            cur= nxt
        # connect three parts
        start.next = cur
        pre.next = node
        return dummy.next
'''