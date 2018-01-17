# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Given a linked list, remove the nth node from the end of list and return its head.
For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode, return head!
        """
        #get the length
        dummy = head
        length = 0
        while dummy:
            length += 1
            dummy = dummy.next
        #find and del
        if n == length: #delete head
            head = head.next
            return head
        count = 0
        p = head
        q = head
        while length - count > n:
            count += 1
            q = p
            p = p.next
        q.next = p.next
        """
        see https://github.com/algorhythms/LeetCode/blob/master/019%20Remove%20Nth%20Node%20From%20End%20of%20List.py
        while p:
            if length - count == n:
                    
                break        
        """

        return head
        
        
            s