# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode(0)
        rear = l
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                rear.next = l1
                rear = l1
                l1 = l1.next
            else:
                rear.next = l2
                rear = l2
                l2 = l2.next
        """
	#this is also okay.
        while l1 is not None:
            rear.next = l1
            rear = l1
            l1 = l1.next
        while l2 is not None:
            rear.next = l2
            rear = l2
            l2 = l2.next
        return l.next
        """
        if l1 is not None:
            rear.next = l1
            rear = l1
        else:
            rear.next = l2
            rear = l2
        return l.next
        
        