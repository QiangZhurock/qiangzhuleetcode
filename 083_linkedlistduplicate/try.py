# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        #note that it is sorted, similar to the list delete, O(n) time
        #dummy = ListNone(0)
        
        #deal with special cases firstly
        if head is None:
            return
        dummy = head
        rear = dummy
        head = head.next
        while head:
            if rear.val != head.val:
                rear.next = head
                rear = head
            head = head.next
        rear.next = None
        return dummy
                
        
        
        